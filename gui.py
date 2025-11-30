import tkinter as tk
from operations import add, subtract, multiply, divide  # Reuse operations from operations.py

def run_gui():
    root = tk.Tk()
    root.title("Simple Calculator")

    # Input fields
    entry1 = tk.Entry(root)
    entry1.pack(pady=5)
    entry2 = tk.Entry(root)
    entry2.pack(pady=5)

    # Result label
    result_label = tk.Label(root, text="Result will appear here")
    result_label.pack(pady=10)

    # Button functions that reuse operations.py
    def do_add():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            result_label.config(text=f"Result: {add(a, b)}")  # calls add() from operations.py
        except ValueError:
            result_label.config(text="Invalid input")

    def do_subtract():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            result_label.config(text=f"Result: {subtract(a, b)}")  # calls subtract()
        except ValueError:
            result_label.config(text="Invalid input")

    def do_multiply():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            result_label.config(text=f"Result: {multiply(a, b)}")  # calls multiply()
        except ValueError:
            result_label.config(text="Invalid input")

    def do_divide():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            result_label.config(text=f"Result: {divide(a, b)}")  # calls divide()
        except ValueError:
            result_label.config(text="Invalid input")

    # Buttons
    tk.Button(root, text="Add", command=do_add).pack(pady=2)
    tk.Button(root, text="Subtract", command=do_subtract).pack(pady=2)
    tk.Button(root, text="Multiply", command=do_multiply).pack(pady=2)
    tk.Button(root, text="Divide", command=do_divide).pack(pady=2)

    root.mainloop()
