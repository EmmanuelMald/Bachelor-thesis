# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:02:11 2022

@author: Amador Maldonado Emmanuel
         
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.1 RECURSO SOLAR TERRESTRE"
nombre= "\\NASA Data 2.csv" #el archivo NASA DATA 2 tiene tanto la irradiancia terrestre como la extraterrestre.
direccion=ruta + nombre
data=pd.read_csv(direccion)
print(data.dtypes)#se revisa que los tipos de datos sean correctos para cada parámetro
#son correctos, por lo que no hay que hacer nada
mes=[]
horas=[]
v_min=[]
v_max=[]
rangos=[]
ancho_clases=[]
"""
La idea de tener tantos datos es la siguiente:
    Hacer un día promedio típico por mes, es decir, hacer un histograma de frecuencias para cada hora en que haya sol, y tomar 
    el valor de irradiancia que más se repita por mes

"""
#%%
"""
ENERO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
enero=data[(data["MO"] == 1) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(enero["HR"]), max(enero["HR"]+1),1):
    IT_horaria.append(enero[enero["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(enero["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Enero")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2))             
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
    #  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure(dpi=980)
    plt.rcParams.update({"font.size":8,"figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de enero a las " + str(i) + " horas",fontsize=8)
    plt.savefig("enero_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
FEBRERO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
febrero=data[(data["MO"] == 2) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(febrero["HR"]), max(febrero["HR"]+1),1):
    IT_horaria.append(febrero[febrero["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(febrero["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Febrero")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
    #  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de febrero a las " + str(i) + " horas",fontsize=8)
    plt.savefig("febrero_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
MARZO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
marzo=data[(data["MO"] == 3) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(marzo["HR"]), max(marzo["HR"]+1),1):
    IT_horaria.append(marzo[marzo["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(marzo["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Marzo")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
    #  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de marzo a las " + str(i) + " horas",fontsize=8)
    plt.savefig("marzo_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
ABRIL

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
abril=data[(data["MO"] == 4) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(abril["HR"]), max(abril["HR"]+1),1):
    IT_horaria.append(abril[abril["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(abril["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Abril")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
#  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de abril a las " + str(i) + " horas",fontsize=8)
    plt.savefig("abril_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
MAYO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
mayo=data[(data["MO"] == 5) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(mayo["HR"]), max(mayo["HR"]+1),1):
    IT_horaria.append(mayo[mayo["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(mayo["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Mayo")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
#  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de mayo a las " + str(i) + " horas",fontsize=8)
    plt.savefig("mayo_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
JUNIO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
junio=data[(data["MO"] == 6) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(junio["HR"]), max(junio["HR"]+1),1):
    IT_horaria.append(junio[junio["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(junio["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Junio")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
   # i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
# GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de junio a las " + str(i) + " horas",fontsize=8)
    plt.savefig("junio_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
JULIO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
julio=data[(data["MO"] == 7) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(julio["HR"]), max(julio["HR"]+1),1):
    IT_horaria.append(julio[julio["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(julio["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Julio")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
#  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de julio a las " + str(i) + " horas",fontsize=8)
    plt.savefig("julio_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
AGOSTO

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
agosto=data[(data["MO"] == 8) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(agosto["HR"]), max(agosto["HR"]+1),1):
    IT_horaria.append(agosto[agosto["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(agosto["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Agosto")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
# GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de agosto a las " + str(i) + " horas",fontsize=8)
    plt.savefig("agosto_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
SEPTIEMBRE

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
sep=data[(data["MO"] == 9) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(sep["HR"]), max(sep["HR"]+1),1):
    IT_horaria.append(sep[sep["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(sep["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Septiembre")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
# GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de septiembre a las " + str(i) + " horas",fontsize=8)
    plt.savefig("septiembre_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
OCTUBRE

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
octubre=data[(data["MO"] == 10) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(octubre["HR"]), max(octubre["HR"]+1),1):
    IT_horaria.append(octubre[octubre["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(octubre["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Octubre")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
#  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de octubre a las " + str(i) + " horas",fontsize=8)
    plt.savefig("octubre_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
NOVIEMBRE

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
nov=data[(data["MO"] == 11) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(nov["HR"]), max(nov["HR"]+1),1):
    IT_horaria.append(nov[nov["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(nov["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Noviembre")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
#  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de noviembre a las " + str(i) + " horas",fontsize=8)
    plt.savefig("nov_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
DICIEMBRE

Lo que busco con este código es hacer un día común de cada mes del año

Para esto necesito la irradiancia total de cada día de cada hora, para poder hacer un
histograma de frecuencias por hora.

"""
diciembre=data[(data["MO"] == 12) & (data["IT EXT"] != 0)]
IT_horaria=[]
for hora in range(min(diciembre["HR"]), max(diciembre["HR"]+1),1):
    IT_horaria.append(diciembre[diciembre["HR"]==hora]["IT EXT"].values) #creo una lista, donde cada entrada tiene una lista de irradiancia por hora, empieza a las 7 am y termina a las 17

i=min(diciembre["HR"])
for hora in IT_horaria:
    num_clases=int(1+np.log2(hora.shape[0]))#regla de Sturges
    rango=max(hora)-min(hora)
    ancho_clase=rango/num_clases
    print("hora: ",i,"valor mínimo: ", round(min(hora),2),"valor máximo:",round(max(hora),2),"rango: ",round(rango,2),"ancho de clase:",round(ancho_clase,2))
    mes.append("Diciembre")
    horas.append(i)
    v_min.append(round(min(hora),2))
    v_max.append(round(max(hora),2))
    ancho_clases.append(round(ancho_clase,2))
    rangos.append(round(rango,2)) 
    #i+=1 #Este i, cuando se van a graficar, eliminarlo, el i está en la parte final
#  GRÁFICAS, VAN JUNTO AL FOR DE ARRIBA, SI ES QUE SE QUIEREN GRAFICAR
    fig=plt.figure()
    plt.rcParams.update({"font.size":8, "figure.dpi":980,"font.family":"Times New Roman"}) 
    plt.hist(hora,bins=num_clases,density=False, color="orange",edgecolor="black")
    plt.xlabel("Irradiancia total. "+ r"$(W/m^{2})$")
    plt.ylabel("Frecuencia (días)")
    plt.title("Histograma de irradiancia extraterrestre de diciembre a las " + str(i) + " horas",fontsize=8)
    plt.savefig("diciembre_hora_"+str(i)+".png", dpi=980)
    i+=1
#%%
"""
mes=[]
hora=[]
v_min=[]
v_max=[]
ancho_clase=[]
rangos=[]
"""
dia_prom={
    "mes" : mes,
    "hora" : horas,
    "v min" : v_min,
    "v max" : v_max,
    "ancho clase" : ancho_clases,
    "rango": rangos
    }

diaprom=pd.DataFrame(dia_prom)
diaprom.to_csv("diaprom_EXT.csv",index=False)
