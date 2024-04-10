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
    except FileNotFoundError:
        raise Exception(f'Your path ({input_file_name}) is incorrect!')


def main():
    phrase = convert_the_file_to_text(
        r'C:\Users\Alex\Desktop\ISB_test_file.txt')
    print(phrase)


if __name__ == "__main__":
    main()
