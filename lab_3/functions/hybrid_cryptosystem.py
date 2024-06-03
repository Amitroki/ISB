from functions.asymetric_algorithm import AsymmetricCriptography
from functions.general_functions import Functions
from functions.symmetric_algorithm import SymmetricCryptography


class HybridCriptography:
    @staticmethod
    def generate_keys(path_to_the_symmetric_key: str, path_to_the_private_key: str, path_to_the_public_key: str,) -> None:
        """
        This function allows you to generate symmetric, 
        private and public (asymmetric) encryption keys

        Args:
            path_to_the_symmetric_key (str): The path to the file that will contain the symmetric key
            path_to_the_private_key (str): The path to the file that will contain the private key
            path_to_the_public_key (str): The path to the file that will contain the public key

        Raises:
            Exception: Signals about any error in the key generation process
        """
        try:
            symmetric = SymmetricCryptography.generate_key(16)
            private, public = AsymmetricCriptography.generate_asymmetric_keys()
            symmetric_key = AsymmetricCriptography.encrypt_key(
                symmetric, public)
            Functions.write_bytes(symmetric_key, path_to_the_symmetric_key)
            Functions.write_private_key(private, path_to_the_private_key)
            Functions.write_public_key(public, path_to_the_public_key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')

    @staticmethod
    def encrypt_the_text(path_to_the_default_text: str, path_to_the_encrypted_text: str, path_to_the_symmetric_key: str, path_to_the_private_key: str) -> None:
        """
        This function reads the key encrypted with an asymmetric algorithm from a file, 
        decrypts it with a private key, and then uses it to encrypt the source text

        Args:
            path_to_the_default_text (str): The path to the file that contain the source text
            path_to_the_encrypted_text (str): The path to the file that will contain the encrypted text
            path_to_the_symmetric_key (str): The path to the file that contain the symmetric key
            path_to_the_private_key (str): The path to the file that contain the private key

        Raises:
            Exception: Signals about any error in the encryption process
        """
        try:
            private_key = Functions.read_private_key(path_to_the_private_key)
            encrypted_key = SymmetricCryptography.deserialize_key(
                path_to_the_symmetric_key)
            symmetric_key = AsymmetricCriptography.decrypt_key(
                encrypted_key, private_key)
            SymmetricCryptography.encrypt(
                path_to_the_default_text, path_to_the_encrypted_text, symmetric_key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')

    @staticmethod
    def decrypt_the_text(path_to_the_encrypted_text: str, path_to_the_decrypted_text: str, path_to_the_symmetric_key: str, path_to_the_private_key: str) -> None:
        """
        This function reads the key encrypted with an asymmetric algorithm from a file, 
        decrypts it with a private key, and then uses it to decrypt the encrypted text

        Args:
            path_to_the_encrypted_text (str): The path to the file that contain the encryted text
            path_to_the_decrypted_text (str): The path to the file that will contain the decrypted text
            path_to_the_symmetric_key (str): The path to the file that contain the symmetric key
            path_to_the_private_key (str): The path to the file that contain the private key

        Raises:
            Exception: Signals about any error in the decryption process
        """
        try:
            private_key = Functions.read_private_key(path_to_the_private_key)
            encrypted_key = SymmetricCryptography.deserialize_key(
                path_to_the_symmetric_key)
            symmetric_key = AsymmetricCriptography.decrypt_key(
                encrypted_key, private_key)
            SymmetricCryptography.decrypt(
                path_to_the_encrypted_text, path_to_the_decrypted_text, symmetric_key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
