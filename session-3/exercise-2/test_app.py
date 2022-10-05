from app import print_name
from unittest.mock import patch

@patch("builtins.input")
@patch("builtins.print")
def test_print_name(mock_print, mock_input):
    # assemble
    mock_input.return_value = "Ajay"
    expected_args = "Hello, Ajay!"
    
    #act
    print_name()
    
    #assert
    mock_print.assert_called_with(expected_args)