def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return reverse


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Reversed number:", reverse_number(num))