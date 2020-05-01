import math
while True:
	try:
		a = input()
		b = []
		b = a.split(' ')
		r = int(b[0])
		x = int(b[1])
		y = int(b[2])
		r2 = int(b[3])
		x2 = int(b[4])
		y2 = int(b[5])
		j = math.sqrt(((x-x2)**2)+((y-y2)**2))
		if(r>=j+r2):
			print("RICO")
		else:
			print("MORTO")
	except EOFError:
		break