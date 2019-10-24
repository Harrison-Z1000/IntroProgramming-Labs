# CMPT 120 Intro to Programming
# Lab #6 - Arithmetic Function
# Author: Harrison Zheng
# Date: 2019-10-24


def show_intro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")


def show_outro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")


def do_loop():
    while True:
        cmd = input("What computation do you want to perform?: ")
        # Converts user's input to lowercase to prevent errors due to uppercase letters
        cmd = cmd.lower()

        if cmd == "add":
            numbers = get_numbers()
            result = numbers[0] + numbers[1]
        elif cmd == "sub":
            numbers = get_numbers()
            result = numbers[0] - numbers[1]
        elif cmd == "mult":
            numbers = get_numbers()
            result = numbers[0] * numbers[1]
        elif cmd == "div":
            numbers = get_numbers()
            result = numbers[0] / numbers[1]
        elif cmd == "quit":
            break
        else:
            print("'" + cmd + "'", "is not a valid command.")
            break

        # Computer only prints the result if user puts in a valid command that is not 'quit'
        print("The result is:", result, "\n")


def get_numbers():
    # Separate method ensures computer does not ask for numbers if user puts in 'quit' or an invalid command
    while True:
        try:
            # Will crash if either input is non-numeric
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            frac = num1 / num2
        except ValueError:
            print("Enter numbers only! \n")
            # Computer asks user to enter numbers again if it catches an error
            continue
        return [num1, num2]


def main():
    show_intro()
    do_loop()
    show_outro()


main()
