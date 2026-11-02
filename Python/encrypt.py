import random
import string

chars=" "+ string.digits + string.ascii_letters + string.punctuation
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)


#encrpyt
og=input("Enter string to encrypt: ")
enc=""

for letters in og:
    index=chars.index(letters)      #Finds index of og letters from og list
    enc+=keys[index]                #Appends letters from key list to the enc variable
print(f"Original Text: {og}")
print(f"Encrypted Text: {enc}")


#decrpyt
enc=input("Enter string to decrypt: ")
og=""

for letters in enc:
    index=keys.index(letters)    
    og+=chars[index]
print(f"Encrypted Text: {enc}")
print(f"Original Text: {og}")
