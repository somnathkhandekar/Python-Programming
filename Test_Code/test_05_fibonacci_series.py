import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "05_fibonacci_series.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

fibonacci = module.fibonacci

assert fibonacci(0) == []
assert fibonacci(1) == [0]
assert fibonacci(2) == [0, 1]
assert fibonacci(5) == [0, 1, 1, 2, 3]
assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

print("All test cases passed.")