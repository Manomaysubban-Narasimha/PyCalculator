# Author: Manomay Subban Narasimha
# Python Version 3.8.2
'''
Description:
Models a calculator that can perform addition, subtraction, multiplication,
division, exponentiation, and take logarithms.
Skills applied: recursion, exception handling, logical thinking, writing bug-free code,
dictionaries, functions, enhancing user experience, loops, and flags
'''
from calculator_art import logo as calculator_diagram
import math


MAX_DECIMAL_PLACES = 3

def add(num1, num2):
    '''
        Adds the two parameters and returns the value.
        Time complexity: O(1)
    '''
    return round((num1 + num2), MAX_DECIMAL_PLACES)


def subtract(num1, num2):
    '''
        Subtracts the two parameters and returns the value.
        Time complexity: O(1)
    '''
    return round((num1 - num2), MAX_DECIMAL_PLACES)


def multiply(num1, num2):
    '''
        Multiplies the two parameters and returns the value.
        Time complexity: O(1)
    '''
    return round((num1 * num2), MAX_DECIMAL_PLACES)


def divide(num1, num2):
    '''
        Divides the two parameters and returns the value. If num2 is 0, then re-prompts the user
        to enter a non-zero number to avoid the ZeroDivisionError.
        Time complexity: O(1)
    '''
    divide_by_zero = False
    if num2 == 0:
        divide_by_zero = True
    while divide_by_zero:
        print("Please do not enter 0 since it is not possible to divide by 0.")
        num2 = get_num_input("second")
        if num2 != 0.0:
            divide_by_zero = False

    answer = round((num1 / num2), MAX_DECIMAL_PLACES)
    return answer


def exponentiate(num1, num2):
    '''
        Returns num1 to the power of num2.
        Time complexity: O(1) since simple arithmetic operations takes constant time
        Space complexity: O(1) since constant extra space is consumed independent of the input size
    '''
    return round(num1 ** num2, MAX_DECIMAL_PLACES)


def logarithm(base, num):
    '''
        Returns either the floor or the ceiling value of log base base of num depending
        on the user's preference.
        Time complexity: O(log(n)) where n is the value of num2
        Space complexity: O(1) since the space consumed remains independent of the input size
    '''
    if num == 1:
        return 0
    elif num <= 0:
        return "Cannot take log of a number that is lesser than or equal to 0"
    elif base <= 0:
        return "The base cannot be lesser than or equal to 0"
    return round(math.log(num, base), MAX_DECIMAL_PLACES)
        


def get_num_input(position):
    '''
        Gets an integer input from the user. Repeatedly asks the user to re-enter the
        input as long as the input is not a number.
        Time complexity: O(n) where n is the total number of wrong inputs
        Space complexity: O(1) since the space consumed does not increase as input size increases
    '''
    while True:
        number = input(f"Please enter the {position} number: ")
        try:
            number = float(number)
            break
        except ValueError:
            print("Please enter a NUMBER and not any other input")
    return number


def get_input_operation():
    '''
        Continuously prompts the user input until they enter a valid operation
        which is either +, or -, or /, or *
        Time complexity: O(n) where n is the total number of invalid user inputs
        Space complexity: O(1) since constant additional space is consumed.
    '''
    operation = input("Please enter an operation: ")
    valid_operations = ['+', '-', '*', '/', '^', 'log']
    while operation not in valid_operations:
        print(f"Please enter one of these valid operations: {valid_operations}")
        operation = input("Please enter an operation: ")
    return operation


def display_calculator():
    '''
        Displays the visual of a calculator to provide an enhanced user experience.
        Time complexity: O(1) 
        Space complexity: O(1)
    '''
    print(calculator_diagram)

    
# create a dictionary to store the operations and their corresponding functions
operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
    '^' : exponentiate,
    'log' : logarithm,
}

display_calculator()

def calculator():
    def get_operation():
        # ask the user which operation they would like
        # Time complexity: O(1) since the loop runs for the number of operations which
        # doesn't change based on the input size
        for operation in operations:
            print(operation)
        preferred_operation = get_input_operation()
        return preferred_operation

    chosen_operation = get_operation()    
    # prompt the user for input
    num1 = get_num_input("first")

    def phase2(num1, chosen_operation):
        continue_calculating = True
        while True:
            num2 = get_num_input("second")
            answer = operations[chosen_operation](num1, num2)
            if chosen_operation != "log":
                print(f"{num1} {chosen_operation} {num2} = {answer}")
            else:
                try:
                    answer = float(answer)
                    print(f"{chosen_operation} base {num1} of {num2} = {answer}")
                except ValueError:
                    print(answer)
                    break

            while True:
                choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation or type 'quit' to exit: ").lower()
                if choice == 'quit':
                    continue_calculating = False
                    break
                elif choice == 'y':
                    num1 = answer
                    chosen_operation = get_operation()
                    phase2(num1, chosen_operation)
                elif choice == 'n':
                    calculator()
                print("Please enter a valid choice")

            if not continue_calculating:
                break
    phase2(num1, chosen_operation)
            
calculator()


print("Thank you for trying out the calculator app. Have a great day!")
        
    

