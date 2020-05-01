import math

y = int(input())
for i in range(y):
	#print(i)
	n = int(input())
	#print(n)
	resp = int(((math.sqrt((4*(2*n))+1))-1)/2);
	print(resp)
