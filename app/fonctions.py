def initiales(nom):
    for i in range(len(nom)):
        if nom[i]==' ':
            res = nom[0]+nom[i+1]
    
    return res


def verifier_type(type, musique):
    if musique[7]+musique[8]+musique[9]==type:
        res = True
    else :
        res = False
    return res