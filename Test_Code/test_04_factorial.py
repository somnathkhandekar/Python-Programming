import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "04_factorial.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

factorial = module.factorial

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(3) == 6

print("All test cases passed.")