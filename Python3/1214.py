import math
a = int(input())
for i in range(a):
	s = []
	s = input()
	l = []
	l = s.split(' ')
	m = int(0)
	cont = int(0)
	size = int(l[0])
	for i in range(size):
		m+=int(l[i+1])
	resp = float(m/size)
	for i in range(size):
		if int(l[i+1])>resp:
			cont+=1
	r = float(cont*100/size)
	print("%.3f" % r + "%")
	