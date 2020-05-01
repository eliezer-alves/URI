n=int(input())
i=0
from decimal import *
for i in range(n):
	a=input()
	x=Decimal(len(a)*0.01)
	print("%.2f" % x)