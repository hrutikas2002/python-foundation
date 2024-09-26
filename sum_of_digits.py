num = int(input("enter the number: "))

sum = 0

for i in range (num):
    digit = num%10         # modulus gives last digit from the number
    sum+=digit
    num  = num//10          # floor division divides num by 10 and eliminate decimal points and generate whole number. hence last gigit from number gets remove

print("sum: ",sum)