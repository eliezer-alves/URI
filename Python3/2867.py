a = int(input())
for i in range(a):
	s=input()
	x,y=s.split(' ')
	x = int(x)
	y = int(y)
	k = x**y
	k = str(k)
	print(len(k))