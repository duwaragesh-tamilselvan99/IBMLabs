num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for 1 in range(1,num + 1):
        factorial = factorial * 1
print("The factorial of",num,"is",factorial)        