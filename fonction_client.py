import socket
import time
import sys
import os

# La Classe ConnexionClient permet d'ouvrir et de fermer la connexion d'un client avec son serveur associé
class ConnexionClient():

	def __init__(self):

		self.hote = "localhost"
		self.port = 12800

		self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connexion_avec_serveur.connect((self.hote, self.port))
		print("Connexion établie avec le serveur sur le port {}".format(self.port))


	def fermeture_connexion(self):

		print("Fermeture de la connexion")

		time.sleep(5)

		self.connexion_avec_serveur.close()


# La Classe CommandeClient permet de vérifier que le client soumet une proposition valide pour son action du robot
class CommandeClient():

	def __init__(self):

		self.debut_de_partie = True
		self.premier_cycle = True
		self.multipas_en_cours = False
		self.compteur_multipas = 0
		self.direction_multipas = ""

	# l'attribut commande="" sert pour unittest
	def test_commande(self, commande=""):

	# tant que l'on a pas vérifié que la commande du joueur n'est pas un mauvais choix, on boucle ici
	# ça permet de tester plusieurs possibilités, et d'envoyer une commande valide au serveur
		self.mauvais_choix = True

		while self.mauvais_choix == True :

			self.commande = commande

			if self.multipas_en_cours == True :
				self.commande = self.direction_multipas + str(self.compteur_multipas)
				self.compteur_multipas -= 1
				print("Déplacement automatique.")
				time.sleep(1)
				if self.compteur_multipas == 0 :
					self.multipas_en_cours = False
					self.direction_multipas = ""
			elif self.commande != "":
				pass
			else :
				self.commande = input("Commande : ")

			if len(self.commande) > 2 :
				print("Veuillez saisir une lettre correspondant à une des actions.\nAvec, optionnellement un seul et unique chiffre.")
				time.sleep(0.5)
				continue

			if len(self.commande) <= 0 :
				print("Vous n'avez rien saisit...")
				time.sleep(0.5)
				continue

			try :
				self.commande = int(self.commande)
				print("Veuillez saisir une commande, et pas uniquement des chiffres.")
				time.sleep(0.5)
				continue
			except:
				pass

			self.commande = self.commande.capitalize()
					
			try :
				lettre = str(self.commande[0])
			except :
				print("Commande non valide.")
				time.sleep(0.5)
				continue

			try:
				nombre = int(self.commande[1])
			except IndexError :
				nombre = 1
			except ValueError :
				print("Uniquement une seule lettre et un seul chiffre. Avec la lettre, suivi du chiffre.")
				time.sleep(0.5)
				continue
			except UnboundLocalError :
				print("Merci de taper une seule commande, et une unique fois.")
				time.sleep(0.5)
				continue

			choix_possible = ["N", "S", "O", "E", "Q", "P", "M"]
			direction_possible = ["N", "S", "O", "E"]

			if str(self.commande[0]) not in choix_possible :
				print("On dirait que ce n'est pas une commande disponible.")
				time.sleep(0.5)
				continue

			if str(self.commande[0]) == "P":
				direction = input("      N\n  O   S   E\nDans quelle direction percer le mur ? ")
				direction = direction.capitalize()
				if direction not in direction_possible:
					print("Désolé, mais ce n'est pas une direction valide pour percer un mur.")
					time.sleep(0.5)
					continue
				self.commande += direction

			if str(self.commande[0]) == "M":
				direction = input("      N\n  O   S   E\nDans quelle direction murer la porte ? ")
				direction = direction.capitalize()
				if direction not in direction_possible:
					print("Désolé, mais ce n'est pas une direction valide pour murer une porte.")
					time.sleep(0.5)
					continue
				self.commande += direction
				
			if len(self.commande) == 1 and self.commande != "Q" :
					self.commande = self.commande + "1"
			
			if (self.commande[0] in direction_possible) and (int(self.commande[1]) > 1) :
					self.compteur_multipas = int(self.commande[1]) - 1
					self.direction_multipas = self.commande[0]
					self.multipas_en_cours = True
					self.commande = self.commande[0] + "1"

			self.mauvais_choix = False

			return self.commande
