def read_the_file(input_file_name: str) -> str:
    """

    This function takes the path to the file, 
    checks whether it can be opened 
    and, if possible, converts the text from the file to a string variable, 
    and if impossible, throws an exception

    Args:
        input_file_name (str): a string containing the path to the file

    Raises:
        Exception: an exception appears if the file can not be opened

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


def text_to_file(output_file_path: str, text_for_file: str) -> None:
    """

    This function writes the text passed to it 
    to the file passed to it (the path to this file is passed to the function), 
    and if this is not possible, throws an exception

    Args:
        output_file_path (str): a string containing the path to the file to write to
        text_for_file (str): the text that will be written to the file, in the form of a string

    Raises:
        Exception: an exception appears if the file can not be opened

    """    
    try:
        with open(output_file_path, "w", encoding="UTF-8") as file:
            file.write(text_for_file)
    except Exception as error:
<<<<<<< HEAD
        raise Exception(f'There is a trouble: {error}')
=======
        raise Exception(f'There is a trouble: {error}')
>>>>>>> 772d72edee08094fc6481143da125742ac74f803
