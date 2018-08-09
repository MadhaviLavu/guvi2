a=int(input())   
temp=a
sum=0
while(a>0):
    rem=a%10
    sum=rem**3+sum
    a=a//10
if(temp==sum):
    print("Yes")
else:
    print("no")



