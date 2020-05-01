n = int(input())
for i in range(n):
	s = input()
	x,y = s.split('x')
	x=int(x)
	y=int(y)
	cont = int(5)
	for j in range(6):
		if x != y:
			print(x,"x",cont,"=",x*cont,"&&",y,"x",cont,"=",y*cont)
		else:
			print(x,"x",cont,"=",x*cont)
		cont+=1