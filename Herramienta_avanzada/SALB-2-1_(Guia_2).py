"""

    
"""



#%% 
import numpy as np 
import random
# ! Definicion de las variables
duracion=[5,2,3,4,3,2,3,3.5,1,2.5,1] 
N=4 #numero minimo de estacion # ? Variable a cambiar de 4 a 5 en el problema
precedesores=[[0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0],#F
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,1,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0],
              [0,0,0,1,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,1,0]]
asignacion_tarea_estacion=[[],[],[],[]]
δ=0.05



s=0 #índice de la estación que está siendo considerada
U=sum(duracion)
#X=U/(N-s+1) #Tiempo ideal que tomamos como primer objetivo 
X=np.zeros((1,N))
X[0][0]=U/(N-s+1)
capa_ET=np.zeros((1,N))
asignacion_tarea_estacion=[[],[],[],[]]
opAsig=np.zeros((1,N)) #vector inicial de cero que indica 1 en la posicion i si la tarea i ya fue asignada a un ET


#%% Lazo

asignacion_terminada=False
while not asignacion_terminada :


    # * Etapa 5 :
    w=np.zeros((1,len(precedesores)))
    
    
    for i in range(N) : #recorrer todas las actividades p ver si pueden ingresar a w
            if opAsig[0][i]==0 : #si la operacion no fue aun asignada
                j=0
                puedeEjecutarse=1 #val aux que vale 1 si la act i esta en condiciones de ejecutarse
                
                while j<N :  #recorrer todas las actividades
                    if precedesores[i][j]==0 or opAsig[0][j]==1 : #si no tiene predecesores o el predecesor ya fue asignado
                        j+=1
                    else : #cas ou la tache a un prédecesseurs qui n'a pas encore été asigné 
                        puedeEjecutarse=0
                        break #salgo del while 
                        
                        

                if puedeEjecutarse==1: #and duracion[i]+capa_ET[0][s]<=TC : # ! A REVOIR CETTE LIGNE
                    w[0][i]=1 
                    #si act i cumple con los req de predecesores y
                    #tiene una duracion menos al tiempo remanente en la ET
                    #puede in
    # * Fin Etapa 5
    
    numero_de_estacion_en_w=sum(w[0])
    for index,statut in enumerate(w[0]):
        index_tarea_max_tiempo=0
        if statut==1 :
            if duracion[index]>duracion[index_tarea_max_tiempo] :
                index_tarea_max_tiempo=index
    
    k=index_tarea_max_tiempo
    
    # * Etapa 7.1 : Caso donde acceptamos la tarea en la estacion
    if y+duracion[k]<=X[0][s] :
        y=y+duracion[k]
        opAsig[0][s]=1
        asignacion_tarea_estacion[s].append(k)
    
    else : # * Etapa 7.2
        U-=y
        s+=1
        if s>N : # * Etapa 7.2.3 (return a zero)
            X[0][0]+=δ
            y=0
            s=0
            U=sum(duracion)
            capa_ET=np.zeros((1,N))
            asignacion_tarea_estacion=[[],[],[],[]]
            opAsig=np.zeros((1,N)) #vector inicial de cero que indica 1 en la posicion i si la tarea i ya fue asignada a un ET
            
        X[0][s]=U/(N-s+1)
        if X[0][s]<=X[0][s-1] : # * Etapa 7.2.5
            X[0][s]=X[0][s-1]
            y=0 
        else :
            X[0][0]+=δ
            s=0
            y=0
            U=sum(duracion)
            capa_ET=np.zeros((1,N))
            asignacion_tarea_estacion=[[],[],[],[]]
            opAsig=np.zeros((1,N)) #vector inicial de cero que indica 1 en la posicion i si la tarea i ya fue asignada a un ET
                    
    if len(opAsig[0])==sum(opAsig[0]) :
        asignacion_terminada=True
        