from unittest.mock import Mock
from app import add_two_numbers

def test_common_case_add_two_numbers():
    #assemble
    var_1 = 10
    
    mock_random_number_getter_function = Mock(return_value=5)
    result = add_two_numbers(var_1, mock_random_number_getter_function)
    