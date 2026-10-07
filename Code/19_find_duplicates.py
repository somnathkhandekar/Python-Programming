def find_duplicates(numbers):
    duplicates = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Duplicate elements:", find_duplicates(numbers))