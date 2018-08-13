N,A,D=map(int,input().split())
sum=0
for j in range(N):
    sum=sum+A
    A=A+D
    j=j+1
print (sum)    
