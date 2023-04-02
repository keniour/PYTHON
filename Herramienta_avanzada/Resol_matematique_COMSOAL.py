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
import random

#Definicion del tiempo de ciclo
TC=12

num_tot_act=11

#duracion de cada actividad :
duracion=[5,2,3,4,3,2,3,3.5,1,2.5,1]

#Matriz de relacion es decedencia (vale 1 si j precede a i)
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

eff_max=0
sol=np.zeros((num_tot_act,num_tot_act)) #matriz de cero donde se pondra la mejor solucion
sol_capa_ET=np.zeros((1,num_tot_act)) #vector solucion que indica la capacidad de cada ET
sol_num_ET=0#solucion de la Q de ET

iteracion=5000


for g in range(iteracion): #500=numero d'iteracion
    
    opAsig=np.zeros((1,num_tot_act)) #vector inicial de cero que indica 1 en la posicion i si la tarea i ya fue asignada a un ET
    capa_ET=np.zeros((1,num_tot_act)) #Vector que indica la capacidad de cada ET
    
    matriz_act=np.zeros((num_tot_act,num_tot_act)) #matriz que guarda las actividades que añadamos durante el process 
    #(cada linea=un ET y se pone el numero de las actividades que hace este ET en su linea)
    #! ATTENTION : les chiffres dans la matriz_act désigne les activités comment commencant par 1 (et non pas par 0)
    num_ET=0
    
    w=np.zeros((1,num_tot_act))
    
    asignacion_terminada=False #variable para terminar el lazo while
    
    I=-1 #variable aux utilizada para guardar las act que realiza cada ET
    
    while not asignacion_terminada  :
        for i in range(num_tot_act) : #recorrer todas las actividades p ver si pueden ingresar a w
            if opAsig[0][i]==0 : #si la operacion no fue aun asignada
                j=0
                puedeEjecutarse=1 #val aux que vale 1 si la act i esta en condiciones de ejecutarse
                
                while j<num_tot_act :  #recorrer todas las actividades
                    if precedesores[i][j]==0 or opAsig[0][j]==1 : #si no tiene predecesores o el predecesor ya fue asignado
                        j+=1
                    else : #cas ou la tache a un prédecesseurs qui n'a pas encore été asigné 
                        puedeEjecutarse=0
                        break #salgo del while 
                        
                        

                if puedeEjecutarse==1 and duracion[i]+capa_ET[0][num_ET]<=TC : 
                    w[0][i]=1 
                    #si act i cumple con los req de predecesores y
                    #tiene una duracion menos al tiempo remanente en la ET
                    #puede incluirse dentro de las candidatas
        

        
        
        aux=sum(w[0]) #variable auxiliar para determinar que actividad se va a seleccionar 
        
        if aux>0 :  #si en w hay componentes 
            aleat=random.randint(1,aux)#se elige aleatoriamente una actividad
            k=0         #k e i variable auxiliares
            i=-1
            while k<aleat :     #se busca la actividad num aleat de las asignadas a w
                i+=1
                k+=w[0][i]
                

            I+=1
            #! 4-Asignar la tarea a la ET bajo análisis. Actualizar tiempos de la ET.
            opAsig[0][i]=1  #se asigna la act elegida
            w[0][i]=0   #se quita de w
            capa_ET[0][num_ET]+=duracion[i]    #actualizar capacidad ocupada en la estacion vigente
            matriz_act[num_ET][I]=i+1    #se guarda q act se hace en cada ET
            #!5-Actualizar el grupo de tareas candidatas.
            #actualizacion del vector w
            for k in range(num_tot_act) : #se actualiza w sacando las actividades donde su tiempo es mayor que la capacidad de la ET
                if w[0][k]==1 and duracion[i]+capa_ET[0][num_ET]>TC : #? j'ai modifié i en k ici
                    w[0][k]=0 
            
            #!6-Repetir hasta que todas que todas las tareas estén asignadas a una ET
            
            if sum(opAsig[0])==num_tot_act : #si asignaron todas las actividades
                asignacion_terminada=1
            
        else :
            num_ET+=1
            I=-1
    
    #! Calcular la eficiencia de la solucion actual y guardar la solucion solo si mejora la eficiencia de la solucion considerada como la mejor hasta el momento
    
    TCT=max(capa_ET[0])
    aux2=sum(capa_ET[0])/(TCT*num_ET) #calculo de la eficiencia 
    if aux2>eff_max :  #para determinar si es mas eficiente que la anterior
        eff_max=aux2
        sol=matriz_act
        sol_capa_ET=capa_ET
        sol_num_ET=num_ET+1



# Affichage des résultats :

print(f"Después {iteracion} iteraciones, la mejor solución encontrada es : ")
print(f"Efficacidad : {eff_max}\n")
print(f"Composicion ET : ")
for range,line in enumerate(sol) :
    if sum(line)!=0 :
        print(f"ET n°{range+1} :")
        for value in line :
            if value!=0:
                print(value)

        print(f"Capacidad total : {sol_capa_ET[0][range]}\n")




    
        