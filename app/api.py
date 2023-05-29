from fastapi import FastAPI
from pymongo import MongoClient
from db import *
from musique import *
from magasin import * 
from bson.objectid import ObjectId

app = FastAPI()

client = MongoClient(connect)
Musiques = client[db]
titres = Musiques[collection]
magasins = Musiques[collection2]


# Routes pour les Titres


@app.get("/titres")
async def get_titres():
    res = []
    for titre in titres.find():
        res.append(Musique(**titre))
    return res


@app.post("/titres")
async def create_musique(musique: Musique):

    result = titres.insert_one(dict(musique))
    
    return {"_id": str(result.inserted_id)} | dict(musique)


@app.get("/titres/{immatriculation:path}")
async def get_musique(immatriculation: str):
    titre = titres.find_one({"immatriculation": immatriculation})
    if titre:
        return Musique(**titre)
    else:
        raise HTTPException(status_code=404, detail="titre not found")

@app.put("/titres/{immatriculation:path}")
async def update_music(immatriculation: str, musique: Musique):
    res = titres.find_one({"immatriculation": immatriculation})

    if res :
        

        titres.update_one({"immatriculation": immatriculation}, {"$set": dict(musique)})

        return {"immatriculation": immatriculation} | dict(musique)

    else : 
        return {"message": "Music not found"}



@app.delete("/titres/{immatriculation:path}}")
def delete_music(immatriculation: str):
    res = titres.find_one({"immatriculation": immatriculation})

    if res :
        
        titres.delete_one({"immatriculation": immatriculation})

        return {"message": "Music deleted"}

    else :

        return {"message": "Music not found"}


# Routes pour les Magasins 



@app.get("/magasins")
async def get_magasins():
    res = []
    for magasin in magasins.find():
        res.append(Magasin(**magasin))
    return res

@app.post("/magasins")
async def create_magasin(magasin : Magasin):

    result = magasins.insert_one(dict(magasin))
    
    return {"_id": str(result.inserted_id)} | dict(magasin)


@app.get("/magasins/{id}")
async def get_magasin(id: str):
    magasin = magasins.find_one({"_id": ObjectId(id)})
    if magasin:
        return Magasin(**magasin)
    else:
        raise HTTPException(status_code=404, detail="titre not found")

@app.put("/magasins/{id}")
async def update_magasin(id: str, magasin :Magasin):
    res = magasins.find_one({"_id": ObjectId(id)})

    if res :
        
        magasins.update_one({"_id": ObjectId(id)}, {"$set": dict(magasin)})

        return {"_id": id} | dict(magasin)

    else:
        return {"message": "Magasin not found"}



@app.delete("/magasins/{id}}")
def delete_magasin(id: str):
    res = magasins.find_one({"_id": ObjectId(id)})

    if res :
        
        magasins.delete_one({"_id": ObjectId(id)})

        return {"message": "Magasin deleted"}

    else :

        return {"message": "Magasin not found"}


#Ajout dans la liste de vinyles 



@app.put("/magasins/{id}/vinyles/{immatriculation:path}")
async def add_musique_to_vinyles_magasins(id: str, immatriculation :str):
    res = magasins.find_one({"_id": ObjectId(id)})
    res2 = titres.find_one({"immatriculation": immatriculation})

    if res and res2:
        
        magasins.update_one({"_id": ObjectId(id)}, { "$push": { "vinyles" : dict(Musique(**res2)) }})

        return dict(Magasin(**res))
    else:
        return {"message": "Magasin not found or Musique not found "}

#Ajout dans la liste de dvds


@app.put("/magasins/{id}/dvds/{immatriculation:path}")
async def add_musique_to_dvds_magasins(id: str, immatriculation :str):
    res = magasins.find_one({"_id": ObjectId(id)})
    res2 = titres.find_one({"immatriculation": immatriculation})

    if res and res2:
        
        magasins.update_one({"_id": ObjectId(id)}, { "$push": { "dvds" : dict(Musique(**res2)) }})

        return dict(Magasin(**res))
    else:
        return {"message": "Magasin not found or Musique not found "}


#Retirer de la liste de dvds


@app.put("/magasins/{id}/remove-dvds/{immatriculation:path}")
async def remove_musique_from_dvds_magasins(id: str, immatriculation :str):
    res = magasins.find_one({"_id": ObjectId(id)})
    res2 = titres.find_one({"immatriculation": immatriculation})

    if res and res2:
        
        magasins.update_one({"_id": ObjectId(id)}, { "$pull": { "dvds" : dict(Musique(**res2)) }})

        return dict(Magasin(**res))
    else:
        return {"message": "Magasin not found or Musique not found "}


#Retirer de la liste de vinyles

@app.put("/magasins/{id}/remove-vinyles/{immatriculation:path}")
async def remove_musique_from_vinyles_magasins(id: str, immatriculation :str):
    res = magasins.find_one({"_id": ObjectId(id)})
    res2 = titres.find_one({"immatriculation": immatriculation})

    if res and res2:
        
        magasins.update_one({"_id": ObjectId(id)}, { "$pull": { "vinyles" : dict(Musique(**res2)) }})

        return dict(Magasin(**res))
    else:
        return {"message": "Magasin not found or Musique not found "}
