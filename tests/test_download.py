import asyncio
import copy
import os
import tempfile

import pytest

from download import Download

import requests


class TestDownload:
    base_url = "https://gitea.radium.group/radium/project-configuration"
    paths = ["file1.txt", "file2.txt, file3.txt, file4.txt"]
    local_dir = tempfile.mkdtemp(dir="./")

    def test_request_response(self):
        response = requests.get(self.base_url)

        assert response.ok

    @pytest.mark.asyncio(scope="module")
    async def test_number_of_stream(self, mocker):
        mocker.patch('download.Download.download_file', return_value=None)
        instance = Download(TestDownload.paths, TestDownload.base_url, TestDownload.local_dir)

        tasks = await instance.run()

        assert instance.NUMBER_OF_STREAMS == len(tasks)

    def test_download_files(self, mocker):
        def create_files():
            for filename in TestDownload.paths:
                with open(f"{TestDownload.local_dir}/{filename}", "w"):
                    pass  # Create an empty file

        def get_list_of_files():
            return [f for f in os.listdir(TestDownload.local_dir)]

        mocker.patch('download.Download.download_file', side_effect=create_files(), return_value=None)

        instance = Download(copy.deepcopy(TestDownload.paths), TestDownload.base_url, TestDownload.local_dir)
        instance.run()

        assert TestDownload.paths == get_list_of_files()


@pytest.fixture(scope='class', autouse=True)
def cleanup_after_class(request):
    def teardown():
        os.rmdir(f"./{TestDownload.local_dir}")

    request.addfinalizer(teardown)
