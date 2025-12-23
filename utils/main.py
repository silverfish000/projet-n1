import os
import time
from verif_mdp import verif_mdp, demander_mdp_valide
from config import dictionnaire_auto, dictionnaire_auto_add, dictionnaire_interdit

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def bonjour() :
    clear()
    print("-="*40)
    print(r"""
██████╗  █████╗ ███████╗███████╗    ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗
██████╔╝███████║███████╗███████╗    ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║    ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║
██║     ██║  ██║███████║███████║    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ 
""")

    print("by Silver".center(72))
    print("-="*40)
    pseudo = input("Quel est ton pseudo ?")
    while (True) :
        code_admin = input("As-tu un code ADMIN ou un code de triche ? (o/n)")
        if (code_admin.lower() == 'o') :
            clear()
            print("Code de triche active")
            time.sleep(1)
            break
        elif (code_admin.lower() == 'n') :
            clear()
            print("Code de triche desactive")
            time.sleep(1)
            break
        else :
            clear()
            print("ERREUR : (ONLY o/n)")
    while (True) :
        choix_user = input("Veux-tu faire le tutoriel ? (o/n)")
        if (choix_user.lower() == 'o') :
            clear()
            print("Tutoriel active")
            time.sleep(1)
            break
        elif (choix_user.lower() == 'n') :
            clear()
            print("Tutoriel desactive")
            time.sleep(1)
            break
        else :
            clear()
            print("ERREUR : (ONLY o/n)")
    return pseudo

pseudo = bonjour() # Bienvenue sur PASSWORLD

def admin_choix(pseudo) :
    global dictionnaire_auto
    global dictionnaire_auto_add
    global choix_admin_categories

    clear()
    while (True) :
        print("="*70)
        print(" CONFIGURATION ADMIN ".center(70, "═"))
        print(f"connecte en tant que {pseudo}".center(70))
        print("="*70)
        noms = [tuples[0] for tuples in dictionnaire_auto_add['categories_mot_de_passe']]
        print(f"\n Catégories actuelles : {', '.join(noms)}")
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
            noms_existants = [tuples[0] for tuples in dictionnaire_auto_add['categories_mot_de_passe']]
            if (choix_admin_categories.lower() in dictionnaire_interdit['categories_mots_interdits']) :
                print(f"ATTENTION : '{choix_admin_categories}' est un mot interdit")
                time.sleep(3)
                clear()
            elif (choix_admin_categories in noms_existants):
                clear()
                print(f"🔴 La categorie '{choix_admin_categories}' existe deja\n")
            else :
                dictionnaire_auto_add['categories_mot_de_passe'].append(choix_admin_categories)
                clear()
                print(f"✅ La categorie '{choix_admin_categories}' a bien etait rajoutee !\n")

def add_mdp(dictionnaire) :
    while (True) :
        clear()
        print("="*75)
        print(" AJOUT MOT DE PASSE ".center(75, "/"))
        print("="*75)
        print("1) AJOUTER UN MOT DE PASSE\n")
        print("2) QUITTER (Retour au menu)")
        choix_user_add_mdp = int(input(""))
        if (choix_user_add_mdp == 1) :
            clear()
            print(f"Voici la liste des categories de {pseudo} : \n")
            noms_base = [tuples[0] for tuples in dictionnaire_auto_add['categories_mot_de_passe']]
            for i in noms_base :
                print(f"- {i} ", end="")
            print()
            choix_user_categorie = input("\nParmi les catégories ci-dessus, choisis-en une : ")
            noms_categories = [tuples[0].lower() for tuples in dictionnaire_auto_add['categories_mot_de_passe']]
            if (choix_user_categorie.lower() in noms_categories) :
                    demander_mdp_valide(choix_user_categorie, dictionnaire)
            else :
                print(f"ERREUR : la categorie '{choix_user_categorie}' est inexistante")
                time.sleep(2)
        elif (choix_user_add_mdp == 2) :
            clear()
            break
        else :
            print("ERREUR : (ONLY 1 / 2)")
            time.sleep(2)

def supp_mdp(dictionnaire) :
    print(dictionnaire)


def aff_menu() :
    while (True) :
        clear()
        print("-="*35)
        print("GESTIONNAIRE DE MOT DE PASSE".center(65))
        print("-="*35)
        print("by Silver\n")
        print("1 - Ajouter un mot de passe (v1 pas fini)\n")
        print("2 - Modifier un mot de passe (in build)\n")
        print("3 - Supprimer un mot de passe (in build)\n")
        print("4 - Admin Choix (ONLY ADMIN) (v1 fini)\n")
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
                admin_choix(pseudo)
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