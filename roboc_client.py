

from fonction_client import *


# mise en place de la connexion client sur le serveur associé
client_connected = ConnexionClient()

msg_recu = client_connected.connexion_avec_serveur.recv(1024)
print(msg_recu.decode() + "\n")

# attente qu'un joueur lance la partie
lancement_partie = ""
while lancement_partie == "" :
	lancement_partie = input("Appuyez sur 'C' pour lancer la partie.\nOu n'importe quelle autre touche pour rejoindre la partie et attendre son début.\n>")

lancement_partie = lancement_partie.encode()
client_connected.connexion_avec_serveur.send(lancement_partie)

msg_recu = ""

while msg_recu[:7] != "Bonjour" :
	msg_recu = client_connected.connexion_avec_serveur.recv(1024)
	msg_recu = msg_recu.decode()
	print(msg_recu + "\n")


# mise en place des différentes conditions qui serviront dans les boucles de jeu
tour_de_jeu_client = CommandeClient()

# boucle de jeu a répéter en boucle tant que la partie n'est pas fini
while tour_de_jeu_client.debut_de_partie == True :

	
	# le joueur est en attente d'un message du serveur pour lui annoncer son tour de jeu
	msg_recu = client_connected.connexion_avec_serveur.recv(1024)
	while msg_recu.decode()[:5] == "X = R":
		os.system("cls")
		print(msg_recu.decode() + "\n")
		msg_recu = client_connected.connexion_avec_serveur.recv(1024)
	print(msg_recu.decode() + "\n")
	# on vérifit les conditions de victoire ici, car les joueurs qui ne sont pas entrain de jouer attende à cette étape de la boucle
	if msg_recu.decode()[:13] == "FIN DE PARTIE":
		tour_de_jeu_client.debut_de_partie = False
		continue

	time.sleep(1)

	client_connected.connexion_avec_serveur.send(b"ok")

	# affichage de la carte du jeu, juste avant de jouer
	os.system("cls")
	#while msg_recu.decode()[:5] != "X = R":
	msg_recu = client_connected.connexion_avec_serveur.recv(1024)
	print(msg_recu.decode() + "\n")


	time.sleep(1)
	# le multipas s'active uniquement si on a fait des commandes multiples, comme E3 ou S2...
	if tour_de_jeu_client.multipas_en_cours == True :
		pass
	# affichage des commandes, avec ou sans astuce, en fonction du premier tour du joueur ou pas
	elif tour_de_jeu_client.premier_cycle == True :
		print("\n     Commande de jeu :\n\n     N              Nord\n  O     E        Ouest/Est\n     S              Sud\n\nP: Percer un mur // M: Murer une porte\n\nQ: sauvegarder et Quitter\n\nAstuce: vous pouvez indiquer le nombre \nde pas à coté de la direction.\nexemple: \"S3\" vous fera vous déplacer \nde 3 pas vers le Sud.\nATTENTION : dans cet exemple, vous\nvous vérouillez les trois prochains\ntours de jeu !!!\n")
		tour_de_jeu_client.premier_cycle = False
	else :
		print("\n     Commande de jeu :\n\n     N              Nord\n  O     E        Ouest/Est\n     S              Sud\n\nP: Percer un mur // M: Murer une porte\n\nQ: sauvegarder et Quitter\n")
	

	commande = tour_de_jeu_client.test_commande()


	commande = commande.encode()
	client_connected.connexion_avec_serveur.send(commande)

	# le joueur est en attente d'un message du serveur pour lui annoncer ce qu'a accomplit son action
	msg_recu = client_connected.connexion_avec_serveur.recv(1024)
	print(msg_recu.decode() + "\n")

	time.sleep(2)


client_connected.fermeture_connexion()