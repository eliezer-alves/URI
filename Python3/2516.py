while True:
	try:
		j = input().split(' ')
		x = float(j[0])
		y = float(j[1])
		z = float(j[2])
		if y<=z:
			print("impossivel")
		else:
			h=float(x/(y-z))
			if h<=x:
				print("%.2f" %h)
			else:
				print("impossivel")
	except EOFError:
    		break