from librairy.jsonWorkOnline import *
from librairy.dectectionOS import *

class CTigerDemon :
    def __init__(self,nameSoft : str,url :str):
        # objet
        self.__system = OS()
        depotFile = jsonWorkOnline()
        # load depots
        depotFile.loadInternet(url)
        # Chargement des informations du logiciel
        self.__dictSofts = depotFile.dictJson()[nameSoft]

    def checkUpdate(self):

        versionInstalled = self.getVersionSoft()

        if (versionInstalled != "IXXXX-XXX"):
            versionOnline = self.__dictSofts["version"]
            if (versionInstalled != versionOnline):
                return True
            else:
                return False

    def getVersionSoft(self):
        versionInstalled = ""
        with open("VERSION", "r") as fichier:
            for ligne in fichier:
                # Si la ligne commence par "VERSION="
                if ligne.startswith("VERSION="):
                    # Supprimer le saut de ligne éventuel et récupérer la valeur
                    version = ligne.strip().split("=")[1]
                    versionInstalled = version
            fichier.close()

        return versionInstalled