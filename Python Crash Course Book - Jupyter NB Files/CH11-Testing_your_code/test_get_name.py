from name_function import get_formatted_name

def test_get_formatted_name():
    '''test function to check if inputs first, last will work?'''
    formatted_name = get_formatted_name('first','last')
    assert formatted_name == "First Last"

#  An assertion is a claim about a condition. 
#  means we have to verify that our claim and output of function is equal.
# When writing a test, you can make any claim that can be expressed as a conditional statement.

def test_get_foratted_name_number_input():
    numInput = get_formatted_name(1,2)
    assert numInput == "1 2"