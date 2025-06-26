def pattern(number):
    for i in range(1,number+1):
        print("*"*(number-i+1))

number = int(input("Enter a number: "))
pattern(number)