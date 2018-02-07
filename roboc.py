# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu."""



# différent import qui permette de clear la console, ou d'importer/exporter les sauvegardes

import os
import pickle

# importation des classes du jeu

from carte import *





# On charge toutes les différentes cartes existantes dans la variable Cartes()

diffrentes_cartes_de_jeu = Cartes()

for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].capitalize()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            diffrentes_cartes_de_jeu._noms_des_cartes.append(nom_carte)
            diffrentes_cartes_de_jeu._labyrinthes_des_cartes.append(contenu) 


# Initialisation de la boucle principale qui permet de lancer une partie, et de lancer automatiquement les suivantes            
            
alors_on_joue = True

while alors_on_joue == True :

# Import de la sauvegarde si elle existe, tout en propsante au joueur de l'importe ou non

	try :

		os.system("cls")
		with open('sauvegarde_laby', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)

			choix_de_charger = input("Vous avez une sauvegarde en cours sur ce jeu.\nSouhaitez vous la chargez ? (Y/N) ")
			choix_de_charger = str(choix_de_charger)
			choix_de_charger = choix_de_charger.capitalize()
			if choix_de_charger == "Y" :
				carte_du_jeu_en_cours = mon_depickler.load()
			elif choix_de_charger == "N" :
				os.remove('sauvegarde_laby')
				continue
			else :
				input("Votre demande n'est pas valide.")
				continue

# Si il n'existe pas de sauvegarde, ou que le joueur a choisite de pas la charger, on propose au joueur de choisir une nouvelle carte
	except IOError:

		os.system("cls")
# On affiche les cartes existantes
		print("Labyrinthes existants :\n")
		for i, carte in enumerate(diffrentes_cartes_de_jeu._noms_des_cartes):
		    print("  {} - {}".format(i + 1, carte))


# On fait une boucle pour que le joueur choisise son labyrinthe
		i = True
		while i == True:
			choix_du_labyrinthe = input("\nQuelle labyrinthe choisisez-vous ? ")
			try :
				choix_du_labyrinthe = int(choix_du_labyrinthe)
				if choix_du_labyrinthe <= 0 or choix_du_labyrinthe > len(diffrentes_cartes_de_jeu._noms_des_cartes):
					print("Ce numéro de labyrinthe n'existe pas !")
					continue
				i = False
				input("Vous avez choisit le labyrinthe {}, qui se nomme \"{}\"".format(choix_du_labyrinthe, diffrentes_cartes_de_jeu._noms_des_cartes[choix_du_labyrinthe - 1]))
			except ValueError:
				print("On vous a demandé de choisir le numéro du labyrinthe.")

		# Initialisation de la carte choisit dans la classe Carte_en_cours() pour lui donner toutes ses fonctionnalités
		carte_du_jeu_en_cours = Carte_en_cours(diffrentes_cartes_de_jeu._labyrinthes_des_cartes[choix_du_labyrinthe - 1])

	# On lance le jeu sur la carte qui a été choisit
	carte_du_jeu_en_cours.partie_en_cours()


