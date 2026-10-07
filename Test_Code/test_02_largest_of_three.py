import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "02_largest_of_three.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

largest_of_three = module.largest_of_three

assert largest_of_three(10, 20, 30) == 30
assert largest_of_three(50, 20, 10) == 50
assert largest_of_three(5, 50, 25) == 50
assert largest_of_three(10, 10, 5) == 10
assert largest_of_three(-1, -5, -3) == -1

print("All test cases passed.")