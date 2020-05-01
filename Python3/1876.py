def resp(x):
	maior = int(-1)
	for i in range(1, len(x)-1, 1):
		if maior < len(x[i])/2:
			maior = round(len(x[i])/2)
	if maior < len(x[0]):
			maior = len(x[0])
	if maior < len(x[len(x)-1]):
			maior = len(x[len(x)-1])
	return maior
		
while True:
	try:
		a = input()
		a = a.split('x')
		print(resp(a))
	except EOFError:
    		break