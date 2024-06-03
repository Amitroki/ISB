from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes

class AsymmetricCriptography:

    @staticmethod
    def generate_asymmetric_keys() -> tuple:
        """
        This function creates private and public keys for asymmetric encryption

        Returns:
            tuple: Private and public keys
        """        
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return keys, keys.public_key()

    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        This function encrypts a symmetric key with an asymmetric public key

        Args:
            symmetric_key (bytes): The symmetric key
            public_key (rsa.RSAPublicKey): The public key

        Returns:
            bytes: Encrypted symmetric key
        """        
        return public_key.encrypt(symmetric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

    @staticmethod
    def decrypt_key(symmeric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        This function decrypts the symmetric key with a private asymmetric key

        Args:
            symmeric_key (bytes): The symmetric key
            private_key (rsa.RSAPrivateKey): The private key

        Returns:
            bytes: Decrypted symmetric key
        """        
        return private_key.decrypt(symmeric_key, padding.OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

