from app import greeting
from unittest.mock import patch

@patch("builtins.input")
def test_greeting(mock_input):
    #assemble
   
    mock_input.return_value = "John"
    expected_result = "Nice to meet you, John"
    
    #act
    actual_result = greeting()
    
    #assert
    assert actual_result == expected_result



