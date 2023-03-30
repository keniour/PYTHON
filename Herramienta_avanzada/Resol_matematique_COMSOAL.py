"""Ce programme est déstiné a résoudre les problèmes COMSOAL
    de manière mathématique grâce aux modèles données
    Ce programme pourra donc être liés aux deux précédents pour créer 
    une interface de résolution plus agréable et plus friendly
"""
# ? question
# ! urgent
# * comentaire classique 

#%%Definicion de las variables 
import numpy as np


#Definicion del tiempo de ciclo
TC=40

num_tot_act=15

#duracion de cada actividad :
duracion=[10,12,7,8,20,4,11,6,9,12,15,13,9,8,9]

#Matriz de relacion es decedencia (vale 1 si j precede a i)
precedesores=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
              [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]

eff_max=0
sol=np.zeros((num_tot_act,num_tot_act)) #matriz de cero donde se pondra la mejor solucion
sol_capa_ET=np.zeros((1,num_tot_act)) #vector solucion que indica la capacidad de cada ET
sol_num_ET=0#solucion de la Q de ET

#%%

for g in range(1,500): #500=numero d'iteracion
    
    asig_tarea=np.zeros((1,num_tot_act)) #vector inicial de cero que indica 1 en la posicion i si la tarea i ya fue asignada a un ET
    capa_ET=np.zeros((1,num_tot_act)) #Vector que indica la capacidad de cada ET
    
    matriz_act=np.zeros((num_tot_act,num_tot_act)) #matriz que guarda las actividades que añadamos durante el process
    num_ET=1
    
    w=np.zeros((1,num_tot_act))
    
    asignacion_terminada=False #variable para terminar el lazo while
    
    I=0 #variable aux utilizada para guardar las act que realiza cada ET
    
    while not asignacion_terminada  :
        for i in range(1,num_tot_act) : #recorrer todas las actividades p ver si pueden ingresar a w
            if asig_tarea[0][i]==0 : #si la operacion no fue aun asignada
                j=1
                puedeEjecutarse=1 #val aux que vale 1 si la act i esta en condiciones de ejecutarse
                
                while j<=num_tot_act :  #recorrer todas las actividades
                    
                    if     #si no tiene predecesores o el predecesor ya fue asignado
                    
                    else : #cas ou la tache a un prédecesseurs qui n'a pas encore été asigné 
                        j=num_tot_act+1 #salgo del while 
                        puedeEjecutarse=0
                        

                if puedeEjecutarse==1 and duracion[i]+capa_ET[0][num_ET]<=TC :
                    #si act i cumple con los req de predecesores y
                    #tiene una duracion menos al tiempo remanente en la ET
                    #puede incluirse dentro de las candidatas
        

        
        #attention a la fonction sum la :
        aux=sum(w) #variable auxiliar para determinar que actividad se va a seleccionar 
        
        if aux>0 :  #si en w hay componentes 
            aleat=      #se elige aleatoriamente una actividad
            k=0         #k e i variable auxiliares
            i=0
            while k<aleat :     #se busca la actividad num aleat de las asignadas a w
                i+=1
                k+=w[0][i]

            I+=1
            
            asig_tarea[0][i]=1  #se asigna la act elegida
            w[0][i]=0   #se quita de w
                        #actualizar capacidad ocupada en la estacion vigente
            matriz_act[num_ET][I]=i     #se guarda q act se hace en cada ET
        
            #actualizacion del vector w
            for k in range(1,num_tot_act) : #se actualiza w sacando las actividades donde su tiempo es mayor que la capacidad de la ET
                if w[0][k]==1 and duracion[k]+capa_ET[num_ET]>TC :
                    w[0][k]=0
            
            #!Repetir hasta que todas
     








    
        