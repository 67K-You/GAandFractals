#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:51:22 2020

@author: stanislas
"""


import matplotlib.pyplot as plt
import math
from tkinter import *
from matplotlib.figure import Figure
import fonctions as fc
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np

choices = [1, 2, 3, 4]
init=True

def nombre_random():
    import random as rd
    return 2*(rd.random()-0.5)

points=fc.creer_liste(fc.pas)
page=Tk()
page.title("Choix des fractales")
Titre=Label(page,text="Choississez la fractale qui vous convient le mieux",font=("Courrier",40))
Titre.pack()
frame=Frame(page)
frame.pack()
left_frame=Frame(frame)
right_frame=Frame(frame)
extreme_frame=Frame(frame)
TextChoix1=Label(extreme_frame,text="Meilleur choix")
TextChoix1.pack()
variable1 = StringVar(extreme_frame)
variable1.set(choices[0])
Choix1=OptionMenu(extreme_frame,variable1,*choices)
Choix1.pack()
TextChoix2=Label(extreme_frame,text="Choix 2")
TextChoix2.pack()
variable2 = StringVar(extreme_frame)
variable2.set(choices[1])
Choix2=OptionMenu(extreme_frame,variable2,*choices)
Choix2.pack()
TextChoix3=Label(extreme_frame,text="Choix 3")
TextChoix3.pack()
variable3 = StringVar(extreme_frame)
variable3.set(choices[2])
Choix3=OptionMenu(extreme_frame,variable3,*choices)
Choix3.pack()
TextChoix4=Label(extreme_frame,text="Pire choix")
TextChoix4.pack()
variable4 = StringVar(extreme_frame)
variable4.set(choices[3])
Choix4=OptionMenu(extreme_frame,variable4,*choices)
Choix4.pack()
def mosaique(L):
    left_frame.grid(row=0,column=0,sticky=N)
    right_frame.grid(row=0,column=1,sticky=W)
    extreme_frame.grid(row=0,column=2,sticky=E)
    # scrollbar = Scrollbar (frame) 
    # scrollbar.pack()
    
    #####################################################
    c1Re=nombre_random()
    c2Re=nombre_random()
    c3Re=nombre_random()
    c4Re=nombre_random()
    c1Im=nombre_random()
    c2Im=nombre_random()
    c3Im=nombre_random()
    c4Im=nombre_random()
    
    
    c1=c1Re+c1Im*1j
    c2=c2Re+c2Im*1j
    c3=c3Re+c3Im*1j
    c4=c4Re+c4Im*1j
    fig1=fc.fractale(c1,-1.5,1.5,-1.5,1.5)
    fig2=fc.fractale(c2,-1.5,1.5,-1.5,1.5)
    fig3=fc.fractale(c3,-1.5,1.5,-1.5,1.5)
    fig4=fc.fractale(c4,-1.5,1.5,-1.5,1.5)
    ######################################################
    text1=Label(left_frame,text="1")
    text1.pack()
    # Button1=Button(left_frame,text="Choisir la fractale 1")
    # Button1.pack()
    # Sup1=Button(left_frame,text="Supprimer la fractale 1")
    # Sup1.pack()
    canvas1=FigureCanvasTkAgg(fig1,left_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack()
    canvas1._tkcanvas.pack()

    
    text2=Label(right_frame,text="2")
    text2.pack()
    # Button2=Button(right_frame,text="Choisir la fractale 2")
    # Button2.pack()
    # Sup2=Button(right_frame,text="Supprimer la fractale 2")
    # Sup2.pack()
    canvas2=FigureCanvasTkAgg(fig2,right_frame)
    canvas2.draw()
    canvas2.get_tk_widget()
    canvas2._tkcanvas.pack()

    text3=Label(left_frame,text="3")
    text3.pack()
    # Button3=Button(left_frame,text="Choisir la fractale 3")
    # Button3.pack()
    # Sup3=Button(left_frame,text="Supprimer la fractale 3")
    # Sup3.pack()
    canvas3=FigureCanvasTkAgg(fig3,left_frame)
    canvas3.draw()
    canvas3.get_tk_widget()
    canvas3._tkcanvas.pack()

    
    text4=Label(right_frame,text="4")
    text4.pack()
    # Button4=Button(right_frame,text="Choisir la fractale 4")
    # Button4.pack()
    # Sup4=Button(right_frame,text="Supprimer la fractale 4")
    # Sup4.pack()
    canvas4=FigureCanvasTkAgg(fig4,right_frame)
    canvas4.draw()
    canvas4.get_tk_widget()
    canvas4._tkcanvas.pack()



    Valider=Button(extreme_frame,text='Prochaine génération',command=lambda:update(L,init,variable1,extreme_frame,c1Re,c2Re,c3Re,c4Re,c1Im,c2Im,c3Im,c4Im))
    Valider.pack()
    
    print(L)
    frame.pack()

def update(L,init,variable1,extreme_frame,c1Re,c2Re,c3Re,c4Re,c1Im,c2Im,c3Im,c4Im):
    if init:
        V1=int(variable1.get())
        V2=int(variable2.get())
        V3=int(variable3.get())
        V4=int(variable4.get())
        print(5-V1)
        print(5-V2)
        print(5-V3)
        print(5-V4)
        L.append([5,None])    
        L.append([5-V1,[c1Re,c1Im]])
        L.append([5-V2,[c2Re,c2Im]])
        L.append([5-V3,[c3Re,c3Im]])
        L.append([5-V4,[c4Re,c4Im]])
        L.append([0,None])
        L.sort(key=lambda sublist:sublist[0],reverse=True)
        extreme_frame.destroy()
        init=False
    else:
        V4=int(variable4.get())
        print(V4)
        fc.new_values([c4Re,c4Im],L,V4)
        if V4==4:
            L[4][0]=0.1
        L.sort(key=lambda sublist:sublist[0],reverse=True)
    print(L)
    left_frameupdate=Frame(frame)
    right_frameupdate=Frame(frame)
    left_frameupdate.grid(row=0,column=0,sticky=N)
    right_frameupdate.grid(row=0,column=1,sticky=W)
    extreme_frameupdate=Frame(frame)
    extreme_frameupdate.grid(row=0,column=2,sticky=E)
    # scrollbar = Scrollbar (frame) 
    # scrollbar.pack()
    TextChoix1=Label(extreme_frameupdate,text="Où voulez vous placer la nouvelle fractale?")
    TextChoix1.pack()
    variable1 = StringVar(extreme_frameupdate)
    variable1.set(choices[0])
    Choix1=OptionMenu(extreme_frameupdate,variable4,*choices)
    Choix1.pack()
    Valider=Button(extreme_frameupdate,text='Prochaine génération',command=lambda:update(L,init,variable1,extreme_frame,c1Re,c2Re,c3Re,c4Re,c1Im,c2Im,c3Im,c4Im))
    Valider.pack()
    #####################################################
    fitness=fc.best_approximate(L,points)
    imax=np.argmax(fitness)
    c4Re=imax//(2*(1/fc.pas))*fc.pas
    c4Im=imax%(2*(1/fc.pas))*fc.pas
    print(c4Re)
    print(c4Im)
    c1Re=L[1][1][0]
    c2Re=L[2][1][0]
    c3Re=L[3][1][0]
    c1Im=L[1][1][1]
    c2Im=L[2][1][1]
    c3Im=L[3][1][1]
    
    plt.close('all')
    c1=c1Re+c1Im*1j
    c2=c2Re+c2Im*1j
    c3=c3Re+c3Im*1j
    c4=c4Re+c4Im*1j
    fig1=fc.fractale(c1,-1.5,1.5,-1.5,1.5)
    fig2=fc.fractale(c2,-1.5,1.5,-1.5,1.5)
    fig3=fc.fractale(c3,-1.5,1.5,-1.5,1.5)
    fig4=fc.fractale(c4,-1.5,1.5,-1.5,1.5)
    ######################################################
    text1=Label(left_frameupdate,text="1")
    text1.pack()
    # Button1=Button(left_frame,text="Choisir la fractale 1")
    # Button1.pack()
    # Sup1=Button(left_frame,text="Supprimer la fractale 1")
    # Sup1.pack()
    canvas1=FigureCanvasTkAgg(fig1,left_frameupdate)
    canvas1.draw()
    canvas1.get_tk_widget().pack()
    canvas1._tkcanvas.pack()

    
    text2=Label(right_frameupdate,text="2")
    text2.pack()
    # Button2=Button(right_frame,text="Choisir la fractale 2")
    # Button2.pack()
    # Sup2=Button(right_frame,text="Supprimer la fractale 2")
    # Sup2.pack()
    canvas2=FigureCanvasTkAgg(fig2,right_frameupdate)
    canvas2.draw()
    canvas2.get_tk_widget()
    canvas2._tkcanvas.pack()

    text3=Label(left_frameupdate,text="3")
    text3.pack()
    # Button3=Button(left_frame,text="Choisir la fractale 3")
    # Button3.pack()
    # Sup3=Button(left_frame,text="Supprimer la fractale 3")
    # Sup3.pack()
    canvas3=FigureCanvasTkAgg(fig3,left_frameupdate)
    canvas3.draw()
    canvas3.get_tk_widget()
    canvas3._tkcanvas.pack()

    
    text4=Label(right_frameupdate,text="4")
    text4.pack()
    # Button4=Button(right_frame,text="Choisir la fractale 4")
    # Button4.pack()
    # Sup4=Button(right_frame,text="Supprimer la fractale 4")
    # Sup4.pack()
    canvas4=FigureCanvasTkAgg(fig4,right_frameupdate)
    canvas4.draw()
    canvas4.get_tk_widget()
    canvas4._tkcanvas.pack()
    left_frame=left_frameupdate
    right_frame=right_frameupdate
    extreme_frame=extreme_frameupdate
L=[]    
mosaique(L)
page.mainloop()

