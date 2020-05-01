a = 0

while a != -1:
	x=int(input())
	a = x
	if a == -1:
		break
	if x > 0:
		print(x-1)
	if x <= 0:
		print(0)
