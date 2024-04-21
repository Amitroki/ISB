def convert_the_file_to_text(input_file_name: str) -> str:
    """
    This function takes the path to the file, 
    checks whether it can be opened 
    and, if possible, converts the text from the file to a string variable, 
    and if impossible, throws an exception

    Args:
        input_file_name (str): a string containing the path to the file

    Raises:
        Exception: an exception appears if the path to the file is incorrect (if it cannot be opened)

    Returns:
        str: text from the file
    """
    try:
        text = ""
        with open(input_file_name, "r", encoding="UTF-8") as file:
            text = file.read()
        return text
    except Exception as error:
        raise Exception(f'There is a trouble: {error}')
    
def message_encryption(key_word: str, source_text: str) -> str:
    """
    This function receives the key for encryption, 
    the text for encryption and, through the use of column-by-column transposition, 
    encrypts the text, after which it outputs a string as the result of the function

    Args:
        source_text (str): a string containing the source text
        key_word (str): a string containing the key word

    Returns:
        str: encrypted text
    """
    result = ''
    matrix = []
    key = key_word.lower()

    text_len = len(source_text)
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
            row.append(source_text[index % len(source_text)])
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

    return result

def main():
    phrase = convert_the_file_to_text(
        r'C:\Users\Alex\Desktop\ISB_test_file.txt')
    print(phrase)
    print(len(phrase))
    key = "пропилпарагидроксибензоат"
    encrypted_text = message_encryption(key, phrase)
    print(encrypted_text)



if __name__ == "__main__":
    main()
