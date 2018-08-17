m,N= input().split(' ')
m,N=int(m),int(N)
m = m ^ N;
N = m ^ N;
m = m ^ N;
print(m,N)
