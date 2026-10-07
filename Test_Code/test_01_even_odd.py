import sys
sys.path.append("..")  # Add the parent directory to the sys.path
from Code.Check_Even_Odd_NUM import check_even_odd

def test_check_even_odd():
    assert check_even_odd(10) == "Even"
    assert check_even_odd(7) == "Odd"
    assert check_even_odd(0) == "Even"
    assert check_even_odd(-4) == "Even"
    assert check_even_odd(-5) == "Odd"
print("All test cases passed!")