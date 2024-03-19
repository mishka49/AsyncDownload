import asyncio

import calculator_sha256 as calculator
from download import Download
from repository import Repository


if __name__ == "__main__":
    remote_repo_url = "https://gitea.radium.group/radium/project-configuration"
    repo = Repository(remote_repo_url)
    paths = repo.HEAD_commit_files_paths
    download = Download(repo.HEAD_commit_files_paths, remote_repo_url, repo.directory)
    asyncio.run(download.run())

    sha256_results = calculator.calculate_sha256_for_directory(repo.directory)

    for file, sha256_hash in sha256_results.items():
        print(f"{file}: {sha256_hash}")

