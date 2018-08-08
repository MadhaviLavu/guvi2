a,b=input().split()
a,b=int(a),int(b)
for i in range(a+1,b):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    else:
        if(count==2):
            print(i,end=' ')

