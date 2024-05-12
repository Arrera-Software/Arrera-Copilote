from ObjetsNetwork.arreraNeuron import*
from copilotefonction.copiloteAgenda import*
from copilotefonction.copiloteTask import*
from tkinter import*

class neuronAgendatCopilote :
    def __init__(self,jsonUser:jsonWork):
        self.__jsonUser = jsonUser
        self.__fncAgenda = CArreraCopiloteAgenda("fileUser/agenda.json")
        self.__fncTask = CArreraCopiloteTask("fileUser/task.json")
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
        if (("ajouter un rendez-vous" in statement) or ("ajoute un rendez-vous"  in statement) or 
            ("ajoute evenement" in statement) or ("ajoute rappel" in statement) or 
            ("ajoute un evenement" in statement) or ("ajoute un rappel" in statement) or 
            ("ajouter un evenement" in statement) or ("ajouter  un rappel" in statement)):
            self.__fncAgenda.activeAddWindows()
            sortie = ["Ok "+genreUser+" "+nameUser+" . Je vous ouvre l'interface de l'agenda.",
                      "Il te reste plus qu'a suivre l'interface pour ajouter votre rendez-vous"]
            nb = 1 
        else :
            if (("suppr un rendez-vous" in statement) or ("supprimer un rendez-vous"  in statement) or 
                ("suppr evenement" in statement) or ("suppr rappel" in statement) or 
                ("suppr un evenement" in statement) or ("suppr un rappel" in statement) or 
                ("supprimer un evenement" in statement) or ("supprimer un rappel" in statement)or
                ("supprime un evenement" in statement) or ("supprime un rappel" in statement or
                ("supprimer un rendez-vous" in statement))):
                self.__fncAgenda.activeSupprWindows()
                sortie = ["Ok "+genreUser+" "+nameUser+" . Je vous ouvre l'interface de l'agenda.",
                      "Il te reste plus qu'a suivre l'interface pour supprimer votre rendez-vous"]
                nb = 1
            
            else :
                if (("evenement d'aujourd'hui" in statement) or ("evenement du jour" in statement) 
                    or ("rendez-vous d'aujourd'hui" in statement) or ("rappel aujourd'hui" in statement)):
                    nbEvent= self.__fncAgenda.getNbEventToday()
                    if (nbEvent==0):
                        sortie = ["Vous avez rien de prevu aujourd'hui "+genreUser,"Toujours la pour te servir"]
                    else :
                        listEvent = self.__fncAgenda.getEventToday()
                        texteRyley = ""
                        for i in range(0,nbEvent):
                            texteRyley = texteRyley+"\n"+listEvent[i]
                        if(nbEvent==1):
                            textSix = "Ryley vous montre votre seule événement "+genreUser
                        else :
                            textSix = "Ryley vous montre vos "+str(nbEvent)+" événement "+genreUser
                        sortie = [textSix,texteRyley]
                    nb = 1
                else :
                    if("montre mes tache"in statement):
                        sortie =["",""]
                        self.__fncTask.activeViewTask()
                        nb = 1
                    else :
                        if("ajoute une tache"in statement):
                            sortie =["",""]
                            self.__fncTask.activeViewAdd()
                            nb = 1
                        else :
                            if("supprime une tache"in statement):
                                sortie =["",""]
                                self.__fncTask.activeViewSuppr()
                                nb = 1
                            else :
                                if("fini une tache"in statement):
                                    sortie =["",""]
                                    self.__fncTask.activeViewCheck()
                                    nb = 1
                                else :
                                    sortie = ["",""]
                                    nb = 0
        
        return nb , sortie