t=(10,20,30,40,50)
l=len(t)
n=int(input("Enter index to rmv: "))
def rem(tup,num):
    if n<l:
        return (t[:n])+(t[n+1:])
    else:
        return "Invalid Index"
print(rem(t,n))