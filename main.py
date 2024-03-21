"""
This script is used to download files from a remote repository.

calculate their SHA256 hash, and print the results.

It uses asyncio for efficient IO-bound operations.
"""

import asyncio

import calculator_sha256
from download import Downloader
from repository import Repository


def print_sha256_results(sha256_results):
    """
    Print the SHA256 results to console.

    Args:
        sha256_results (dict): A dictionary where the keys are file names and.
        the values are their SHA256 hash.
    """
    for filename, sha256_hash in sha256_results.items():
        print(filename, sha256_hash)


async def main():
    """Orchestrates the downloading and SHA256 calculation."""
    remote_repo_url = 'https://gitea.radium.group/radium/project-configuration'
    repo = Repository(remote_repo_url)
    paths = repo.HEAD_commit_files_paths
    download = Downloader(paths, remote_repo_url, repo.directory)
    await download.run()

    sha256_results = calculator_sha256.calculate_sha256_for_directory(
        repo.directory,
    )
    print_sha256_results(sha256_results)


if __name__ == '__main__':
    asyncio.run(main())
