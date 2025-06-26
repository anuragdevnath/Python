def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
print(f"The factorial of the number {number} is {factorial(number)}")