import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "12_reverse_string.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_string = module.reverse_string

assert reverse_string("hello") == "olleh"
assert reverse_string("python") == "nohtyp"
assert reverse_string("abc") == "cba"
assert reverse_string("") == ""
assert reverse_string("A") == "A"

print("All test cases passed.")