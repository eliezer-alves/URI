x=int(input())
z=int(input())
while z<=x:
	z=int(input())
k=int(0)
cont=int(0)
while k<=z:
	k=k+x
	x+=1
	cont+=1
print(cont)