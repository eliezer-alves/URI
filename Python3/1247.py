import math
while True:
	
	try:
		a = input()
		x,y,z = a.split(' ')
		d = int(x)
		vf = int(y)
		vg = int(z)
		if vf>vg:
			print("N")
		else:
			tf = float(12/vf)
			dg = float(math.sqrt(144+(d**2)))
			tg = float(dg/vg)
			
			if tg<=tf:
				print("S")
			else:
				print("N")
	except EOFError:
		break
	