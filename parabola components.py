# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:13:20 2022

@author: Emmanuel Amador

En este script se desarrolla una breve figura acerca de las componentes principales de una parábola que
deben ser tomados en cuenta para el desarrollo de un concentrador solar cilindro parabólico.

"""

import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(dpi=1600)
plt.rcParams["font.family"]="Times New Roman"
x0=2
theta=70
p=x0/(4*np.sin(theta*np.pi/180))*(1+np.cos(theta*np.pi/180))
x=np.linspace(-1,1)
x1=np.linspace(-1,0)
x2=np.linspace(-0.1,0)
y=x**2/(4*p)
y1=0.714+0.364*x1
y2=-np.sqrt(0.15**2-x2**2)+0.714+.056
plt.plot(x2,y2,color="gray",linestyle="--",label="Ángulo de apertura")
print(x[0]**2/(4*p),x0/(4*np.sin(theta*np.pi/180))*(1+np.cos(theta*np.pi/180)))
plt.scatter(0,p,color="blue",label="Foco")
plt.plot(x,y,color="orange")
plt.plot(x1,y1,color="#98FF98",linestyle="--")
plt.axvline(x=0,ymin=0, ymax=x[0]**2/(4*p)+1,linestyle='--',label="Eje de la parábola", color="red")
plt.axvline(x=0,ymin=0, ymax=0.839,linestyle='--', color="blue",label="Distancia focal")
plt.axhline(xmin=0.083,xmax=0.916,y=(-1)**2/(4*p),linestyle='--', label="Apertura", color="purple")
plt.scatter(0,0,color="green",label="Vértice")
plt.title("Componentes de la parábola")
plt.xlim(-1.2,1.2)
plt.ylim(0,x[0]**2/(4*p)+0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()




