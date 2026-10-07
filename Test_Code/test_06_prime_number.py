import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "06_prime_number.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_prime = module.is_prime

assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(10) == False
assert is_prime(1) == False
assert is_prime(0) == False

print("All test cases passed.")