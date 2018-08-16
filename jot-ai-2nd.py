re=[int(s) for s in input().split()]
a=re[0]
b=re[1]
c=re[2]
d=re[3]
k=re[4]
cnt=0
if(a<=c and c<=d and d<=b):
    if(c<=k<=d):
        print(d-c)
    else:
        print(d-c+1)
elif(a<=c and c<=b and b<=d):
    if(c<=k<=b):
        print(b-c)
    else:
        print(b-c+1)
elif(c<=a and a<=d and d<=b):
    if(a<=k<=d):
        print(d-a)
    else:
        print(d-a+1)
elif(c<=a and a<=b and b<=d):
    if(a<=k<=b):
        print(b-a)
    else:
        print(b-a+1)
elif(a<=b and b<=c and c<=d):
    print(0)
elif(c<=d and d<=a and a<=b):
    print(0)
#siva140191
