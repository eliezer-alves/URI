while True:
	try:
		x=input()
		x=x.split(' ')
		a=int(x[0])
		b=int(x[1])
		print(a^b)
	except EOFError:
    		break