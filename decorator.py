# Decorator function
def decorate_factorial(fun):
    def wrapper(n):
        print(f"Calculating factorial of {n}...")
        result = fun(n)
        print(f"Factorial of {n} is {result}")
        return result
    return wrapper

# Factorial function with decorator
@decorate_factorial
def factorial(n):
    if n < 0:
        print("Not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

no = int(input("Enter a number: "))
factorial(no)
