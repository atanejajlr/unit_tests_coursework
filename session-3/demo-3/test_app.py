from unittest.mock import patch
from app import hello_to_you

@patch("builtins.print")
def test_hello_to_you(mock_print):
    #assemble
    name = 'John'
    expected_terminal_result = 'Hello, John!'
    
    #act
    hello_to_you(name)
    
    #assert
    mock_print.assert_called_with(expected_terminal_result)