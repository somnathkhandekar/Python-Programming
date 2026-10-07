import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "18_missing_number.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

missing_number = module.missing_number

assert missing_number([1, 2, 3, 5], 5) == 4
assert missing_number([1, 2, 4, 5], 5) == 3
assert missing_number([1, 3, 4, 5], 5) == 2
assert missing_number([2, 3, 4, 5], 5) == 1

print("All test cases passed.")