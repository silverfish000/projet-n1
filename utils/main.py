# Ajouter/Modifier/Supprimer des mots de passe
import os
import time
from verif_mdp import verif_mdp


def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_choix() :
    dictionnaire_auto = {
    'categories_mot_de_passe' : [
        "Netflix", "Amazon", "Github", "Apple", 
        "Google", "Facebook", "Spotify", "Steam", 
        "Adobe", "LinkedIn", "Instagram", "Discord"]
    }
    dictionnaire_auto_add = {
    'categories_mot_de_passe' : [
        "Netflix", "Amazon", "Github", "Apple", 
        "Google", "Facebook", "Spotify", "Steam", 
        "Adobe", "LinkedIn", "Instagram", "Discord"]
    }
    clear()
    print("="*70)
    print(" CONFIGURATION ADMIN ".center(70, "═"))
    print("="*70)
    while (True) :
        print(f"\n Catégories actuelles : {', '.join(dictionnaire_auto_add['categories_mot_de_passe'])}")
        print("-" * 30)
        print("- Tapez le NOM d'une catégorie pour l'ajouter")
        print("- Tapez 'AUTO' pour charger la configuration par défaut")
        print("- Tapez 'STOP' pour finaliser et quitter")
        print("-" * 30)
        choix_admin_categories = input("Ecris ton choix -->")
        clear()
        if (choix_admin_categories.lower() == 'auto') :
            print("Tu as choisis la fonction 'auto' le systeme va le mettre en place")
            categorie_final = dictionnaire_auto
            time.sleep(2)
            break
        else :
            print("Pour arreter : tape 'STOP'\n")
            if (choix_admin_categories.lower() == 'stop') :
                print("tu viens de taper 'STOP' tu vas etre rediriger vers le menu dans quelques secondes ...")
                time.sleep(2)
                categorie_final = dictionnaire_auto_add
                aff_menu()
            elif (choix_admin_categories in dictionnaire_auto_add['categories_mot_de_passe']):
                        clear()
                        print(f"🔴 La categorie '{choix_admin_categories}' existe deja\n")
            else :
                dictionnaire_auto_add['categories_mot_de_passe'].append(choix_admin_categories)
                clear()
                print(f"✅ La categorie '{choix_admin_categories}' a bien etait rajoutee !\n")
    print(categorie_final)
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


def aff_menu() :
    while (True) :
        clear()
        print("-="*35)
        print("GESTIONNAIRE DE MOT DE PASSE".center(65))
        print("-="*35)
        print("by Silver\n")
        print("1 - Ajouter un mot de passe\n")
        print("2 - Modifier un mot de passe\n")
        print("3 - Supprimer un mot de passe\n")
        print("4 - Admin Choix (ONLY ADMIN)\n")
        print("5 - QUITTER\n")
        try :
            choix_user = int(input("Fais ton choix (QUE DES CHIFFRES) :"))
        except ValueError :
            print("ERREUR : Tu ne dois que choisir des nombres")
        while (True) :
            if (choix_user == 1) :
                print("Tu as choisis l'option 1")
                add_mdp()
            elif (choix_user == 2) :
                print("Tu as choisis l'option 2")
                # Ajouter le systeme modif_mdp
            elif (choix_user == 3) :
                print("Tu as choisis l'option 3")
                # Ajouter le systeme supp_mdp
            elif (choix_user == 4) :
                print("Tu as choisis l'option 4")
                admin_choix()
            elif (choix_user == 5) :
                clear()
                decision_quitter = input("Vous etes sur de vouloir quitter ? (o/n)")
                if (decision_quitter.lower() == 'o') :
                    exit()
                else :
                    break
            else :
                clear()
                print("ERREUR : ONLY (1 - 5)")
                time.sleep(2)
                break




choix = aff_menu()

aff_menu()


# _0_