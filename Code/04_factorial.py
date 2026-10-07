def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))