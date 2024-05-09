import argparse

from functions import read_the_file, frequency_bitwise_test, same_consecutive_bits_test, longest_sequence_of_units_in_a_block_test


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Statistical analysis of pseudorandom sequences")
    parser.add_argument('cxx', type=str,
                        help='A file (.txt) with the sequence')

    args = parser.parse_args()

    sequence = read_the_file(args.cxx)
    print(f"C++ sequence: {sequence}")
    print(f"1 test result: {frequency_bitwise_test(sequence)}")
    print(f"2 test result: {same_consecutive_bits_test(sequence)}")
    print(f"3 test result: {longest_sequence_of_units_in_a_block_test(sequence)}")


if __name__ == "__main__":
    main()

# python lab_2\\nist.py lab_2\\results\\cxx.txt