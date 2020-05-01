n = int(input())

for i in range(n):
	s = input()
	v = s.split(' ')
	resp = list(set(v))
	resp.sort()
	
	for j in range(len(resp)):
		print(resp[j], end="")
		if j < (len(resp))-1:
			print(" ", end="")
	print("")