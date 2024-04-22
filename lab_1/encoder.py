import argparse

from sources.functions_for_tasks import read_the_file, text_to_file, checking_the_correctness_of_the_key


def message_encryption(key_word_path: str, source_text_path: str, result_text_path: str) -> str:
    """
    This function receives the key for encryption, 
    the path to the text for encryption and the path to the file which will contain the result 
    and, through the use of column-by-column transposition, 
    encrypts the text, after which it outputs a string as the result of the function

    Args:
        source_text (str): a string containing the path to the source text
        key_word (str): a string containing the path to the file with key word
        result (str): a string containing the path to the file with encrypted text
    """
    result = ''
    matrix = []
    key = read_the_file(key_word_path)
    key = key.lower()

    text = read_the_file(source_text_path)
    text_len = len(text)
    key_len = len(key)
    """
    In this part, each letter of the original text is written into an array, 
    the number of columns in which is equal to the length of the key word, 
    and the number of rows is equal to the rounded up division 
    of the number of characters in the text by the length of the key
    """
    index = 0
    if text_len % key_len != 0:
        text_len += key_len - (text_len % key_len)
    for i in range(text_len // key_len):
        row = []
        for j in range(key_len):
            row.append(text[index % len(text)])
            index += 1
        matrix.append(row)
    """
    In this part, the columns according to the sorted order of letters in the key 
    will be written in the top-down order into the encrypted message
    """
    sorted_key = sorted(key)
    for i in range(key_len):
        column = key.find(sorted_key[i])
        for j in range(text_len // key_len):
            result += matrix[j][column]

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

    if (checking_the_correctness_of_the_key(args.key) == False):
        print("Use a keyword without duplicate letters!")
        return
    
    message_encryption(args.key, args.input, args.output)


if __name__ == "__main__":
    main()

# python lab_1\\encoder.py lab_1\\sources\\task_1\\input.txt lab_1\\sources\\task_1\\key_word.txt lab_1\\sources\\task_1\\output.txt
