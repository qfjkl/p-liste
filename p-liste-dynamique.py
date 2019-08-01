import os

class Pliste:

	def __init__(self,Tstring,ensemble):
		""" initialisation des variables
			
			paramètres : Tstring (Taille de la chaine de caractère à générer), 
						 ensemble (Ensemble d'élément à parcourir afin de générer les p-listes)

		 """

		self.taille = Tstring
		self.ensemble = ensemble
		self.tEnsemble = len(ensemble)-1
		self.genliste = Pliste.occurence(self,Tstring)
		self.liste = list("".join(self.genliste))
		self.cpt = 1
		print(Tstring, ensemble)

	def isOk(self,tab,item,i,reponse=bool):
		"""function permettant de vérrifier que tout les éléments présents dans un tableau correspondent à une valeur optionnel)
		
		paramètre : tab (array dans lequel on compare que les éléments sont égaux),
					item (élément optionnel à comparer avec tout le reste du tableau),
					i (taille du tableau)
		@return : boolean (True si tout les éléments correspondent et False dans le cas contraire)
			
		"""
		while i >= 0:
			# si l'élément à parcouru est égal à la valeur passé en paramètre 
			if(tab[i] == item):
				
				reponse = True
				# lorsque toute les valeurs du tableau n'ont pas été parcouru on passe à l'élément précédent
				if(i > 0):
					Pliste.isOk(self,tab,item,i-1,reponse)
			# Au cas ou une seule valeur du tableau est différente de la valeur optionnelle alors reponse = false 
			else:
				reponse = False
				break
			i-=1
		# On renvoi la reponse à l'utilisateur
		return reponse		

	def occurence(self,n):
		"""Function permettant de creer un tableau ayant pour taille la taille de la chaine de caractère à générer
		et ayant pour valeur le premier élément de notre ensemble à parcourir			
		
		Retourne le tableau d'élément creer

		"""
		occ = list()
		i = 0
		while i <= n:
			occ.append(self.ensemble[0])
			i+=1
		return occ


	def genPListe(self,tTab):
		""" Fonction permettant de parcourir l'ensemble des p-liste d'un ensemble d'élément
			
			Paramètre : tTab (taille de la p-liste à générer)

		"""
		# Au cas nous avons des p-listes à parcourir
		if(not Pliste.isOk(self,self.liste[-1],self.ensemble[-1],len(self.liste[-1])-1) ):
			
			if(tTab >= 0):
				# on parcourt les éléments de notre grand t'ensemble
				for i,element in enumerate(self.ensemble):
					# pour éviter qu'il y'est des doublons on exclus certaines valeurs
					if (tTab > 0 and i >= 0):
						self.genliste[tTab] = element
					else:	
						self.genliste[tTab] = element
						resultat="".join(self.genliste)
						self.liste.append(resultat)
						print(self.cpt,' : ',resultat)
						self.cpt+=1
					Pliste.genPListe(self,tTab-1)

		return self.liste

# element = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
c = 0
content = list() 

while c<=255:
	content.append(str(c))
	c+=1

nElement = len(content)-1
P = Pliste(2,content)
P.genPListe(2)

os.system("pause")