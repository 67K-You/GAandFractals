# -*- coding: utf-8 -*-

import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from sklearn.model_selection import train_test_split # 'sklearn', scikit-learn, is a library with tools for machine learning and manipulating data
# create a SymbolicRegressor object
from gplearn.genetic import SymbolicRegressor

xres=100.0
yres=100.0
pas=0.001

def creer_liste(pas):
	points=np.ndarray(shape=(int((2/pas)**2),2))
	x=-1
	y=-1
	i=0
	while x<1 : 
		while y<1 : 
			points[i]=[x,y]
			y+=pas
			i+=1
		x+=pas
		i+=1
	return points


def fractale(c,xmin,xmax,ymin,ymax,imax=200):
	t=time.time()
	x=xmax-xmin
	y=ymax-ymin
	matfrac=np.ndarray((int(xres),int(yres)))
	mini=1
	maxi=imax
	for xi in range(int(xres)):
		for yj in range(int(yres)):
			i=1
			z=x*xi/xres+xmin+1j*(y*yj/yres+ymin)
			Rez=z.real
			Imz=z.imag

			while Rez>=xmin and Rez<=xmax and Imz>=ymin and Imz<=ymax and i<=imax:
				i+=1
				z=z**2+c
				Rez=z.real
				Imz=z.imag
			matfrac[xi][yj]=i
	elapsed=time.time()-t
	print(elapsed)
	fig,ax=plt.subplots()
	i=ax.imshow(matfrac, cmap=cm.gnuplot2, interpolation='bicubic')
	return fig

def best_approximate(L,points):
	n=len(L)
	datax=[item[1] for item in L]
	datax.pop()
	datax.pop(0)
	datay=[item[0] for item in L]
	datay.pop()
	datay.pop(0)
	print(datax)
	print(datay)
	X_train, X_test, y_train, y_test = train_test_split(datax, datay, test_size=0.33) # random_state here is a random seed, fixed so that we always get the same results


	sr = SymbolicRegressor(		population_size=500,
    	    generations=20,
    	    stopping_criteria=0.01,	# stop if the mean squared error of the best solution is lower than this
        	function_set=('add', 'sub', 'mul', 'div'), # functions that the symbolic regression can use
        	p_crossover=0.54, 	# probabilities of activation of different genetic operators
        	p_subtree_mutation=0.1,	#
        	p_hoist_mutation=0.05, 	#
        	p_point_mutation=0.3,	#
        	verbose=1,		# print a lot of stuff to screen
	      )

	# launch the evolution
	sr.fit(X_train, y_train)
	Ypred=sr.predict(points)
	return Ypred

def new_values(new_fractal,L,i):
	value = (L[i-1][0]+L[i][0])/2
	L.insert(i,[value,new_fractal])

#def maxind()