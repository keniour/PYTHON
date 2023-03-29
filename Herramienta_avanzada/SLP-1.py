"""Ce programme est destinné dans un premier temps à résoudre des problèmes d'attributions
de centre d'activité à l'aide de la méthode SLP-1"""



#%%

import matplotlib.pyplot as plt
import tache


def afficher_graph(points):
    del(points[0])
    nbr_tache=len(points)
    #construction de la grille
    plt.xlim(0,nbr_tache+2)
    plt.ylim(0,10)
    plt.grid=True
    #récupération du nbr de points par niveau
    niveau=[0 for ii in range(100)]
    for tache in points :
        niv=tache.niveau
        niveau[niv]+=1

    #Création des points que l'on placera sur le graph
    points_x=[]
    points_y=[]
    for tache in points :
        niv=tache.niveau
        x=niv
        #combien de points sont déjà placé sur ce niveau ?
        compteur=0
        for i in points_x:
            if i==x:
                compteur+=1
        
        y=0+(10/niveau[niv])*(compteur+1)
        
        points_x.append(x)
        points_y.append(y)
        tache.x=x
        tache.y=y
    
    #création sur le graph des liens entre les taches
    for pos,tache in enumerate(points):
        predesseurs=tache.pred
        if predesseurs!="" :
            for pred in predesseurs :
                plt.plot([tache.x,points[pred-1].x],[tache.y,points[pred-1].y])
        
        else :
            pass

        #création des points de tache :
        plt.plot(tache.x,tache.y,marker="o",markersize=34)
        plt.text(tache.x,tache.y,f'T{pos+1}')
    
    plt.show()

# %%

def construccion_grafo_precedencia():
    """Construction du graphique de precedencia qui définie dans quel ordre chaque tache doit etre réalisé"""

    nbr_tache=int(input('Nombre de taches : '))
    

    #Création des taches du niveau 1
    niv_1=int(input("nbr de taches au niveau 1 : "))
    
    T0=tache("T0",0)
    T0.niveau=0
    liste_tache=[T0]
    for i in range(niv_1):
        temps_exec=int(input(f"Temps de la tache {i+1} (en seconde)"))
        liste_tache.append(tache(f"T{i+1}",temps_exec))
        
    
    afficher_graph(liste_tache)
    

    
    
# %%

if __name__=="__main__" :
    
    


