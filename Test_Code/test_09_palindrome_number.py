import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "09_palindrome_number.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome = module.is_palindrome

assert is_palindrome(121) == True
assert is_palindrome(1221) == True
assert is_palindrome(123) == False
assert is_palindrome(10) == False
assert is_palindrome(0) == True

print("All test cases passed.")