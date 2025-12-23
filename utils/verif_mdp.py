import time

def verif_mdp(mot_de_passe, dictionnaire):
    
    if len(mot_de_passe) < 8:
        return False, "ERREUR : Le mot de passe doit contenir au moins 8 caracteres"
    

    majuscule_trouve = False

    for lettre in mot_de_passe:
        if lettre.isupper():
            majuscule_trouve = True
            break

    if not majuscule_trouve:
        return False, "ERREUR : Doit contenir au moins une majuscule !"
    

    minuscule_trouve = False

    for lettre in mot_de_passe:
        if lettre.islower():
            minuscule_trouve = True
            break

    if not minuscule_trouve:
        return False, "ERREUR : Doit contenir au moins une minuscule!"


    caracteres_speciaux = "!@#$%^&*()_+-=?/"
    special_trouve = False

    for caractere in mot_de_passe:
        if caractere in caracteres_speciaux:
            special_trouve = True
            break
        
    if not special_trouve:
        return False, "ERREUR : Doit contenir au moins un caractere special !!"
    

    for categorie in dictionnaire['categories_mot_de_passe'] :
        if (categorie[1] == mot_de_passe and categorie[1] != '') :
            return False, "ERREUR : Ce mot de passe n'existe pas !"
    
    return True, "Mot de passe valider"


def demander_mdp_valide(categorie_nom, dictionnaire):
    while True:
        nouveau_mdp = input(f"Choisis ton mot de passe pour {categorie_nom} : ")
        valide, message = verif_mdp(nouveau_mdp, dictionnaire)
        
        if valide:
            print(f"\n {message}")
            time.sleep(1)
            return nouveau_mdp
        else:
            print(f"\n Erreur : {message}")
            print("\nRecommence !\n")
            time.sleep(1)

# _0_