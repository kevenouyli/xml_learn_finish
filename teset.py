import numpy as np
a=[[100,10],[2,14],[52,56],[4,72],[5,27],[6,32]]
b=np.array(a)
def get_max(a):
	b=[]
	for i in a:
		b.append(i[1])
	return	max(b)
d=get_max(a)

g=np.where(b==d)
print(g[0][0])