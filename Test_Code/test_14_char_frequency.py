import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "14_char_frequency.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

character_frequency = module.character_frequency

assert character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert character_frequency("aaa") == {"a": 3}
assert character_frequency("abc") == {"a": 1, "b": 1, "c": 1}

print("All test cases passed.")