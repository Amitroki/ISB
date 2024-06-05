import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from functions.general_functions import Functions


class SymmetricCryptography:

    @staticmethod
    def generate_key(byte_size=16) -> bytes:
        """
        This function generates a random key of 16 bytes (128 bits) in size

        Args:
            byte_size (int, optional): A value that displays the required number of bytes in a symmetric key. Defaults to 16.

        Returns:
            bytes: byte representation of the key
        """
        return os.urandom(byte_size)

    @staticmethod
    def encrypt(path_to_text: str, path_to_encrypted_text: str, key: bytes) -> None:
        """
        This function uses a decrypted symmetric key 
        to encrypt the source text read from the file, 
        and then writes the resulting path to the encrypted file using the specified parameter

        Args:
            path_to_text (str): The path to the file that contain the source text
            path_to_encrypted_text (str): The path to the file that will contain the encrypted text
            key (bytes): Decrypted symmetric key

        Raises:
            Exception: Indicates any problems during text encryption
        """
        try:
            text_for_encryption = Functions.read_file(path_to_text)

            padder = padding.ANSIX923(16).padder()
            text: bytes = bytes(text_for_encryption, "UTF-8")
            padded_text: bytes = padder.update(text) + padder.finalize()
            iv: bytes = os.urandom(8)
            cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            c_text: bytes = iv + \
                encryptor.update(padded_text) + encryptor.finalize()

            Functions.write_bytes(c_text, path_to_encrypted_text)
        except Exception as error:
            raise Exception(f'There is a troubleQ: {error}')

    @staticmethod
    def decrypt(path_to_text: str, path_to_decrypted_text: str, key: bytes) -> None:
        """
        This function uses a decrypted symmetric key 
        to decrypt the encrypted text read from the file, 
        and then writes the resulting text to the decrypted file

        Args:
            path_to_text (str): The path to the file that contain the encrypted text
            path_to_decrypted_text (str): The path to the file that will contain the decrypted text
            key (bytes): Decrypted symmetric key

        Raises:
            Exception: Indicates any problems during text decryption
        """
        try:
            default_text = Functions.read_bytes(path_to_text)

            iv = default_text[:8]
            text_for_decryption = default_text[8:]

            cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
            decrypt = cipher.decryptor()

            unpacker_text = decrypt.update(
                text_for_decryption) + decrypt.finalize()
            decrypt_text = unpacker_text.decode('UTF-8')

            Functions.write_file(decrypt_text, path_to_decrypted_text)
        except Exception as error:
            raise Exception(f'There is a troubleQ: {error}')
