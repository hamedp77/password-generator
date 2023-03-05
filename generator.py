import argparse
import random
import string
# from time import perf_counter

parser = argparse.ArgumentParser(
    description='A python CLI tool for generating random passwords ')

parser.add_argument('-l', '--length', type=int, default=8,
                    nargs='?', help='Length of the generated password (between 5-32, default=8)')
parser.add_argument('-c', '--count', type=int, default=1, nargs='?',
                   help='Number of passwords to be generated (default=1)')
parser.add_argument('--no-digit', action='store_false',
                    dest='digits_allowed', help='Do not use digits in the password')
parser.add_argument('--no-symbol', action='store_false',
                    dest='symbols_allowed', help='Do not use symbols in the password')
parser.add_argument('--no-upper', action='store_false', dest='upper_allowed',
                    help='Do not use uppercase letters in the password')

args = parser.parse_args()

INCLUDE_DIGITS = args.digits_allowed
INCLUDE_SYMBOLS = args.symbols_allowed
INCLUDE_UPPERCASE = args.upper_allowed


def generator(length: int) -> str:
    """"Generate a random password of specified length and characters.


    """
    source_chars = string.ascii_lowercase
    if INCLUDE_DIGITS:
        source_chars += string.digits
    if INCLUDE_SYMBOLS:
        source_chars += string.punctuation
    if INCLUDE_UPPERCASE:
        source_chars += string.ascii_uppercase

    password = ''
    for i in range(length):
        password += random.choice(source_chars)
    if INCLUDE_DIGITS and not check_min_digit(password):
        generator(length)
    if INCLUDE_SYMBOLS and not check_min_symbols(password):
        generator(length)
    if INCLUDE_UPPERCASE and not check_min_uppercase(password):
        generator(length)
    return password


def check_min_digit(password: str) -> bool:
    for c in string.digits:
        if c in password:
            return True
    return False


def check_min_uppercase(password: str) -> bool:
    for c in string.ascii_uppercase:
        if c in password:
            return True
    return False


def check_min_symbols(password: str) -> bool:
    for c in string.punctuation:
        if c in password:
            return True
    return False


for i in range(args.count):
    print(generator(args.length))
