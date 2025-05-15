from tkinter import*
import webbrowser as w
from librairy.travailJSON import*
from ObjetsNetwork.gestion import*


class CHLibrairy:
    def __init__(self,ConfigNeuron:jsonWork,gest:gestionNetwork):
        self.__lienLibrairy = "https://github.com/Arrera-Software/Arrera-librairy"
        self.__lienReadme =  "https://github.com/Arrera-Software/Arrera-librairy/blob/main/README.md"
        self.__lienObjetPython = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/python"
        self.__lienObjetCPP = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/C%2B%2B"
        self.__mainColor = ConfigNeuron.lectureJSON("interfaceColor")
        self.__textColor = ConfigNeuron.lectureJSON("interfaceTextColor")
        self.__iconAssistant = ConfigNeuron.lectureJSON("iconAssistant") 
        self.__name = ConfigNeuron.lectureJSON("name")
        self.objNET = gest.getNetworkObjet()
    
    def active(self):
        # Test de la connexion internet
        self.__screenLibrairy = Toplevel()
        self.__varName = StringVar(self.__screenLibrairy)
        self.__screenLibrairy.title(self.__name + ": codeHelp librairy")
        self.__screenLibrairy.iconphoto(False, PhotoImage(file=self.__iconAssistant))
        self.__screenLibrairy.minsize(700, 500)
        self.__screenLibrairy.configure(bg=self.__mainColor)
        Label(self.__screenLibrairy, text="Arrera Librairy", bg=self.__mainColor,
              fg=self.__textColor,
              font=("arial", 25)).place(relx=0.5, rely=0.0, anchor="n")
        if (self.objNET.getEtatInternet() == True):
            # Recuperation de l'index de la librairy
            try:
                response = requests.get(
                    "https://raw.githubusercontent.com/Arrera-Librairy/index-codehelp/refs/heads/main/index.json")
                response.raise_for_status()
                contenuJson = response.json()
                nb = len(contenuJson)+1
                listLib = []
                dictURLName = {}
                for i in range(1,nb):
                    listLib.append(contenuJson[str(i)]['name'])
                    dictURLName[contenuJson[str(i)]['name']] = contenuJson[str(i)]['url']

            except requests.exceptions.RequestException as e:
                # Message d'erreur
                Label(self.__screenLibrairy, text="Impossible de récuper l'index", bg=self.__mainColor,
                      fg=self.__textColor,
                      font=("arial", 15)).place(relx=0.5, rely=0.5, anchor="center")
                return False
            # Creation de l'interface
            self.__varName.set(listLib[0])
            # Widget
            self.__optionName = OptionMenu(self.__screenLibrairy, self.__varName, *listLib)
            btnView = Button(self.__screenLibrairy, text="consulter",bg=self.__mainColor,fg=self.__textColor,
                             command= lambda : w.open(dictURLName[self.__varName.get()]),font=("arial",15))
            # affichage
            self.__optionName.place(relx=0.5, rely=0.5, anchor="center")
            btnView.place(relx=0.5, rely=1.0, anchor="s")
            return True
        else:
            # Message d'erreur
            Label(self.__screenLibrairy, text="Erreur de connexion internet",bg=self.__mainColor,fg=self.__textColor,
                  font=("arial",15)).place(relx=0.5, rely=0.5, anchor="center")
            return False