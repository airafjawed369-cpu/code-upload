n=int(input("Enter no: "))
m=n
p=m
c=0
a=0
while(n>0):
    ld= n%10
    c+=1
    n//=10
while(m>0):
    l= m%10
    a+=(l**c)
    m//=10
if(a==p):
    print("armstrong")
else:
    print("not a armstrong")