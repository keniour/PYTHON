"""Classe : Tache 
L'objectif de cette classe est de pouvoir caractériser toute les taches de nos process
dans le but d'acceder facilement a ses prédecesseurs, succédeurs, temps d'application ou 
toutes autres caractéristique utiles"""

#%%

class tache :
    
    def __init__(self,name,temps, succedeurs=[0], predecesseurs=""):
        
        self.name=name
        self.temps=temps
        self.pred=predecesseurs
        self.succ=succedeurs
        

        niveau=1
        for i in self.pred:
            if i.niveau>=niveau :
                niveau=i.niveau+1
            
        self.niveau=niveau
        
        #Position sur le graph :
        self.x=0
        self.y=0
        

    

if __name__=="__main__":
    
    #création de la tache 0 :
    T0=tache(0,0,predecesseurs="")
    T0.niveau=0