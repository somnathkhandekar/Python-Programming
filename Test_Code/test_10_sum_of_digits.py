import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "10_sum_of_digits.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

sum_of_digits = module.sum_of_digits

assert sum_of_digits(123) == 6
assert sum_of_digits(456) == 15
assert sum_of_digits(100) == 1
assert sum_of_digits(5) == 5
assert sum_of_digits(0) == 0

print("All test cases passed.")