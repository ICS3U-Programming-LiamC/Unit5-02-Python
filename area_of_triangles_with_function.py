#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 2, 2021
# This program calculates the area of a triangle
# with given inputs


# function that does gets the parameters and then calcualtes
# the area, then prints it to the user
def calc_area(length, height):
    area = length * height / 2
    print("The area is {:.2f}units^2".format(area))


def main():
    print("This program calcualtes the area of a triangle")
    # get dimentions
    user_length = input("What is the length of your triangle: ")
    user_height = input("What is the height of your triangle: ")

    # make sure the users nums can be integers
    try:
        user_length = float(user_length)
        user_height = float(user_height)

        if (user_height > 0 and user_length > 0):
            # can the function and pass it the parameters
            calc_area(user_length, user_height)
        else:
            print("Numbers must be positive")
            main()

    # if there is an error converting the users input
    except ValueError:
        print("Not valid input")
        main()


if __name__ == "__main__":
    main()
