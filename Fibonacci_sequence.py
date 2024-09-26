num = int(input("Enter the number: "))

a,b = 0,1

if num<=0:
    print("Enter valid number..")

elif num==1:
    print("Fibonnacci sequence: ",a)

else:
    print("Fibonnacci sequence: ")
    for i in range(num):
        print(a,end=" ")
        temp = a
        a = b
        b = temp +b