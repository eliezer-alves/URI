f=float(0)
while True:
	try:
		n=int(input())
		for i in range(n):
			z=input().split(' ')
			x=int(z[0])
			y=int(z[1])
			if y/x>f:
				print(i+1)
				f=y/x
		f=0
	except EOFError:
    		break
