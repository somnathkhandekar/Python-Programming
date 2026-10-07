import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "07_primes_in_range.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

primes_in_range = module.primes_in_range

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(10, 20) == [11, 13, 17, 19]
assert primes_in_range(2, 5) == [2, 3, 5]
assert primes_in_range(1, 1) == []

print("All test cases passed.")