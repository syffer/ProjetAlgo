
from Cellule import *


# les liens reliant les cellules du terrain
# représente les arêtes du graphe
class Lien:

	# Cellule u : une cellule de l'un des bouts du lien
	# Cellule v : l'autre cellule au bout du lien
	# Int distance : la distance séparant les cellules u et v
	def __init__(self, u, v, distance):

		# on mettra toujours la cellule ayant le plus petit numéro en premier
		if( u.getNumero() > v.getNumero() ):
			u, v = v, u

		self.u = u
		self.v = v
		
		# on ajoute ce lien à la liste des liens des cellules
		self.u.ajouterLien( self )
		self.v.ajouterLien( self )
		
		
		self.distance = distance
		
		# liste de Mouvement
		self.vers_u = [] 		# mouvements de V vers U
		self.vers_v = []		# mouvements de U vers V


	# retourne la cellule enregistré sous U
	# return : Cellule
	def getU(self):
		return self.u

	# retourne la cellule enregistré sous V
	# return : Cellule
	def getV(self):
		return self.v

	# retourne la longueur du lien (la distance entre les deux cellules)
	# return : Integer
	def getDistance(self):
		return self.distance



	
	# ajoute un mouvement VERS la cellule enregistrée sous V
	# Mouvement mouvement : le mouvement à ajouter
	def ajouterMouvementVersV( self, mouvement ):
		self.vers_v.append( mouvement )
	
	# ajoute un mouvement VERS la cellule enregistrée sous U
	# Mouvement mouvement : le mouvement à ajouter
	def ajouterMouvementVersU( self, mouvement ):
		self.vers_u.append( mouvement )
	
	
	
	# vide la liste des mouvements vers V
	def clearVersV( self ):
		self.vers_v = []
		
	# vide la liste des mouvements vers U
	def clearVersU( self ):
		self.vers_u = []
	
	# supprime tous les mouvements présent sur ce lien
	def clearAllMouvements( self ):
		self.clearVersU()
		self.clearVersV()
		
	
	# ajoute un mouvement VERS la cellule spécifiée
	# si la cellule ne fait pas partie de ce lien, on lance une Exception
	# Cellule cellule : la cellule vers lequel le mouvement est en direction
	# Mouvement mouvement : le mouvement à ajouter
	def ajouterMouvementVersCellule( self, cellule , mouvement ):
		
		# on vérifie que la cellule est bien l'un des bords du lien
		
		if( cellule == self.getU() ): 		# si c'est U
			self.ajouterMouvementVersU(mouvement)
			
		elif( cellule == self.getV() ): 	# si c'est V
			self.ajouterMouvementVersV(mouvement)
			
		else:
			raise Exception("la cellule spécifiée ne fait pas partie de ce lien (ajouterMouvementCellule)")
	
	
	
	
	
	

	def toString(self):
		return "( " + self.u.toString() + " ; " + self.v.toString() + " ; " + str(self.distance) + " )" 




	# utlisé pour ranger les liens dans un dictionnaire
	def hash(self):
		return str( self.u.getNumero() ) + str( self.v.getNumero() )


	# détermine la valeur du hash d'un lien à partir de deux cellules
	# appel : Lien.hashage(...)
	# Cellule cellule1
	# Cellule cellule2
	def hashage(cellule1 , cellule2):
		n1, n2 = cellule1.getNumero(), cellule2.getNumero()
		if( n1 > n2 ):
			n1, n2 = n2, n1
		return str(n1) + str(n2)