from app import full_name_creator
from unittest.mock import patch

@patch("builtins.input", side_effect=['Ajay', 'Taneja'])
def test_full_name_creator(mock_input):
    #assemble
    expected_result = "Ajay Taneja"
    
    #act
    actual_result = full_name_creator()
    
    #assert
    assert actual_result == expected_result
    