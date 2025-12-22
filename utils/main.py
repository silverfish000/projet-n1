# Ajouter/Modifier/Supprimer des mots de passe
import os
import time


# ------------ db de categories et tout les mots de passes (non chiffres) ------------
dictionnaire_admin = {
    'categories_mot_de_passe' : [""]
}
dictionnaire_auto = {
    'categories_mot_de_passe' : ["Netflix", "Amazon", "Github"]
}
# ------------ FIN ------------


def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_choix(categorie, categorie_auto) : # pour plus tard
    clear()
    print("-="*35)
    print("GESTIONNAIRE DES CHOIX UTILISATEURS (ONLY ADMIN)".center(65))
    print("-="*35)
    print("Avant de commencer ton expérience ...")
    while (True) :
            choix_admin_categories = input("Choisis une catégorie à ajouter pour les users (ex : Netflix, Amazon, Github, Apple)\n" + "Ou tape 'auto' pour utiliser les catégories par défaut : ")
            clear()
        # Verification du choix ADMIN
            if (choix_admin_categories == 'auto') :
                print("Tu as choisis la fonction 'auto' le systeme va le mettre en place")
                # Systeme auto declenchement a mettre
                time.sleep(2)
            else :
                print("Pour arreter : tape 'STOP'\n")
                if (choix_admin_categories == 'STOP') :
                    print("tu viens de taper 'STOP' tu vas etre rediriger vers le menu dans quelques secondes ...")
                    time.sleep(2)
                    break
                elif (choix_admin_categories in categorie['categories_mot_de_passe']):
                            clear()
                            print(f"La categorie '{choix_admin_categories}' existe deja\n")
                else :
                    categorie['categories_mot_de_passe'].append(choix_admin_categories)
                    clear()
                    print(f"La categorie '{choix_admin_categories}' a bien etait rajoutee !\n")


admin_choix(dictionnaire_auto, dictionnaire_auto)

def aff_menu() :
    clear()
    print("-="*35)
    print("GESTIONNAIRE DE MOT DE PASSE".center(65))
    print("-="*35)
    print("by Silver & Squash\n")
    print("1) Ajouter un mot de passe\n")
    print("2) Modifier un mot de passe\n")
    print("3) Supprimer un mot de passe\n")
    while (True) :
        try :
            choix_user = int(input("Fais ton choix (QUE DES CHIFFRES) :"))
            break
        except ValueError :
            print("ERREUR : Tu ne dois que choisir des nombres")
    if (choix_user == 1) :
        print("Tu as choisis l'option 1")
    elif (choix_user == 2) :
        print("Tu as choisis l'option 2")
    else :
        print("Tu as choisis l'option 3")
    return choix_user



def add_mdp(choix_user) :
    if (choix_user == 1) :
        input("Choisis")
    elif (choix_user == 2) :
        print("Tu as choisis l'option 2")
    else :
        print("Tu as choisis l'option 3")
choix = aff_menu()

add_mdp(choix)


# _0_