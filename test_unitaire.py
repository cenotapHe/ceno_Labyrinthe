from carte import *

from fonction_serveur import *

import unittest

from fonction_client import *

import random



class TestMap(unittest.TestCase):

	"""Test case utilisé pour tester les fonctions du module 'Carte_en_cours'."""
	def setUp(self):
		"""Initialisation des tests."""
		self.carte = Carte_en_cours("0000\n0 O0\n0000")
		self.carte.placement_du_robot()

	def test_largeur(self):
		"""Test le fonctionnement de la fonction 'Carte_en_cours.largeur_plateau'."""
		largeur = self.carte.largeur_plateau()
		self.assertEqual(4, largeur)

	def test_longeur(self):
		"""Test le fonctionnement de la fonction 'Carte_en_cours.longeur_plateau'."""
		longeur = self.carte.longeur_plateau()
		self.assertEqual(3, longeur)

	def test_robot_depart(self):
		"""Test le placement d'un robot au début de la partie avec la fonction 'Carte_en_cours.placement_du_robot'."""
		self.assertIn(str(self.carte.nombre_de_robot - 1), self.carte._plateau_de_jeu)

	def test_carte_visible(self):
		"""Test que la carte affiche un robot X avant d'envoyer la carte au joueur avec la fonction 'Carte_en_cours.carte_visible_joueur_en_cours'."""
		carte_a_tester = self.carte.carte_visible_joueur_en_cours(1)
		self.carte._plateau_de_jeu = carte_a_tester
		self.assertIn("X", self.carte._plateau_de_jeu)

	def test_destruction_mur(self):
		"""Test d'un mur qui vient de se faire détruire par le robot avec la fonction 'Carte_en_cours.percer_mur'."""
		carte_a_tester = self.carte.carte_visible_joueur_en_cours(2)
		self.carte._plateau_de_jeu = carte_a_tester
		self.carte.percer_mur("E")
		self.assertNotIn("O", self.carte._plateau_de_jeu)


class TestServer(unittest.TestCase):

	"""Test case utilisé pour tester les fonctions du module 'Carte'."""
	def setUp(self):
		"""Initialisation des tests."""
		self.liste = Cartes()

	def test_importation(self):
		"""Test le fonctionnement de la fonction 'Cartes.importation_cartes' sur leur importation et leur stockage."""
		self.liste.importation_cartes()
		self.assertEqual(len(self.liste._noms_des_cartes),len(self.liste._labyrinthes_des_cartes))
		self.assertNotEqual(len(self.liste._noms_des_cartes), 0)


class TestCommandeClient(unittest.TestCase):

	"""Test case utilisé pour tester que le client envoit toujours une commande valide au serveur."""
	def setUp(self):
		self.test_tour_de_jeu_client = CommandeClient()

	def test_commande_client(self):
		""" Test qui permet de vérifier que la fonction 'test_commande' envoit bien une commande compréhensible par le serveur."""

		self.commande_valide = ["S1", "N1", "O1", "E1"]
		self.commande_a_tester = ["o9", "s1", "N", "E7"]
		test_commande = self.test_tour_de_jeu_client.test_commande(self.commande_a_tester[random.randint(0, 3)])
		while test_commande == None :
			test_commande = self.test_tour_de_jeu_client.test_commande(self.commande_a_tester[random.randint(0, 3)])
		self.assertIn(test_commande, self.commande_valide)
