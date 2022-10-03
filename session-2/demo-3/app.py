import random

def get_random_number():
    return random.randint(1, 10)


def random_list_generator(n, function_name):
    
    result = []
    
    for _ in range(n):
        result.append(function_name())
    return result 

my_random_list = random_list_generator(5, get_random_number)
print(my_random_list)