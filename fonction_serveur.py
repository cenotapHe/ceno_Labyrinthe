import os
import socket
import select


# La classe Cartes() qui importe toutes les différentes cartes en elle, et permet au joueur d'en choisir une
class Cartes():

	def __init__(self, base = {}, **couple_nom_labyrinthe):

		# Les cartes sont importé dans deux listes, une avec leur nom, une avec leur visuel
		self._noms_des_cartes = []
		self._labyrinthes_des_cartes = []

	def importation_cartes(self):
		# On importe les cartes depuis le dossier ou elles sont, et sous leur extension .txt


		for nom_fichier in os.listdir("cartes"):
		    if nom_fichier.endswith(".txt"):
		        chemin = os.path.join("cartes", nom_fichier)
		        nom_carte = nom_fichier[:-4].capitalize()
		        with open(chemin, "r") as fichier:
		            contenu = fichier.read()
		            self._noms_des_cartes.append(nom_carte)
		            self._labyrinthes_des_cartes.append(contenu)


	def liste_labyrinthe(self):
		# On affiche une liste avec tout les labyrinthes à disposition

		chaine = "###########################"
		chaine += "\n" + "# LABYRINTHES EXISTANTS : #"
		chaine += "\n" + "###########################\n"
		for i, carte in enumerate(self._noms_des_cartes):
			chaine += "\n" + "  {} - {}".format(i + 1, carte)
		print(chaine)


	def choix_du_labyrinthe(self):
		# On va demander au serveur de choisir un labyrinthe
		i = True
		while i == True :
			self.numero_du_labyrinthe = input("\nQuel labyrinthe choisisez-vous ?")
			try :
				self.numero_du_labyrinthe = int(self.numero_du_labyrinthe)
				if self.numero_du_labyrinthe <= 0 or self.numero_du_labyrinthe > len(self._noms_des_cartes):
					print("Ce numéro de labyrinthe n'existe pas !")
					continue
				i = False
				print("Vous avez choisit le labyrinthe {}, qui se nomme \"{}\"\n".format(self.numero_du_labyrinthe, self._noms_des_cartes[self.numero_du_labyrinthe - 1]))
			except ValueError :
				print("On vous a demandé de choisir le numéro du labyrinthe.")

		return self.numero_du_labyrinthe


	def autre_chose(self):
		pass

# La classe ConnexionServeur permet au serveur d'initialiser sa connexion, et d'écouter sur le port configuré
class ConnexionServeur():

	def __init__(self):

		self.hote = ''
		self.port = 12800

		self.connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.connexion_principale.bind((self.hote, self.port))
		self.connexion_principale.listen(5)
		print("Le serveur écoute à présent sur le port {}".format(self.port))












#class Cartes():


#    def __init__(self, base = {}, **couple_nom_labyrinthe):

    	# Les cartes sont importées dans deux listes, une avec leur nom, une avec la carte
#        self._noms_des_cartes = []
#        self._labyrinthes_des_cartes = []