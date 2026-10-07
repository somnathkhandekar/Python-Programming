import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parent.parent / "Code" / "11_vowels_consonants.py"
spec = importlib.util.spec_from_file_location("program_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

count_vowels_consonants = module.count_vowels_consonants

assert count_vowels_consonants("hello") == (2, 3)
assert count_vowels_consonants("python") == (1, 5)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("abc") == (1, 2)

print("All test cases passed.")