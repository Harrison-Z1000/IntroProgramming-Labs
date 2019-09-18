# Introduction to Programming
# Author: Harrison Zheng
# Date: 09/18/19
# This program uses four words from the user to create a Mad Lib.


def main():
    print("This program creates Mad Libs.")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    adj = input("Enter an adjective: ")
    print("Every Tuesday night, when no one is looking, the ", end='')
    print(adj + " " + noun + " goes to " + place + " to " + verb + ".")
main()