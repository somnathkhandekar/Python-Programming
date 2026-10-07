import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "19_find_duplicates.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates

assert find_duplicates([1, 2, 2, 3, 3]) == [2, 3]
assert find_duplicates([1, 2, 3]) == []
assert find_duplicates([5, 5, 5]) == [5]
assert find_duplicates([1, 1, 2, 3, 3]) == [1, 3]

print("All test cases passed.")