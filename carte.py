# -*-coding:Utf-8 -*

# différentes importations qui permettent de clear la console, d'importer/exporter des sauvegardes ou de quitter le programme

import os
import sys
import pickle
import random

        


# La classe Carte_en_cours() récupère une seule une carte de la classe Cartes() et lui donne les attributs pour lui permettre de devenir un plateau de jeu
class Carte_en_cours():

	nombre_de_robot = 1

	def __init__(self, _plateau_de_jeu):

		# Initialisation d'un plateau de jeu sur lequel le Robot va se déplacer
		self._plateau_de_jeu = _plateau_de_jeu

		self.carte_vierge = _plateau_de_jeu

		self.victoire = False

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

	# variable qui calcule la longeur du labyrinthe
	def longeur_plateau(self):

		j = self.largeur_plateau()
		j = int(j)
		j += 1
		i = 1
		longeur = 1
		boucle = True
		while boucle == True :
			try :
				if self._plateau_de_jeu[j * i] == "0" :
					longeur += 1
					i += 1
			except IndexError:
				boucle = False

		return longeur


	# Creation d'un mouvement du robot, en effancant le robot de sa précédente case pour l'inscrire sur la case suivante
	def deplacement(self, direction, nombre="1"):

		self.direction = direction
		nombre = int(nombre)
		mouvement = nombre
		emplacement_future_case = 0
		j = self.largeur_plateau()
		pas = 0
		chaine = ""

		while nombre > 0 :
			i = 0
			nombre -= 1
			while i < len(self._plateau_de_jeu) :
				i += 1
				try:
					if self._plateau_de_jeu[i] == str('X'):
						if self.direction == "E":
							emplacement_future_case = i + 1
						if self.direction == "O":
							emplacement_future_case = i - 1
						if self.direction == "S":
							emplacement_future_case = i + j + 1
						if self.direction == "N":
							emplacement_future_case = i - j - 1

						# détermine la condition de victoire
						if self._plateau_de_jeu[emplacement_future_case] == str('U'):
							pas += 1
							nombre = 0
							self.victoire = True
							continue
						# empêche de traverser les obstacles
						elif self._plateau_de_jeu[emplacement_future_case] == str('O') or self._plateau_de_jeu[emplacement_future_case] == str('0') :
							chaine += "On ne peut pas traverser les murs !\n"
							nombre = 0
							continue
						# déplace le robot vers la droite
						else:
							self._plateau_de_jeu = self._plateau_de_jeu[:i] + " " + self._plateau_de_jeu[(i + 1):]
							self._plateau_de_jeu = self._plateau_de_jeu[:(emplacement_future_case)] + "X" + self._plateau_de_jeu[(emplacement_future_case + 1):]
							pas += 1
							break
					
				except IndexError:
					pass

		# renvoit d'un message au joueur, en fonction de la direction qu'il a prit
		if self.direction == "E":
			chaine += "Vous vous êtes déplacez de {} pas vers l'Est.\n".format(pas)
		if self.direction == "O":
			chaine += "Vous vous êtes déplacez de {} pas vers l'Ouest.\n".format(pas)
		if self.direction == "S":
			chaine += "Vous vous êtes déplacez de {} pas vers le Sud.\n".format(pas)
		if self.direction == "N":
			chaine += "Vous vous êtes déplacez de {} pas vers le Nord.\n".format(pas)

		return chaine

	# fonction du robot, sur une des cases adjacentes, qui détruit un mur pour le remplacer pour une case vide
	def percer_mur(self, direction):

		self.direction = direction
		emplacement_mur_a_detruire = 0
		j = self.largeur_plateau()
		chaine = ""

		i = 0
		while i < len(self._plateau_de_jeu) :
			i += 1
			try:
				if self._plateau_de_jeu[i] == str('X'):
					if self.direction == "E":
						emplacement_mur_a_detruire = i + 1
					if self.direction == "O":
						emplacement_mur_a_detruire = i - 1
					if self.direction == "S":
						emplacement_mur_a_detruire = i + j + 1
					if self.direction == "N":
						emplacement_mur_a_detruire = i - j - 1

					if self._plateau_de_jeu[emplacement_mur_a_detruire] != str('O'):
						chaine += "Ce n'est pas un mur que l'on peut détruire...\n"
						continue
					else :
						self._plateau_de_jeu = self._plateau_de_jeu[:(emplacement_mur_a_detruire)] + " " + self._plateau_de_jeu[(emplacement_mur_a_detruire + 1):]
						if self.direction == "E":
							chaine += "Vous venez de détruire le mur à votre droite.\n"
						if self.direction == "O":
							chaine += "Vous venez de détruire le mur à votre gauche.\n"
						if self.direction == "S":
							chaine += "Vous venez de détruire le mur en dessous de vous.\n"
						if self.direction == "N":
							chaine += "Vous venez de détruire le mur au dessus de vous.\n"
						break

			except IndexError:
				pass

		return chaine

	# fonction du robot, sur une des cases adjacentes, qui remplace une porte par un mur
	def murer_porte(self, direction):

		self.direction = direction
		emplacement_future_case = 0
		j = self.largeur_plateau()
		chaine = ""

		i = 0
		while i < len(self._plateau_de_jeu) :
			i += 1
			try:
				if self._plateau_de_jeu[i] == str('X'):
					if self.direction == "E":
						emplacement_porte_a_murer = i + 1
					if self.direction == "O":
						emplacement_porte_a_murer = i - 1
					if self.direction == "S":
						emplacement_porte_a_murer = i + j + 1
					if self.direction == "N":
						emplacement_porte_a_murer = i - j - 1

					if self._plateau_de_jeu[emplacement_porte_a_murer] != str('.'):
						chaine += "Ce n'est pas une porte...\n"
						continue
					else :
						self._plateau_de_jeu = self._plateau_de_jeu[:(emplacement_porte_a_murer)] + "O" + self._plateau_de_jeu[(emplacement_porte_a_murer + 1):]
						self.carte_vierge = self.carte_vierge[:(emplacement_porte_a_murer)] + "O" + self.carte_vierge[(emplacement_porte_a_murer + 1):]
						if self.direction == "E":
							chaine += "Vous venez de murer la porte à votre droite.\n"
						if self.direction == "O":
							chaine += "Vous venez de murer la porte à votre gauche.\n"
						if self.direction == "S":
							chaine += "Vous venez de murer la porte en dessous de vous.\n"
						if self.direction == "N":
							chaine += "Vous venez de murer la porte au dessus de vous.\n"
						break

			except IndexError:
				pass

		return chaine


	# variable qui place un robot par joueur a une case aléatoire sur la carte chargée
	# les robots sont stockés par la map sous la forme de "numéro du joueur"
	def placement_du_robot(self):
		
		placement_ok = False
		k = self.largeur_plateau()
		h = self.longeur_plateau()

		nom_du_robot = str(Carte_en_cours.nombre_de_robot)

		while placement_ok == False:
			i = random.randint(0, (k * h))
			if self._plateau_de_jeu[i] == str(' '):
				self._plateau_de_jeu = self._plateau_de_jeu[:i] + nom_du_robot + self._plateau_de_jeu[(i + 1):]
				placement_ok = True

		Carte_en_cours.nombre_de_robot += 1


	# variable qui créer une carte visible par le joueur en cours
	# la carte est créé à partir du plateau de jeu de la carte
	def carte_visible_joueur_en_cours(self, numero_joueur):

		carte_visible = ""

		self.numero_joueur = numero_joueur
		i = 0
		while i < len(self._plateau_de_jeu) :
			i += 1
			try :
				if self._plateau_de_jeu[i] == str(self.numero_joueur) :
					carte_visible = self._plateau_de_jeu[:i] + 'X' + self._plateau_de_jeu[(i + 1):]
			except IndexError:
				pass
		i = 0
		while i < len(self._plateau_de_jeu) :
			i += 1
			try :
				if ((carte_visible[i] == str(self.numero_joueur + 1)) or (carte_visible[i] == str(self.numero_joueur + 2)) or (carte_visible[i] == str(self.numero_joueur + 3)) or\
					(carte_visible[i] == str(self.numero_joueur + 4)) or (carte_visible[i] == str(self.numero_joueur + 5)) or (carte_visible[i] == str(self.numero_joueur - 1)) or\
					(carte_visible[i] == str(self.numero_joueur - 2)) or (carte_visible[i] == str(self.numero_joueur - 3)) or (carte_visible[i] == str(self.numero_joueur - 4)) or\
					(carte_visible[i] == str(self.numero_joueur - 5))) and carte_visible[i] != "0" :
					carte_visible = carte_visible[:i] + 'x' + carte_visible[(i + 1):]
			except IndexError:
				pass	
		i = 0
		while i < len(self.carte_vierge) :
			i +=1
			try :
				if self.carte_vierge[i] == '.' and carte_visible[i] != 'X' and carte_visible[i] != 'x' :
					carte_visible = carte_visible[:i] + '.' + carte_visible[(i + 1):]
			except IndexError:
				pass

		return carte_visible

	# permet d'afficher la map avec l'aide incrustée
	def affichage_map(self, map_a_afficher):

		self.map_a_afficher = map_a_afficher
		chaine = "X = Robot\nx = Robot Enemie\nU = Sortie\n. = Porte\nO = Mur\n0 = Mur Indestructible\n\n" + map_a_afficher
		return chaine