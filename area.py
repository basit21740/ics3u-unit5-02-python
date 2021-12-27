#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# This program calculate area of triangle


def caculate_area(base, height):
    # calculate area of triangle

    # process
    area = 1 / 2 * base * height

    # output
    print("The area of triangle is {0} cm²".format(area))


def main():
    # input
    base = input("Enter the base of triangle (integer): ")
    height = input("Enter the height of triangle (integer): ")

    # call functions
    try:
        integer_as_base = int(base)
        integer_as_height = int(height)
        caculate_area(integer_as_base, integer_as_height)
    except Exception:
        print("It is not an integer")

    print("\nDone.")


if __name__ == "__main__":
    main()
