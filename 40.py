m=int(input(" "))
a=0
b=1
count=0
if(m==0):
     print(a)
elif(m<0):
     print("positive number")
else:
    while(count<m):
         print(a)
         nexterm= a+b
         a=b
         b=nexterm
         count+=1
