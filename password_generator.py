import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generates a random password with specified criteria."""

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character type must be selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            password_length_str = input("Enter the desired password length: ")
            password_length = int(password_length_str)
            if password_length <= 0:
                print("Password length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

    while True:
        include_lowercase_input = input("Include lowercase letters? (y/n): ").lower()
        if include_lowercase_input in ['y', 'n']:
            include_lowercase = include_lowercase_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    while True:
        include_uppercase_input = input("Include uppercase letters? (y/n): ").lower()
        if include_uppercase_input in ['y', 'n']:
            include_uppercase = include_uppercase_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    while True:
        include_digits_input = input("Include digits? (y/n): ").lower()
        if include_digits_input in ['y', 'n']:
            include_digits = include_digits_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    while True:
        include_symbols_input = input("Include symbols? (y/n): ").lower()
        if include_symbols_input in ['y', 'n']:
            include_symbols = include_symbols_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    generated_password = generate_password(
        length=password_length,
        use_lowercase=include_lowercase,
        use_uppercase=include_uppercase,
        use_digits=include_digits,
        use_symbols=include_symbols
    )

    print("\nGenerated Password:", generated_password)