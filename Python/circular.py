n=int(input("Enter number: "))
ld=0
for i in range(0,1):
    ld=n%10
    n//=10
print(f"{ld}{n}")
    