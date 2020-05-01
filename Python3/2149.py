v=[]
v.append(0)
v.append(1)
x=0
y=1
z=0
t=0
for i in range(17):
    x=y+z
    v.append(x)
    t=x*y
    v.append(t)
    z=x
    y=t
while True:
    try:
        n=int(input())
        print(v[n-1])
    except EOFError:
    	break

