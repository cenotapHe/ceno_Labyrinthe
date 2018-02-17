
import time

# importation des classes du jeu
from carte import *
from fonction_serveur import *


# On charge toutes les différentes cartes existantes dans la variable Cartes()
differentes_cartes_de_jeu = Cartes()

differentes_cartes_de_jeu.importation_cartes()

os.system("cls")

differentes_cartes_de_jeu.liste_labyrinthe()

numero = differentes_cartes_de_jeu.choix_du_labyrinthe()

# Initialisation de la carte choisit dans la classe Carte_en_cours() pour lui donner toutes ses fonctionnalités
carte_du_jeu_en_cours = Carte_en_cours(differentes_cartes_de_jeu._labyrinthes_des_cartes[numero - 1])


# On donne les caractéristiques pour initialiser la connexion du serveur
serveur_launch = ConnexionServeur()


# On attends les joueurs
serveur_lance = True
clients_connectes = []
clients_joueurs = []

bienvenue = b"Bienvenue sur le serveur.\nNous sommes en attente de joueur pour commencer la partie. (5joueurs MAXIMUM)"
msg_recu = " "
i = 1
debut_de_partie = " "

# On boucle pour ajouter les joueurs qui arrivent sur le serveur
while serveur_lance :

	connexions_demandees, wlist, xlist = select.select([serveur_launch.connexion_principale], [], [], 0.05)

	for connexion in connexions_demandees :

		connexion_avec_client, infos_connexion = connexion.accept()

		clients_connectes.append(connexion_avec_client)

		connexion_avec_client.send(bienvenue)

	# A partir d'ici, on commence à écouter les commandes des joueurs
	client_a_lire = []
	try :
		client_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
	except select.error :
		pass
	else :

		for client in client_a_lire :

			# Boucle tant que le serveur n'a pas lancé la partie
			if debut_de_partie != "C":

				message_validation = "Serveur : Votre demande est valide.\nVous êtes inscrit dans la partie !\nIl y a {} joueur(s) dont la validation a été effectué !".format(i)
				message_validation = message_validation.encode()
				client.send(message_validation)
				print("Il y a {} joueur(s) dont la validation a été effectué !".format(i))

				clients_joueurs.append(client)

				debut_de_partie = client.recv(1024)
				debut_de_partie = debut_de_partie.decode()

				i += 1

				if len(clients_joueurs) == 5:
					debut_de_partie = 'C'

			while debut_de_partie == "C":

				b = 3
				while b > 0:
					if carte_du_jeu_en_cours.victoire == False :
						print("La partie démarre dans {} secondes !!!".format(b))
					else :
						print("La connexion se ferme dans {} secondes !!!".format(b))
					time.sleep(1)
					b -= 1



				# A PARTIR DE CETTE BOUCLE ON COMMENCE VRAIMENT LA PARTIE
				j = 1
				while j <= len(clients_joueurs) :
					message = "Bonjour et Bienvenue dans la partie.\nVous êtes le joueur {}.".format(j)
					message = message.encode()
					clients_joueurs[j - 1].send(message)
					carte_du_jeu_en_cours.placement_du_robot()
					j += 1

				# MAINTENANT ON ATTAQUE LES TOURS DE JEU
				h = 1
				j = 1
				while h == 1 :

					message = "C'est à vous de jouer, joueur {}.".format(j)
					message = message.encode()
					clients_joueurs[j - 1].send(message)
					message = ""

					time.sleep(1)

					ok_joueur_present = clients_joueurs[j - 1].recv(1024)

					# création d'une map visible propre au joueur en cours,(X pour lui, x pour les autres) puis on lui envoit
					chaine = carte_du_jeu_en_cours.affichage_map(carte_du_jeu_en_cours.carte_visible_joueur_en_cours(j))
					chaine = chaine.encode()
					clients_joueurs[j - 1].send(chaine)

					time.sleep(1)

					# création d'une carte de jeu avec le joueur en cours X, pour lui permettre de faire des déplacement
					k = j
					i = 0
					while i < len(carte_du_jeu_en_cours._plateau_de_jeu) :
						i += 1
						try :
							if carte_du_jeu_en_cours._plateau_de_jeu[i] == str(k) :
								carte_du_jeu_en_cours._plateau_de_jeu = carte_du_jeu_en_cours._plateau_de_jeu[:i] + 'X' + carte_du_jeu_en_cours._plateau_de_jeu[(i + 1):]
						except IndexError:
							pass

					commande_recu = clients_joueurs[j - 1].recv(1024)
					commande_recu = commande_recu.decode()
					if commande_recu == "ok":
						continue

					print("Le joueur {} vient d'effectuer la commande : {}".format(j, commande_recu))

					# réaction en fonction des différentes commandes recus par le joueur en cours
					if commande_recu[0] == "S" or commande_recu[0] == "N" or commande_recu[0] == "O" or commande_recu[0] == "E":
						message = carte_du_jeu_en_cours.deplacement(commande_recu[0], commande_recu[1])

					if commande_recu[0] == "Q":
						message = ("On est en multijoueur mec... Tu crois pas t'échapper comme ça ?\nC'est un combat jusqu'à la mort !")

					if commande_recu[0] == "P":
						message = carte_du_jeu_en_cours.percer_mur(commande_recu[1])

					if commande_recu[0] == "M":
						message = carte_du_jeu_en_cours.murer_porte(commande_recu[1])
					
					# vérification des conditions de victoire pour le joueur en cours	
					if carte_du_jeu_en_cours.victoire == True :
						print("Le joueur {} vient de gagner la partie !!!".format(j))
						message = "Vous venez de vous échapper du Labyrinthe !\nEt vous gagnez la partie !"
					
					# retour pour le joueur de la réponse à sa commande
					message = message.encode()
					clients_joueurs[j - 1].send(message)
					
					# si le joueur en cours à gagné, on alerte tout les joueurs de sa victoire, et puis on enclenche le processus de déconnexion
					if carte_du_jeu_en_cours.victoire == True :
						for client in clients_joueurs :
							message_final = "FIN DE PARTIE !\nLe joueur {} vient de gagner la partie !!!".format(j)
							message_final = message_final.encode()
							client.send(message_final)
							client.close()
						h = 0
						continue

					# création d'une carte stocké par le serveur, ou chaque robot n'est pas représenté par un X, mais par son numéro de joueur
					k = j
					i = 0
					while i < len(carte_du_jeu_en_cours._plateau_de_jeu) :
						i += 1
						try :
							if carte_du_jeu_en_cours._plateau_de_jeu[i] == 'X' :
								carte_du_jeu_en_cours._plateau_de_jeu = carte_du_jeu_en_cours._plateau_de_jeu[:i] + str(k) + carte_du_jeu_en_cours._plateau_de_jeu[(i + 1):]
						except IndexError:
							pass


					# envoit aux joueurs de la dernière carte, avec le dernier mouvement, ou la derniere actions, effectué(e)
					# chacun avec sa propre vision du robot principal
					l = 1
					while l <= len(clients_joueurs):
						chaine = carte_du_jeu_en_cours.affichage_map(carte_du_jeu_en_cours.carte_visible_joueur_en_cours(l))
						chaine = chaine.encode()
						clients_joueurs[l - 1].send(chaine)
						l += 1

					time.sleep(3)

					j += 1
					if j > len(clients_joueurs) :
						j = 1

# une fois les conditions de victoire activé, on sort de la boucle, et on ferme le serveur
print("Fermeture de la connexion")

time.sleep(3)

connexion_principale.close()