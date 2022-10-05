from app import add_product, get_user_details
from unittest.mock import patch

@patch("builtins.input")
def test_add_product_no_update(mock_input):
    
    #assemble
    mock_input.return_value = 'Diet Coke'
    prod_list = ['Diet Pepsi', 'Diet Coke', 'Lemonade']
    expected_result = ['Diet Pepsi', 'Diet Coke', 'Lemonade']
    
    #act
    actual_result = add_product(prod_list)
    
    #assert
    assert actual_result == expected_result
    
    
@patch("builtins.input")
def test_add_product_update(mock_input):
    
    #assemble
    mock_input.return_value = 'Diet Coke'
    prod_list = ['Diet Pepsi', 'Sprite', 'Lemonade']
    expected_result = ['Diet Pepsi', 'Sprite', 'Lemonade', 'Diet Coke']
    
    #act
    actual_result = add_product(prod_list)
    
    #assert
    assert actual_result == expected_result
    
@patch('builtins.input', side_effect=['Jim', '20'])
@patch("builtins.print")
def test_get_user_details(mock_print, mock_input):
    
    #assemble
    expected_terminal_result  = 'Thank you, your name is Jim and your age is 20'
    
    #act
    get_user_details()
    
    #assert
    mock_print.assert_called_with(expected_terminal_result)
    
    
    

    

