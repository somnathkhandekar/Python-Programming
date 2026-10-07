def is_palindrome(text):
    text = text.lower()
    reverse = ""

    for char in text:
        reverse = char + reverse

    return text == reverse


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Palindrome" if is_palindrome(text) else "Not Palindrome")
