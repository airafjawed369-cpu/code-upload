t=(99,70,20,110,90)
l=len(t)
def larg(tup):
    lar=t[0]
    sec=0
    dic={}
    for i in range(1,l):
        if lar>tup[i]:
            continue
        else:
            sec=lar
            lar=tup[i]
    dic["Largest"]=lar
    dic["Second Largest"]=sec
    return dic
print(larg(t))
    


    