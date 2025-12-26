import os
import time
from verif_mdp import verif_mdp, demander_mdp_valide
from config import dictionnaire_auto, dictionnaire_auto_add, dictionnaire_interdit

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')



def code_admin_verif() :
    clear()
    print("VERIFICATION CODE ADMIN".center(70, "="))
    code_admin_input = input("Entre le code ADMIN : ")
    if (code_admin_input == "SILVER2024") :
        print("Code ADMIN valide tu vas etre rediriger vers le menu ADMIN")
        time.sleep(2)
        return True
    else :
        print("ERREUR : Code ADMIN invalide tu vas etre rediriger vers le menu principal")
        time.sleep(2)
        return False


def tutoriel() :
    clear()
    print("TUTORIEL PASSWORLD".center(70, "="))
    print("""
Bienvenue dans le tutoriel de PASSWORLD !
Voici les différentes fonctionnalités disponibles :
- Ajouter un mot de passe : Permet d'ajouter un nouveau mot de passe à une catégorie existante.
- Modifier un mot de passe : Permet de modifier un mot de passe existant.
- Supprimer un mot de passe : Permet de supprimer un mot de passe d'une catégorie.
- Admin Choix : Permet à l'administrateur de gérer les catégories de mots de passe.
Prends le temps de te familiariser avec l'interface et les options disponibles.
Amuse-toi bien avec PASSWORLD !
""")
    input("Appuie sur Entrée pour continuer...")
tutoriel()

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
            if (code_admin_verif()) :
                print("Code de triche active")
                menu_admin()
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
            tutoriel()
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
        noms = [caca[0] for caca in dictionnaire_auto_add]
        print(f"\n Catégories actuelles : {', '.join(noms)}")
        print("-" * 30)
        print("- Tapez le NOM d'une catégorie pour l'ajouter")
        print("- Tapez 'AUTO' pour charger la configuration par défaut")
        print("- Tapez 'STOP' pour finaliser et quitter")
        print("-" * 30)
        choix_admin_categories = input("Ecris ton choix -->")
        mdp = ''
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
                time.sleep(2)
            else :
                dictionnaire_auto_add['categories_mot_de_passe'].append((choix_admin_categories, mdp))
                clear()
                print(f"✅ La categorie '{choix_admin_categories}' a bien etait rajoutee !\n")
                time.sleep(2)

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

def gerer_mdp(dictionnaire) :
    while (True) :
        clear()
        print("="*75)
        print(" GERER MOT DE PASSE ".center(75, "/"))
        print("="*75)
        print("1) MODIFIER UN MOT DE PASSE\n")
        print("2) SUPPRIMER UN MOT DE PASSE\n")
        print("3) RECHERCHER UN MOT DE PASSE (in build)\n")
        print("4) Afficher tous les mots de passe (in build)\n")
        print("5) QUITTER (Retour au menu)")
        choix_user_gerer_mdp = int(input(""))
        if (choix_user_gerer_mdp == 1) :
            clear()
            print("MODIFIER UN MOT DE PASSE".center(75, "-"))
            # Ajouter le systeme modifier_mdp
            input("Appuie sur Entrée pour continuer...")
        elif (choix_user_gerer_mdp == 2) :
            clear()
            print("SUPPRIMER UN MOT DE PASSE".center(75, "-"))
            # Ajouter le systeme supprimer_mdp
            input("Appuie sur Entrée pour continuer...")
        elif (choix_user_gerer_mdp == 3) :
            clear()
            break
        else :
            print("ERREUR : (ONLY 1 / 2 / 3)")
            time.sleep(2)

def aff_menu() :
    while (True) :
        clear()
        print("-="*35)
        print("GESTIONNAIRE DE MOT DE PASSE".center(65))
        print("-="*35)
        print("by Silver\n")
        print("1 - Ajouter un mot de passe (v1 pas fini)\n")
        print("2 - Gerer les mots de passes (in build)\n")
        print("4 - Paramètres (in build)\n")
        print("5 - Tutoriel (in build)\n")
        print("6 - Quitter\n")
        try :
            choix_user = int(input("Fais ton choix (QUE DES CHIFFRES) :"))
            if (choix_user == 1) :
                add_mdp(dictionnaire_auto_add)
            elif (choix_user == 2) :
                gerer_mdp(dictionnaire_auto_add)
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