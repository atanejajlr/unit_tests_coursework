import random


def random_number_getter_function():
    return random.randint(1, 10)

def add_two_numbers(a, function_name = random_number_getter_function):
    return a + function_name()
    