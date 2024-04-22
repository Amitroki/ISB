import argparse

from collections import Counter

from sources.functions_for_tasks import read_the_file, text_to_file


def find_the_frequency_dictionary(source_text_path: str, output_file_path: str) -> None:
    """
    This function reads the text from the file, 
    the path to which is specified in the parameters during transmission, 
    counts the frequency of occurrence in the text for each character 
    and writes the frequency dictionary to the path to the final file transmitted in the parameters

    Args:
        source_text_path (str): a string containing the path to the source file
        output_file_path (_type_): a string containing the path to the resulting file
    """
    text = read_the_file(source_text_path)
    letter_counter = Counter(text)
    text_len = len(text)
    table = ''
    for key, value in letter_counter.most_common():
        table += f"{key} : {round(value / text_len, 5)}\n"
    text_to_file(output_file_path, table)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Counting the frequency of occurrence of characters")
    parser.add_argument('input', type=str,
                        help='A file (.txt) with the source text')
    parser.add_argument('frequency_dictionary', type=str,
                        help='A file (.txt) containing the table with symbols and their frequency')

    args = parser.parse_args()

    find_the_frequency_dictionary(args.input, args.frequency_dictionary)


if __name__ == "__main__":
    main()

# python lab_1\\frequency_analysis.py lab_1\\sources\\task_2\\input.txt lab_1\\sources\\task_2\\frequency.txt
