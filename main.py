#A simple calculator that performs addition, substraction, multiplication and division operations with two numbers until the user decides to exit.
#The calculator has both a text-based interface and a graphical user interface (GUI) using Tkinter.

from app import run_calculator
from gui import run_gui

if __name__ == "__main__":
    choice = input("Run calculator in (1) text mode or (2) GUI mode? ")
    if choice == "1":
        run_calculator()
    elif choice == "2":
        run_gui()
    else:
        print("Invalid choice")