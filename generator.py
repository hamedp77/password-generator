"""Password Generator

This python script allows the user to generate random passwords of various lengths and characters.
By default, it produces an 8-character long password including digits, uppercase and lowercase
letters and punctuation symbols. You can use it as a CLI tool as well.
To customize the length of the password or included characters check the help menu of the CLI.
"""

import argparse
import random
import string


def generator(length: int, use_digits: bool = True,
              use_symbols: bool = True, use_uppercase: bool = True) -> str:
    """Generate a random password of specified length and characters."""

    source_chars = string.ascii_lowercase
    if use_digits:
        source_chars += string.digits
    if use_symbols:
        source_chars += string.punctuation
    if use_uppercase:
        source_chars += string.ascii_uppercase

    source_chars_list = list(source_chars)
    random.shuffle(source_chars_list)
    source_chars = ''.join(source_chars_list)

    password = ''
    for _ in range(length):
        password += random.choice(source_chars)
    if use_digits and not check_min_digit(password):
        password = generator(length)
    if use_symbols and not check_min_symbols(password):
        password = generator(length)
    if use_uppercase and not check_min_uppercase(password):
        password = generator(length)
    return password


def check_min_digit(password: str) -> bool:
    """Check for minimum number of digits in the password.

    returns True if there is at least 1 digit in the password, False otherwise.
    """
    return any(char in string.digits for char in password)


def check_min_uppercase(password: str) -> bool:
    """Check for minimum number of uppercase letters in the password.

    returns True if there is at least 1 uppercase letter in the password, False otherwise.
    """
    return any(char.isupper() for char in password)


def check_min_symbols(password: str) -> bool:
    """Check for minimum number of symbols in the password.

    returns True if there is at least 1 symbol in the password, False otherwise.
    """
    return any(char in string.punctuation for char in password)


def main():
    """main function

    Argument parsing and calling the password generator function for the CLI happens here. 
    This way, the whole script can be imported as a module.
    """
    parser = argparse.ArgumentParser(
        description='A python CLI tool for generating random passwords ')

    parser.add_argument('-l', '--length', type=int, default=8,
                        nargs='?', help='Length of the generated password (default=8)')
    parser.add_argument('-c', '--count', type=int, default=1, nargs='?',
                        help='Number of passwords to be generated (default=1)')
    parser.add_argument('--no-digit', action='store_false',
                        dest='digits_allowed', help='Do not use digits in the password')
    parser.add_argument('--no-symbol', action='store_false',
                        dest='symbols_allowed', help='Do not use symbols in the password')
    parser.add_argument('--no-upper', action='store_false', dest='upper_allowed',
                        help='Do not use uppercase letters in the password')
    args = parser.parse_args()

    for _ in range(args.count):
        print(generator(args.length, args.digits_allowed,
                        args.symbols_allowed, args.upper_allowed))


if __name__ == '__main__':
    main()
