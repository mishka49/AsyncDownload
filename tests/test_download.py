"""Module to testing Downloader class"""
import asyncio
import shutil
import sys

sys.path.append('C:/Different/Python/AsyncDownload/')

import copy
import os
import tempfile
import pytest
from download import Downloader
import requests


class TestDownloader:
    """This class contains tests for the Downloader class."""

    base_url = "https://gitea.radium.group/radium/project-configuration"
    paths = ["file1.txt", "file2.txt, file3.txt, file4.txt"]
    local_dir = tempfile.mkdtemp(dir="./")

    def test_request_response(self):
        """Test if the response from the base URL is successful."""
        response = requests.get(self.base_url)

        assert response.ok

    def test_downloader_initialization(self):
        """Test if the repository initialized success"""
        repo_url = 'https://gitea.radium.group/radium/project-configuration'  # replace with a real repository URL
        downloader = Downloader(TestDownloader.paths,
                                TestDownloader.base_url,
                                TestDownloader.local_dir,
                                )

        assert downloader.paths == TestDownloader.paths
        assert downloader.base_url == TestDownloader.base_url
        assert downloader.local_dir == TestDownloader.local_dir

    @pytest.mark.asyncio(scope="module")
    async def test_number_of_stream(self, mocker):
        """
        Test if the number of streams is equal to the number of tasks.

        Args:
            mocker (pytest_mock.plugin.MockerFixture): A pytest fixture that
            provides several methods to control the behavior of all or
            specific mock objects, and it is used here to patch
            the 'download.Downloader.download_file' method.
        """
        mocker.patch('download.Downloader.download_file', return_value=None)
        instance = Downloader(
            TestDownloader.paths,
            TestDownloader.base_url,
            TestDownloader.local_dir,
        )

        tasks = await instance.run()

        assert instance.NUMBER_OF_STREAMS == len(tasks)

    def test_download_files(self, mocker):
        """
        Test if the downloaded files are the same as the paths.

        Args:
            mocker (pytest_mock.plugin.MockerFixture): A pytest fixture that
            provides several methods to control the behavior of all or
            specific mock objects, and it is used here to patch
            the 'download.Downloader.download_file' method.
        """

        def create_files():
            for filename in TestDownloader.paths:
                with open(f"{TestDownloader.local_dir}/{filename}", "w"):
                    pass  # Create an empty file

        def get_list_of_files():
            return [f for f in os.listdir(TestDownloader.local_dir)]

        mocker.patch(
            'download.Downloader.download_file',
            side_effect=create_files(), return_value=None
        )

        instance = Downloader(
            copy.deepcopy(TestDownloader.paths),
            TestDownloader.base_url,
            TestDownloader.local_dir,
        )

        instance.run()

        assert TestDownloader.paths == get_list_of_files()

    @pytest.fixture(scope="module")
    def download_file(self):
        """
        A pytest fixture that sets up a file for testing.

        This fixture creates an instance of the Downloader class and uses it to download a file.
        The file is downloaded using the asyncio event loop to handle the asynchronous operation.

        Returns:
            str: The path to the downloaded file.
        """
        file_name = 'README.md'
        file_path = os.path.join(TestDownloader.local_dir, file_name)

        instance = Downloader(
            copy.deepcopy(TestDownloader.paths),
            TestDownloader.base_url,
            TestDownloader.local_dir,
        )

        loop = asyncio.get_event_loop()
        task = loop.create_task(instance.download_file(file_name))
        loop.run_until_complete(task)

        return file_path

    @pytest.mark.asyncio
    async def test_file_exists(self, download_file):
        """
        An asynchronous test that checks if a file exists at the specified path.

        This test uses the download_file fixture to get the path to a file, and then checks if a file exists at that path.

        Args:
            download_file (str): The path to the file to check.
        """
        assert os.path.exists(download_file)

    @pytest.mark.asyncio
    async def test_file_isfile(self, download_file):
        """
        An asynchronous test that checks if the path points to a file.

        This test uses the download_file fixture to get the path to a file, and then checks if the path points to a file (and not a directory).

        Args:
            download_file (str): The path to the file to check.
        """
        assert os.path.isfile(download_file)


@pytest.fixture(scope='class', autouse=True)
def cleanup_after_class(request):
    """
    Cleanup after running the tests. Remove the temporary directory.

    Args:
        request: A fixture from pytest.
        It provides several methods and attributes
        to inspect the "testing context" or
        to interact with the pytest runner.
    """

    def teardown():
        shutil.rmtree(f"./{TestDownloader.local_dir}")

    request.addfinalizer(teardown)
