from app import add_two_numbers
import pytest
#test

def test_my_common_case():
    #assemble
    my_first_var = 10
    my_second_var = 15
    expected_result = 25
    
    #act
    result = add_two_numbers(my_first_var, my_second_var)
    
    # assert
    assert expected_result == result

def test_my_corner_case():
    #assemble
    first_var = "10"
    second_var = 20
    
    with pytest.raises(Exception):
        add_two_numbers(first_var, second_var)

test_my_common_case()