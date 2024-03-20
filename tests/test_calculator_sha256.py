"""Module for testing the calculator_sha256 module."""

import hashlib
from pathlib import Path

import pytest

import calculator_sha256 as calculator


class TestCalculator:
    """Class for testing calculator_sha256 module."""

    @pytest.fixture
    def create_temp_directory(self, tmp_path):
        """Create a temporary directory with two files.

        Args:
            tmp_path (Path): The path of the temporary directory.

        Returns:
            Path: The path of the temporary directory.
        """
        temp_dir = tmp_path

        file1 = temp_dir / "file1.txt"
        file2 = temp_dir / "file2.txt"
        with open(file1, "w") as f1, open(file2, "w") as f2:
            f1.write("File 1 content")
            f2.write("File 2 content")

        return temp_dir

    @pytest.fixture
    def create_temp_file(self, tmp_path):
        """Create a temporary file.

        Args:
            tmp_path (Path): The path of the temporary directory.

        Returns:
            Path: The path of the temporary file.
        """
        temp_dir = tmp_path
        file1 = temp_dir / "file1.txt"

        with open(file1, "w") as f1:
            f1.write("File 1 content")

        return file1

    def test_calculate_sha256_for_file(self, create_temp_file):
        """Test the calculate_sha256_for_file function."""
        file_path = create_temp_file
        expected_hash = hashlib.sha256(b"File 1 content").hexdigest()

        actual_hash = calculator.calculate_sha256_for_file(file_path)

        assert actual_hash == expected_hash

    def test_calculate_sha256_for_directory(self, create_temp_directory):
        """Test the calculate_sha256_for_directory function."""
        temp_dir = create_temp_directory

        expected_hashes = {
            "file1.txt": hashlib.sha256(b"File 1 content").hexdigest(),
            "file2.txt": hashlib.sha256(b"File 2 content").hexdigest(),
        }

        actual_hashes = calculator.calculate_sha256_for_directory(temp_dir)

        assert actual_hashes == expected_hashes
