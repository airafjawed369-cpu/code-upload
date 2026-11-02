n=int(input("Enter a number: "))
c=0
i=1
while(i<=n):
    if (n%i==0):
        c+=1
    i+=1
if (c==2):
    print("Prime")
else:
    print("Not Prime")