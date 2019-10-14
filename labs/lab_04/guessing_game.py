# Introduction to Programming
# Author: Harrison Zheng
# Date: 10/3/19
# This is a game where the user tries to guess the animal that the programmer was thinking of.


def main():
    animal = "Penguin"
    userAnimal = "Something"
    while userAnimal != animal:
        print("The computer is thinking of an animal.")
        userAnimal = str(input("What kind of animal do you think it is?: "))
        if userAnimal == animal:  # If the user guesses correctly, the program breaks out of the while loop.
            print("Congratulations! You are correct!")
            break
        else:  # If the user guesses incorrectly, they are prompted to guess again.
            print("Sorry, that is incorrect. Please try again.")
            userAnimal = str(input("What kind of animal do you think it is?: "))


main()


