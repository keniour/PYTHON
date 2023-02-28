
# %%

class Participant() :
    """Cette classe a pour mission de transformer la ligne excel 
    d'un participant en un objet 'participant' avec ces propres donées 
    en attribut"""
    
    def __init__(self,ligne_participant):
        
        self.respondent_ID=ligne_participant[0]
        self.vu_films=ligne_participant[1]
        self.status_fan_SW=ligne_participant[2]
        self.films_vu=[film for film in ligne_participant[3:9] if film!='nan']
        _films_concernees=['Star Wars: Episode I  The Phantom Menace','Star Wars: Episode II  Attack of the Clones','Star Wars: Episode III  Revenge of the Sith','Star Wars: Episode IV  A New Hope','Star Wars: Episode V The Empire Strikes Back','Star Wars: Episode VI Return of the Jedi']
        self.classementSW={}
        for i in range(len(_films_concernees)):
            self.classementSW[_films_concernees[i]]=ligne_participant[9+i]
        
        #creation du dico des affinités :
        self.affinite={}
        _perso_concerne=['Han Solo','Luke Skywalker', 'Princess Leia Organa', 'Anakin Skywalker','Obi Wan Kenobi', 'Emperor Palpatine', 'Darth Vader','Lando Calrissian', 'Boba Fett', 'C-3P0', 'R2 D2', 'Jar Jar Binks','Padme Amidala', 'Yoda']
        for i in range(len(_perso_concerne)) : 
            self.affinite[_perso_concerne[i]]=ligne_participant[15+i]
        self.shot_first=ligne_participant[-9]
        self.status_familiar_expended_universe=ligne_participant[-8]
        self.status_fan_expended_universe=ligne_participant[-7]
        self.status_fan_star_treck=ligne_participant[-6]
        self.gender=ligne_participant[-5]
        self.age=ligne_participant[-4]
        self.revenu=ligne_participant[-3]
        self.education=ligne_participant[-2]
        self.location=ligne_participant[-1]


    def presentation_participant(self):
        print(f'Respondent ID : {self.respondent_ID}')
        print(f"A t'il vu au moins un des SW ? Response : {self.vu_films}")
        print(f"Est'il un fan de la franchise SW ? Response : {self.status_fan_SW}")
        print(f"Quel films SW a t'il vu ? Response : {self.films_vu}")
        print(f"Ranking films SW : {self.classementSW}")
        print(f"Affinités en fct des caractères : {self.affinite}")
        print(f"Qui a tiré le premier ? Response : {self.shot_first}")
        print(f"Es tu familier avec l'univers étendu ? Response : {self.status_familiar_expended_universe}")
        print(f"Te considère tu comme un fan de l'univers étendu ? Response : {self.status_fan_expended_universe}")
        print(f"Te considères tu comme un fan de Star Treck ? Response : {self.status_fan_star_treck}")
        print(f"Sexe : {self.gender}")
        print(f"Tranche d'age : {self.age}")
        print(f"Tranche de revenu : {self.revenu}")
        print(f"Niveau d'éducation : {self.education}")
        print(f"Localisation : {self.location}")



if __name__=="__main__":
    
    import pandas as pd
    excel="../multiples_bases_de_données/star-wars-survey/StarWars.csv"
    data=pd.read_csv(excel, encoding="ISO-8859-1")
    p=Participant(data.values[1])
    print('Données du participant numero 1 :')
    p.presentation_participant()
    
        