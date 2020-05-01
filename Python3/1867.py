def resp(x):
	z = str(x)
	k = int(0)
	for i in range(len(z)):
		k += int(z[i])
	z = str(k)
	if len(z) == 1:
		return k;
	else:
		return resp(z)
while True:
	a=input();
	a = a.split(' ')
	if a[0] == a[1] and a[1] == "0":
		break
	if resp(a[0]) > resp(a[1]):
		print(1)
	elif resp(a[0]) < resp(a[1]):
		print(2)
	else:
		print(0)