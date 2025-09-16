def odd_even(n):
    if n%2!=0:
        return True
    return False
    
num = int(input("Enter the number: "))
flag = True
for i in range(2, num-1):
    if num % i == 0:
        flag = False
        break

if flag == True and odd_even(num):
    print(f"{num} is a prime number and odd number")
else:
    print(f"{num} is not a prime number and odd number")

#added new code
