# Introduction to Programming
# Author: Harrison Zheng
# Date: 10/16/19
# This is a game where the user tries to guess the animal that the programmer was thinking of.


def main():
    animal = "penguin"
    userAnimal = "some animal"
    while userAnimal != animal:
        print("Enter 'Quit' at any time to quit the game. \n")
        print("The computer is thinking of an animal.")
        userAnimal = str(input("What kind of animal do you think it is?: "))
        userAnimal = userAnimal.lower()  # User's input is converted to all lowercase letters to make comparing easier
        if userAnimal == animal:  # If the user guesses correctly, the program breaks out of the while loop.
            print("Congratulations! You are correct!")
            break
        elif userAnimal == "quit":
            break
        else:  # If the user guesses incorrectly, they are prompted to guess again.
            print("Sorry, that is incorrect. Please try again.")
            userAnimal = str(input("What kind of animal do you think it is?: "))


main()

