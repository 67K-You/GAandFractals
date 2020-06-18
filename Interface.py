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
import afficher_fractale
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

def nombre_random():
    import random as rd
    return rd.random()*rd.randint(1,3)

def mosaique(L):
    page=Tk()
    page.title("Choix des fractales")
    Titre=Label(page,text="Choississez la fractale qui vous convient le mieux",font=("Courrier",40))
    Titre.pack()
    


    frame=Frame(page)
    left_frame=Frame(frame)
    right_frame=Frame(frame)
    left_frame.grid(row=0,column=0,sticky=N)
    right_frame.grid(row=0,column=1,sticky=W)
    extreme_frame=Frame(frame)
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
    fig1=afficher_fractale.fractale(c1,-1.5,1.5,-1.5,1.5)
    fig2=afficher_fractale.fractale(c2,-1.5,1.5,-1.5,1.5)
    fig3=afficher_fractale.fractale(c3,-1.5,1.5,-1.5,1.5)
    fig4=afficher_fractale.fractale(c4,-1.5,1.5,-1.5,1.5)
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

    TextChoix1=Label(extreme_frame,text="Meilleur choix")
    TextChoix1.pack()
    Choix1=Entry(extreme_frame)
    Choix1.pack()
    TextChoix2=Label(extreme_frame,text="Choix 2")
    TextChoix2.pack()
    Choix2=Entry(extreme_frame)
    Choix2.pack()
    TextChoix3=Label(extreme_frame,text="Choix 3")
    TextChoix3.pack()
    Choix3=Entry(extreme_frame)
    Choix3.pack()
    TextChoix4=Label(extreme_frame,text="Pire choix")
    TextChoix4.pack()
    Choix4=Entry(extreme_frame)
    Choix4.pack()
    
    
    

    choix1=int(Choix1.get())
    choix2=int(intChoix2.get())
    choix3=int(Choix3.get())
    choix4=int(Choix4.get())
    
    L=[]
    L.append(choix1)
    L.append(choix2)
    L.append(choix3)
    L.append(choix4)
    
    Valider=Button(extreme_frame,text='Prochaine génération',command=lambda:mosaique(L))
    Valider.pack()
    
    frame.pack()
    page.mainloop()

L=[0,0,0,0]    
mosaique(L)