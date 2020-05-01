cont=1;
while True:
	n = int(input())
	if n<0:
		break
	print("Experiment %d: %d full cycle(s)" %(cont,n/2))
	cont+=1