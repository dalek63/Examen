from pydantic import BaseModel, validator
from fonctions import initiales

class Musique(BaseModel):
    titre : str
    artiste : str
    immatriculation : str 


    
    


    @validator("immatriculation")
    def is_valid(cls, v, values):

        slashError = 'Il manque un "/" '

        if(len(v)!=15):
            raise ValueError('Mauvais nombre de caractères')
        
        if(v[0]+v[1]!=initiales(values["artiste"])):
            raise ValueError('Initiales ne correspondent pas')
        
        if(v[2]!='/'):
            raise ValueError(slashError)
        

        temps = v[3]+v[4]+v[5]
        if(temps.isdigit()== False):
            raise ValueError('Valeurs non numériques')
        
        if(v[6]!='/'):
            raise ValueError(slashError)
        

        typesMusiques = {'RAP','POP','RNB'}

        if(v[7]+v[8]+v[9] not in typesMusiques):
            raise ValueError('Mauvais type de Musique')
        
        if(v[10]!='/'):
            raise ValueError(slashError)
        

        identifiant = v[11]+v[12]+v[13]+v[14]

        if(identifiant.find('6')== True):
            raise ValueError("L'identifiant ne peut pas posséder de 6")
        
        return v


''' Petit test '''
    
#m = Musique(titre = 'titre', artiste = 'John Doe', immatriculation = 'JD/250/POP/1234')

