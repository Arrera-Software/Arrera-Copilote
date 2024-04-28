from ObjetsNetwork.arreraNeuron import*

class ArreraCopilote :
    def __init__(self):
        #objet assistant
        self.__assistantSix = ArreraNetwork("configuration/configUser.json",
                                          "configuration/six.json",
                                          "configuration/listFete.json")
        self.__assistantRyley = ArreraNetwork("configuration/configUser.json",
                                          "configuration/ryley.json",
                                          "configuration/listFete.json")
        #fenetre tkinter
        self.__screen = Tk()
        self.__screen.title("Arrera : Copilote")
        self.__screen.maxsize(700,700)
        self.__screen.minsize(700,700)
        # emplacement icon 
        self.__iconSix = "asset/icon/six/logo-normal.png"
        self.__iconRyley = "asset/icon/ryley/icon.png"
        self.__iconCopilote = "asset/icon/copilote/icon.png"
        # Ajout icon a la fenetre
        self.__screen.iconphoto(False,PhotoImage(file=self.__iconCopilote))

    def active(self):
        self.__screen.mainloop()