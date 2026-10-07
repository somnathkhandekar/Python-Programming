import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "08_reverse_number.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_number = module.reverse_number

assert reverse_number(123) == 321
assert reverse_number(4567) == 7654
assert reverse_number(100) == 1
assert reverse_number(5) == 5
assert reverse_number(0) == 0

print("All test cases passed.")