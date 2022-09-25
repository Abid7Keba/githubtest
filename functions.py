import random
"""
A module full of functions
:author: Mathew
"""

def welcome_message():
    """
    A function that prints out a welcome message
    no parameters, no return
    :return: None
    """
    print("welcome to comp 1516")


def welcome_message2(name):
    """
    A function that prints out a welcome message to the given name
    has parameter, no returns
    :param name: A string, person's name
    :return: None
    """
    print("Hello", name)
    print("Welcome to comp 1516")


def get_random_num():
    """
    A function to return a random number from 0.0 to 1.0
    no parameters, has return
    :return: a random number from 0.0 to 1.0
    """
    return random.random()


def calculate_area_square(side_length_m):
    """
    A function to calculate the area of a square
    has parameters, has return
    :param side_length_m: a number in meters that is the length of a single side
    :return: side_length_m ** 2, the area of a square in m^2
    """
    # area = side_length_m ** 2
    # return area
    return side_length_m ** 2

def get_product_description():
    return input("Please describe your product")

def get_amount():
    return int(input("How many of the item did you buy?"))

def get_price():
    return float(input("cost per item?"))

def calc_total(amount, price):
    return amount * price



if __name__ == '__main__':
    print("I should not be called")

