def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two distinct numbers.")

    unique_numbers.sort()
    return unique_numbers[-2]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Second largest:", second_largest(numbers))