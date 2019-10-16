# Introduction to Programming
# Author: Harrison Zheng
# Date: 10/16/19
# This is a game where the user tries to guess the animal that the programmer was thinking of.


def main():
    animal = "penguin"
    userAnimal = "some animal"
    print("Enter a command that begins with 'q' any time to quit the game. \n")
    while userAnimal != animal:
        print("The computer is thinking of an animal.")
        userAnimal = str(input("What kind of animal do you think it is?: "))
        userAnimal = userAnimal.lower()  # User's input is converted to all lowercase letters to make comparing easier
        if userAnimal[0] == "q":
            break
        elif userAnimal == animal:  # If the user guesses correctly, the program asks them whether they like the
            # animal and prints a comment before breaking out of the loop.
            print("Congratulations! You are correct!")
            usersOpinion = str(input("Do you like the " + animal + "? (Enter 'y' or 'n'): "))
            if usersOpinion == "y":
                print("Awesome! The " + animal + " is a fascinating creature.")
                break
            else:
                print("That's unfortunate. The " + animal + " is such a cool animal.")
                break
        else:  # If the user guesses incorrectly, they are prompted to guess again.
            print("Sorry, that is incorrect. Please try again.")
            userAnimal = str(input("What kind of animal do you think it is?: "))


main()

