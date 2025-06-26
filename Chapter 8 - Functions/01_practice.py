# Greater of three numbers

def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a,b,c = int(input("Enter three numbers: ")),int(input()),int(input())
print(f"The greater number is {greater(a,b,c)}")