# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 02:23:27 2022
Emmanuel Amador Maldonado

En este script se hace la limpieza, flitrado y análisis de los datos obtenidos de la producción de 
tala sustentable de pino y encino obtenido del Atlas Nacional de Biomasa (ANBIO) y que fueron guardados en el
archivo DURANGO-CHIHUAHUA.xlsx

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
#Primero se hace una limpieza de los datos, se revisa el tipo de dato o si hay valores nulos
data=pd.read_excel(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\ARREGLOS\EVIDENCIAS PYTHON\1.- BIOMASA\DURANGO-CHIHUAHUA.xlsx")
print(data.dtypes)
data["producción de biomasa (ton/año)"]=pd.to_numeric(data["producción de biomasa (ton/año)"])
data["PCI (MJ/kg)"]=pd.to_numeric(data["PCI (MJ/kg)"])
print(data.dtypes)
#print(pd.isnull(data["producción de biomasa (ton/año)"]).values.ravel().sum())
data=data.dropna(0,"any")

#se revisa que esté bien escrito el tipo de biomasa posible
tipo_biomasa=data.groupby("Tipo de Biomasa")
tipo=[]
for x, dato in tipo_biomasa:
    tipo.append(x)
print(tipo) # se revisa que solo exista tres tipos de biomasa, en caso de no ser así, arreglarlo a estos tres parámetros
#bosque de encino
#bosque mixto
#bosque de pino
data=data.replace("bosque  de encino","bosque de encino")
data=data.replace("bosque mixto ","bosque mixto")
data=data.replace("osque de encino","bosque de encino")
data=data.replace("bosue de encino","bosque de encino")

print(data.groupby("Tipo de Biomasa").size())#se verifica que ya esté bien escrito


#%%
#Se separan los datos por estados y se convierte cada estado en un dataframe
durango=data[data["Estado"]=="Durango"]
chihuahua=data[data["Estado"]=="Chihuahua"]
chihuahua.reset_index(inplace=True)




#%%
"""
Se revisa que no hayan datos repetidos para ningún municipio de Durango

"""
    
repetidos_durango=[]
for index in range(len(durango)):
    for i in range(len(durango)):
        if i != index:
            if durango.loc[index]["producción de biomasa (ton/año)"] == durango.loc[i]["producción de biomasa (ton/año)"]  and durango.loc[index]["Tipo de Biomasa"] == durango.loc[i]["Tipo de Biomasa"] and durango.loc[index]["Municipio"] == durango.loc[i]["Municipio"]: 
                #print("Hay un valor repetido en las posiciones ", i, "y ", index)
                #print(durango.loc[i][:])
                #print(durango.loc[index][:])
                #print("\n\n")
                if i not in repetidos_durango and index not in repetidos_durango:
                    repetidos_durango.append(i) #en los pares están los repetidos (0,2,4...)
                    repetidos_durango.append(index)

for x in range(len(repetidos_durango)):
    if x%2==0:
        durango=durango.drop(repetidos_durango[x])
        
print("Hay ",len(durango),"datos de Durango")
                
#%%
"""
Se revisa que no haya ningún dato repetido en ningún municipio de Chihuahua

"""
            
repetidos_chihuahua=[]
for index in range(len(chihuahua)):
        for i in range(len(chihuahua)):
            if i != index:
                 if chihuahua.loc[index]["producción de biomasa (ton/año)"] == chihuahua.loc[i]["producción de biomasa (ton/año)"]  and chihuahua.loc[index]["Tipo de Biomasa"] == chihuahua.loc[i]["Tipo de Biomasa"] and chihuahua.loc[index]["Municipio"] == chihuahua.loc[i]["Municipio"]: 
                     #print("Hay un valor repetido en las posiciones ", i, "y ", index)
                     #print(chihuahua.loc[i][:])
                     #print(chihuahua.loc[index][:])
                     #print("\n\n")
                     if i not in repetidos_chihuahua and index not in repetidos_chihuahua:
                         repetidos_chihuahua.append(i) #en los pares están los repetidos (0,2,4...)
                         repetidos_chihuahua.append(index)

for x in range(len(repetidos_chihuahua)):
     if x%2==0:
         chihuahua=chihuahua.drop(repetidos_chihuahua[x])   

print("Hay ",len(chihuahua),"datos de Chihuahua")


#%%
"""
DURANGO

Se agrupan los datos por municipio"""
durango_municipios=durango.groupby("Municipio")
print("Hay ", len(durango_municipios), "municipios en Durango con tala sustentable")
print("En Durango, se produce en total",durango["producción de biomasa (ton/año)"].sum()," toneladas de biomasa/año mediante tala sustentable")
pos_mun_max=durango_municipios["producción de biomasa (ton/año)"].sum().idxmax()
print("El municipio que más produce de Durango es ",pos_mun_max, " con ",durango_municipios["producción de biomasa (ton/año)"].sum()[pos_mun_max],"ton/año")




#%%
"""
CHIHUAHUA

Se agrupan los datos por municipio"""
chihuahua_municipios=chihuahua.groupby("Municipio")
print("Hay ", len(chihuahua_municipios), "municipios en Chihuahua con tala sustentable")
print("En Chihuahua, se produce en total",chihuahua["producción de biomasa (ton/año)"].sum()," toneladas de biomasa/año mediante tala sustentable")
mun_prod_max_chihuahua=chihuahua_municipios["producción de biomasa (ton/año)"].sum().idxmax()
print("El municipio que más produce de Chihuahua es ",mun_prod_max_chihuahua, " con ",chihuahua_municipios["producción de biomasa (ton/año)"].sum()[mun_prod_max_chihuahua],"ton/año")

#%%
"""
NOTAS A MI YO DEL FUTURO

Cuando haces una agrupación de un df con groupby, ese tipo de dato 
(tipo groupby) se maneja como una lista, para acceder a ellos tienes dos 
variables, la variable agrupada, y los datos dentro de los grupos

Ej, vas a agrupar los datos de chihuahua por municipio, entonces es

municipios_chihuahua=chihuahua.groupby("Municipios")
print(municipios_chihuahua.size()) te da los municipios y el número de datos que almacena cada uno

for municipio, datos in municipios_chihuahua:
    Puedes moverte por "datos" como si fuera una lista

Para hacerle una operación matemática a una sola columna del groupby creado
se pone

municipios_chihuahua["columna a la que quieres hacer la suma"].sum()

para este punto, la línea de arriba crea un nuevo df, donde el índice ahora
es el municipio y las columnas son la suma de la producción de biomasa 
de cada estado

para encontrar el índice donde se tiene la suma máxima (o en otras palabras
el estado que más biomasa produce), se le agrega .idxmax()

municipios_chihuahua["columna a la que quieres hacer la suma"].sum().idxmax()

pero como la línea de arriba te da el índice, pero el índice ahora es el 
nombre del municipio, te da el municipio que más genera, y para acceder 
al valor de la suma, solo es volver a hacer el df de la suma, y pedirle la fila
con el índice que encontraste.

Por eso se ve un desmadre cuando aparece el municipio que más genera, porque 
en ese instante se crea otro df con la suma de la producción de biomasa por estado
pero lo hice para no tener tantas variables en la memoria.

suma_prod_chihuahua=chihuahua_municipios["producción de biomasa (ton/año)"].sum()
municipio_max_chihuahua=suma_prod_chihuahua.idxmax()
print(municipio_max_chihuahua, suma_prod_mun_chihuahua[municipio_max_chihuahua])

El código de arriba es lo mismo, pero ocupas más memoria
"""
#%%
#Se guardan los datos limpios en csv para ahorrar tiempo y ya tenerlos listos

data.to_excel("Data Cleaned Chihuahua-Durango.xlsx", index=False)
chihuahua.to_excel("Data Cleaned Chihuahua.xlsx", index=False)
durango.to_excel("Data Cleaned Durango.xlsx", index=False)

#%%
"""
Se cargan los datos limpios

"""


data=pd.read_excel(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\ARREGLOS\EVIDENCIAS PYTHON\TT1\1.- BIOMASA\Data Cleaned Chihuahua-Durango.xlsx")
chihuahua=pd.read_excel(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\ARREGLOS\EVIDENCIAS PYTHON\1.- BIOMASA\CARACTERIZACIÓN DE LA BIOMASA\Data Cleaned Chihuahua.xlsx")
durango=pd.read_excel(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\ARREGLOS\EVIDENCIAS PYTHON\1.- BIOMASA\CARACTERIZACIÓN DE LA BIOMASA\Data Cleaned Durango.xlsx")


#%%

"""
Una vez que se sabe cuál estado y municipio se va a utilizar, se procede
a realizar las gráficas correspondientes para ejemplificarlo

"""
plt.rcParams["figure.dpi"] = 2000
plt.rcParams["font.family"]="Times New Roman"
df_prod_munchi=chihuahua.groupby("Municipio")["producción de biomasa (ton/año)"].sum()
fig=df_prod_munchi.plot(kind="barh",width=0.5, color="green",title="Biomass production by municipality in Chihuahua (tons/year)", fontsize=6,xlim=[0,450000])
fig.axes.title.set_size(9)
for rect in fig.patches:
    fig.text(
        rect.get_width()+0.5,
        rect.get_y()+rect.get_height()/20,
        round(rect.get_width(),2),
        fontsize=5
        )
#%%
plt.rcParams["figure.dpi"] = 2000
plt.rcParams["font.family"]="Times New Roman"
df_chidu=data.groupby("Estado")["producción de biomasa (ton/año)"].sum()
fig2=df_chidu.plot(kind="barh",width=0.45, color=["#378FAE","orange"],title="Producción de biomasa por estado (ton/año)", fontsize=10,xlim=[0,4e6])

for rect2 in fig2.patches:
    fig2.text(
        rect2.get_width()+0.5,
        rect2.get_y()+rect.get_height()/2,
        round(rect2.get_width(),2),
        fontsize=10
        )
#%%
plt.rcParams["figure.dpi"] = 2000
plt.rcParams["font.family"] = "Times New Roman"
df_prod_mundu=durango.groupby("Municipio")["producción de biomasa (ton/año)"].sum()
fig=df_prod_mundu.plot(kind="barh",width=0.5, color="#53B8B4",title="Biomass production by municipality in Durango (tons/year)", fontsize=8,xlim=[0,450000])
fig.axes.title.set_size(10)
for rect in fig.patches:
    fig.text(
        rect.get_width()+0.5,
        rect.get_y()+rect.get_height()/20,
        round(rect.get_width(),2),
        fontsize=7.5
        )



