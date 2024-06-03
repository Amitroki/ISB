from functions.symmetric_algorithm import SymmetricCryptography
from functions.asymetric_algorithm import AsymmetricCriptography
from functions.general_functions import Functions

class HybridCriptography:
    @staticmethod
    def generate_keys(path_to_the_symmetric_key: str, path_to_the_private_key: str, path_to_the_public_key: str,) -> None:
        symmetric = SymmetricCryptography.generate_key(16)
        private, public = AsymmetricCriptography.generate_asymmetric_keys()
        symmetric_key = AsymmetricCriptography.encrypt_key(
            symmetric, public)
        Functions.write_bytes(symmetric_key, path_to_the_symmetric_key)
        Functions.write_private_key(private, path_to_the_private_key)
        Functions.write_public_key(public, path_to_the_public_key)

    @staticmethod
    def encrypt_the_text(path_to_the_default_text: str, path_to_the_encrypted_text: str, path_to_the_symmetric_key: str, path_to_the_private_key: str) -> None:
        try:
            private_key = Functions.read_private_key(path_to_the_private_key)
            encrypted_key = SymmetricCryptography.deserialize_key(path_to_the_symmetric_key)
            symmetric_key = AsymmetricCriptography.decrypt_key(encrypted_key, private_key)
            SymmetricCryptography.encrypt(path_to_the_default_text, path_to_the_encrypted_text, symmetric_key)
        except Exception as error:
            raise Exception(f'There is a trouble1: {error}')

    @staticmethod
    def decrypt_the_text(path_to_the_encrypted_text: str, path_to_the_decrypted_text: str, path_to_the_symmetric_key: str, path_to_the_private_key: str) -> None:
        private_key = Functions.read_private_key(path_to_the_private_key)
        encrypted_key = SymmetricCryptography.deserialize_key(path_to_the_symmetric_key)
        symmetric_key = AsymmetricCriptography.decrypt_key(encrypted_key, private_key)
        SymmetricCryptography.decrypt(path_to_the_encrypted_text, path_to_the_decrypted_text, symmetric_key)
