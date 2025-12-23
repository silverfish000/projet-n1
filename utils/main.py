import os
import time
from verif_mdp import verif_mdp
from config import dictionnaire_auto, dictionnaire_auto_add, dictionnaire_interdit

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_choix() :
    global dictionnaire_auto
    global dictionnaire_auto_add
    global choix_admin_categories
    clear()
    while (True) :
        print("="*70)
        print(" CONFIGURATION ADMIN ".center(70, "═"))
        print("="*70)
        print(f"\n Catégories actuelles : {', '.join(dictionnaire_auto_add['categories_mot_de_passe'])}")
        print("-" * 30)
        print("- Tapez le NOM d'une catégorie pour l'ajouter")
        print("- Tapez 'AUTO' pour charger la configuration par défaut")
        print("- Tapez 'STOP' pour finaliser et quitter")
        print("-" * 30)
        choix_admin_categories = input("Ecris ton choix -->")
        clear()
        if (choix_admin_categories.lower() == 'auto') :
            choix_user_auto = input("ATTENTION TA LISTE QUE TU AS CREER VA ETRE SUPPRIMEE TU ES SUR QUE TU VEUX CONTINUER ? (o/n)")
            if (choix_user_auto.lower() == 'o') :
                if (dictionnaire_auto == dictionnaire_auto_add) :
                    print("Le systeme 'auto' est deja activer sur ta machine")
                    time.sleep(2)
                else :
                    print("Tu as choisis la fonction 'auto' le systeme va le mettre en place")
                    dictionnaire_auto_add = dictionnaire_auto
                    time.sleep(2)
            elif (choix_user_auto.lower() == 'n') :
                clear()
            else :
                print("ERREUR : ONLY (o/n)")
        elif (choix_admin_categories.lower() == 'stop') :
            print("tu viens de taper 'STOP' tu vas etre rediriger vers le menu dans quelques secondes ...")
            time.sleep(2)
            break
        else :
            if (choix_admin_categories.lower() in dictionnaire_interdit['categories_mots_interdits']) :
                print(f"ATTENTION : '{choix_admin_categories}' est un mot interdit")
                time.sleep(3)
                clear()
            elif (choix_admin_categories in dictionnaire_auto_add['categories_mot_de_passe'] ):
                        clear()
                        print(f"🔴 La categorie '{choix_admin_categories}' existe deja\n")
            else :
                dictionnaire_auto_add['categories_mot_de_passe'].append(choix_admin_categories)
                clear()
                print(f"✅ La categorie '{choix_admin_categories}' a bien etait rajoutee !\n")

def add_mdp(dictionnaire) :
    clear()
    print("="*75)
    print(" AJOUT MOT DE PASSE ".center(75, "/"))
    print("="*75)
    print("Voici la liste des categories de user : \n")
    for i in dictionnaire['categories_mot_de_passe']:
        print(f"- {i} ", end="")
    input("")

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
            if (choix_user == 1) :
                add_mdp(dictionnaire_auto_add)
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
                while (True) :
                    clear()
                    decision_quitter = input("Vous etes sur de vouloir quitter ? (o/n)")
                    if (decision_quitter.lower() == 'o') :
                        clear()
                        print("A la prochaine mon bro !!!!")
                        time.sleep(1.5)
                        exit()
                    elif (decision_quitter.lower() == 'n') :
                        break
                    else :
                        print("ERREUR : ONLY (o/n)")
                        time.sleep(2)
            else :
                clear()
                print("ERREUR : ONLY (1 - 5)")
                time.sleep(2)
        except ValueError :
            print()

aff_menu()


# _0_