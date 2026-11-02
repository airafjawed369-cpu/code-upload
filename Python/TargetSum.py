t=(1,2,3,1,4,5,8)
target=9
sum=0
for i in t:
    for j in t:
        sum=i+j
        if sum==target:
            print(f"{i} + {j} = {sum}")
        else:
            continue