"""Modul for getting list of files from remote repository."""

import os
import shutil
import tempfile

import git


class Repository(object):
    """Represents a Git repository and provides methods to interact with it."""

    def __init__(self, remote_repo_url):
        """
        Initialize a Repository instance.

        Args:
            remote_repo_url (str): The URL of the remote Git repository.
        """
        self.directory = tempfile.mkdtemp(dir='./')
        self.remote_repo_url = remote_repo_url
        self.HEAD_commit_hash = self._get_head_commit_hash()
        self.HEAD_commit_tree = self._get_head_commit_tree()
        self.HEAD_commit_files_paths = self._get_head_commit_files_paths()

    def update(self):
        """
        Update the repository state.

        by fetching the latest HEAD commit information.
        """
        self.HEAD_commit_hash = self._get_head_commit_hash()
        self.HEAD_commit_tree = self._get_head_commit_tree()

    def _get_head_commit_hash(self):
        """
        Retrieve the hash of the HEAD commit from the remote repository.

        Returns:
            str: The HEAD commit hash.
        """
        remote_refs = {}
        git_instance = git.cmd.Git()
        for ref in git_instance.ls_remote(self.remote_repo_url).split('\n'):
            hash_ref_list = ref.split('\t')
            remote_refs[hash_ref_list[1]] = hash_ref_list[0]

        return remote_refs.get('HEAD', '')

    def _get_head_commit_tree(self):
        """
        Clone the remote repository and retrieve the HEAD commit tree.

        Returns:
            git.Tree: The HEAD commit tree.
        """
        try:
            git.Repo.clone_from(self.remote_repo_url, self.directory)
            self._clean_folder_except_specific(self.directory, ['.git'])
        except git.GitCommandError:
            pass

        repo = git.Repo(self.directory)
        commit = repo.commit(self.HEAD_commit_hash)

        return commit.tree

    def _clean_folder_except_specific(self, directory, exceptions):
        """
        Clean the repository folder, excluding specific files or directories.

        Args:
            directory (str): Path to the repository directory.
            exceptions (list): List of filenames or directories to exclude.
        """
        for filename in os.listdir(directory):
            item_path = os.path.join(directory, filename)
            if filename not in exceptions:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

    def _get_head_commit_files_paths(self):
        """
        Retrieve a list of file paths from the HEAD commit tree.

        Returns:
             list: List of file paths.
        """
        return [_.path for _ in self.HEAD_commit_tree.traverse()]

