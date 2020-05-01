n = int(input())
for i in range(n):
	c = input()
	a,b=c.split(' ')
	m=int(a)
	n=int(b)
	if m == 0:
		print(n+1)
	elif m==1:
		
		print(2+(n+3)-3)
	elif m==2:
		print(2*(n+3)-3)
	elif m == 3:
		print((2**(n + 3)) - 3)
	elif m==4 and n>2:
		print("65533")
	elif m==4:
		resp=int(2)
		cont=int(2)
		for j in range(n+2):
			resp=2**resp	
			
		print(resp-3)