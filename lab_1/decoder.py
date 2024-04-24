import argparse

from sources.functions_for_tasks import read_json_file, text_to_file, read_the_file


def text_decryption(source_text_path: str, key_word_path: str, result_text_path: str) -> str:
    """
    This function receives the key for encryption,
    the path to the text for decryption and the path to the file which will contain the result
    and using the available key decodes the message, 
    after which it outputs a string as the result of the function

    Args:
        source_text_path (str): a string containing the path to the source text
        key_word_path (str): a string containing the path to the file with key word
        result_text_path (str): a string containing the path to the file with encrypted text

    Return:
        str: the decrypted text
    """
    key = read_json_file(key_word_path)
    text = read_the_file(source_text_path)

    result = ''
    for letter in text:
        result += key.get(letter, letter)
    print(result)

    text_to_file(result_text_path, result)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Post-columnar transposition",
        description="Text encryption by post-column transposition")
    parser.add_argument('input', type=str,
                        help='A file (.txt) with the source text')
    parser.add_argument(
        'key', type=str, help='A file (.txt) with an encryption key')
    parser.add_argument('output', type=str,
                        help='A file (.txt) containing encrypted text')

    args = parser.parse_args()

    text_decryption(args.input, args.key, args.output)


if __name__ == "__main__":
    main()

# python lab_1\\decoder.py lab_1\\sources\\task_2\\input.txt lab_1\\sources\\task_2\\key.json lab_1\\sources\\task_2\\output.txt
