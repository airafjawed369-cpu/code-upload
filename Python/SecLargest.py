num=int(input("Enter number: "))
lar=0
sec=0
for i in range(1,num+1):
    n=int(input("Enter number: "))
    if(n>lar):
        sec=lar
        lar=n
    elif(n>sec and n!=lar):
        sec=n
print("Second largest: ", sec)