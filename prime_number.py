num = int(input("Enter the number: "))

if num<=1:
    is_prime=False

else:
    is_prime = True
    for i in range(2,num):
        if num%i==0:
            is_prime=False

if is_prime:
    print("Number is prime")

else:
    print("Number is not prime")