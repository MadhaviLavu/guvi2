a,b=input().split()
a,b=int(a),int(b)
for i in range(a+1,b):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    else:
        if(c==2):
            print(i,end=' ')


