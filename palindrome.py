str = input("Enter the string: ")
rev = str[::-1]                 # start:end:step
if str==rev:
    print("String is palindrome")
else:
    print("String is not palindrome")