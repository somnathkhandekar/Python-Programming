def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Palindrome" if is_palindrome(num) else "Not Palindrome")