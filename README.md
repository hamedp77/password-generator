# About this script

This python script allows you to generate random passwords of various lengths and characters. By default, it produces an 8-character long password including digits, symbols, uppercase and lowercase letters. You can use it as a CLI tool as well as importing it as a module in your own Python project.

## Usage

### Command Line

1. Make sure you have Python installed on your system
2. Clone the project using `git clone https://github.com/hamedp77/password-generator.git`
3. While in the project's root directory, run the script using `python generator.py`

#### Options

- To generate a password with custom length use `-l` or `--length`
- To generate more than one password use `-c` or `--count`
- If you don't want the password(s) to contain digits, use `--no-digit`
- If you don't want the password(s) to contain symbols, use `--no-symbol`
- If you don't want the password(s) to contain uppercase letters, use `--no-upper`
- If you don't want the password(s) to contain lowercase letters, use `--no-lower`
- **Note**: If you ommit all the possible characters, the resulting password will **only** contain lowercase letters.

### As a module

You can clone the project in your app's directory and then import it in your code or just copy the raw content of the `generator.py` to a file in your machine and then import that.

After importing the module, you can call `generate_password()` from the module which returns a password in string format with the default attributes. Default behavior is a password with 8 random characters including **at least** 1 digit, 1 symbol, 1 lowercase letter and 1 uppercase letter. Pass appropriate arguments to the function in order to override the defaults.

- **Warning**: Password length **should not be less than 4** and if so, it will raise a ValueError exception. A strong password is usually between 14-16 characters long.
- **Note**: If you ommit all the possible characters, the resulting password will **only** contain lowercase letters.
