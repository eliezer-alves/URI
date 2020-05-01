x=0
cont=0
while True:
	try:
		
		a=int(input())
		if cont!=0:
			print("")
		cont=1
		x=0
		if (a%4==0 and a%100!=0) or a%400==0:
			x=1
			print("This is leap year.")
			if a%15==0:
				print("This is huluculu festival year.")
			if a%55==0:
				print("This is bulukulu festival year.")
		elif a%15==0:
			x=1
			print("This is huluculu festival year.")
		if x==0:
			print("This is an ordinary year.")
		

	except EOFError:
    		break