from app import slow_function_without_DI
from unittest.mock import patch

@patch("app.api_call")
def test_slow_function_without_DI(mock_api_call):
    
    #assemble
    mock_api_call.return_value = 10
    first_var = 5
    expected_result = 5 * 10
    
    #act
    actual_result = slow_function_without_DI(first_var)
    
    #assert
    assert actual_result == expected_result
    