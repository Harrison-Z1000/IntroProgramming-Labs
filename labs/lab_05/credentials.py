# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Harrison Zheng
# Date: 2019-10-16


def main():
    names = getNames()
    uname = createUsername(names)
    getPassword()
    print("Account configured. Your new email address is",
          uname + "@marist.edu")


def getNames():
    # Get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]


def createUsername(names):
    uname = names[0] + "." + names[1]  # Generate a Marist-style username
    uname = uname.lower()
    return str(uname)


def getPassword():
    passwd = input("Create a new password: ")  # Ask user to create a new password
    checkPassword(passwd)
    return passwd


def checkPassword(passwd):
    # Ensure the password has at least 8 characters and contains both upper and lowercase ones
    while len(passwd) != 0:
        if len(passwd) < 8 or passwd.lower() == passwd or passwd.upper() == passwd:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        else:
            print("The force is strong in this one...")
            break
    return True


main()
