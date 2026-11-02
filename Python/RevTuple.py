# t=(10,20,30,40)
# l=len(t)
# def rev(tup):
#     r=()
#     for i in range(1,len(t)):
#         print(tup) 
#     return r
# print(rev(t))

#Rev by k positions

t=(10,20,30,40,50)
k=int(input("Enter position: "))
l=len(t)
def rev(tup, pos):
    return t[-k:]+t[:-k]
print(rev(t,k))