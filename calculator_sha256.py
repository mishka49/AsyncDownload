import hashlib
import os

class Calculator:
    @staticmethod
    def calculate_sha256_for_file(file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    @staticmethod
    def calculate_sha256_for_directory(directory_path):
        sha256_dict = {}
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                sha256_hash = Calculator.calculate_sha256_for_file(file_path)
                sha256_dict[file] = sha256_hash
        return sha256_dict


