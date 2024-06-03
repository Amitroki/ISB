import json

from typing import Dict

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

class Functions:

    @staticmethod
    def read_json_file(source_file_path: str) -> Dict[str, str]:
        try:
            with open(source_file_path, "r", encoding="UTF-8") as file:
                return json.loads(file.read())
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')

    @staticmethod
    def write_bytes(key: bytes, source_file_path: str) -> None:
        try:
            with open(source_file_path, 'wb') as key_file:
                key_file.write(key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def read_bytes(source_file_path: str) -> bytes:
        try:
            with open(source_file_path, 'rb') as file:
                return file.read()
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def read_file(source_file_path: str) -> str:
        try:
            with open(source_file_path, mode = "r", encoding='utf-8') as file:
                return file.read()
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')

    @staticmethod
    def write_file(text: str, source_file_path: str) -> str:
        try:
            with open(source_file_path, mode = "w", encoding='utf-8') as file:
                file.write(text)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def write_public_key(public_key: rsa.RSAPublicKey, path: str) -> None:
        try:
            with open(path, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')

    @staticmethod
    def write_private_key(private_key: rsa.RSAPrivateKey, path: str) -> None:
        try:
            with open(path, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                            encryption_algorithm=serialization.NoEncryption()))
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def read_private_key(source_file_path: str) -> rsa.RSAPrivateKey:
        try:
            with open(source_file_path, "rb") as file:
                return load_pem_private_key(file.read(), password=None)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
        
    @staticmethod
    def read_public_key(source_file_path: str) -> rsa.RSAPublicKey:
        try:
            with open(source_file_path, "rb") as file:
                return load_pem_public_key(file.read())
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')