import os

from general_functions import write_bytes, read_bytes


class SymmetricCryptography:

    def __init__(self):
        self.key = None

    @staticmethod
    def generate_key(self, size=16) -> bytes:
        self.key = os.urandom(size)

    @staticmethod
    def serialize_key(source_file_path: str, key: bytes) -> None:
        try:
            write_bytes(source_file_path, key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def deserialize_key(source_file_path: str) -> bytes:
        try:
            return read_bytes(source_file_path)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
    
