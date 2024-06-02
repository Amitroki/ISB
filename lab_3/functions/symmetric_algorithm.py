import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from general_functions import Functions


class SymmetricCryptography:

    @staticmethod
    def generate_key(byte_size=16) -> bytes:
        return os.urandom(byte_size)
    
    @staticmethod
    def serialize_key(source_file_path: str, key: bytes) -> None:
        try:
            Functions.write_bytes(key, source_file_path)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}') 
        
    @staticmethod
    def deserialize_key(source_file_path: str) -> bytes:
        try:
            return  Functions.read_bytes(source_file_path)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def encrypt(path_to_text: str, path_to_encrypted_text: str, key: bytes) -> None:
        text_for_encryption = Functions.read_file(path_to_text)

        padder = padding.ANSIX923(128).padder()
        text = bytes(text, "UTF-8")
        padded_text = padder.update(text) + padder.finalize()

        iv = os.urandom(16)
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        encryptor = cipher.encryptor()    
