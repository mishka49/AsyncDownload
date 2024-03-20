"""Module to testing Downloader class"""

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
        os.rmdir(f"./{TestDownloader.local_dir}")

    request.addfinalizer(teardown)
