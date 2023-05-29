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


titres_peuple = [
        {"titre":"titre","artiste":"John Doe","immatriculation":"JD/250/POP/1234"},
        {"titre":"anus","artiste":"Younes Assaouci","immatriculation":"YA/250/RAP/1235"},
        {"titre":"dans la street","artiste":"Alexandre Wolak","immatriculation":"AW/250/RAP/1236"},
        {"titre":"Souleymane","artiste":"Souleymane Siby","immatriculation":"SS/230/POP/6789"}
]


magasins_peuples = [
        {"type_musique":"POP","vinyles":[],"dvds":[]},
        {"type_musique":"RAP","vinyles":[],"dvds":[]},
        {"type_musique":"RNB","vinyles":[],"dvds":[]}
]


titres.insert_many(titres_peuple)

magasins.insert_many(magasins_peuples)