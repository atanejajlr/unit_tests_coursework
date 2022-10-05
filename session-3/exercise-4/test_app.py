from app import add_multiple_products
from unittest.mock import patch

@patch("builtins.input", side_effect=['Coke', 'Pepsi'])
def test_add_multiple_products(mock_input):
    #assemble
    prod_list = ['Coke', 'Fanta']
    expected_result = ['Coke', 'Fanta', 'Pepsi']
    
    #act
    actual_result = add_multiple_products(prod_list, 2)
    
    #assert
    assert actual_result == expected_result
    assert mock_input.call_count == 2

    