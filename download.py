import asyncio
import urllib.request
from urllib.parse import quote


class Download:
    def __init__(self, paths, base_url, local_dir):
        self.paths = paths
        self.base_url = base_url
        self.local_dir = local_dir
        self.NUMBER_OF_STREAMS = 3

    async def __download_files(self):
        while self.paths:
            path = quote(self.paths.pop())

            try:
                await self.download_file(path)
            except ():
                pass

    async def download_file(self, path):
        urllib.request.urlretrieve(f"{self.base_url}/src/branch/master/{path}",
                                   f"{self.local_dir}/{path.split('/')[-1]}")

    async def run(self):
        tasks = []
        for _ in range(self.NUMBER_OF_STREAMS):
            tasks.append(asyncio.create_task(self.__download_files()))

        for task in tasks:
            await task

        return tasks
