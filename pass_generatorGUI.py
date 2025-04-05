import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

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

def generate_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input for password length.")
        return

    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    generated_password = generate_password(
        length=length,
        use_lowercase=include_lowercase,
        use_uppercase=include_uppercase,
        use_digits=include_digits,
        use_symbols=include_symbols
    )

    password_output.config(state=tk.NORMAL)  # Enable editing of the text widget
    password_output.delete(1.0, tk.END)      # Clear previous content
    password_output.insert(tk.END, generated_password)
    password_output.config(state=tk.DISABLED) # Disable editing

def copy_to_clipboard():
    generated_password = password_output.get(1.0, tk.END).strip()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showinfo("Info", "No password generated yet.")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")

# --- Input Frame ---
input_frame = ttk.LabelFrame(root, text="Password Options", padding=10)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Length Label and Entry
length_label = ttk.Label(input_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_entry = ttk.Entry(input_frame, width=10)
length_entry.insert(0, "12")  # Default length
length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Checkboxes for character types
lowercase_var = tk.BooleanVar(value=True)
lowercase_check = ttk.Checkbutton(input_frame, text="Include Lowercase", variable=lowercase_var)
lowercase_check.grid(row=1, column=0, padx=5, pady=2, sticky="w")

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = ttk.Checkbutton(input_frame, text="Include Uppercase", variable=uppercase_var)
uppercase_check.grid(row=2, column=0, padx=5, pady=2, sticky="w")

digits_var = tk.BooleanVar(value=True)
digits_check = ttk.Checkbutton(input_frame, text="Include Digits", variable=digits_var)
digits_check.grid(row=1, column=1, padx=5, pady=2, sticky="w")

symbols_var = tk.BooleanVar(value=True)
symbols_check = ttk.Checkbutton(input_frame, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=2, column=1, padx=5, pady=2, sticky="w")

# Generate Button
generate_button = ttk.Button(input_frame, text="Generate Password", command=generate_button_click)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# --- Output Frame ---
output_frame = ttk.LabelFrame(root, text="Generated Password", padding=10)
output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Password Output Text Area
password_output = tk.Text(output_frame, height=2, width=30, state=tk.DISABLED)
password_output.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Copy to Clipboard Button
copy_button = ttk.Button(output_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Configure column weights for resizing
root.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
output_frame.columnconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()