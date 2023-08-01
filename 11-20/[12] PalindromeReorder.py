from collections import Counter
letters = input()
letarr = list(letters)
counter = Counter(letters)
counted = counter.values()
oddnumcounter = 0
final = ""
if len(letters) % 2 == 0:
    for i in counted:
        if i % 2 == 1:
            print("NO SOLUTION")
            quit()
    # First we remove half of all letters
    # print the letters in any order, reverse them and then add it on to the normal order
    for (key, value) in counter.items():
        # Add the key value/2 times to the string
        
        for i in range (int(value/2)):
            final += key
    final += final[::-1]
        
else:
    for i in counted:
        if i % 2 == 1:
            oddnumcounter += 1
    if oddnumcounter != 1:
        print("NO SOLUTION")
        quit()
    tempnumber = ""
    for (key, value) in counter.items():
        if value % 2 == 1:
            tempnumber += key
        for i in range(int(value/2)):
            final += key
    final += str(tempnumber) + final[::-1]
print(final)