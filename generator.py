"""Password Generator

This python script allows the user to generate random passwords of various lengths and characters.
By default, it produces an 8-character long password including digits, symbols,
uppercase and lowercase letters. You can use it as a CLI tool as well.
To customize the length of the password or included characters check the help menu of the CLI.
"""

import random
import string


def generate_password(length: int = 8, use_digits: bool = True,
                      use_symbols: bool = True, use_uppercase: bool = True,
                      use_lowercase: bool = True) -> str:
    """Generate a random password of specified length and characters.

    By default, it returns an 8-character long password including digits, symbols,
    uppercase and lowercase letters. Pass appropriate parameters to customize
    the generated password. Passwords with a length of less than 4 will throw exception.
    If you ommit all the possible characters the resulting password will ONLY contain
    lowercase letters.
    """

    # throw an exception for lengths less than 4
    if length < 4:
        raise ValueError('length should not be less than 4.')

    # preparing the source characters based on user input
    source_chars = []
    if use_digits:
        source_chars.extend(string.digits)
    if use_symbols:
        source_chars.extend(string.punctuation)
    if use_uppercase:
        source_chars.extend(string.ascii_uppercase)
    if use_lowercase:
        source_chars.extend(string.ascii_lowercase)

    # making sure source_chars is populated with lowercase letters if all the flags are set to False
    if not source_chars:
        source_chars.extend(string.ascii_lowercase)
        use_lowercase = True

    # shuffling the base characters (for better randomness?)
    random.shuffle(source_chars)

    # generating the password and making sure conditions are met
    password = ''.join(random.choices(source_chars, k=length))
    if use_digits and not check_min_digit(password):
        generate_password(length, use_digits, use_symbols,
                          use_uppercase, use_lowercase)
    if use_symbols and not check_min_symbols(password):
        generate_password(length, use_digits, use_symbols,
                          use_uppercase, use_lowercase)
    if use_uppercase and not check_min_uppercase(password):
        generate_password(length, use_digits, use_symbols,
                          use_uppercase, use_lowercase)
    if use_lowercase and not check_min_lowercase(password):
        generate_password(length, use_digits, use_symbols,
                          use_uppercase, use_lowercase)

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


def check_min_lowercase(password: str) -> bool:
    """Check for minimum number of lowercase letters in the password.

    returns True if there is at least 1 lowercase letter in the password, False otherwise.
    """

    return any(char.islower() for char in password)


def check_min_symbols(password: str) -> bool:
    """Check for minimum number of symbols in the password.

    returns True if there is at least 1 symbol in the password, False otherwise.
    """

    return any(char in string.punctuation for char in password)


def main():
    """main function

    Argument parsing and calling the password generator function for the CLI happens here. 
    This way, the whole script can be imported and used as a module.
    """

    import argparse

    parser = argparse.ArgumentParser(
        description='A python CLI tool for generating random passwords ')

    parser.add_argument('-l', '--length', type=int, default=8,
                        nargs='?', help='Length of the generated password (>=4, default=8)')
    parser.add_argument('-c', '--count', type=int, default=1, nargs='?',
                        help='Number of passwords to be generated (default=1)')
    parser.add_argument('--no-digit', action='store_false',
                        dest='digits_allowed', help='Do not use digits in the password')
    parser.add_argument('--no-symbol', action='store_false',
                        dest='symbols_allowed', help='Do not use symbols in the password')
    parser.add_argument('--no-upper', action='store_false', dest='upper_allowed',
                        help='Do not use uppercase letters in the password')
    parser.add_argument('--no-lower', action='store_false', dest='lower_allowed',
                        help='Do not user lowercase letters in the password')
    args = parser.parse_args()

    if args.count < 1:
        print('Count must be more than 0')
        exit()

    for _ in range(args.count):
        print('|', '-' * (args.length + 4), '|', sep='')
        print('|  ', end='')
        print(generate_password(args.length,
                                args.digits_allowed,
                                args.symbols_allowed,
                                args.upper_allowed,
                                args.lower_allowed
                                ), end=''
              )
        print('  |')
    print('|', '-' * (args.length + 4), '|', sep='', end='')


if __name__ == '__main__':
    main()
