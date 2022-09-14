import re
from tkinter import Tk, Label



def get_input():
    first = input("First Number:\n")
    operator = input("Input Operator:\n")
    second = input("Second Number:\n\n")

    return first, operator, second


def check_operator(x):
    # function to check operator
    if x.strip() == "":
        return None
    elif x.strip() == "+":
        return "+"
    elif x.strip() == "-":
        return "-"
    elif x.strip() == "*":
        return "*"
    elif x.strip() == "/":
        return "/"
    else:
        return None


def check_inputs(val1, val2):
    try:
        float(val1)
        float(val2)
        return True
    except ValueError:
        return None


def addition(val1, val2):
    input_equals = float(val1) + float(val2)
    display_output(str(input_equals))


def subtraction(val1, val2):
    input_equals = float(val1) - float(val2)
    display_output(str(input_equals))


def multiply(val1, val2):
    input_equals = float(val1) * float(val2)
    display_output(str(input_equals))


def divide(val1, val2):
    input_equals = float(val1) / float(val2)
    display_output(str(input_equals))


def display_output(x):
    clean = re.search(r"\.0+\Z", x)

    if clean:
        remove_zeros = re.sub(r"\.0+", "", x)
        x = remove_zeros

    # print(f"The output is {str(x)}")
    root = Tk()
    root.title("Zach's Calculator")

    label = Label(root, text=f"The output is {str(x)}")
    label.pack()

    root.mainloop()


def main_loop():
    # this gets the user input
    get_info = get_input()

    # first check the operator
    get_operator = check_operator(get_info[1])
    if not get_operator:
        print("Operator must be +, -, /, *\n")
        main_loop()
        return
    else:
        operator = get_info[1]

    # check if inputs are both numbers
    check_numbers = check_inputs(get_info[0], get_info[2])
    if not check_numbers:
        print("Inputs must be numbers only!\n")
        main_loop()
        return
    else:
        if operator == "+":
            addition(get_info[0], get_info[2])
        elif operator == "-":
            subtraction(get_info[0], get_info[2])

        elif operator == "/":
            divide(get_info[0], get_info[2])
        elif operator == "*":
            multiply(get_info[0], get_info[2])


main_loop()
