def celtofarenheit(c):
    return (c*9/5)+32

c = int(input("Enter the temperature in Celsius: "))
print(f"The temperature in Fahrenheit is {celtofarenheit(c)}")
