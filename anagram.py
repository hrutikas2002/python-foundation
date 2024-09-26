str1 = input("Enter the first string: ")

str2 = input("Enter the second string: ")

string1 = str1.replace(" ","").lower()  #replace space by ""
string2 = str2.replace(" ","").lower()

if len(string1)!=len(string2):
    print(f"{str1} and {str2} are not anagram")

elif sorted(string1)==sorted(string2):          # sorted method sort the string in ascending order alphabetically
    print(f"{string1} and {string2} are anagram")

else:
    print(f"{str1} and {str2} are not anagram")


