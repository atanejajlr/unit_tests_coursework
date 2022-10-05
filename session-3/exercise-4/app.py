# Write a function named add_multiple_products with the following
# requirements:
# • It should accept two arguments, products_list (list) and
# number_of_new_products (int)
# • Based on the value of number_of_new_products it should ask user
# to write product names in terminal one by one.
# • For any of the user input products, if the product is not already available
# in the products_list it should add it to the end of list, otherwise it
# should skip that product.
# • At the end, the function should return the updated products_list.
# Write unit-tests to verify the functionality of your code

from ast import List


def add_multiple_products(prod_list: list, number_of_new_products):
    
    updated_prod_list = prod_list
    for _ in range(number_of_new_products):
        prod_name = input("Input the product name: ")
        if prod_name not in prod_list:
            updated_prod_list.append(prod_name)
            
    return updated_prod_list
  