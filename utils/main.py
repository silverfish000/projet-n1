from dotenv import load_dotenv
load_dotenv()
import os
import time
from verif_mdp import verif_mdp, demander_mdp_valide
from config import dictionnaire_auto, dictionnaire_auto_add, dictionnaire_interdit

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')



def code_admin_verif() :
    clear()
    print("VERIFICATION CODE ADMIN".center(70, "="))
    essai = 3
    code_admin_input = input("Entre le code ADMIN : ")
    if (code_admin_input == os.getenv("APP.PASSWORD")) :
        print("Code ADMIN valide tu vas etre rediriger vers le menu ADMIN")
        time.sleep(2)
        return True
    else :
        while (essai > 1) :
            essai -= 1
            clear()
            print("VERIFICATION CODE ADMIN".center(70, "="))
            code_admin_input = input("ERREUR : Code ADMIN invalide, re-essaye : ")
            if (code_admin_input == os.getenv("APP.PASSWORD")) :
                print("Code ADMIN valide tu vas etre rediriger vers le menu ADMIN")
                time.sleep(2)
                return True
        clear()
        print("VERIFICATION CODE ADMIN".center(70, "="))
        print("ERREUR : Trop d'essais, retour au menu principal")
        time.sleep(2)
        return False


def tutoriel() :
    clear()
    print("TUTORIEL PASSWORLD".center(70, "=")) # Tutoriel interactif
    print("\nBienvenue dans le tutoriel de PASSWORLD !\n")
    print("Ici, tu apprendras a utiliser les fonctionnalites principales de l'application.\n")
    time.sleep(1.5)
    print("1) Ajouter un mot de passe :")
    time.sleep(0.5)
    print("- Pour ajouter un mot de passe, selectionne l'option 'Ajouter un mot de passe' dans le menu principal.")
    time.sleep(0.5)
    print("- Choisis une categorie existante ou cree-en une nouvelle.")
    time.sleep(0.5)
    print("- Entre un mot de passe qui respecte les criteres de securite.")
    time.sleep(0.5)
    print("- Confirme l'ajout du mot de passe.\n")
    time.sleep(0.5)
    print("\n2) Gerer les mots de passe :")
    time.sleep(1.5)
    print("- Pour gerer tes mots de passe, selectionne l'option 'Gerer les mots de passe' dans le menu principal.")
    time.sleep(0.5)
    print("- Tu pourras modifier, supprimer ou rechercher des mots de passe existants.")
    time.sleep(0.5)
    print("- Suis les instructions a l'ecran pour effectuer les actions desirees.\n")
    time.sleep(0.5)
    print("N'hesite pas a consulter ce tutoriel a tout moment depuis le menu principal si tu as besoin d'aide.\n")
    print("Bonne gestion de tes mots de passe avec PASSWORLD !")
    time.sleep(2)
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
    while (True) :
        pseudo = input("Quel est ton pseudo ? ")
        if (len(pseudo) < 3 or len(pseudo) > 15) :
            clear()
            print("ERREUR : Ton pseudo doit contenir entre 3 et 15 caracteres")
            time.sleep(2)
        elif (not pseudo.isalnum()) :
            clear()
            print("ERREUR : Ton pseudo ne doit contenir que des caracteres alphanumeriques (lettres et chiffres)")
            time.sleep(2)
        elif (pseudo.lower() in dictionnaire_interdit['categories_mots_interdits']) :
            clear()
            print(f"ERREUR : Le pseudo '{pseudo}' est interdit, choisis-en un autre")
            time.sleep(2)
        else :
            print(f"Bienvenue {pseudo} ! Tu vas etre rediriger vers le menu principal dans quelques secondes ...")
            time.sleep(2)
            break
    clear()
    while (True) :
        code_admin = input("As-tu un code ADMIN ou un code de triche ? (o/n)")
        if (code_admin.lower() == 'o') :
            clear()
            if (code_admin_verif()) :
                print("Code de triche active")
                menu_admin() # code de triche & admin panel
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
        if (choix_user_add_mdp == 1) : # Ajouter un mot de passe
            clear()
            print("AJOUTER UN MOT DE PASSE".center(75, "-"))
            noms = [caca['name'] for caca in dictionnaire]
            print(f"\n Catégories actuelles : {', '.join(noms)}")
            print("-" * 30)
            categorie_nom = input("Dans quelle catégorie veux-tu ajouter un mot de passe ? ")
            categorie_trouve = False
            for categorie in dictionnaire :
                if categorie['name'].lower() == categorie_nom.lower() :
                    categorie_trouve = True
                    nouveau_mdp = demander_mdp_valide(categorie_nom, dictionnaire_auto)
                    categorie['mdp'] = nouveau_mdp
                    print(f"\n Le mot de passe pour la catégorie '{categorie_nom}' a été ajouté/modifié avec succès.")
                    time.sleep(2)
                    break
            if not categorie_trouve :
                print(f"\n ERREUR : La catégorie '{categorie_nom}' n'existe pas.")
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
        if (choix_user_gerer_mdp == 1) : # Ajouter un mot de passe
            clear()
            add_mdp(dictionnaire)
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