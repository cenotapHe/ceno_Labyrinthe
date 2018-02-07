# -*-coding:Utf-8 -*

# différentes importations qui permettent de clear la console, d'importer/exporter des sauvegardes ou de quitter le programme

import os
import sys
import pickle


# La classe Cartes() qui importe toutes les différentes cartes en elle, et permet au joueur d'en choisir une
class Cartes():


    def __init__(self, base = {}, **couple_nom_labyrinthe):

    	# Les cartes sont importées dans deux listes, une avec leur nom, une avec la carte
        self._noms_des_cartes = []
        self._labyrinthes_des_cartes = []


# La classe Carte_en_cours() récupère une seule une carte de la classe Cartes() et lui donne les attributs pour lui permettre de devenir un plateau de jeu
class Carte_en_cours():


	def __init__(self, _plateau_de_jeu):


		# Initialisation d'un plateau de jeu sur lequel le Robot va se déplacer
		self._plateau_de_jeu = _plateau_de_jeu

		self.victoire = False

		# Initialisation d'un plateau de jeu sans le robot, qui permet de réinitialiser des élèments comme les portes
		self._plateau_vierge = _plateau_de_jeu
		i = 0
		while i < len(self._plateau_vierge) :
			i += 1
			try :
				if self._plateau_vierge[i] == str('X'):
					self._plateau_vierge = self._plateau_vierge[:i] + " " + self._plateau_vierge[(i + 1):]
			except IndexError:
					pass

		# Initialisation des fonctions d'affichages relatives au plateau de jeu
	def __repr__(self):

		os.system("cls")
		chaine = "X = Robot\nU = Sortie\n. = Porte\nO = Mur\n\n" + self._plateau_de_jeu
		return chaine

	def __str__(self):

		return __repr__(self)

	# Creation d'un mouvement du robot, en effancant le robot de sa précédente case pour l'inscrire sur la case suivante
	def deplacement_droite(self, nombre):

		# détermine le mouvement indiqué par le joueur
		mouvement = nombre

		# comptabilise le nombre de pas vraiment effectué
		pas = 0

		while nombre > 0 :
			i = 0
			nombre -= 1
			while i < len(self._plateau_de_jeu) :
				i += 1
				try:
					if self._plateau_de_jeu[i] == str('X'):
						# détermine la condition de victoire
						if self._plateau_de_jeu[i + 1] == str('U'):
							pas += 1
							nombre = 0
							self.victoire = True
							continue
						# empêche de traverser les obstacles
						elif self._plateau_de_jeu[i + 1] == str('O'):
							print("On ne peut pas traverser les murs !")
							nombre = 0
							continue
						# déplace le robot vers la droite
						else:
							self._plateau_de_jeu = self._plateau_de_jeu[:i] + " " + self._plateau_de_jeu[(i + 1):]
							self._plateau_de_jeu = self._plateau_de_jeu[:(i + 1)] + "X" + self._plateau_de_jeu[(i + 2):]
							pas += 1
							break
					
				except IndexError:
					pass

		# affiche le nombre de pas vraiment effectué
		input("Vous vous êtes déplacez de {} pas vers l'Est.".format(pas))


	# le déplacement vers la gauche fonctionne exactement comme le déplacement vers la droite
	def deplacement_gauche(self, nombre):

		mouvement = nombre
		pas = 0

		while nombre > 0 :
			i = len(self._plateau_de_jeu)
			nombre -= 1
			while i > 0 :
				i -= 1
				try:
					if self._plateau_de_jeu[i] == str('X'):
						
						if self._plateau_de_jeu[i - 1] == str('U'):
							pas += 1
							nombre = 0
							self.victoire = True
							continue

						elif self._plateau_de_jeu[i - 1] == str('O'):
							print("On ne peut pas traverser les murs !")
							nombre = 0
							continue

						else:
							self._plateau_de_jeu = self._plateau_de_jeu[:i] + " " + self._plateau_de_jeu[(i + 1):]
							self._plateau_de_jeu = self._plateau_de_jeu[:(i - 1)] + "X" + self._plateau_de_jeu[i:]
							pas += 1
							break
					
				except IndexError:
					pass

		input("Vous vous êtes déplacez de {} pas vers l'Ouest.".format(pas))

	# variable qui calcule la largeur du labyrinthe
	def largeur_plateau(self):

		largeur = 2
		i = 1
		boucle = True
		while boucle == True :
			if self._plateau_de_jeu[i] == self._plateau_de_jeu[i + 1]:
				largeur += 1
				i +=1
			else:
				boucle = False

		return largeur

	# en se servant de la largeur du labyrinthe on peut déplacer le robot vers le bas, de la même manière que les déplacements latéraux
	def deplacement_bas(self, nombre):

		mouvement = nombre
		pas = 0

		j = self.largeur_plateau()

		while nombre > 0 :
			i = 0
			nombre -= 1
			while i < len(self._plateau_de_jeu) :
				i += 1
				try:
					if self._plateau_de_jeu[i] == str('X'):

						if self._plateau_de_jeu[i + j + 1] == str('U'):
							pas += 1
							nombre = 0
							self.victoire = True
							continue

						elif self._plateau_de_jeu[i + j + 1] == str('O'):
							print("On ne peut pas traverser les murs !")
							nombre = 0
							continue

						else:
							self._plateau_de_jeu = self._plateau_de_jeu[:i] + " " + self._plateau_de_jeu[(i + 1):]
							self._plateau_de_jeu = self._plateau_de_jeu[:(i + j + 1)] + "X" + self._plateau_de_jeu[(i + j + 2):]
							pas += 1
							break
					
				except IndexError:
					pass

		input("Vous vous êtes déplacez de {} pas vers le Sud.".format(pas))

	# en se servant de la largeur du labyrinthe on peut déplacer le robot vers le haut, de la même manière que les déplacements latéraux
	def deplacement_haut(self, nombre):

		mouvement = nombre
		pas = 0

		j = self.largeur_plateau()

		while nombre > 0 :
			
			i = 0
			nombre -= 1
			while i < len(self._plateau_de_jeu) :

				i += 1
				try:
					if self._plateau_de_jeu[i] == str('X'):

						if self._plateau_de_jeu[i - j - 1] == str('U'):
							pas += 1
							nombre = 0
							self.victoire = True
							continue

						elif self._plateau_de_jeu[i - j - 1] == str('O'):
							print("On ne peut pas traverser les murs !")
							nombre = 0
							continue

						else:
							self._plateau_de_jeu = self._plateau_de_jeu[:i] + " " + self._plateau_de_jeu[(i + 1):]
							self._plateau_de_jeu = self._plateau_de_jeu[:(i - j - 1)] + "X" + self._plateau_de_jeu[(i - j):]
							pas += 1
							break
					
				except IndexError:
					pass

		input("Vous vous êtes déplacez de {} pas vers le Nord.".format(pas))


	# lance la partie en cours en fonction du plateau de jeu que l'on a définit
	def partie_en_cours(self):

		jeu_en_cours = True
		premier_cycle = True

		while jeu_en_cours == True :

			os.system("cls")
			chaine = "X = Robot\nU = Sortie\n. = Porte\nO = Mur\n\n" + self._plateau_de_jeu
			print(chaine)

			# affichage du plateau avec ou sans les astuces (en fonction du début de partie ou pas)
			if premier_cycle == True :
				commande = input("\n     Commande de jeu :\n\n     N              Nord\n  O     E        Ouest/Est\n     S              Sud\n\nQ: sauvegarder et Quitter\n\nAstuce: vous pouvez indiquer le nombre \nde pas à coté de la direction.\nexemple: \"S3\" vous fera vous déplacer \nde 3 pas vers le Sud.\n\n Commande :  ")
				premier_cycle = False
			else :
				commande = input("\n     Commande de jeu :\n\n     N              Nord\n  O     E        Ouest/Est\n     S              Sud\n\nQ: sauvegarder et Quitter\n\n Commande :  ")

			# vérification de la commande rentrée par le joueur
			# de toute les manières possibles
			if len(commande) > 2 :
				input("Veuillez saisir une lettre correspondant à une des actions.\nAvec, optionnellement un seul et unique chiffre.")
				continue

			if len(commande) <= 0 :
				input("Vous n'avez rien saisit...")
				continue

			try :
				commande = int(commande)
				input("Veuillez saisir une commande, et pas uniquement des chiffres.")
				continue
			except:
				pass

			commande = commande.capitalize()
			
			try :
				lettre = str(commande[0])
			except :
				input("Commande non valide.")
				continue

			try:
				nombre = int(commande[1])
			except IndexError :
				nombre = 1
			except ValueError :
				input("Uniquement une seule lettre et un seul chiffre !!")
				continue
			except UnboundLocalError :
				input("Merci de taper une seule commande, et une unique fois.")
				continue

			# mouvement du robot en fonction du choix du joueur
			if lettre == "S":
				self.deplacement_bas(nombre)
			elif lettre == "N":
				self.deplacement_haut(nombre)
			elif lettre == "O":
				self.deplacement_gauche(nombre)
			elif lettre == "E":
				self.deplacement_droite(nombre)
			# quitte la partie tout en la sauvegardant
			elif lettre == "Q":
				input("\nAurevoir grand fou !")
				self.sauvegarde_de_la_partie()
				sys.exit()
			# en cas de commande non-répertorié
			else :
				input("Je suis désolé, je n'ai pas compris votre demande.")

			# affichage du plateau vierge qui permet de réactualiser toutes les portes
			i = 0
			while i < len(self._plateau_vierge) :
				i += 1
				try :
					if self._plateau_de_jeu[i] == str('X'):
						self._plateau_de_jeu = self._plateau_vierge[:i] + "X" + self._plateau_vierge[(i + 1):]
				except IndexError:
						pass			

			# sauvegarde automatique après chaque mouvement effectué
			self.sauvegarde_de_la_partie()

			# vérification des conditions de victoire
			if self.victoire == True :
				jeu_en_cours = False
				input("\nVous venez de vous échapper du labyrinthe !!!")
				# destruction de la sauvegarde pour lancer une nouvelle partie
				os.remove('sauvegarde_laby')

	# fonction qui permet de sauvegarder la partie dans un fichier nommé sauvegarde_laby
	def sauvegarde_de_la_partie(self) :

		with open('sauvegarde_laby', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self)


