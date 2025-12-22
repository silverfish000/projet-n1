# Ajouter/Modifier/Supprimer des mots de passe
import os

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_choix() :
    clear()
    print("-="*35)
    print("GESTIONNAIRE DES CHOIX UTILISATEURS (ONLY ADMIN)".center(65))
    print("-="*35)


def aff_menu() :
    clear()
    print("-="*35)
    print("GESTIONNAIRE DE MOT DE PASSE".center(65))
    print("-="*35)
    print("by Silver & Squash")
    admin_choix()
    
    


def add_mdp() :
    aff_menu()
    choix_user = 0
    while (True) :
        try :
            choix_user = int(input("Fais ton choix :"))
            break
        except ValueError :
            print("ERREUR : Tu ne dois que choisir des nombres")
    
add_mdp()