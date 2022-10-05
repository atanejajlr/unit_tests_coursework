# Write a unit test for the below function add_two_random_numbers . You will need to update the code to make use of dependency injection and create a mock
# function.
# from random import randint
# def get_random_number():
# return randint(1, 10)
# def add_two_random_numbers():
# return get_random_number() + get_random_number()

import random
from random import randint

def add_two_numbers(a, b):
    return a + b

def get_random_number(get_randint = randint):
    return get_randint(1, 10)

def add_number_with_random_number(a, get_random_number_function = get_random_number):
    return a + get_random_number_function()

def add_two_random_numbers(get_rand_num_fun_A = get_random_number, get_rand_num_fun_B = get_random_number):
    return get_rand_num_fun_A() + get_rand_num_fun_B()

