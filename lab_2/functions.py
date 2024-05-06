import math

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
    
def frequency_bitwise_test(sequence: str) -> float:
    """
    the function receives a string containing a sequence, 
    after which it counts the sum of its elements (if the element is 1, 
    then it is added as 1 to this sum, if 0 - then as -1), 
    divides by the square root of the number of elements in the sequence, 
    after which the P value is calculated using the special error function erfc

    Args:
        sequence (str): a string containing a sequence of 0 and 1

    Returns:
        float: the P value for the frequency bitwise test
    """    
    s = 0
    for i in len(sequence):
        element = (1 if sequence[i] == '1' else -1)
        s += element
    s /= math.sqrt(len(sequence))
    return math.erfc(s/math.sqrt(2))