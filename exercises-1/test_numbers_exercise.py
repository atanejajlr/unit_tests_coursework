from unittest.mock import Mock
from numbers_exercise import add_number_with_random_number, \
    add_two_numbers, add_two_random_numbers, get_random_number

def test_add_two_numbers():
    
    #assemble
    a = 4
    b = 5
    
    #act
    actual_result = add_two_numbers(a, b)
    expected_result = 9
    
    #assert
    assert actual_result == expected_result
    
def test_add_number_with_random_number():
    
    #assemble
    a = 10
    mock_random_number_function = Mock(return_value = 8)
    
    #act
    actual_result = add_number_with_random_number(a, mock_random_number_function)
    expected_result = 18
    
    #assert
    assert actual_result == expected_result
    
def test_add_two_random_numbers():
    
    #assemble
    mock_rand_fun_1 = Mock(return_value = 5)
    mock_rand_fun_2 = Mock(return_value = 6)
    
    #act
    actual_result = add_two_random_numbers(mock_rand_fun_1, mock_rand_fun_2)
    expected_result = 11
    
    #assert
    assert actual_result == expected_result
    
def test_get_random_number():
    
    #assemble
    mock_get_randint = Mock(return_value=5)
    expected_result = 5
    
    #act
    actual_result = get_random_number(mock_get_randint)
    
    #assert
    assert actual_result == expected_result
    
    
    
    
    
    
    