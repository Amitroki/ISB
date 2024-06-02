import argparse

from functions.hybrid_cryptosystem import HybridCriptography
from functions.general_functions import Functions

def main() -> None:
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation', help='Key generation mode', action="store_true")
    group.add_argument('-enc','--encryption', help='Text encryption mode', action="store_true")
    group.add_argument('-dec','--decryption', help='Text decryption mode', action="store_true")
    parser.add_argument('-p', '--paths', help = 'Path to json file with paths')

    args = parser.parse_args()

    paths = Functions.read_json_file(args.paths)

    if args.generation is not None:
        HybridCriptography.generate_keys(paths["symmetric_key"], paths["secret_key"], paths["public_key"])
    elif args.encryption is not None:
        HybridCriptography.encrypt_the_text(paths["initial_file"], paths["encrypted_file"], paths["symmetric_key"], paths["secret_key"])
    else:
        HybridCriptography.decrypt_the_text(paths["encrypted_file"], paths["decrypted_file"], paths["symmetric_key"], paths["secret_key"])

if __name__ == "__main__":
    main()

# python lab_3\\main.py -gen -p lab_3\\settings.json - ввести в терминал для генерации ключей