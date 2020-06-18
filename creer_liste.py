import numpy as np

def creer_liste():
	L=np.ndarray(shape=(int(2/pas^2)),2)
	x=-1
	y=-1
	i=0
	pas = 0.001
	while x<1 : 
		while y<1 : 
			L[i]=[x,y]
			y+=pas
			i+=1
		x+=pas
		i+=1
	return(L)
