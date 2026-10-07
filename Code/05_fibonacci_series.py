def fibonacci(n):
    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print(fibonacci(n))