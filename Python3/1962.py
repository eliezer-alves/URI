n=int(input())
while n>=1:
	n=n-1
	ano=int(input())
	if ano<2015:
		print(2015-ano, "D.C.")
	elif ano>2015:
		print((2014-ano)*-1, "A.C.")
	elif(ano==2015):
		print("1 A.C.")
