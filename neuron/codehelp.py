from ObjetsNetwork.chaineCarractere import*
from codehelp.CCHcolorSelector import*
from codehelp.CCHGithub import*
from codehelp.CCHLibrairy import*
from codehelp.CCHOrgaVarriable import*
from codehelp.CCHsearchDoc import*

class neuronCodehelp :
    def __init__(self,mainColor:str,textColor:str,fileCodeHelp:str,fileUser:str):
        self.__configFile = jsonWork(fileCodeHelp)
        self.__jsonUser = jsonWork(fileUser)
        self.searchDoc =  CHsearchDoc()
        self.__github = CHGithub(mainColor,textColor,self.__configFile)
        self.__selecteurColor = CCHcolorSelector(mainColor,textColor)
        self.__lib = CHLibrairy(mainColor,textColor)
        self.__orgaVar = CHOrgraVarriable(mainColor,textColor)
        self.__oldEntrer = ""
        self.__oldSortie = ""

    def neuron(self,requette:str):
        statement = chaine.netoyage(requette)
        texte =  ""
        var = 0
        nameUser = self.__jsonUser.lectureJSON("user")
        genreUser = self.__jsonUser.lectureJSON("genre")
        if (("doc microsoft" in statement )or ("learn" in statement) or ("visual" in statement)) :
            statement = statement.replace("doc microsoft","")
            statement = statement.replace("learn","")
            statement = statement.replace("visual","")
            if self.searchDoc.rechercheMicrosoft(statement) == True :
                texte = "Okay je t'ouverture de la documentation de microsoft."
            else :
                texte = "Une erreur c'est produite lors de la tentative d'ouverture de la documentation de microsoft "+nameUser
            var = 1
        else :
            if ("doc" in statement) : 
                statement = statement.replace("doc","")
                print(statement)
                if self.searchDoc.rechercheDevDoc(statement) == True :
                    texte = "Voici ta recherche sur le site DevDoc ."
                else :
                    texte = "je suis désoler "+nameUser+". Mais une erreur c'est produite qui m'empéche de faire la recherche"
                var = 1
            else :
                if (("liste depos" in statement) or ("depos github" in statement) or ("github depos" in statement)) :
                    texte = "Voici la liste de tes depots"
                    self.__github.GUI()
                    self.__github.GUIListDepos()
                    var = 1
                else :
                    if ("github search" in statement) : 
                        texte = "Voici ta recherche sur github ."
                        statement.replace("github search","")
                        self.__github.search(statement)
                        var = 1
                    else :
                        if ("couleur" in statement) :
                            texte ="Je vous ouvre le logiciel colors selector "+nameUser+"."
                            self.__selecteurColor.bootSelecteur()
                            var = 1
                        else :
                            if (("organisateur de varriable" in statement) or ("orga var" in statement)) :
                                texte ="Je t'ouverture de l'organisateur de varriable"
                                self.__orgaVar.bootOrganisateur()
                                var = 1
                            else :
                                if (("librairy" in statement) or ("lib" in statement)) :
                                    texte = "Ouverture de la librairy Arrera ."
                                    self.__lib.librairy()
                                    var = 1
                                else :
                                    if ("github" in statement) :
                                        texte = "Ouverture de l'interface qui permet de naviguer dans github."
                                        self.__github.GUI()
                                        var = 1
                                    else :
                                        if ("enregistrement token"in statement):
                                            texte = "Okay taper votre token dans la zone de reponse ."
                                            var = 1 
                                        else :
                                            if (("enregistrement token"in self.__oldEntrer)and(self.__oldSortie=="Okay taper votre token dans la zone de reponse .")):
                                                texte = "Votre token Github est enregister "+nameUser
                                                self.__configFile.EcritureJSON("token",requette)
                                                var = 1 
        self.__oldEntrer = statement
        self.__oldSortie = texte
        return var,texte