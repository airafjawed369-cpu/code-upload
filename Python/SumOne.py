n=int(input("Enter number: "))
sum=0
while(n>0 or sum>9):
    if(n==0):
         n=sum
         sum=0
    l=n%10
    sum+=l
    n//=10
print(sum)