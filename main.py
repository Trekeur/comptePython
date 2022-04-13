from abc import ABC, abstractmethod

class bcolors:
    """ Pour me permetre de mettre mes commentaire en couleur"""
    GREEN = '\033[92m' #GREEN
    BLUE  = '\033[94m' #BLUE
    RED   = '\033[91m' #RED
    AQUA  = '\033[96m' #TURQUOISE
    RESET = '\033[0m' #RESET COLOR


class Compte(ABC):
    """
    Ma classe compte

    """
    @abstractmethod
    def __init__(self, numero_Compte, nom_Proprietaire, mon_Solde):
        print("Mon numéro de compte !")
        """ 
        Mes attribut sont -> Attributs: numeroCompte, nompProprietaire, solde
    
        self.numero_Comtpe = 1
        self.nom_Proprietaire  = "Alex"
        self.solde = 0
        """
        """ """
        self.compte = numero_Compte
        self.proprietaire = nom_Proprietaire
        self.solde = mon_Solde

    """_______________________________________________________________________"""

    def Versement(self, somme):
        """ test versement """
        self.solde = self.solde + somme
        return self.solde
    """_______________________________________________________________________"""

    def Retrait(self, somme):
        """ test retrait """

        if (somme > self.solde):
            print("Tu n'as pas assez d'argent ")
        else:
            self.solde = self.solde - somme
            print(bcolors.AQUA,f"monsolde : {self.solde}", bcolors.RESET)
        return self.solde

    """_______________________________________________________________________"""

    """ test agio """
    """
    def Agios(self):
        self.solde = self.solde*90/100

    """
    """ test interet"""
    """
    Le montant des intérêts sera ex de 1 000 x 6 / 100, soit 60 €    
    """
    """
    def Interet(selft):

        self.solde = self.solde * 6 /100
    """

    """_______________________________________________________________________"""


"""
ETAPE DEUX !!!!!!!
"""


class CompteCourant(Compte):
    """
    Création de ma class Courant qui compose de ma function -> agios
    """

    def __init__(self, pourcentage_agios):
        super().__init__(1465, "Alex", 150)
       # print("Mon compte Courant !")

        "self.decouvert = autorisation_Decouvert"
        self.agios = pourcentage_agios
        #print("avant ma fonction Agios ")

    def Agios(self):
        print("avant mon solde -> agios")
        solde = self.solde
        solde_agios = solde * self.agios / 100
        print("Mon solde est de :", solde_agios)

        solde = solde - solde_agios
        print( "resulta de mon agios :", solde )
        print(bcolors.GREEN,"----------------------------------------- \n", bcolors.RESET)
        print(bcolors.RED, f"monsolde : {solde}", bcolors.RESET)

        return self.solde

"""_______________________________________________________________________"""

""" ETAPE 3 !!!!   """


class CompteEpargne(Compte):
    """
    Création de ma class EPARGNE
    """

    def __init__(self, pourcentage_interets):
        super().__init__(2500, "Alex", 300)
        print("Mon compte Epargne !")

        self.interets = pourcentage_interets


    def Interet(self):
        print("avant mon calcule interet")

        solde = self.solde
        solde_ajouter = solde * self.interets / 100
        print("avant solde ajouter ->", solde)
        print("mon solde_ajouter ->", solde_ajouter)

        if (self.solde < 0):
            print("Tu n'as pas d'interet ")
        else:
            self.solde = self.interets + self.solde

        print("après mon calcul de mes interet ")
        print("résulta de mes interet : ", self.solde)
        print(bcolors.RED, f"monsolde : {solde}", bcolors.RESET)

        return self.solde


if __name__ == "__main__":
    """_______________________________________________________________________"""
    try:
        compte = CompteCourant(0)
        print(bcolors.GREEN,"quelle valeur veux tu ajouter sur le compte :",bcolors.RESET)
        valeur = input()
        compte.Versement(int(valeur))
    except:
        print(bcolors.RED,'tu as rentré des lettres, veulliez saisir que des chiffres svp',bcolors.RESET)
    try:
        print(bcolors.BLUE,"quelle valeur veux tu enlever sur le compte :",bcolors.RESET)
        valeurs = input()
        compte.Retrait(int(valeurs))
    except:
        print(bcolors.RED, 'tu as rentré des lettres, veulliez saisir que des chiffres svp', bcolors.RESET)
    #compte.Versement(450)
    #compte.Retrait(250)
    #compte.Versement(750)
    #print(bcolors.GREEN,"--------------------------------------------------------", bcolors.RESET)
    #cptC = CompteCourant(90)
    #print(bcolors.GREEN,"je suis ici fonction agios ---\n", bcolors.RESET)

   # cptC.Agios()


    #print(bcolors.BLUE,"--------------------------------------------------------", bcolors.RESET)
    #cptE = CompteEpargne(6)
    #print(bcolors.BLUE, "je suis ici fonction interet ---\n", bcolors.RESET)
    #print(cptC.Versement(150))
    #print(cptC.Retrait(2))
    #cptE.Interet()
    #print(bcolors.BLUE,"-----------------------------------------------------------\n", bcolors.RESET)

    # _______________________________________________________________________
    """compte = CompteCourant(5,1)
    compte = CompteEpargne(1)"""

    print("numero de compte N°", compte.compte)
    print("proprietaire :", compte.proprietaire)
    print("mon solde est de : ", compte.solde)
