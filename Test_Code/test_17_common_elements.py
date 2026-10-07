import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "17_common_elements.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

common_elements = module.common_elements

assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert common_elements([1, 2, 3], [4, 5, 6]) == []
assert common_elements([1, 1, 2], [1, 2]) == [1, 2]
assert common_elements([], [1, 2]) == []

print("All test cases passed.")