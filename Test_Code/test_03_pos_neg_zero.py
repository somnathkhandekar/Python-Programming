import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "03_pos_neg_zero.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

check_number = module.check_number

assert check_number(10) == "Positive"
assert check_number(1) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(-1) == "Negative"
assert check_number(0) == "Zero"

print("All test cases passed.")