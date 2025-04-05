# Python Password Generator

This repository contains a Python script that can generate strong, random passwords based on user-specified criteria. 
You can choose the desired length and whether to include lowercase letters, uppercase letters, digits, and symbols.

## Features

* **Customizable Length:** Specify the exact length of the password you need.
* **Character Set Options:** Control which types of characters are included:
    * Lowercase letters (a-z)
    * Uppercase letters (A-Z)
    * Digits (0-9)
    * Symbols (punctuation marks)
* **Command-Line Interface (CLI):** A simple text-based interface for generating passwords.
* **Graphical User Interface (GUI):** A user-friendly windowed application for easier interaction (available in `pass_generatorGUI.py`).
* **Input Validation:** Ensures that the password length is a positive integer and that character type choices are valid.
* **Copy to Clipboard (GUI):** Easily copy the generated password to your system's clipboard.

## Files in this Repository

* `password_generator.py`: The Python script for the command-line password generator.
* `pass_generatorGUI.py`: The Python script for the graphical user interface password generator (requires `tkinter`).
* `README.md`: This file, providing information about the project.

## How to Use

### Command-Line Interface

1.  **Save the script:** Download or clone the `password_generator.py` file to your local machine.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved the file using the `cd` command.
4.  **Run the script:**
    ```bash
    python password_generator.py
    ```
5.  **Follow the prompts:** The script will ask you for the desired password length and whether to include different character types (lowercase, uppercase, digits, symbols).
6.  **The generated password will be displayed** in the terminal.

### Graphical User Interface

1.  **Save the script:** Download or clone the `password_generator_gui.py` file to your local machine.
2.  **Make sure you have `tkinter` installed.** It's usually included with standard Python installations. If not, you might need to install it using your system's package manager (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).
3.  **Open your terminal or command prompt.**
4.  **Navigate to the directory** where you saved the file.
5.  **Run the GUI script:**
    ```bash
    python password_generator_gui.py
    ```
6.  **A window will appear** with options to set the password length and choose character types.
7.  **Click the "Generate Password" button** to create a new password.
8.  **The generated password will be displayed** in the output area.
9.  **Click the "Copy to Clipboard" button** to copy the password to your clipboard.

## Contributing

If you have any suggestions for improvements or find any bugs, feel free to open an issue or submit a pull request.
