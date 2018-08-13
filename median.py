n=int(input(""))
lst=[int(x) for x in input().split()]
c=0
for i in range(0,n):
    c+=lst[i]
print(int(c/n))   
