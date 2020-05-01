n=int(input())
p=[]
im=[]
for i in range(n):
	num = int(input())
	if num%2==0:
		p.append(num)
	else:
		im.append(num)
p.sort()
im.sort()
for j in p:
	print(j)

h=len(im)-1
for k in im:
	print(im[h])
	h-=1

