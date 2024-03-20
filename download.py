"""Module for downloading files from remote repository."""


import asyncio
from urllib.parse import quote

import requests


class Downloader(object):
    """Represent downloader which provides methods to download files."""

    def __init__(self, paths, base_url, local_dir):
        """
         Initialize a Downloader instance.

        Args:
            paths (list): List of file paths relative to the base_url.
            base_url (str): Path to the remote source.
            local_dir (str): Path to the local directory.
        """
        self.paths = paths
        self.base_url = base_url
        self.local_dir = local_dir
        self.NUMBER_OF_STREAMS = 3

    async def download_file(self, path):
        """
        Download file from the remote source.

        Args:
            path (str): Relative path of the file.
        """
        url = '/'.join([self.base_url, 'src', 'branch', 'master', path])
        filename = path.split('/')[-1]
        response = requests.get(url, timeout=5)

        with open('/'.join([self.local_dir, filename]), 'wb') as rf:
            rf.write(response.content)

    async def run(self):
        """
        Run asynchronous tasks.

        Returns:
            list: List of running tasks.
        """
        tasks = [
            asyncio.create_task(self._download_files())
            for _ in range(self.NUMBER_OF_STREAMS)
        ]
        await asyncio.gather(*tasks)
        return tasks

    async def _download_files(self):
        """Download files from the paths list."""
        while self.paths:
            path = quote(self.paths.pop())
            await self.download_file(path)
