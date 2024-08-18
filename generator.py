import random
import string
import tkinter as tk


def generate(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

def generate_password_interface():
    length_password = int(entry_length.get())
    if length_password < 8:
        label_result.config(text="Password length must be greater than 8")
    else:
        password_generated = generate(length_password)
        label_result.config(text="Password generated: " + password_generated)

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Password length: ")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate", command=generate_password_interface)
button_generate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()