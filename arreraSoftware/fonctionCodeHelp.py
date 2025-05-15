from objet.CHOrgraVarriable import*
from objet.CHsearchDoc import*
from objet.CCHcolorSelector import*
from objet.CHGithub import*
from librairy.dectectionOS import*
from objet.CHLibrairy import*

class fncCodehelp :
    def __init__(self,configNeuron:jsonWork,dectOs:OS,gestNeuron:gestionNetwork) -> None:
        self.__orgaVar = CHOrgraVarriable(configNeuron,dectOs)
        self.__searchDoc = CHsearchDoc()
        self.__colorSelector = CCHcolorSelector(configNeuron)
        self.__githubObjet = CHGithub(configNeuron,gestNeuron)
        self.__librairyCodehelp = CHLibrairy(configNeuron,gestNeuron)
    
    def activeOrgaVar(self):
        self.__orgaVar.bootOrganisateur()

    def rechercheDoc(self,mode:int,recherche:str):
        """
        1 : DevDoc
        2 : Microsoft
        3 : Python 
        """
        match mode :
            case 1 :
                # DevDoc
                self.__searchDoc.rechercheDevDoc(recherche)
            case 2 : 
                # Microsoft 
                self.__searchDoc.rechercheMicrosoft(recherche)
            case 3 :
                # Python 
                self.__searchDoc.recherchePython(recherche)
    
    def activeColorSelecteur(self):
        self.__colorSelector.bootSelecteur()
    
    def searchGithub(self,requette:str):
        self.__githubObjet.search(requette)
    
    def openSiteGithub(self):
        w.open("www.github.com")
    
    def openGestionGithub(self):
        self.__githubObjet.GUI()
    
    def openOutilLibrairy(self):
        self.__librairyCodehelp.active()