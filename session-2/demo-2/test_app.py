from cgitb import reset
from unittest import result
from app import Rectangle, get_todays_price_per_unit, mock_get_price

def test_common_case_get_price():
    #assemble
    w = 5
    l = 12
    
    def mock_get_price():
        return 100
    
    expected_result = w * l * 100
    
    #act
    
    my_temp_rect = Rectangle(w, l)
    result = my_temp_rect.get_price(mock_get_price)
    
    #assert
    assert result == expected_result