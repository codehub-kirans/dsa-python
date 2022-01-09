def factorial(number):
    if number <= 0:
        return 1

    return number * factorial(number- 1)

#Test Factorial
print(factorial(4))