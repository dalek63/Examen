from fastapi import FastAPI
from pymongo import MongoClient
from musique import Musique
from magasin import Magasin
from bson.objectid import ObjectId
from db import *

app = FastAPI()

client = MongoClient(connect)
Musiques = client[db]
titres = Musiques[collection]
magasins = Musiques[collection2]

musique = Musique (titre = 'titre', artiste = 'John Doe', immatriculation = 'JD/250/POP/1234')


mu = {
        "titre" : musique.titre,
        "artiste" : musique.artiste,
        "immatriculation" : musique.immatriculation
}

res = titres.insert_one(mu)

magasin = Magasin(type_musique = "POP")
'''
ma = {
        "type_musique" : magasin.type_musique,
        "vinyles" : magasin.vinyles,
        "dvds" : magasin.dvds
}

res = magasins.insert_one(ma)


'''

#magasins.update_one({"_id" : ObjectId('64749321d1a7b261369671b1')}, { "$push": { "vinyles" : mu }})