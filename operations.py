#Addition function
def add(a, b):
    return a + b

#Subtraction function
def subtract(a, b):
    return a - b

#Multiplication function
def multiply(a, b):
    return a * b

#Division function
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not possible."
    return a / b

#Exit function
def exit_program():
    print("Exiting the program.")
    exit()