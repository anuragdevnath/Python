number = int(input("Enter a number: "))
primeFlg = 1
for i in range (2,(number)):
    if(number % i == 0):
        primeFlg = 0
        break

if(primeFlg == 0):
    print(f"{number} is not a prime number")
else : 
    print(f"{number} is a prime number")