def reverse_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    return reverse


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))