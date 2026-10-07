import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "20_word_frequency.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

word_frequency = module.word_frequency

assert word_frequency("hello world hello") == {"hello": 2, "world": 1}
assert word_frequency("python is easy python") == {"python": 2, "is": 1, "easy": 1}
assert word_frequency("hello") == {"hello": 1}
assert word_frequency("") == {}

print("All test cases passed.")