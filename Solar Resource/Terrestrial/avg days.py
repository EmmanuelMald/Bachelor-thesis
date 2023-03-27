# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 01:30:05 2022

@author: Amador Maldonado Emmanuel
         
En este script se desarrollan las gráficas de la irradiancia de un día promedio de cada mes, cada una de las gráficas
tiene barras de errores y los puntos obtenidos en estas son unidos mediante un ajuste polinomial de 
mínims cuadrados.


Los resultados obtenidos fueron las gráficas guardadas en la carpeta "Curvas de irradiancia diaria frecuente 
por mes con error TNR" y el archivo "datos generales.csv" que se encuentra en esta misma carpeta y que se usa en este
script.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.1 RECURSO SOLAR TERRESTRE"
nombre= "\\diaprom.csv"
direccion=ruta + nombre
data=pd.read_csv(direccion)
print(data.dtypes)
meses=data.groupby("mes") #agrupa los datos por mes
horasol=[] #Todas estas listas es para formar otro dataset
itotaldia_marca=[]
listames=[]
itotaldia_inf=[]
itotaldia_sup=[]
for mes, dato in meses:
    print(mes)
    horasol.append(len(dato)) #las horas de sol son la longitud de los datos del mes
    itotaldia_marca.append(dato["marca"].sum()) #la irradiancia total en un día común al mes
    itotaldia_inf.append(dato["limif"].sum())
    itotaldia_sup.append(dato["limsup"].sum())
    listames.append(str(mes))
    print("irradiancia total al día en el mes de ", mes,": ",dato["marca"].sum(),"W/m2")
    print("Las horas de sol al día promedio en el mes de", mes, "son: ", len(dato),"hrs.")
   
    #%%ESTO ES PARA GENERAR LAS GRÁFICAS, PERO PARA QUE NO SE REPITAN LAS PUSE EN OTRO CUADRO, AUNQUE VAN PEGADAS AL FOR
    x=np.linspace(dato["hora"].iloc[0],dato["hora"].iloc[-1])
    coef=np.polyfit(dato["hora"],dato["marca"],4)
    y=coef[0]*x**4+coef[1]*x**3+coef[2]*x**2+coef[3]*x+coef[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
    plt.rcParams["font.family"]="Times New Roman"
    fig=plt.figure()
    plt.plot(x,y,color="orange")
    
    
    plt.errorbar(dato["hora"],dato["marca"],yerr=dato["ancho clase"]/2,fmt="o", markerfacecolor="black",ecolor="#0979B0") #fmt se usa cuando no quieres que se genere una recta para unir puntos, sino se pone marker
    plt.title("Irradiancia de un día típico en el mes de " + str(mes))
    plt.xlabel("Hora del día (0 a 23 hrs)")
    plt.ylabel("Irradiancia total " + r"$W/m^{2}$")
    #plt.savefig("Irradiancia diaria típica en "+str(mes)+".png",dpi=980)

#%% Hacemos otro archivo csv con los datos generales mensuales
data2=pd.DataFrame({
    "mes":listames,
    "horas sol/dia":horasol, #horas de sol/día más frecuentes en el mes específico
    "Irradiancia total/dia":itotaldia_marca, #irradiancia total más frecuente en el mes, se toma la marca de clase
    "Irradiancia min total/dia": itotaldia_inf,# Irradiancia min total/día más frecuente en el mes
    "Irradiancia max total/dia": itotaldia_sup #Irradiancia max total/día más frecuente en el mes
    })
data2.to_csv("datos_generales.csv",index=False)
#%%
"""
NOTA: LAS BARRAS DE ERROR SON EL ANCHO DE CLASE/2, PARA QUE LA LONGITUD TOTAL DE LA BARRA SEA EL ANCHO DE LA CLASE

En esta parte del código se realiza una gráfica de la energía solar típica día de cada mes del año

"""

ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.1 RECURSO SOLAR TERRESTRE"
nombre= "\\datos_generales.csv"
data2=pd.read_csv(ruta+nombre)
fig=plt.figure(dpi=1000)
plt.rcParams["font.family"]="Times New Roman"
plt.barh(data2["mes"],data2["horas sol/dia"],color="orange")
plt.title("Horas promedio de sol al día",fontsize=9)
plt.ylabel("mes")
plt.xlabel("horas")
##plt.savefig("Horas_promedio_sol_dia_mes.png",dpi=980) 

fig=plt.figure(dpi=1000)
plt.rcParams["font.family"]="Times New Roman"
x=np.linspace(0,11)
coef=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],data2["Irradiancia total/dia"],6)
y=coef[0]*x**6+coef[1]*x**5+coef[2]*x**4+coef[3]*x**3+coef[4]*x**2+coef[5]*x+coef[6] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
plt.rcParams["font.family"]="Times New Roman"
fig=plt.figure(dpi=1000)
plt.plot(x,y,color="orange")
plt.errorbar(data2["mes"],data2["Irradiancia total/dia"],yerr=data2["ancho clase"]/2, fmt="o", markerfacecolor="black", ecolor="lightblue")
plt.xticks(rotation=45,fontsize=9)
plt.title("Energía solar total típica",fontsize=9)
plt.xlabel("mes")
plt.ylabel("Energía solar típica diaria. " + r"$Wh/m^{2}/día$")
##plt.savefig("Irradiancia_total_diaria_por_mes.png",dpi=980)
