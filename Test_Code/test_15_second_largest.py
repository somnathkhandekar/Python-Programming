import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "15_second_largest.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

second_largest = module.second_largest

assert second_largest([10, 20, 30]) == 20
assert second_largest([5, 10, 3, 8]) == 8
assert second_largest([100, 50, 75]) == 75
assert second_largest([1, 2, 3, 4]) == 3

print("All test cases passed.")