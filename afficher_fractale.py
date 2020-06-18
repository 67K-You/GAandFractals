#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:21:02 2020

@author: stanislas
"""

import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

xres=100.0
yres=100.0

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

# if __name__ == "__main__":
#  	fractale(-1.5,1.5,-1.5,1.5)