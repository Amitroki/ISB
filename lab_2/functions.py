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
    This function receives a string containing a sequence, 
    after which it counts the sum of its elements (if the element is 1, 
    then it is added as 1 to this sum, if 0 - then as -1), 
    divides by the square root of the number of elements in the sequence, 
    after which the P value is calculated using the special error function erfc

    Args:
        sequence (str): a string containing a sequence of 0 and 1

    Returns:
        float: the P value for the frequency bitwise test
    """
    s = abs(sum(list(map(lambda x: 1 if x == '1' else -1, sequence)))) / \
        math.sqrt(len(sequence))
    return math.erfc(s / math.sqrt(2))


def same_consecutive_bits_test(sequence: str) -> float:
    """
    This function searches for all sequences of identical bits, after which the number and sizes of these sequences are analyzed for compliance with a truly random reference sequence (in short, set the frequency of 1 and 0 shifts)

    Args:
        sequence (str): a string containing a sequence of 0 and 1

    Returns:
        float: the P value for the to test for the same consecutive bits
    """
    zeta = sum(list(map(lambda x: 1 if x == '1' else 0, sequence))
               ) / len(sequence)
    if abs(zeta - 1 / 2) < 2 / math.sqrt(len(sequence)):
        v = 0
        for i in range(len(sequence) - 1):
            v += 0 if sequence[i] == sequence[i + 1] else 1
        p = math.erfc((abs(v - 2 * len(sequence) * zeta * (1 - zeta))) /
                      (2 * math.sqrt(2 * len(sequence)) * zeta * (1 - zeta)))
    else:
        return 0
    return p
