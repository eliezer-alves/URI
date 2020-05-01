while True:
	n = int(input())
	if n == 0:
		break;
	resp = int(0)
	for i in range(n):
		n = input()
		n = n.split(' ')
		x = int(n[1])
		if x%2 != 0:
			x-=1
		resp +=x
			
	print(round((resp-0.1)/4))
	resp=0