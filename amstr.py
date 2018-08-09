b=int(input())   
temp=b
sum=0
while(b>0):
    rem=b%10
    sum=rem**3+sum
    b=b//10
if(temp==sum):
    print("Yes")
else:
    print("no")



