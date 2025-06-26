# Sum of n natural numbers

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

number = int(input("Enter a number: "))
print(f"The sum of the first {number} natural numbers is {sum(number)}")
