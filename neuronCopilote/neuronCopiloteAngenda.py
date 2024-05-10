from ObjetsNetwork.arreraNeuron import*
from copilotefonction.copiloteAgenda import*
from tkinter import*

class neuronAgendatCopilote :
    def __init__(self,jsonUser:jsonWork):
        self.__jsonUser = jsonUser
        self.__fncAgenda = CArreraCopiloteAgenda("fileUser/agenda.json")
        self.__oldSortie = ""
    
    def neuron(self,var:str):
        statement = chaine.netoyage(var)
        nameUser = self.__jsonUser.lectureJSON("user")
        genreUser = self.__jsonUser.lectureJSON("genre")
        if(("ouvre l'agenda"in statement)):
            self.__fncAgenda.activeAgenda()
            sortie=["Okay "+genreUser+" "+nameUser+". Je vous ouvre l'agenda"
                    ,"J'espere que l'agenda vous servira"]
            nb = 1 
        if (("ajouter un rendez-vous" in statement) or ("ajout un rendez-vous"  in statement) or 
            ("ajout evenement" in statement) or ("ajout rappel" in statement) or 
            ("ajout un evenement" in statement) or ("ajout un rappel" in statement) or 
            ("ajouter un evenement" in statement) or ("ajouter  un rappel" in statement)):
            self.__fncAgenda.activeAddWindows()
            sortie = ["",""]
            nb = 1 
        else :
            if (("suppr un rendez-vous" in statement) or ("supprimer un rendez-vous"  in statement) or 
                ("suppr evenement" in statement) or ("suppr rappel" in statement) or 
                ("suppr un evenement" in statement) or ("suppr un rappel" in statement) or 
                ("supprimer un evenement" in statement) or ("supprimer un rappel" in statement)):
                self.__fncAgenda.activeSupprWindows()
                sortie = ["",""]
                nb = 1
            
            else :
                if (("evenement d'aujourd'hui" in statement) or ("evenement du jour" in statement) 
                    or ("rendez-vous d'aujourd'hui" in statement) or ("rappel aujourd'hui" in statement)):

                    sortie = ["",""]
                    nb = 1
                else :
                    sortie = ["",""]
                    nb = 0
        
        return nb , sortie