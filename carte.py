# -*-coding:Utf-8 -*

import os

import sys

"""Ce module contient la classe Carte."""

class Cartes:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, base = {}, **couple_nom_labyrinthe):

        self._noms_des_cartes = []
        self._labyrinthes_des_cartes = []


class Carte_en_cours():


	def __init__(self, _plateau_de_jeu):

		self._plateau_de_jeu = _plateau_de_jeu

		self.victoire = False

		self._plateau_vierge = _plateau_de_jeu

		i = 0
		while i < len(self._plateau_vierge) :
			i += 1
			try :
				if self._plateau_vierge[i] == str('X'):
					self._plateau_vierge = self._plateau_vierge[:i] + " " + self._plateau_vierge[(i + 1):]
			except IndexError:
					pass


	def __repr__(self):

		os.system("cls")
		chaine = "X = Robot\nU = Sortie\n. = Porte\nO = Mur\n\n" + self._plateau_de_jeu
		return chaine

	def __str__(self):

		return __repr__(self)


	def deplacement_droite(self, nombre):

		mouvement = nombre
		pas = 0

		while nombre > 0 :
			i = 0
			nombre -= 1
			while i < len(self._plateau_de_jeu) :
				i += 1
				try:
					if self._plateau_de_jeu[i] == str('X'):
						if self._plateau_de_jeu[i + 1] == str('U'):
							pas += 1
							nombre = 0
							self.victoire = True
							continue

						elif self._plateau_de_jeu[i + 1] == str('O'):
							print("On ne peut pas traverser les murs !")
							nombre = 0
							continue

						else:
							self._plateau_de_jeu = self._plateau_de_jeu[:i] + " " + self._plateau_de_jeu[(i + 1):]
							self._plateau_de_jeu = self._plateau_de_jeu[:(i + 1)] + "X" + self._plateau_de_jeu[(i + 2):]
							pas += 1
							break
					
				except IndexError:
					pass

		input("Vous vous êtes déplacez de {} pas vers l'Est.".format(pas))
		if self.victoire == True :
			input("\nVous venez de vous échapper du labyrinthe !!!")

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
		if self.victoire == True :
			input("\nVous venez de vous échapper du labyrinthe !!!")


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
		if self.victoire == True :
			input("\nVous venez de vous échapper du labyrinthe !!!")

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
		if self.victoire == True :
			input("\nVous venez de vous échapper du labyrinthe !!!")

	def partie_en_cours(self):

		jeu_en_cours = True
		premier_cycle = True

		while jeu_en_cours == True :

			os.system("cls")
			chaine = "X = Robot\nU = Sortie\n. = Porte\nO = Mur\n\n" + self._plateau_de_jeu
			print(chaine)

			if premier_cycle == True :
				commande = input("\n     Commande de jeu :\n\n     N              Nord\n  O     E        Ouest/Est\n     S              Sud\n\nQ: sauvegarder et Quitter\n\nAstuce: vous pouvez indiquer le nombre \nde pas à coté de la direction.\nexemple: \"S3\" vous fera vous déplacer \nde 3 pas vers le Sud.\n\n Commande :  ")
				premier_cycle = False
			else :
				commande = input("\n     Commande de jeu :\n\n     N              Nord\n  O     E        Ouest/Est\n     S              Sud\n\nQ: sauvegarder et Quitter\n\n Commande :  ")

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

			if lettre == "S":
				self.deplacement_bas(nombre)
			elif lettre == "N":
				self.deplacement_haut(nombre)
			elif lettre == "O":
				self.deplacement_gauche(nombre)
			elif lettre == "E":
				self.deplacement_droite(nombre)
			elif lettre == "Q":
				input("\nAurevoir grand fou !")
				self.sauvegarde_de_la_partie()
				sys.exit()
			else :
				input("Je suis désolé, je n'ai pas compris votre demande.")


			i = 0
			while i < len(self._plateau_vierge) :
				i += 1
				try :
					if self._plateau_de_jeu[i] == str('X'):
						self._plateau_de_jeu = self._plateau_vierge[:i] + "X" + self._plateau_vierge[(i + 1):]
				except IndexError:
						pass			

			if self.victoire == True :
				jeu_en_cours = False
	
	def sauvegarde_de_la_partie() :

		pass



#    def __repr__(self):
#        return "<Carte {}>".format(self.nom)
