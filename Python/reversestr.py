s="HEllO WORLD"
def rev(s):
    temp="" 
    for i in range(len(s)-1,-1,-1):
        temp=temp+s[i]
    return temp
print(rev(s))


#count the no of vowels, consonants, special characters, and number for a given string.