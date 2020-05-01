cont=3
r=0
c=2
while cont<=39:
	r+=cont/c
	cont=cont+2;
	c=c*2
print("%.2lf" %(r+1))