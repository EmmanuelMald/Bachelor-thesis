# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:22:39 2022

@author: Emmanuel Amador Maldonado


Este script muestra algunos parámetros usados para la captación de irradiancia solar tanto en un concentrador de un 
eje de libertad así como de uno fijo, y compara la captación entre ellos.

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%%
ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\2.- RECURSO SOLAR\\1.2 RECURSO SOLAR EN LA SUPERFICIE DE LA ATMÓSFERA"
nombre= "\\diaprom_EXT.csv"
direccion= ruta + nombre

"""

Toda esta celda es para representar la variación en la profundidad óptica a lo largo de los días. 
La profundidad óptica es un parámetro adimensional que se usa para analizar la captación de irradiancia solar a 
partir de un seguimiento en un eje de libertad.


"""

data=pd.read_csv(direccion)
dmin=0 # primer día del mes
dmax=30 # último día del mes
mesl=[]
dminl=[] 
dmaxl=[]
vmaxl=[]
vminl=[]
difl=[]
variacionl=[]
vproml=[]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
for mes in meses: #Esto es para sacar la profundidad óptica
    vmax=0.174 + 0.035*np.sin(360/365*(dmax-100)*(np.pi/180))
    vmin=0.174 + 0.035*np.sin(360/365*(dmin-100)*(np.pi/180))
    vprom=(vmax+vmin)/2
    dif=abs(vmax-vmin)
    variacion=round(abs(100*(1-vmax/vmin)),2)
    print(mes, dmin, dmax,round(vmin,2),round(vmax,2),round(dif,2),variacion,round(vprom,2))
    mesl.append(mes)
    dminl.append(round(dmin,2))
    dmaxl.append(round(dmax,2))
    vminl.append(round(vmin,2))
    vmaxl.append(round(vmax,2))
    difl.append(round(dif,2))
    variacionl.append(round(variacion,2))
    vproml.append(round(vprom,2))
    dmin += 30
    dmax += 30
profop={
        "mes":mesl,
        "dmin":dminl,
        "dmax":dmaxl,
        "vmax":vmaxl,
        "vmin":vminl,
        "dif":difl,
        "variacion":variacionl,
        "vprom":vproml
        }
profopt=pd.DataFrame(profop)
#profopt.to_csv("Profundidad optica.csv",index=False)
plt.figure()
x=np.linspace(0,365,1000)
y=0.174 + 0.035*np.sin(360/365*(x-100)*(np.pi/180)) #Esta ecuación es la variación en la profundidad óptica en relación a los días
plt.plot(x,y)
plt.rcParams["font.family"]="Times New Roman"
plt.xlabel("día del año (0 a 364)")
plt.title("Variación anual de la profundidad óptica")
#plt.savefig("Profundidad_optica.png",dpi=980)
#%% Esto es para la declinación
dmin=0
dmax=30
dmed=15
decminl=[]
decmaxl=[]
decdifl=[]
variaciondecl=[]
decproml=[]
decmedl=[] #(Ángulo de declinación)
for mes in meses:
    decmin=round(23.45*np.sin(360/365*(284+dmin)*(np.pi/180)),2)
    decmax=round(23.45*np.sin(360/365*(284+dmax)*(np.pi/180)),2)
    decdif=round(abs(decmax-decmin),2)
    variacion=round(abs(100*(1-decmax/decmin)),2)
    decprom=round((decmax+decmin)/2,2)
    decmed=round(23.45*np.sin(360/365*(284+dmed)*(np.pi/180)),2)
    decminl.append(decmin)
    decmaxl.append(decmax)
    decdifl.append(decdif)
    variaciondecl.append(variacion)
    decproml.append(decprom)
    decmedl.append(decmed)
    print(mes,decmin,decmax,decdif,variacion,decprom,decmed)
    dmin +=30
    dmax +=30
    dmed +=30

decli={
        "mes":mesl,
        "dmin":dminl,
        "dmax":dmaxl,
        "decmax":decmaxl,
        "decmin":decminl,
        "decdif":decdifl,
        "variaciondec":variaciondecl,
        "decprom":decproml,
        "decmed":decmedl
        }

declinacion=pd.DataFrame(decli)
#declinacion.to_csv("Declinacion anual.csv",index=False)
#%% Calculando el factor de difusion
dmin=0
dmax=30
dmed=15
Cminl=[] #factor de difusión en el día inicial del mes
Cmaxl=[] #factor de difusión en el día final del mes
Cproml=[] #factor de difusión promedio mes
dmedl=[]
Cvariacionl=[]
Cdifl=[]
Cmedl=[]#factor de difusión en el día  del mes
for mes in meses:
    Cmax=0.095 + 0.04*np.sin(360/365*(dmax-100)*(np.pi/180))
    Cmin=0.095 + 0.04*np.sin(360/365*(dmin-100)*(np.pi/180))
    Cmed=0.095 + 0.04*np.sin(360/365*(dmed-100)*(np.pi/180))
    Cprom=(Cmax+Cmin)/2
    Cdif=abs(Cmax-Cmin)
    Cvariacion=round(abs(100*(1-Cmax/Cmin)),2)
    print(mes,round(Cmin,2),round(Cmax,2),round(Cdif,2),Cvariacion,round(Cprom,2),round(Cmed,2))
    dmedl.append(dmed)
    Cminl.append(round(Cmin,2))
    Cmaxl.append(round(Cmax,2))
    Cdifl.append(round(Cdif,2))
    Cvariacionl.append(round(Cvariacion,2))
    Cproml.append(round(Cprom,2))
    Cmedl.append(round(Cmed,2))
    dmin += 30
    dmax += 30
    dmed += 30

plt.figure()
x=np.linspace(0,365,1000)
y=0.095 + 0.04*np.sin(360/365*(x-100)*(np.pi/180))
plt.plot(x,y,color="orange")
plt.rcParams["font.family"]="Times New Roman"
plt.xlabel("día del año (0 a 364)")
plt.title("Variación anual del factor de difusión")
#plt.savefig("Factor_difusion.png",dpi=980)
FD={
        "mes":mesl,
        "dmin":dminl,
        "dmax":dmaxl,
        "dmed":dmedl,
        "Cmax":Cmaxl,
        "Cmin":Cminl,
        "Cmed":Cmedl,
        "Cdif":Cdifl,
        "Cvariacion":Cvariacionl,
        "Cprom":Cproml,
        "Cmed":Cmedl
        }

FactD=pd.DataFrame(FD)
#FactD.to_csv("Factor Difusion.csv",index=False)

#%% Esto es para calcular la altitud solar, AM,h, y la irradiancia directa y difusa sobre un seguidor de 1 eje
ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\3.- SEGUIMIENTO SOLAR"
nombre= "\\IRRADIANCIA SEGUIDOR FIJO.csv"
L=29.336912 #Latitud del municipio de Madera, Chihuahua
direccion= ruta + nombre
data=pd.read_csv(direccion)
B=[] #Ángulo de altitud solar
AirM=[] #Masa de aire que atraviesa la radiación solar

IDirect=[] #Irradiancia directa que llega a la superficie de la Tierra, valor promedio
IDirecterror=[]# Error de la irradiancia

IDirect1=[]#Irradiancia directa que llega al concentrador con seguimiento de un eje
IDirect1error=[]

IDif1=[]
IDif1error=[]

ITCon1=[] #Irradiancia total en el concentrador solar con 1 eje
ITCon1error=[]

for i in range(len(data)):
    Lrad=L*np.pi/180
    decrad=data["dec"][i]*np.pi/180
    hrad=data["h"][i]*np.pi/180
    k=data["k"][i]
    C=data["C"][i]
    altsolrad=np.arcsin(np.sin(Lrad)*np.sin(decrad)+np.cos(Lrad)*np.cos(decrad)*np.cos(hrad))
    altsol=round(abs(altsolrad*180/np.pi),2)
    AirMass=round(abs(1/np.sin(altsolrad)),2)
    
    Idir=round(data["IEXTPROM"][i]*np.exp(-k*AirMass),2)
    Idirerror=round(data["error"][i]*np.exp(-k*AirMass),2)
    
    Idir1=round(Idir*np.cos(decrad),2)
    Idir1error=round(Idirerror*np.cos(decrad),2)
    
    Idif1=round(C*Idir*(1+np.cos(np.pi/2 - altsolrad + decrad)/2),2)
    Idif1error=round(C*Idirerror*(1+np.cos(np.pi/2 - altsolrad + decrad)/2),2)
    
    ITcon1=round(Idir1+Idif1,2)
    ITcon1error=round(Idir1error+Idif1error,2)
    
    B.append(altsol)
    AirM.append(AirMass)
    
    IDirect.append(Idir)
    IDirect1.append(Idir1)
    
    IDif1.append(Idif1)
    ITCon1.append(ITcon1)
    
    IDirecterror.append(Idirerror)
    IDirect1error.append(Idir1error)
    
    IDif1error.append(Idif1error)
    ITCon1error.append(ITcon1error)
    
data.insert(10,"B",B)
data.insert(11,"AM",AirM)
data.insert(12,"IDirect1",IDirect1)
data.insert(13,"IDif1",IDif1)
data.insert(14,"IT1",ITCon1)

data.insert(15,"IDirect1error",IDirect1error)
data.insert(16,"IDif1error",IDif1error)
data.insert(17,"IT1error",ITCon1error)


#data.to_csv("Irradiancia 1 Eje.csv",index=False)

#%% Calculando la irradiancia sobre un concentrador fijo
#Proponiendo un valor de ángulo azimutal para el concentrador de 0°
ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\3.- SEGUIMIENTO SOLAR"
nombre= "\\Irradiancia 0 Eje.csv"
L=29.336912
Lrad=L*np.pi/180
direccion= ruta + nombre
data0=pd.read_csv(direccion)
inclin=30.72 #ángulo de inclinación del concentador, en grados
inclinrad= inclin*(np.pi/180) #ángulo de inclinación en radianes
Azimut=[] #Ángulo azimutal del sol
AngInc=[] #Ángulo de incidencia
IrBC=[] #Irradiancia directa sobre el concentrador solar de 0 ejes
IDifC=[]
IrT0=[]

IrBCerror=[]
IDifCerror=[]
IrT0error=[]


BNprom=round(data0[data0["hora"]==12]["B"].sum()/len(data0[data0["hora"]==12]),2)
decPROM=round(data0["dec"].mean(),2)
print(BNprom,decPROM)
print("El ángulo de inclinación ideal es:", 90- BNprom + decPROM)



for i in range(len(data0)):
    decrad=data0["dec"][i]*np.pi/180 #declinación en rad
    hrad=data0["h"][i]*np.pi/180 #hora horaria en rad
    k=data0["k"][i] #profundidad óptica
    AM=data0["AM"][i]#Masa de Aire
    C=data0["C"][i] #factor de difusión
    altsolrad=data0["B"][i]*np.pi/180 #altitud solar
    azimutrad=round(np.arcsin(round(np.cos(decrad)*np.sin(hrad)/np.cos(altsolrad),2)),2) #ángulo azimutal solar en rad
    anginc=np.arccos(np.cos(altsolrad)*np.cos(azimutrad)*np.sin(inclinrad)+np.sin(altsolrad)*np.cos(inclinrad))
    
    
    Idir=round(data["IEXTPROM"][i]*np.exp(-k*AM),2)
    Idirerror=round(data["error"][i]*np.exp(-k*AM),2)
    
    Ibc=Idir*np.cos(anginc) #Irradiancia directa sobre el concentrador de 0 ejes
    Idifc=C*Idir*(1+np.cos(inclinrad))/2 #Irradiancia difusa sobre el concentrador de 0 ejes
    irt0=Ibc+Idifc
    
    Ibcerror=Idirerror*np.cos(anginc)
    Idifcerror=C*Idirerror*(1+np.cos(inclinrad))/2
    Irt0error=Ibcerror + Idifcerror
    
    Azimut.append(round(azimutrad*(180/np.pi),2)) #Ángulo azimuth solar
    AngInc.append(round(anginc*(180/np.pi),2)) #Ángulo de incidencia
    IrBC.append(round(Ibc,2))    
    IDifC.append(round(Idifc,2))
    IrT0.append(round(irt0,2))
    
    IrBCerror.append(round(Ibcerror,2))
    IDifCerror.append(round(Idifcerror,2))
    IrT0error.append(round(Irt0error,2))

data0.insert(12,"Azimut",Azimut)
data0.insert(13,"AngIncidencia",AngInc)

data0.insert(14,"IDirect0",IrBC)
data0.insert(15,"IDif0",IDifC)
data0.insert(16,"IT0",IrT0)

data0.insert(17,"IDirect0error",IrBCerror)
data0.insert(18,"IDif0error",IDifCerror)
data0.insert(19,"IT0error",IrT0error)

#data0.to_csv("Irradiancia 0 Eje.csv",index=False)

#%% Esto es para eliminar las filas repetidas de los datasets, si es que los hay, y reescribe el csv
ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\3.- SEGUIMIENTO SOLAR"
nombre0= "\\Irradiancia 0 Eje.csv"
nombre1= "\\Irradiancia 1 Eje.csv"
data0=pd.read_csv(ruta+nombre0)
data=pd.read_csv(ruta+nombre1)

data0=data0.drop_duplicates() #elimina las filas que tienen exactamente los mismos valores
data=data.drop_duplicates()

data0.to_csv("Irradiancia 0 Eje.csv", index=False)
data.to_csv("Irradiancia 1 Eje.csv", index=False)
#Ahora sí concuerdan las horas de sol de la irradiancia extraterrestre con la calculada en la
#irradiancia terrestre jeje

#%%  ESTO ES UNA COMPARATIVA DE IT1 VS IT0. Es decir, la irradiancia total incidente sobre un concentrador fijo
## y uno fijo

ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON"
nombre0= "\\3.- SEGUIMIENTO SOLAR\\Irradiancia 0 Eje.csv"
nombre1= "\\3.- SEGUIMIENTO SOLAR\\Irradiancia 1 Eje.csv"
nombre2="\\2.- RECURSO SOLAR\\1.2 RECURSO SOLAR EN LA SUPERFICIE DE LA ATMÓSFERA\\diaprom_EXT.csv"
data0=pd.read_csv(ruta+nombre0)
data=pd.read_csv(ruta+nombre1)
data2=pd.read_csv(ruta+nombre2)


incIT=round(data["IT1"].sum()/data0["IT0"].sum() - 1 ,2) #Incremento en la captación de irradiancia
incIDirect=round(data["IDirect1"].sum()/data0["IDirect0"].sum() - 1,2)
incIDif=round(data["IDif1"].sum()/data0["IDif0"].sum()-1,2)
print("Se tiene un incremento del ",100*(incIT)," % en IT")
print("Se tiene un incremento del ",100*(incIDirect)," % en IDirecta")
print("Se tiene un incremento del ",100*(incIDif)," % en IDifusa")

meses0=data0.groupby("mes")
meses1=data.groupby("mes")
meses2=data2.groupby("mes")
flag=0
for mes0, datos0 in meses0:
    for mes1, datos1 in meses1:
        if mes1==mes0  and flag<1:
            flag+=1
            plt.figure()
            # IT1 VS IT0
            x=np.linspace(datos1["hora"].iloc[0],datos1["hora"].iloc[-1])
            coef0=np.polyfit(datos0["hora"],datos0["IT0"],4)
            coef1=np.polyfit(datos1["hora"],datos1["IT1"],4)
    
            y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
            y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]
           
            plt.rcParams["font.family"]="Times New Roman"
            plt.plot(x,y1,color="orange")
            plt.plot(x,y0,color="#0979B0")
           
            plt.errorbar(datos1["hora"],datos1["IT1"],yerr=datos1["IT1error"],fmt="o", markerfacecolor="orange",ecolor="orange", label="con seguimiento")
            plt.errorbar(datos0["hora"],datos0["IT0"],yerr=datos0["IT0error"],fmt="o", markerfacecolor="#0979B0",ecolor="#0979B0", label="sin seguimiento") #fmt se usa cuando no quieres que se genere una recta para unir puntos, sino se pone marker
            
            plt.title("Irradiancia total incidente en el concentrador solar en un día típico de " + str(mes0))
            plt.legend()
            plt.xlabel("Hora del día (0 a 23 hrs)")
            plt.ylabel("Irradiancia total " + r"$W/m^{2}$")
            plt.savefig("Irradiancia en el concentrador en "+str(mes0)+".png",dpi=1100)
            
    flag=0
        
#%% ESTO ES PARA GENERAR LAS GRÁFICAS ANUALES
ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\3.- SEGUIMIENTO SOLAR"
nombre0= "\\Irradiancia 0 Eje.csv"
nombre1= "\\Irradiancia 1 Eje.csv"
data0=pd.read_csv(ruta+nombre0)
data=pd.read_csv(ruta+nombre1)
meses0=data0.groupby("mes")
meses1=data.groupby("mes")

ITEXTmes=[]
ITEXTmeserror=[]

IT0mes=[]
IDirect0mes=[]
IDif0mes=[]

IT1mes=[]
IDirect1mes=[]
IDif1mes=[]

IT0meserror=[]
IDirect0meserror=[]
IDif0meserror=[]

IT1meserror=[]
IDirect1meserror=[]
IDif1meserror=[]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

for i in meses:
    for mes1, datos1 in meses1:
        for mes0, datos0 in meses0:
            if mes1==mes0 and i==mes1 and flag<1:
                print(mes1)
                flag+=1
                
                itextmes=round(datos0["IEXTPROM"].sum(),2)
                itextmeserror=round(datos0["error"].sum(),2)
                
                it0mes=round(datos0["IT0"].sum(),2)
                it1mes=round(datos1["IT1"].sum(),2)
                
                idirect0mes=round(datos0["IDirect0"].sum(),2)
                idirect1mes=round(datos1["IDirect1"].sum(),2)
                
                idif0mes=round(datos0["IDif0"].sum(),2)
                idif1mes=round(datos1["IDif1"].sum(),2)
                
                it0meserror=round(datos0["IT0error"].sum(),2)
                it1meserror=round(datos1["IT1error"].sum(),2)
                
                idirect0meserror=round(datos0["IDirect0error"].sum(),2)
                idirect1meserror=round(datos1["IDirect1error"].sum(),2)
                
                idif0meserror=round(datos0["IDif0error"].sum(),2)
                idif1meserror=round(datos1["IDif1error"].sum(),2)
                
                ITEXTmes.append(itextmes)
                ITEXTmeserror.append(itextmeserror)
                
                IT0mes.append(it0mes)
                IDirect0mes.append(idirect0mes)
                IDif0mes.append(idif0mes)
                IT1mes.append(it1mes)
                IDirect1mes.append(idirect1mes)
                IDif1mes.append(idif1mes)
                
                IT0meserror.append(it0meserror)
                IDirect0meserror.append(idirect0meserror)
                IDif0meserror.append(idif0meserror)
                IT1meserror.append(it1meserror)
                IDirect1meserror.append(idirect1meserror)
                IDif1meserror.append(idif1meserror)
            
    flag=0

datgen=pd.DataFrame({
        "mes":meses,
        "IT0mes": IT0mes,
        "IDirect0mes":IDirect0mes,
        "IDif0mes":IDif0mes,
        "IT1mes": IT1mes,
        "IDirect1mes":IDirect1mes,
        "IDif1mes":IDif1mes,
        
        "IT0meserror": IT0meserror,
        "IDirect0meserror":IDirect0meserror,
        "IDif0meserror":IDif0meserror,
        "IT1meserror": IT1meserror,
        "IDirect1meserror":IDirect1meserror,
        "IDif1meserror":IDif1meserror,
        
        "ITEXTmes":ITEXTmes,
        "ITEXTmeserror":ITEXTmeserror
        })

datgen.to_csv("Datos generales concentrador.csv",index=False)

#%% Gráficas anuales
ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\3.- SEGUIMIENTO SOLAR"
nombre= "\\Datos generales concentrador.csv"
datagen=pd.read_csv(ruta+nombre)

fig=plt.figure(dpi=1600)
plt.rcParams["font.family"]="Times New Roman"
x=np.linspace(0,11)

coef0=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["IT0mes"],4)
coef1=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["IT1mes"],4)
coefext=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["ITEXTmes"],4)

y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]
yext=coefext[0]*x**4+coefext[1]*x**3+coefext[2]*x**2+coefext[3]*x+coefext[4]


plt.plot(x,yext,color="green")
plt.plot(x,y1,color="orange")
plt.plot(x,y0,color="#0979B0")

plt.errorbar(datagen["mes"],datagen["ITEXTmes"],yerr=datagen["ITEXTmeserror"], fmt="o", markerfacecolor="green", ecolor="green",label="Parte superior de la atmósfera")
plt.errorbar(datagen["mes"],datagen["IT1mes"],yerr=datagen["IT1meserror"], fmt="o", markerfacecolor="orange", ecolor="orange",label="Concentrador con seguimiento")
plt.errorbar(datagen["mes"],datagen["IT0mes"],yerr=datagen["IT0meserror"], fmt="o", markerfacecolor="#0979B0", ecolor="#0979B0",label="Concentrador fijo")
plt.legend()

plt.xticks(rotation=45,fontsize=9)
plt.title("Energía solar total en un día típico de cada mes",fontsize=10)
plt.ylabel("Energía solar total " + r"$Wh/m^{2}/día$")

"""Esto es para graficar el incremento de la irradiancia directa"""

fig=plt.figure(dpi=1600)
plt.rcParams["font.family"]="Times New Roman"

coef0=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["IDirect0mes"],4)
coef1=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["IDirect1mes"],4)

y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]

plt.plot(x,y1,color="orange")
plt.plot(x,y0,color="#0979B0")
plt.errorbar(datagen["mes"],datagen["IDirect1mes"],yerr=datagen["IDirect1meserror"], fmt="o", markerfacecolor="orange", ecolor="orange",label="Sistema de seguimiento")
plt.errorbar(datagen["mes"],datagen["IDirect0mes"],yerr=datagen["IDirect0meserror"], fmt="o", markerfacecolor="#0979B0", ecolor="#0979B0",label="Sistema fijo")
plt.legend()

plt.xticks(rotation=45,fontsize=9)
plt.title("Energía solar directa incidente en el concentrador durante un día típico de cada mes",fontsize=10)
plt.ylabel("Energía solar directa " + r"$Wh/m^{2}/día$")

"""Esto es para graficar la variación porcentual de la irradiancia incidente"""
fig=plt.figure(dpi=1600)
plt.rcParams["font.family"]="Times New Roman"

plt.bar(datagen["mes"],datagen["varmen"], color="#5DC1B9",width=0.5)
plt.plot(datagen["mes"],datagen["varmen"], color="#0095C7")

plt.xticks(rotation=45,fontsize=9)
plt.title("Incremento de la cantidad de irradiancia captada\n de un sistema de seguimiento solar respecto a un sistema fijo",fontsize=12)
plt.ylabel("%")


"""Esto es para graficar el incremento de la irradiancia difusa"""

fig=plt.figure(dpi=1600)
plt.rcParams["font.family"]="Times New Roman"

coef0=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["IDif0mes"],4)
coef1=np.polyfit([0,1,2,3,4,5,6,7,8,9,10,11],datagen["IDif1mes"],4)

y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]

plt.plot(x,y1,color="orange")
plt.plot(x,y0,color="#0979B0")
plt.errorbar(datagen["mes"],datagen["IDif1mes"],yerr=datagen["IDif1meserror"], fmt="o", markerfacecolor="orange", ecolor="orange",label="Sistema de seguimiento")
plt.errorbar(datagen["mes"],datagen["IDif0mes"],yerr=datagen["IDif0meserror"], fmt="o", markerfacecolor="#0979B0", ecolor="#0979B0",label="Sistema fijo")
plt.legend()

plt.xticks(rotation=45,fontsize=9)
plt.title("Energía solar proveniente de la irradiancia difusa \n incidente en el concentrador durante un día típico de cada mes",fontsize=10)
plt.ylabel("Energía solar difusa " + r"$Wh/m^{2}/día$")
#%% VARIACIÓN DE LA IRRADIANCIA DURANTE LAS MAÑANAS, MEDIOS DÍAS Y TARDES

ruta= "C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\EVIDENCIAS PYTHON\\3.- SEGUIMIENTO SOLAR"
nombre0= "\\Irradiancia 0 Eje.csv"
nombre1= "\\Irradiancia 1 Eje.csv"
data0=pd.read_csv(ruta + nombre0)
data1=pd.read_csv(ruta + nombre1)

horas0=data0.groupby("hora")
horas1=data1.groupby("hora")

datosdiarios=[]

for hora0, datos0 in horas0:
    for hora1, datos1 in horas1:
        if hora0==hora1:
            
            IT0=round(datos0["IT0"].sum()/len(datos0),2)
            IT1=round(datos1["IT1"].sum()/len(datos0),2)
            IT0error=round(datos0["IT0error"].sum()/len(datos0),2)
            IT1error=round(datos1["IT1error"].sum()/len(datos0),2)
            
            IDirect0=round(datos0["IDirect0"].sum()/len(datos0),2)
            IDirect1=round(datos1["IDirect1"].sum()/len(datos0),2)
            IDirect0error=round(datos0["IDirect0error"].sum()/len(datos0),2)
            IDirect1error=round(datos1["IDirect1error"].sum()/len(datos0),2)
            
            IDif0=round(datos0["IDif0"].sum()/len(datos0),2)
            IDif1=round(datos1["IDif1"].sum()/len(datos0),2)
            IDif0error=round(datos0["IDif0error"].sum()/len(datos0),2)
            IDif1error=round(datos1["IDif1error"].sum()/len(datos0),2)
                
            datosdiarios.append([hora0,IT0,IT1,IT0error,IT1error,
                       IDirect0,IDirect1,IDirect0error,IDirect1error,
                       IDif0,IDif1,IDif0error,IDif1error])
          
    
"""Variación de la irradiancia durante las mañanas"""


horas=[]
IT0=[]
IT1=[]
IDirect0=[]
IDirect1=[]
IDif0=[]
IDif1=[]

IT0error=[]
IT1error=[]
IDirect0error=[]
IDirect1error=[]
IDif0error=[]
IDif1error=[]
for dato in datosdiarios:
    horas.append(dato[0])
    IT0.append(dato[1])
    IT1.append(dato[2])
    IT0error.append(dato[3])
    IT1error.append(dato[4])
    
    IDirect0.append(dato[5])
    IDirect1.append(dato[6])
    IDirect0error.append(dato[7])
    IDirect1error.append(dato[8])
    
    IDif0.append(dato[9])
    IDif1.append(dato[10])
    IDif0error.append(dato[11])
    IDif1error.append(dato[12])
#IRRADIANCIA TOTAL HORARIA PROMEDIO ANUAL
plt.figure()
plt.rcParams["font.family"]="Times New Roman"

coef0=np.polyfit(horas,IT0,4)
coef1=np.polyfit(horas,IT1,4)

x=np.linspace(horas[0], horas[-1])
y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]

plt.plot(x,y1,color="orange")
plt.plot(x,y0,color="#0979B0")

plt.errorbar(horas,IT1,yerr=IT1error, fmt="o", markerfacecolor="orange", ecolor="orange",label="Sistema de seguimiento")
plt.errorbar(horas,IT0,yerr=IT0error, fmt="o", markerfacecolor="#0979B0", ecolor="#0979B0",label="Sistema fijo")
plt.title("Irradiancia total incidente\n en un CCP a lo largo de un día promedio anual")
plt.legend(loc="lower center")
plt.ylabel(r"$W/m^{2}$")
plt.xlabel("Hora del día (0-23 hrs)")
plt.savefig("Irradianciahorasanuales.png",dpi=1500)

#IRRADIANCIA DIRECTA HORARIA PROMEDIO ANUAL
plt.figure()
plt.rcParams["font.family"]="Times New Roman"

x=np.linspace(horas[0], horas[-1])
coef0=np.polyfit(horas,IDirect0,4)
coef1=np.polyfit(horas,IDirect1,4)


y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]

plt.plot(x,y1,color="orange")
plt.plot(x,y0,color="#0979B0")

plt.errorbar(horas,IDirect1,yerr=IDirect1error, fmt="o", markerfacecolor="orange", ecolor="orange",label="Sistema de seguimiento")
plt.errorbar(horas,IDirect0,yerr=IDirect0error, fmt="o", markerfacecolor="#0979B0", ecolor="#0979B0",label="Sistema fijo")
plt.title("Irradiancia directa incidente\n en un CCP a lo largo de un día promedio anual")
plt.legend(loc="lower center")
plt.ylabel(r"$W/m^{2}$")
plt.xlabel("Hora del día (0-23 hrs)")
plt.savefig("Irradianciadirectaanuales.png",dpi=1500)

#IRRADIANCIA DIFUSA HORARIA PROMEDIO ANUAL

plt.figure()
plt.rcParams["font.family"]="Times New Roman"

x=np.linspace(horas[0], horas[-1])
coef0=np.polyfit(horas,IDif0,4)
coef1=np.polyfit(horas,IDif1,4)

y0=coef0[0]*x**4+coef0[1]*x**3+coef0[2]*x**2+coef0[3]*x+coef0[4] #TODO ESTO ES MÍNIMOS CUADRADOS PARA UNIR LOS PUNTOS
y1=coef1[0]*x**4+coef1[1]*x**3+coef1[2]*x**2+coef1[3]*x+coef1[4]

plt.plot(x,y1,color="orange")
plt.plot(x,y0,color="#0979B0")

plt.errorbar(horas,IDif1,yerr=IDif1error, fmt="o", markerfacecolor="orange", ecolor="orange",label="Sistema de seguimiento")
plt.errorbar(horas,IDif0,yerr=IDif0error, fmt="o", markerfacecolor="#0979B0", ecolor="#0979B0",label="Sistema fijo")
plt.title("Irradiancia difusa incidente\n en un CCP a lo largo de un día promedio anual")
plt.legend(loc="lower center")
plt.ylabel(r"$W/m^{2}$")
plt.xlabel("Hora del día (0-23 hrs)")
plt.savefig("Irradianciadifusaanuales.png",dpi=1500)

datagenhora=pd.DataFrame({
    "hora":horas,
    "IT1":IT1,
    "IDirect1":IDirect1,
    "IDif1":IDif1,
    "IT0":IT0,
    "IDirect0":IDirect0,
    "IDif0":IDif0,
    
    "IT1error":IT1error,
    "IDirect1error":IDirect1error,
    "IDif1error":IDif1error,
    "IT0error":IT0error,
    "IDirect0error":IDirect0error,
    "IDif0error":IDif0error,
    })

#datagenhora.to_csv("datos hora anuales.csv")
#%% Esto es para comparar los valores

varIT=round(100*(datagen["IT1mes"].sum()/datagen["IT0mes"].sum()-1),2)
varEXT=round(100*(datagen["IT1mes"].sum()/datagen["ITEXTmes"].sum()),2)
varEXT0=round(100*(datagen["IT0mes"].sum()/datagen["ITEXTmes"].sum()),2)
#print(round(datagen["IT0mes"].sum(),2),round(datagen["IT1mes"].sum(),2))
print(varEXT)
print(varEXT0)
print("Los valores de irradiancia total incidente sobre el colector con seguimiento mejoraron en un ", varIT, " % respecto a un concentrador fijo ")
print("Irradiancia directa: ", round(100*(datagen["IDirect0mes"].sum()/datagen["IDirect1mes"].sum()-1),2))
print("Irradiancia difusa: ", round(100*(1-datagen["IDif0mes"].sum()/datagen["IDif1mes"].sum()),2))
varIDir=round(datagen["IDirect1mes"].sum()/datagen["IDirect0mes"].sum()-1,2)
print("IDirecta: ", varIDir)
#Gráfica de la variación porcentual mensual en la captación de energía
varEnero=round(100*(datagen["IT1mes"][0]/datagen["IT0mes"][0]-1),2)
varNov=round(100*(datagen["IT1mes"][10]/datagen["IT0mes"][10]-1),2)
varDic=round(100*(datagen["IT1mes"][11]/datagen["IT0mes"][11]-1),2)
print("La captación de energía solar mejora en un ",varEnero," % durante el mes de enero")
print("La captación de energía solar mejora en un ",varNov," % durante el mes de Nov")
print("La captación de energía solar mejora en un ",varDic," % durante el mes de Dic")

varMay=round(100*(datagen["IT1mes"][4]/datagen["IT0mes"][4]-1),2)
varJun=round(100*(datagen["IT1mes"][5]/datagen["IT0mes"][5]-1),2)
varJul=round(100*(datagen["IT1mes"][6]/datagen["IT0mes"][6]-1),2)
print("La captación de energía solar mejora en un ",varMay," % durante el mes de Mayo")
print("La captación de energía solar mejora en un ",varJun," % durante el mes de JUn")
print("La captación de energía solar mejora en un ",varJul," % durante el mes de Jul")

