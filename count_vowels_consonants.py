string = input("Enter the string: ")

string = string.lower()

vowel = 0
consonants = 0

vowel_found = []
consonants_found = []

vowels = "aeiou"

for char in string:
    if char in vowels:
        vowel+=1
        vowel_found.append(char)
    
    elif char.isalpha():        # checks whether all characters in a string are alphabetic
        consonants+=1
        consonants_found.append(char)

print("Vowels:",vowel)
print("The vowels found in string are: ",vowel_found)

print("Consonants: ",consonants)
print("The consonants found in string are: ",consonants_found)
