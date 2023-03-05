import argparse
import random
import string
# from time import perf_counter

INCLUDE_DIGITS = True
INCLUDE_SYMBOLS = True
INCLUDE_UPPERCASE = True


def generator(length: int = 8) -> str:
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


for i in range(5):
    print(generator(32))
