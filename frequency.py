list_item = [10,10,50,60,20,78,50]

frequency = {}

for item in list_item:
    if item in frequency:
        frequency[item]= frequency[item]+1

    else:
        frequency[item] = 1

print("Frequency of elements: ",frequency)