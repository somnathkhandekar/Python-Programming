import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "13_palindrome_string.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome = module.is_palindrome

assert is_palindrome("madam") == True
assert is_palindrome("level") == True
assert is_palindrome("hello") == False
assert is_palindrome("Python") == False
assert is_palindrome("A") == True

print("All test cases passed.")