def maxf(f,C):
	pas=0.001
	x=-1
	y=-1
	max=f(-1,-1)
	while (x<1):
		while(y<1):
			if (f(x,y)>max) and ((x,y) not in C):
				f(x,y)=max
				nex_max=(x,y)
			y+=pas
		x+=pas
	C.append(new_max)
	return(new_max)