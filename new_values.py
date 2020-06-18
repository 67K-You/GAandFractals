def new_values(new_fractal,L,i):
	value = (L[i][0]+L[i+1][0])/2
	L.insert(i,[value,new_fractal])