
# %% 

import pandas as pd
import class_participants 

excel="../multiples_bases_de_données/star-wars-survey/StarWars.csv"
data=pd.read_csv(excel, encoding="ISO-8859-1")

#Creation de la base de données avec la classe Participant :
#list_ID=[]
list_pa=[]
for ligne in data.values[1:] :
    #list_ID.append(int(ligne[0]))
    list_pa.append(Participant(ligne))


#Classement des SW selon les participants :
#moyenne
films_SW=['Star Wars: Episode I  The Phantom Menace','Star Wars: Episode II  Attack of the Clones','Star Wars: Episode III  Revenge of the Sith','Star Wars: Episode IV  A New Hope','Star Wars: Episode V The Empire Strikes Back','Star Wars: Episode VI Return of the Jedi']
moyenne={}
for film in films_SW :
    moyenne[film]=0
nbr_pa=0
for participant in list_pa :
    for film in films_SW :
        try :
          moyenne[film]+=int(participant.classementSW[film])
          nbr_pa+=1
        except ValueError :
            pass

nbr_pa=nbr_pa/6
