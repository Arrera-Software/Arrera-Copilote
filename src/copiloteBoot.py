from src.copiloteGUI import *
from arreraLynx.arreraLynx import *
from src.CTigerDemon import *
from ObjetsNetwork.userConf import *

class copiloteBoot:
    def __init__(self):
        self.__userConf = userConf()
        # Ouverture JSON
        # Declaration des var
        self.__sortieLynx = False
        # Verification de la configuration de l'assistant
        self.__firstStart = self.__userConf.getFirstRun()
        self.__demonTiger = CTigerDemon("arrera-copilote","https://arrera-software.fr/depots.json")

    def active(self):
        if self.__firstStart:
            lynx = ArreraLynx("fichierJSON/configLynx.json",
                              self.__userConf.getUserSettingPath(),
                              "fichierJSON/configNeuron.json")
            lynx.active()
            self.__sortieLynx = lynx.confiCreate()
        else :
            self.__sortieLynx = True

        self.__boot()


    def __boot(self):
        arrTk = CArreraTK()
        self.__checkUpdate(arrTk)
        if (self.__sortieLynx == False):
            screen = arrTk.aTK(title="Arrera Copilote",resizable=False,width=500,height=350)
            imgCavas = arrTk.createArreraBackgroudImage(screen,
                                                        imageDark="asset/GUI/dark/NoConfig.png",
                                                        imageLight="asset/GUI/light/NoConfig.png",
                                                        width=500,height=350)
            labeltext = arrTk.createLabel(screen,
                                          text="Désoler mais vous avez pas configuer l'assistant correctement",
                                          ppolice="Arial",ptaille=20,
                                          pstyle="bold",bg="#3c2144",
                                          fg="white",pwraplength=300,
                                          justify="left")
            btnConf = arrTk.createButton(screen,text="Configurer",ppolice="Arial",ptaille=20,
                                          pstyle="bold",command=lambda:self.__restartConf(screen))
            imgCavas.pack()
            labeltext.place(x=190,y=40)
            arrTk.placeBottomCenter(btnConf)
            arrTk.view()
        else :
            assistant = guiCopilote("fichierJSON/configNeuronRyley.json",
                                    "fichierJSON/configNeuronSix.json",
                                    self.__demonTiger.getVersionSoft())
            assistant.active(self.__firstStart)

    def __restartConf(self,windows:ctk.CTk):
        windows.destroy()
        self.active()

    def __checkUpdate(self,arrTk:CArreraTK):
        if (self.__demonTiger.checkUpdate()):
            screen = arrTk.aTK(title="Arrera Six",resizable=False,width=500,height=350)
            imgCavas = arrTk.createArreraBackgroudImage(screen,
                                                        imageDark="asset/GUI/dark/NoConfig.png",
                                                        imageLight="asset/GUI/light/NoConfig.png",
                                                        width=500,height=350)
            labeltext = arrTk.createLabel(screen,
                                          text="Une mise à jour d'Arrera copilote est disponible. Installez-la pour bénéficier des dernières fonctionnalités.",
                                          ppolice="Arial",ptaille=20,
                                          pstyle="bold",bg="#3c2144",
                                          fg="white",pwraplength=250,
                                          justify="left")

            btnUpdate = arrTk.createButton(screen,text="Mettre a jour",ppolice="Arial",ptaille=20,
                                           pstyle="bold",bg="#3c2144",
                                           command=lambda :
                                           wb.open("https://github.com/Arrera-Software/Ryley/releases"))

            btnContinuer = arrTk.createButton(screen,text="Me rappeler plus tart",ppolice="Arial",ptaille=20,
                                              pstyle="bold",bg="#3c2144",
                                              command=lambda : screen.destroy())

            imgCavas.pack()
            labeltext.place(x=190,y=40)
            arrTk.placeBottomLeft(btnUpdate)
            arrTk.placeBottomRight(btnContinuer)
            arrTk.view()