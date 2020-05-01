a = input()
b = len(a)
c = int(a)
unid = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', '']
dez = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', '']
cent = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', '']
if b == 3:
	print(cent[int(a[0])-1]+dez[int(a[1])-1]+unid[int(a[2])-1])
if b == 2:
	print(dez[int(a[0])-1]+unid[int(a[1])-1])
if b == 1:
	print(unid[int(a[0])-1])