k=int(-99999999999999999999999999999)
v=int(0)
cont=int(0)
c=int(0)
while True:
	try:
		n=int(input())
		c+=1
		if (n<=k and cont==0):
			v = (k+1)
			cont = 1
		k=n;
	except EOFError:
    		break
if c==1 or cont==0:
	print(n+1)
else:
	print(v)