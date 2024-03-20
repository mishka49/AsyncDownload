

import os
import shutil
import tempfile

import git


class Repository:
    """
    used to get a list of files
    """
    def __init__(self, remote_repo_url):
        self.directory = tempfile.mktemp(dir='./')
        self.remote_repo_url = remote_repo_url
        self.HEAD_commit_hash = self.__get_head_commit_hash()
        self.HEAD_commit_tree = self.__get_head_commit_tree()

        self.HEAD_commit_files_paths = self.__get_head_commit_files_paths()

    def __get_head_commit_hash(self):
        remote_refs = {}
        g = git.cmd.Git()
        for ref in g.ls_remote(self.remote_repo_url).split('\n'):
            hash_ref_list = ref.split('\t')
            remote_refs[hash_ref_list[1]] = hash_ref_list[0]
        return remote_refs['HEAD']

    def __get_head_commit_tree(self):
        try:
            git.Repo.clone_from(self.remote_repo_url, self.directory)
            self.__clean_folder_except_specific(self.directory, ['.git'])
        except:
            pass

        repo = git.Repo(self.directory)

        print('HEAD', self.HEAD_commit_hash)
        commit = repo.commit(self.HEAD_commit_hash)

        return commit.tree

    def __clean_folder_except_specific(self, directory, exceptions):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if item not in exceptions:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

    def __get_head_commit_files_paths(self):
        return [item.path for item in self.HEAD_commit_tree.traverse()]

    def update(self):
        self.HEAD_commit_hash = self.__get_head_commit_hash()
        self.HEAD_commit_tree = self.__get_head_commit_tree()
        self.HEAD_commit_files_paths = self.__get_head_commit_files_paths()
