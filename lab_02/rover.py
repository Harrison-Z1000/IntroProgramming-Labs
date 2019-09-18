# Introduction to Programming
# Author: Harrison Zheng
# Date: 09/17/19
# This program calculates how long it takes a photo from Curiosity to 
# reach NASA when Mars is at its closest orbit to Earth.


def main():
    speed = 186000
    distance = 34000000
    time = distance / speed
    print("The time it takes for a photo from Curiosity to reach NASA ", end='')
    print("when Mars is at its closest orbit to Earth is", time, "seconds or", time / 60, "minutes.")
main()
