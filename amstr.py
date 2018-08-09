n=int(input())   
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=rem**3+sum
    n=n//10
if(temp==sum):
    print("Yes")
else:
    print("no")

