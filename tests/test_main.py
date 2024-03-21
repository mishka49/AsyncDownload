import shutil
import tempfile

import pytest
import asyncio
from unittest.mock import patch, MagicMock

import sys

sys.path.append('C:/Different/Python/AsyncDownload/')

from main import print_sha256_results, main


def test_print_sha256_results(capsys):
    sha256_results = {
        'file1': 'hash1',
        'file2': 'hash2',
    }
    print_sha256_results(sha256_results)
    captured = capsys.readouterr()
    assert captured.out == 'file1 hash1\nfile2 hash2\n'


@pytest.mark.asyncio
async def test_main(capsys):
    with patch('repository.Repository') as mock_repo, \
            patch('download.Downloader') as mock_downloader, \
            patch('calculator_sha256.calculate_sha256_for_directory') as mock_calculator:
        mock_repo.return_value.HEAD_commit_files_paths = ['path1', 'path2']
        mock_downloader.return_value.run = MagicMock()
        mock_calculator.return_value = {'file1': 'hash1', 'file2': 'hash2'}

        await main()

        captured = capsys.readouterr()
        assert captured.out == 'file1 hash1\nfile2 hash2\n'


