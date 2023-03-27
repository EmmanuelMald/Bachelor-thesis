# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 01:30:05 2022

@author: Amador Maldonado Emmanuel

En este script se hacen gráficas comparativas entre la irradiancia incidente en la superficie de la atmósfera, y en 
la superficie de la Tierra
         
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR"
nombre1= "\\1.2 RECURSO SOLAR EN LA SUPERFICIE DE LA ATMÓSFERA\\diaprom_EXT.csv"
nombre2="\\1.1 RECURSO SOLAR TERRESTRE\\diaprom.csv"
direccionEXT=ruta + nombre1
direccionTER=ruta + nombre2
dataEXT=pd.read_csv(direccionEXT)
dataTER=pd.read_csv(direccionTER)
print(dataEXT.dtypes)
print(dataTER.dtypes)
mesesEXT=dataEXT.groupby("mes") #agrupa los datos por mes
mesesTER=dataTER.groupby("mes")
horasolEXT=[] #Todas estas listas es para formar otro dataset
itotaldia_marca_EXT=[]
listames_EXT=[]
itotaldia_inf_EXT=[]
itotaldia_sup_EXT=[]
horasolTER=[] #Todas estas listas es para formar otro dataset
itotaldia_marca_TER=[]
listames_TER=[]
itotaldia_inf_TER=[]
itotaldia_sup_TER=[]
for mesEXT, datoEXT in mesesEXT:
    for mesTER,datoTER in mesesTER:
        if mesTER==mesEXT:
            print(mesEXT)
            print(mesTER)
            horasolTER.append(len(datoTER)) #las horas de sol son la longitud de los datos del mes
            itotaldia_marca_TER.append(datoTER["marca"].sum()) #la irradiancia total en un día común al mes
            itotaldia_inf_TER.append(datoTER["v min"].sum())
            itotaldia_sup_TER.append(datoTER["v max"].sum())
            listames_TER.append(str(mesTER))
            print("irradiancia total al día en el mes de ", mesTER,": ",datoTER["marca"].sum(),"W/m2")
            print("Las horas de sol al día promedio en el mes de", mesTER, "son: ", len(datoTER),"hrs.")
            horasolEXT.append(len(datoEXT)) #las horas de sol son la longitud de los datos del mes
            itotaldia_marca_EXT.append(datoEXT["prom"].sum()) #la irradiancia total en un día común al mes
            itotaldia_inf_EXT.append(datoEXT["v min"].sum())
            itotaldia_sup_EXT.append(datoEXT["v max"].sum())
            listames_EXT.append(str(mesEXT))
            print("irradiancia total al día en el mes de ", mesEXT,": ",datoEXT["prom"].sum(),"W/m2")
            print("Las horas de sol al día promedio en el mes de", mesEXT, "son: ", len(datoEXT),"hrs.")
           
            #ESTO ES PARA GENERAR LAS GRÁFICAS, PERO PARA QUE NO SE REPITAN LAS PUSE EN OTRO CUADRO, AUNQUE VAN PEGADAS AL FOR
            x=np.linspace(datoEXT["hora"].iloc[0],datoEXT["hora"].iloc[-1])
            coefTER=np.polyfit(datoTER["hora"],datoTER["marca"],4)
            coefEXT=np.polyfit(datoEXT["hora"],datoEXT["prom"],4)
            yTER=coefTER[0]*x**4+coefTER[1]*x**3+coefTER[2]*x**2+coefTER[3]*x+coefTER[4]
            yEXT=coefEXT[0]*x**4+coefEXT[1]*x**3+coefEXT[2]*x**2+coefEXT[3]*x+coefEXT[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
            plt.rcParams["font.family"]="Times New Roman"
            fig=plt.figure()
            plt.plot(x,yEXT,color="orange",label="extraterrestre")
            plt.plot(x,yTER,color="#0979B0", label="terrestre")
            
            plt.errorbar(datoEXT["hora"],datoEXT["prom"],yerr=datoEXT["error"],fmt="o", markerfacecolor="orange",ecolor="orange") #fmt se usa cuando no quieres que se genere una recta para unir puntos, sino se pone marker
            plt.errorbar(datoTER["hora"],datoTER["marca"],yerr=datoTER["ancho clase"]/2,fmt="o", markerfacecolor="#0979B0",ecolor="#0979B0")
            plt.title("Comparativa de irradiancia de un día típico en el mes de " + str(mesTER))
            plt.xlabel("Hora del día (0 a 23 hrs)")
            plt.ylabel("Irradiancia total " + r"$W/m^{2}$")
            plt.legend(loc="upper right", frameon=False)
            #plt.savefig("Irradiancia diaria típica en "+str(mesTER)+".png",dpi=980)

#%%
"""
NOTA: LAS BARRAS DE ERROR SON EL ANCHO DE CLASE/2, PARA QUE LA LONGITUD TOTAL DE LA BARRA SEA EL ANCHO DE LA CLASE

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rutaEXT="C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.2 RECURSO SOLAR EN LA SUPERFICIE DE LA ATMÓSFERA"
rutaTER="C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.1 RECURSO SOLAR TERRESTRE"
nombreEXT="\\datos_generales_EXT.csv"
nombreTER="\\datos_generales.csv"
dataTER=pd.read_csv(rutaTER + nombreTER)
dataEXT=pd.read_csv(rutaEXT + nombreEXT)
#fig=plt.figure(dpi=1000)
#plt.rcParams["font.family"]="Times New Roman"
#plt.barh(data2["mes"],data2["horas sol/dia"],color="orange")
#plt.title("Horas promedio de sol al día",fontsize=9)
#plt.ylabel("mes")
#plt.xlabel("horas")
##plt.savefig("Horas_promedio_sol_dia_mes.png",dpi=980) 

fig=plt.figure(dpi=1000)
plt.rcParams["font.family"]="Times New Roman"
x=np.linspace(0,11)
coefTER=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],dataTER["Irradiancia total/dia"],6)
yTER=coefTER[0]*x**6+coefTER[1]*x**5+coefTER[2]*x**4+coefTER[3]*x**3+coefTER[4]*x**2+coefTER[5]*x+coefTER[6]
coefEXT=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],dataEXT["Irradiancia total/dia"],6)
yEXT=coefEXT[0]*x**6+coefEXT[1]*x**5+coefEXT[2]*x**4+coefEXT[3]*x**3+coefEXT[4]*x**2+coefEXT[5]*x+coefEXT[6] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
plt.rcParams["font.family"]="Times New Roman"
fig=plt.figure(dpi=1000)
plt.plot(x,yEXT,color="orange",label="Extraterrestre")
plt.plot(x,yTER,color="#0979B0", label="Terrestre")
plt.errorbar(dataEXT["mes"],dataEXT["Irradiancia total/dia"],yerr=dataEXT["error"], fmt="o", markerfacecolor="black", ecolor="orange")
plt.errorbar(dataTER["mes"],dataTER["Irradiancia total/dia"],yerr=dataTER["ancho clase"]/2, fmt="o", markerfacecolor="black", ecolor="#0979B0")
plt.xticks(rotation=45,fontsize=9)
plt.title("Comparativa de la energía solar total típica",fontsize=9)
plt.ylabel("Energía solar típica diaria. " + r"$Wh/m^{2}/día$")
plt.legend(loc="upper right", frameon=False)

##plt.savefig("Irradiancia_total_diaria_por_mes.png",dpi=980)
