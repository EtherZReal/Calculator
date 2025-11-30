from operations import add, subtract, multiply, divide, exit_program
from ui import show_menu

def run_calculator():
    
    #Infinite loop to keep the program running
    while True: 
        show_menu()

        #User input so the user can choose the operation to perform
        choice = input("Enter choice (1/2/3/4/5): \n") 

        #Exit if the user wants to stop the program
        if choice == '5':
            exit_program()

        #Get numbers from the user
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        #Performs the operation that the user chose
        if choice == '1':
            print(f"{number1} + {number2} = {add(number1, number2)}")
        elif choice == '2':
            print(f"{number1} - {number2} = {subtract(number1, number2)}")
        elif choice == '3':
            print(f"{number1} * {number2} = {multiply(number1, number2)}")
        elif choice == '4':
            print(f"{number1} / {number2} = {divide(number1, number2)}")
        else:
            print("Invalid input")