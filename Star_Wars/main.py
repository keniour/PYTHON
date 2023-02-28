
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
    li=[str(i) for i in participant.classementSW.values()]
    if 'nan' in li:
        pass
    else :
        nbr_pa+=1
        for film in films_SW :
            moyenne[film]+=int(participant.classementSW[film])

for film in moyenne :
    moyenne[film]=moyenne[film]/nbr_pa

def afficher_classement_films_SW(moyenne=moyenne):
    """Prend en paramètre le dico des moyennes de chaque SW pour en retourner 
    un classement affichable"""
    
    print("Classement des SW en fonction des places données par les participants")
    values=[]
    for moy in moyenne.values():
        values.append(moy)
    
    values.sort()
    place=1
    film='Error'
    for value in values :
        print(f"Place numéro {place} :")
        for key in moyenne.keys():
            if moyenne[key]==value :
                film=key
        print(f"{film} avec une moyenne de {value}")
        print("\n")
        place+=1
    

# %%Tentative de recuperation des données de films SW par navigation automatisé sur letterboxd :

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
  
def afficher_film(film):  
    browser=webdriver.Chrome()

    browser.get('https://letterboxd.com/')

    elem=browser.find_element(By.NAME, 'q')
    elem.send_keys(film,Keys.RETURN)
    
    elem=browser.find_element(By.CLASS_NAME,'results')
    elem.find_element(By.CLASS_NAME,'film-title-wrapper')
    elem.click()
    
    #browser.quit()
    
