from app import add_price
from unittest.mock import patch

@patch("builtins.input")
def test_add_price(mock_input):
    #assemble
    
    price_list = [1, 2, 3]
    mock_input.return_value = 4
    expected_result = [1, 2, 3, 4]
    
    #act
    actual_result = add_price(price_list)
    
    #assert
    assert actual_result == expected_result