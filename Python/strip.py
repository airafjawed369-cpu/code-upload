n= input()
'''print(n.strip())
print(n.lstrip())
print(n.rstrip())'''





def lar(s):
    x=s.split()
    l=len(x[0])
    c=0
    a=0
    '''for j in range(0, len(x)):
        for k in range(0, j+1):
            if(len(x[j])==len())'''
    for i in range(1,len(x)):
        if(len(x[i])>l):
            l=len(x[i])
            w=x[i]
        else:
            continue
    for j in range(0,len(x)):
        if(l==len(x[j])):
            a=x[j]

    return w,a

s="Hello world is the very first programe for a coder in every language "
print(lar(s))
