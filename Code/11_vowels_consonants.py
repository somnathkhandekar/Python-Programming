def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


if __name__ == "__main__":
    text = input("Enter a string: ")
    vowels, consonants = count_vowels_consonants(text)
    print("Vowels:", vowels)
    print("Consonants:", consonants)