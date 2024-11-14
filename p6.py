print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:6")

import math

print("Factorial")
num = int(input("Enter a non-negative number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(math.factorial(num))

print("Fibonacci")

def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

terms = int(input("Enter limit: "))

fib_series = fibonacci(terms)

print(f"Fibonacci series of {terms} terms: {fib_series}")

fib_sum = sum(fib_series)
print("Sum of the Fibonacci series:", fib_sum)

def is_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

def generate_even_digit_squares(start, end):
    return [
        num for num in range(start, end + 1)
        if 1000 <= num <= 9999 and is_even_digits(num) and (int(num**0.5))**2 == num
    ]


start_range = 1000
end_range = 9999
print(f"Four-digit even digit perfect squares: {generate_even_digit_squares(start_range, end_range)}")

