# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 01:30:05 2022

@author: Amador Maldonado Emmanuel
        
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.2 RECURSO SOLAR EN LA SUPERFICIE DE LA ATMÓSFERA"
nombre= "\\diaprom_EXT.csv"
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
    itotaldia_marca.append(dato["prom"].sum()) #la irradiancia total en un día común al mes
    itotaldia_inf.append(dato["v min"].sum())
    itotaldia_sup.append(dato["v max"].sum())
    listames.append(str(mes))
    print("irradiancia total al día en el mes de ", mes,": ",dato["prom"].sum(),"W/m2")
    print("Las horas de sol al día promedio en el mes de", mes, "son: ", len(dato),"hrs.")
   
    #ESTO ES PARA GENERAR LAS GRÁFICAS, PERO PARA QUE NO SE REPITAN LAS PUSE EN OTRO CUADRO, AUNQUE VAN PEGADAS AL FOR
    x=np.linspace(dato["hora"].iloc[0],dato["hora"].iloc[-1])
    coef=np.polyfit(dato["hora"],dato["prom"],4)
    y=coef[0]*x**4+coef[1]*x**3+coef[2]*x**2+coef[3]*x+coef[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
    plt.rcParams["font.family"]="Times New Roman"
    fig=plt.figure()
    plt.plot(x,y,color="orange")
    
    
    plt.errorbar(dato["hora"],dato["prom"],yerr=dato["error"],fmt="o", markerfacecolor="black",ecolor="#0979B0") #fmt se usa cuando no quieres que se genere una recta para unir puntos, sino se pone marker
    plt.title("Irradiancia extraterrestre de un día típico en el mes de " + str(mes))
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
data2.to_csv("datos_generales_EXT.csv",index=False)
#%%
"""
NOTA: LAS BARRAS DE ERROR SON EL ANCHO DE CLASE/2, PARA QUE LA LONGITUD TOTAL DE LA BARRA SEA EL ANCHO DE LA CLASE

"""


ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.2 RECURSO SOLAR EN LA SUPERFICIE DE LA ATMÓSFERA"
nombre= "\\datos_generales_EXT.csv"
data2=pd.read_csv(ruta+nombre)
fig=plt.figure(dpi=1000)
plt.rcParams["font.family"]="Times New Roman"
plt.barh(data2["mes"],data2["horas sol/dia"],color="orange")
plt.title("Horas promedio de sol al día",fontsize=9)
plt.ylabel("mes")
plt.xlabel("horas")
#plt.savefig("Horas_promedio_sol_dia_mes.png",dpi=980) 

fig=plt.figure(dpi=1000)
plt.rcParams["font.family"]="Times New Roman"
x=np.linspace(0,11)
coef=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],data2["Irradiancia total/dia"],6)
y=coef[0]*x**6+coef[1]*x**5+coef[2]*x**4+coef[3]*x**3+coef[4]*x**2+coef[5]*x+coef[6] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
plt.rcParams["font.family"]="Times New Roman"
fig=plt.figure(dpi=1000)
plt.plot(x,y,color="orange")
plt.errorbar(data2["mes"],data2["Irradiancia total/dia"],yerr=data2["error"], fmt="o", markerfacecolor="black", ecolor="lightblue")
plt.xticks(rotation=45,fontsize=9)
plt.title("Energía solar total extraterrestre típica",fontsize=9)
plt.xlabel("mes")
plt.ylabel("Energía solar extraterrestre típica diaria. " + r"$Wh/m^{2}/día$")
#plt.savefig("Irradiancia_total_diaria_por_mes.png",dpi=980)
