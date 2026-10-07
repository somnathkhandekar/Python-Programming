def missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    n = int(input("Enter the maximum number: "))
    print("Missing number:", missing_number(numbers, n))