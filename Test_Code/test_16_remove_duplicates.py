import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "16_remove_duplicates.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

remove_duplicates = module.remove_duplicates

assert remove_duplicates([1, 2, 2, 3, 3]) == [1, 2, 3]
assert remove_duplicates([5, 5, 5]) == [5]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []

print("All test cases passed.")