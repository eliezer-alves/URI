a=int(input())
b=int(input())
c=int(input())
a1=int((a*4)+(b*2))
a2=int((a*2)+(c*2))
a3=int((c*4)+(b*2))
if a1<=a2 and a1<=a3:
	print(a1)
elif a2<=a1 and a2<=a3:
	print(a2)
elif a3<=a1 and a3<=a2:
	print(a3)