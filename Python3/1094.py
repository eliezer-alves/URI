c=int(0)
r=int(0)
s=int(0)
n=int(input())
for i in range(n):
	x=input().split(' ')
	if x[1]=='C':
		c=int(x[0]) + c
	elif x[1]=='R':
		r=int(x[0]) + r
	elif x[1]=='S':
		s=int(x[0]) + s
t=(c+r+s)
print("Total: %d cobaias" %t)
print("Total de coelhos: %d" %c)
print("Total de ratos: %d" %r)
print("Total de sapos: %d" %s)
print("Percentual de coelhos: %.2lf %%" %(c*100.00/t))
print("Percentual de ratos: %.2lf %%" %(r*100.00/t))
print("Percentual de sapos: %.2lf %%" %(s*100.00/t))