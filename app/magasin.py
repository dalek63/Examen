from pydantic import BaseModel
from fonctions import verifier_type

class Magasin(BaseModel):
    type_musique : str
    vinyles : list[Musique] = []
    dvds : list[Musique] = []


    @property
    def get_type_musique(self):
        return self.type_musique

    @property
    def get_vinyles(self):
        return self.vinyles

    @property
    def get_dvds(self):
        return self.dvds

    def ajouter_vinyles(self, musique):
        self.vinyles.append(musique)
    
    def retirer_vinyles(self, musique):
        self.vinyles.remove(musique)

    def ajouter_dvds(self, musique):
        self.dvds.append(musique)
    
    def retirer_dvds(self, musique):
        self.dvds.remove(musique)

    
    @validator("type_musique")
    def type_is_valid(cls, v, values):
        vinyles = values["vinyles"]
        dvds = values["dvds"]


        for i in len(range(vinyles)):
            if verifier_type(v, vinyles[i].immatriculation)==False:
                raise ValueError('Musique non conforme au type du magasin détectée')
            
