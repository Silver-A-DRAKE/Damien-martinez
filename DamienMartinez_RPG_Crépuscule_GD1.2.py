################## CLASSE PERSONNAGES #################
from _typeshed import Self

        ### CLASSE MONSTRE ###
class Monstre:

    niveauMax = 99 #propriété statique

    def __init__(self, element, niveau=1, force=200, hp=99999, hpMax=99999, defense=200, endurance=250):
        self.__niveau = niveau #attributs privés
        self.__force = force
        self.__hp = hp
        self.__hpMax = hpMax
        self.__defense = defense
        self.__endurance = endurance
        self.__element = element

    def getForce(self):
        return self.__force

    def getDefense(self):
        return self.__defense

    def getEndurance(self):
        return self.__endurance

    def getHP(self):
        return self.__hp

    def setHP(self, hp):
        self.__hp = hp

    def lvlUp(self):
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20

    def getNiveauMax():
        return Monstre.__niveauMax

    def estVivant(self):
        return self.__hp>0

    def getElement():
        return Self.__element

    def attaquer(self, ennemie):
        ennemie.__hp -= self.__force

        ### CLASSE PERSONNAGE ###
class Personnage:

    niveauMax = 99 #propriété statique

    def __init__(self, sort, element, niveau=1, force=10, hp=100, hpMax=100, defense=10, endurance=25,):
        self.__niveau = niveau #attributs privés
        self.__force = force
        self.__hp = hp
        self.__hpMax = hpMax
        self.__arme = Arme()
        self.__defense = defense
        self.__endurance = endurance
        self.__sort = sort
        self.__element = element

    def equiper(self, arme):
        raise NotImplementedError("Subclass must implement abstract method")

    def getForce(self):
        return self.__force

    def getDefense(self):
        return self.__defense

    def getEndurance(self):
        return self.__endurance

    def getHP(self):
        return self.__hp

    def setHP(self, hp):
        self.__hp = hp

    def lvlUp(self):
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20

    def getNiveauMax():
        return Personnage.__niveauMax

    def estVivant(self):
        return self.__hp>0

    def getSorts(self):
        return self.__sort

    def getElement():
        return Self.__element

    def attaquer(self, ennemie):
        ennemie.__hp -= self.__force * self.__arme.getDegat() #ou + en fonction de nos choix de gameplay


################## CLASSE DRACOLISH #################

class Dracolish (Personnage):

    def __init__(self):
        super().__init__() #réutilise le constructeur de la super classe Personnage
        self.__rage = 20
        self.__magie = 15

    def lvlUp(self):
        """
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20
        """
        super().lvlUp()
        self.__rage +=5

        super().lvlUp()
        self.__magie +=2

        ### Aptitudes ###
    def getSorts(self, sort):
        if isinstance(sort):
            self.__sort = sort
        return self.__sort

    def attaquer(self, ennemie):
        ennemie.setHP(ennemie.getHP()- (self.getForce() + self.__rage) * self.__arme.getDegat())

    def equiper (self, arme):
        if isinstance(arme, Epee):
            self.__arme = arme

################## CLASSE GUERRIER #################

class Guerrier (Personnage):

    def __init__(self):
        super().__init__() #réutilise le constructeur de la super classe Personnage
        self.__rage = 20

    def lvlUp(self):
        """
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20
        """
        super().lvlUp()
        self.__rage +=5

    def attaquer(self, ennemie):
        ennemie.setHP(ennemie.getHP()- (self.getForce() + self.__rage) * self.__arme.getDegat())

    def equiper (self, arme):
        if isinstance(arme, Epee):
            self.__arme = arme

################## CLASSE MAGE #################

class Mage (Personnage):

    def __init__(self):
        super().__init__() #réutilise le constructeur de la super classe Personnage
        self.__magie = 20

    def lvlUp(self):
        """
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20
        """
        super().lvlUp()
        self.__magie +=2

    def attaquer(self, ennemie):
        ennemie.setHP(ennemie.getHP()- (self.getForce() + self.__magie) * self.__arme.getDegat())

    def equiper (self, arme):
        if isinstance(arme, Baton):
            self.__arme = arme

################## CLASSE ARMES #################

class Arme:

    def __init__(self, degatArme = 1):
        self.__degat = degatArme

    def getDegat(self):
        return self.__degat

class ArtMartial(Arme):

    def __init__(self, degatArme = 2):
        super().__init__(degatArme)

class Baton(Arme):

    def __init__(self, degatArme = 2):
        super().__init__(degatArme)
        self.type = "Feu"
        self.type = "Eau"
        self.type = "Foudre"
        self.type = "Glace"
        self.type = "Vent"
        self.type = "Roche"

class Epee(Arme):

    def __init__(self, degatArme = 2):
        super().__init__(degatArme)

class Hache(Arme):

    def __init__(self, degatArme = 10):
        super().__init__(degatArme)

class Arc(Arme):

    def __init__(self, degatArme = 1):
        super().__init__(degatArme)

class Claymore(Arme):

    def __init__(self, degatArme = 5):
        super().__init__(degatArme)

class AutoArbalète(Arme):

    def __init__(self, degatArme = 5):
        super().__init__(degatArme)

class EpeeDesForges(Arme):

    def __init__(self, degatArme = 100):
        super().__init__(degatArme)
        self.type = "Feu"

################## CLASSE RPG #################

class RPG:

    def playGame():
        ### PERSONNAGE PRINCIPAL ###
        Silver = Personnage()

        epee = Epee(10)
        Silver.equiper(epee)

        baton = Baton(5)
        Silver.equiper(baton)

        hache = Hache(10)
        Silver.equiper(hache)

        claymore = Claymore(5)
        Silver.equiper(claymore)

        arc = Arc(5)
        Silver.equiper(arc)

        autoarbalète = AutoArbalète(5)
        Silver.equiper(autoarbalète)

        Silver.lvlUp()


        ### ALLIERS ###
        allier = Personnage()

        epee = Epee(10)
        allier.equiper(epee)

        baton = Baton(5)
        allier.equiper(baton)

        hache = Hache(10)
        allier.equiper(hache)

        claymore = Claymore(5)
        allier.equiper(claymore)

        arc = Arc(5)
        allier.equiper(arc)

        autoarbalète = AutoArbalète(5)
        allier.equiper(autoarbalète)


        ### MECHANTS ###
        mechant = Personnage()

        epee = Epee(10)
        mechant.equiper(epee)

        baton = Baton(5)
        mechant.equiper(baton)

        hache = Hache(10)
        mechant.equiper(hache)

        claymore = Claymore(5)
        mechant.equiper(claymore)

        arc = Arc(5)
        mechant.equiper(arc)

        autoarbalète = AutoArbalète(5)
        mechant.equiper(autoarbalète)



        Timonero = Monstre("eau")


#       print(Personnage.niveauMax)#appel d'une propriété statique      
        while Silver.estVivant() and mechant.estVivant() and allier.estVivant():
            
            Silver.attaquer(mechant, Timonero)
            allier.attaquer(mechant, Timonero)
            mechant.attaquer(allier, Silver, Timonero)
            Timonero.attaquer(allier, Silver, mechant)

        if (allier.estVivant()):
            allier.lvlUp()
            print("Le héros a gagné!")
        else:
            mechant.lvlUp()
            print ("Le méchant a gagné!")
        
RPG.playGame()