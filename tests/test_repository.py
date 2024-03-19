import unittest
import os
import tempfile
import shutil
from unittest.mock import patch
from repository import Repository

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.remote_repo_url = "https://gitea.radium.group/radium/project-configuration"
        self.repo = Repository(self.remote_repo_url)

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.repo.directory)

    def test_get_head_commit_hash(self):
        # Mock the ls_remote output
        with patch("git.cmd.Git.ls_remote") as mock_ls_remote:
            mock_ls_remote.return_value = "HEAD\t123456"
            self.assertEqual(self.repo._Repository__get_head_commit_hash(), "123456")

    def test_get_head_commit_tree(self):
        # Mock the clone_from method
        with patch("git.Repo.clone_from") as mock_clone_from:
            mock_clone_from.return_value = None
            self.repo._Repository__get_head_commit_tree()
            mock_clone_from.assert_called_once_with(self.remote_repo_url, self.repo.directory)

    def test_clean_folder_except_specific(self):
        # Create a temporary directory with some files
        temp_dir = tempfile.mkdtemp()
        file1 = os.path.join(temp_dir, "file1.txt")
        file2 = os.path.join(temp_dir, "file2.txt")
        os.makedirs(file1)
        os.makedirs(file2)

        # Call the method to clean the folder
        self.repo._Repository__clean_folder_except_specific(temp_dir, ["file1.txt"])

        # Check if only file1.txt is left
        self.assertTrue(os.path.exists(file1))
        self.assertFalse(os.path.exists(file2))

    def test_get_head_commit_files_paths(self):
        # Mock the commit tree
        with patch("git.Commit.tree") as mock_commit_tree:
            mock_commit_tree.return_value.traverse.return_value = [
                type("MockItem", (object,), {"path": "file1.txt"}),
                type("MockItem", (object,), {"path": "folder/file2.txt"}),
            ]
            paths = self.repo._Repository__get_head_commit_files_paths()
            self.assertEqual(paths, ["file1.txt", "folder/file2.txt"])

    def test_update(self):
        # Mock the methods called in update
        with patch.object(self.repo, "_Repository__get_head_commit_hash") as mock_get_hash, \
             patch.object(self.repo, "_Repository__get_head_commit_tree") as mock_get_tree, \
             patch.object(self.repo, "_Repository__get_head_commit_files_paths") as mock_get_paths:
            mock_get_hash.return_value = "123456"
            mock_get_tree.return_value = None
            mock_get_paths.return_value = ["file1.txt", "folder/file2.txt"]
            self.repo.update()
            self.assertEqual(self.repo.HEAD_commit_hash, "123456")
            self.assertIsNone(self.repo.HEAD_commit_tree)
            self.assertEqual(self.repo.HEAD_commit_files_paths, ["file1.txt", "folder/file2.txt"])

if __name__ == "__main__":
    unittest.main()
