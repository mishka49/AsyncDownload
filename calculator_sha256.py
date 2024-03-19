"""Module for calculating SHA256 hash for files and directories."""

import hashlib
from pathlib import Path

CHUNK_SIZE = 4096  # Size of the chunk to read and update hash.


def read_chunks(file_stream):
    """Read file in chunks.

    Args:
        file_stream (file): The file stream to read from.

    Yields:
        bytes: The next chunk of the file.
    """
    while True:
        chunk = file_stream.read(CHUNK_SIZE)
        if not chunk:
            break
        yield chunk


def calculate_sha256_for_file(file_path: Path) -> str:
    """Calculate SHA256 hash for a file.

    Args:
        file_path (Path): The path of the file.

    Returns:
        str: The SHA256 hash of the file.
    """
    sha256_hash = hashlib.sha256()
    with file_path.open('rb') as opened_file:
        for chunk in read_chunks(opened_file):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def calculate_sha256_for_directory(directory_path: str) -> dict:
    """Calculate SHA256 hash for all files in a directory.

    Args:
        directory_path (str): The path of the directory.

    Returns:
        dict: A dictionary where the keys are the file names
         and the values are the SHA256 hashes.
    """
    directory_path = Path(directory_path)
    sha256_dict = {}
    for file_path in directory_path.rglob('*'):
        if file_path.is_file():
            sha256_hash = calculate_sha256_for_file(file_path)
            sha256_dict[file_path.name] = sha256_hash
    return sha256_dict
