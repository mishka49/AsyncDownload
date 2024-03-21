import pytest
from repository import Repository  # replace 'your_module' with the name of your module


def test_repository_initialization():
    repo_url = 'https://gitea.radium.group/radium/project-configuration'  # replace with a real repository URL
    repo = Repository(repo_url)

    assert repo.remote_repo_url == repo_url
    assert repo.HEAD_commit_hash is not None
    assert repo.HEAD_commit_tree is not None
    assert repo.HEAD_commit_files_paths is not None


def test_repository_update():
    repo_url = 'https://gitea.radium.group/radium/project-configuration'  # replace with a real repository URL
    repo = Repository(repo_url)

    old_commit_hash = repo.HEAD_commit_hash
    repo.HEAD_commit_hash = '0000000000000000000000000000000000000000'  # set to an invalid value

    repo.update()

    assert repo.HEAD_commit_hash != '0000000000000000000000000000000000000000'  # assert that the value was updated
    assert repo.HEAD_commit_hash == old_commit_hash  # assert that the value was updated to the correct commit hash
