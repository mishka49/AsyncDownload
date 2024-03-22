from repository import Repository


def test_repository_initialization():
    repo_url = 'https://gitea.radium.group/radium/project-configuration'
    repo = Repository(repo_url)

    assert repo.remote_repo_url == repo_url
    assert repo.HEAD_commit_hash is not None
    assert repo.HEAD_commit_tree is not None
    assert repo.HEAD_commit_files_paths is not None


def test_repository_update():
    repo_url = 'https://gitea.radium.group/radium/project-configuration'
    repo = Repository(repo_url)

    old_commit_hash = repo.HEAD_commit_hash
    repo.HEAD_commit_hash = '0000000000000000000000000000000000000000'

    repo.update()

    assert repo.HEAD_commit_hash != '0000000000000000000000000000000000000000'
    assert repo.HEAD_commit_hash == old_commit_hash
