# Ajouter/Modifier/Supprimer des mots de passe
import os
import time
import string

def verif_mdp(mot_de_passe, dictionnaire):
    
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caracteres"
    
    if not any(c.isupper() for c in mot_de_passe):
        return False, "Doit contenir au moins une majuscule"
    
    if not any(c.islower() for c in mot_de_passe):
        return False, "Doit contenir au moins une minuscule"
    
    if not any(c in string.punctuation for c in mot_de_passe):
        return False, "Doit contenir au moins un caractere special"
    
    for cle, valeur in dictionnaire.items():
        if cle != 'categories_mot_de_passe' and valeur == mot_de_passe:
            return False, "Ce mot de passe existe deja"
    
    return True, "Mot de passe valide"

# ------------ db de categories et tout les mots de passes (non chiffres) ------------
dictionnaire_admin = {
    'categories_mot_de_passe' : [""]
}
dictionnaire_auto = {
    'categories_mot_de_passe' : [
        "Netflix", "Amazon", "Github", "Apple", 
        "Google", "Facebook", "Spotify", "Steam", 
        "Adobe", "LinkedIn", "Instagram", "Discord"
    ]
}
# ------------ FIN ------------


def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_choix(categorie, categorie_auto) :
    clear()
    print("="*70)
    print(" CONFIGURATION ADMIN ".center(70, "═"))
    print("="*70)
    while (True) :
        print(f"\n Catégories actuelles : {', '.join(categorie['categories_mot_de_passe'])}")
        print("-" * 30)
        print("- Tapez le NOM d'une catégorie pour l'ajouter")
        print("- Tapez 'AUTO' pour charger la configuration par défaut")
        print("- Tapez 'STOP' pour finaliser et quitter")
        print("-" * 30)
        choix_admin_categories = input("Ecris ton choix -->")
        clear()
        if (choix_admin_categories == 'AUTO') :
            print("Tu as choisis la fonction 'auto' le systeme va le mettre en place")
            categorie_final = categorie_auto
            time.sleep(2)
            break
        else :
            print("Pour arreter : tape 'STOP'\n")
            if (choix_admin_categories == 'STOP') :
                print("tu viens de taper 'STOP' tu vas etre rediriger vers le menu dans quelques secondes ...")
                time.sleep(2)
                categorie_final = categorie
                break
            elif (choix_admin_categories in categorie['categories_mot_de_passe']):
                        clear()
                        print(f"🔴 La categorie '{choix_admin_categories}' existe deja\n")
            else :
                categorie['categories_mot_de_passe'].append(choix_admin_categories)
                clear()
                print(f"✅ La categorie '{choix_admin_categories}' a bien etait rajoutee !\n")
    print(categorie_final)
    time.sleep(3)
    return categorie_final

def add_mdp(choix_user) : # a faire plus tard 
    if (choix_user == 1) :
        input("Choisis")
    elif (choix_user == 2) :
        print("Tu as choisis l'option 2")
    else :
        print("Tu as choisis l'option 3")

def supp_mdp(choix_user) :
    print(choix_user)


def aff_menu() : # a ameliorer
    clear()
    print("-="*35)
    print("GESTIONNAIRE DE MOT DE PASSE".center(65))
    print("-="*35)
    print("by Silver & Squash\n")
    print("1) Ajouter un mot de passe\n")
    print("2) Modifier un mot de passe\n")
    print("3) Supprimer un mot de passe\n")
    print("4) Admin Choix (ONLY ADMIN)")
    while (True) :
        try :
            choix_user = int(input("Fais ton choix (QUE DES CHIFFRES) :"))
            break
        except ValueError :
            print("ERREUR : Tu ne dois que choisir des nombres")
    if (choix_user == 1) :
        print("Tu as choisis l'option 1")
        # Ajouter le systeme add_mdp
    elif (choix_user == 2) :
        print("Tu as choisis l'option 2")
        # Ajouter le systeme modif_mdp
    elif (choix_user == 3) :
        print("Tu as choisis l'option 3")
        # Ajouter le systeme supp_mdp
    else :
        print("Tu as choisis l'option 4")
        admin_choix(dictionnaire_auto, dictionnaire_auto)
    return choix_user




choix = aff_menu()

aff_menu()


# _0_
