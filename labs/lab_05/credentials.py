# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Harrison Zheng
# Date: 2019-10-16


def main():
    names = getNames()
    uname = createUsername(names)
    passwd = getPassword()
    print("Account configured. Your new email address is",
          uname + "@marist.edu")


def getNames():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]


def createUsername(names):
    uname = names[0] + "." + names[1]  # Generates a Marist-style username
    return str(uname)


def getPassword():
    passwd = input("Create a new password: ")  # Ask user to create a new password
    # Ensures the password has at least 8 characters
    while len(passwd) != 0:
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        else:
            print("The force is strong in this one...")
            break
    return passwd


main()
