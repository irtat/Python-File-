# Assignment 03:

def calculate_factorial(n):
    if n == 0 or n == 1:
        print(f"Factorial of {n} is: 1")
        return 1
    else:
        result = n * calculate_factorial(n - 1)
        print(f"Factorial of {n} is: {result}")
        return result


def multiply_numbers(a, b):
    result = a * b
    print(f"{a} multiplied by {b} is: {result}")
    return result


def divide_numbers(a, b):
    if b != 0:
        result = a / b
        print(f"{a} divided by {b} is: {result}")
        return result
    else:
        print("Error: Division by zero is not possible.")
        return None


n = 5
calculate_factorial(n)

a = 10
b = 3
multiply_numbers(a, b)
divide_numbers(a, b)
