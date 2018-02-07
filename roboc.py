# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import *



# On charge les cartes existantes
diffrentes_cartes_de_jeu = Cartes()

for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].capitalize()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()

            #print(nom_carte)
            #print(contenu)

            diffrentes_cartes_de_jeu._noms_des_cartes.append(nom_carte)
            diffrentes_cartes_de_jeu._labyrinthes_des_cartes.append(contenu) # on l'imprime sous la forme print(diffrentes_cartes_de_jeu._labyrinthe[i])


            
            # Création d'une carte, à compléter
alors_on_joue = True

while alors_on_joue == True :

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
				print("Ce numéro de labyrtinhe n'existe pas !")
				continue
			i = False
			input("Vous avez choisit le labyrinthe {}, qui se nomme \"{}\"".format(choix_du_labyrinthe, diffrentes_cartes_de_jeu._noms_des_cartes[choix_du_labyrinthe - 1]))
		except ValueError:
			print("On vous a demandé de choisir le numéro du labyrinthe.")


	carte_du_jeu_en_cours = Carte_en_cours(diffrentes_cartes_de_jeu._labyrinthes_des_cartes[choix_du_labyrinthe - 1])

	carte_du_jeu_en_cours.partie_en_cours()






#carte_du_jeu_en_cours.deplacement_droite(4)


#mouvement = input("On va allez à droite, alors appuyer sur D")
#if mouvement == "d":

	
os.system("pause")



# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
