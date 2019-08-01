x11=int(input())
l=list(map(int,input().split()))
y11=""
for o in range(x11-1):
	y11=y11+str(max(l[o],l[o+1]))+" "
print(y11.strip())
