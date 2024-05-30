import os

from general_functions import write_bytes


class SymmetricCryptography:

    @staticmethod
    def generate_key(size: int) -> bytes:
        return os.urandom(size)

    @staticmethod
    def serialize_key(path: str, key: bytes) -> None:
        try:
            write_bytes(path, key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
