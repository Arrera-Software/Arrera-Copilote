import time

from librairy.arrera_tk import CArreraTK
from ObjetsNetwork.arreraNeuron import *
from src.CLanguageRyley import *
import threading as th
import signal
from setting.CArreraGazelleUIRyleyCopilote import *

VERSION = "I2025-1.00"

class guiRyley:
    def __init__(self, neuronConfigFile: str,version: str):
        # Varriable
        self.__nameSoft = "Arrera RYLEY"
        self.__version = version
        self.__codeHelpActived = False
        self.__litleWindowsActived = False
        # Boot ArreraTK
        self.__arrTK = CArreraTK()

        # Demarage Neuron Network
        self.__assistantRyley = ArreraNetwork(neuronConfigFile)

        # Demarage objet language Ryley
        self.__language = CLanguageRyley("fichierJSON/paroleRyley.json",
                                              "fichierJSON/aideRyley.json",
                                              "fichierJSON/firstBootRyley.json")

        # Teste sur de l'OS hote
        objOS = OS()
        self.__windowsOS = objOS.osWindows()
        self.__linuxOS = objOS.osLinux()
        del objOS

        # Demarage de l'interface
        self.__screen = self.__arrTK.aTK(0,title=self.__nameSoft, resizable=False,
                                         width=500, height=600)

        self.__screen.protocol("WM_DELETE_WINDOW", self.__quitRyley)

        # Demage de l'objet parametre

        self.__arrGazelle = CArreraGazelleUIRyleyCopilote(self.__arrTK, self.__screen,
                                                          "fichierJSON/configUser.json",
                                                          "fichierJSON/configNeuron.json",
                                                          "fichierJSON/ryleyConfig.json",
                                                          "fichierJSON/configSetting.json")
        self.__arrGazelle.passApropos(self.__apropos)

        # Icon
        if self.__windowsOS:
            self.__emplacementIcon = "asset/Ryley.ico"
        else :
            self.__emplacementIcon = "asset/Ryley.png"

        # Definition des images
        emplacementLight = "asset/GUI/light/"
        emplacementDark = "asset/GUI/dark/"

        listIMG = ["top.png",#0
                   "bottom.png",#1
                   "send.png",#2
                   "settings.png",#3
                   "iconRyleyCodehelp.png",#4
                   "tableur.png",#5
                   "word.png",#6
                   "projet.png",#7
                   "bottomOpen.png",#8
                   "booting1.png",#9
                   "booting2.png",#10
                   "booting3.png",#11
                   "booting4.png",#12
                   "booting5.png",#13
                   "booting6.png",#14
                   "actu.png",#15
                   "firstBoot.png",#16
                   "bottomCodeHelp.png",#17
                   "topCodehelp.png",#18
                   "btnColorSelector.png",#19
                   "btnGestGithub.png",#20
                    "btnLibrairy.png",#21
                    "btnOrgaVar.png",#22
                   "litlewindows.png",#23
                   "btnbigwindows.png",#24
                   "btnlittlewindows.png"#25
                   ]
        # Creation des images

        imgSend = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[2],
                                           pathDark=emplacementDark + listIMG[2],
                                           tailleX=30, tailleY=30)
        imgPara = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[3],
                                             pathDark=emplacementDark + listIMG[3],
                                             tailleX=30, tailleY=30)

        imgCodehelp = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[4],
                                             pathDark=emplacementDark + listIMG[4],
                                             tailleX=30, tailleY=30)

        imgRyley = self.__arrTK.createImage(pathLight=self.__emplacementIcon,
                                            pathDark=self.__emplacementIcon,
                                            tailleX=30, tailleY=30)

        imgTableurOpen = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[5],
                                                    pathDark=emplacementDark + listIMG[5],
                                                    tailleX=30, tailleY=30)
        imgWordOpen = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[6],
                                                    pathDark=emplacementDark + listIMG[6],
                                                    tailleX=30, tailleY=30)
        imgProjetOpen = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[7],
                                                    pathDark=emplacementDark + listIMG[7],
                                                    tailleX=30, tailleY=30)

        imgCHColorSelector = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[19],
                                                    pathDark=emplacementDark + listIMG[19],
                                                    tailleX=30, tailleY=30)

        imgCHGestGithub = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[20],
                                                     pathDark=emplacementDark + listIMG[20],
                                                     tailleX=30, tailleY=30)

        imgCHLibrairy = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[21],
                                                   pathDark=emplacementDark + listIMG[21],
                                                   tailleX=30, tailleY=30)

        imgCHOrgaVar = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[22],
                                                   pathDark=emplacementDark + listIMG[22],
                                                   tailleX=30, tailleY=30)

        imgBTNBigWindows = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[24],
                                                pathDark=emplacementDark + listIMG[24],
                                                tailleX=30, tailleY=30)

        imgBTNLittleWindows = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[25],
                                                pathDark=emplacementDark + listIMG[25],
                                                tailleX=30, tailleY=30)


        # Frame
        self.__topBackgrown = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + listIMG[0],
                                                                      imageDark=emplacementDark + listIMG[0],
                                                                      width=500, height=400)
        self.__bottomBackgrown = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                         imageLight=emplacementLight + listIMG[1],
                                                                         imageDark=emplacementDark + listIMG[1],
                                                                         width=500, height=70)
        self.__backgroundActu = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[15],
                                                                        imageDark=emplacementDark + listIMG[15],
                                                                        width=500, height=600)

        self.__backgroundLitleWindows = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[23],
                                                                        imageDark=emplacementDark + listIMG[23],
                                                                        width=500, height=110)

        self.__fBottomLitleWindows = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=90,
                                                         bg="#081ec7", corner_radius=0)

        self.__frameBackgroud = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=130,
                                                         bg="#081ec7",corner_radius=0)

        self.__backgroundFirstboot = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[16],
                                                                        imageDark=emplacementDark + listIMG[16],
                                                                        width=500, height=600)

        self.__bottomBackgrownOpen = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                             imageLight=emplacementLight + listIMG[8],
                                                                             imageDark=emplacementDark + listIMG[8],
                                                                             width=500, height=70,)

        self.__backgroudBoot1 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[9],
                                                                        imageDark=emplacementDark + listIMG[9],
                                                                        width=500, height=600)

        self.__backgroudBoot2 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[10],
                                                                        imageDark=emplacementDark + listIMG[10],
                                                                        width=500, height=600)
        self.__backgroudBoot3 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[11],
                                                                        imageDark=emplacementDark + listIMG[11],
                                                                        width=500, height=600)
        self.__backgroudBoot4 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[12],
                                                                        imageDark=emplacementDark + listIMG[12],
                                                                        width=500, height=600)
        self.__backgroudBoot5 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[13],
                                                                        imageDark=emplacementDark + listIMG[13],
                                                                        width=500, height=600)
        self.__backgroudBoot6 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + listIMG[14],
                                                                        imageDark=emplacementDark + listIMG[14],
                                                                        width=500, height=600)

        self.__backgroundTopCodehelp = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + listIMG[18],
                                                                      imageDark=emplacementDark + listIMG[18],
                                                                      width=500, height=400)
        self.__backgroundBottomCodehelp = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                             imageLight=emplacementLight + listIMG[17],
                                                                             imageDark=emplacementDark + listIMG[17],
                                                                             width=500, height=70)
        self.__frameBackgroudCodehelp = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=130,
                                                         bg="#656565", corner_radius=0)

        fDockCodeHelpApp = self.__arrTK.createFrame(self.__frameBackgroudCodehelp, width=350, height=45, bg="#656565")
        fDockCodeHelpAppRight = self.__arrTK.createFrame(fDockCodeHelpApp, width=175, height=45, bg="#656565")
        fDockCodeHelpAppleft = self.__arrTK.createFrame(fDockCodeHelpApp, width=175, height=45, bg="#656565")


        # Widget
        # Entry
        self.__entryUserRyley = self.__arrTK.createEntry(self.__frameBackgroud,
                                                         ppolice="Arial", ptaille=25, width=350)

        self.__entryUserCodehelp = self.__arrTK.createEntry(self.__frameBackgroudCodehelp,
                                                         ppolice="Arial", ptaille=25, width=350)

        self.__entryUserLittle = self.__arrTK.createEntry(self.__fBottomLitleWindows,
                                                        ppolice="Arial", ptaille=25, width=350)

        # Bouton
        # Partie Ryley
        btnSendRyley = self.__arrTK.createButton(self.__frameBackgroud, image=imgSend,
                                                 width=40, height=40, command=self.__actionBTNRyley,
                                                 bg="#3b4bca", hoverbg="#051484")

        btnParaRyley = self.__arrTK.createButton(self.__frameBackgroud,image=imgPara,
                                            width=40, height=40,command=self.__viewParametre,
                                            bg="#3b4bca",hoverbg="#051484")

        btnCodehelp = self.__arrTK.createButton(self.__frameBackgroud,image=imgCodehelp,
                                                width=40,height=40,command=self.__modeCodehelp,
                                                bg="#3b4bca", hoverbg="#051484")
        btnLittleWindows = self.__arrTK.createButton(self.__frameBackgroud,image=imgBTNLittleWindows,
                                                       width=40,height=40,command=self.__modeLittleWindows,
                                                       bg="#3b4bca", hoverbg="#051484")
        # Btn open

        self.__btnTableurOpenRyley = self.__arrTK.createButton(self.__bottomBackgrownOpen, width=35, height=35,
                                                               image=imgTableurOpen,
                                                               command=lambda: self.__winHelpFileAndProjet(1),
                                                               bg="#3b4bca", hoverbg="#051484")

        self.__btnWordOpenRyley = self.__arrTK.createButton(self.__bottomBackgrownOpen, width=35, height=35,
                                                            image=imgWordOpen,
                                                            command=lambda: self.__winHelpFileAndProjet(2),
                                                            bg="#3b4bca", hoverbg="#051484")

        self.__btnProjetOpenRyley = self.__arrTK.createButton(self.__bottomBackgrownOpen, width=35, height=35,
                                                              image=imgProjetOpen,
                                                              command=lambda: self.__winHelpFileAndProjet(3),
                                                              bg="#3b4bca", hoverbg="#051484")

        # Partie Codehelp
        btnSendCodehelp = self.__arrTK.createButton(self.__frameBackgroudCodehelp, image=imgSend,
                                                    width=40, height=40, command=self.__actionBTNCodehelp,
                                                    bg="#8c8c8c", hoverbg="#4e4e4e")

        btnParaCodehelp = self.__arrTK.createButton(self.__frameBackgroudCodehelp, image=imgPara,
                                                 width=40, height=40, command=self.__viewParametre,
                                                 bg="#8c8c8c", hoverbg="#4e4e4e")

        btnRyley = self.__arrTK.createButton(self.__frameBackgroudCodehelp, image=imgRyley,
                                                width=40, height=40,command=self.__modeRyley,
                                                bg="#8c8c8c", hoverbg="#4e4e4e")

        btnCHOrgaVar = self.__arrTK.createButton(fDockCodeHelpAppRight, width=40,height=40,
                                                 image=imgCHOrgaVar,command=self.__activeOrgaVar,
                                                 bg="#8c8c8c", hoverbg="#4e4e4e")

        btnCHColorSelecteur = self.__arrTK.createButton(fDockCodeHelpAppRight,  width=40,height=40,
                                                 image=imgCHColorSelector,command=self.__activeColorSelecteur,
                                                 bg="#8c8c8c", hoverbg="#4e4e4e")

        btnCHGestGit = self.__arrTK.createButton(fDockCodeHelpAppleft,  width=40,height=40,
                                                 image=imgCHGestGithub,command=self.__activeGestGit,
                                                 bg="#8c8c8c", hoverbg="#4e4e4e")

        btnCHLibrairy = self.__arrTK.createButton(fDockCodeHelpAppleft,  width=40,height=40,
                                                 image=imgCHLibrairy,command=self.__activeLibrairy,
                                                 bg="#8c8c8c", hoverbg="#4e4e4e")



        # Btn open

        self.__btnTableurOpenCodehelp = self.__arrTK.createButton(self.__backgroundBottomCodehelp, width=35, height=35,
                                                               image=imgTableurOpen,
                                                               command=lambda: self.__winHelpFileAndProjet(1),
                                                               bg="#8c8c8c", hoverbg="#4e4e4e")

        self.__btnWordOpenCodehelp = self.__arrTK.createButton(self.__backgroundBottomCodehelp, width=35, height=35,
                                                            image=imgWordOpen,
                                                            command=lambda: self.__winHelpFileAndProjet(2),
                                                            bg="#8c8c8c", hoverbg="#4e4e4e")

        self.__btnProjetOpenCodehelp = self.__arrTK.createButton(self.__backgroundBottomCodehelp, width=35, height=35,
                                                              image=imgProjetOpen,
                                                              command=lambda: self.__winHelpFileAndProjet(3),
                                                              bg="#8c8c8c", hoverbg="#4e4e4e")

        # Partie litle windows

        # Bouton open

        self.__btnTableurOpenLittle = self.__arrTK.createButton(self.__fBottomLitleWindows, width=35, height=35,
                                                               image=imgTableurOpen,
                                                               command=lambda: self.__winHelpFileAndProjet(1),
                                                               bg="#3b4bca", hoverbg="#051484")

        self.__btnWordOpenLitte = self.__arrTK.createButton(self.__fBottomLitleWindows, width=35, height=35,
                                                            image=imgWordOpen,
                                                            command=lambda: self.__winHelpFileAndProjet(2),
                                                            bg="#3b4bca", hoverbg="#051484")

        self.__btnProjetOpenLitte = self.__arrTK.createButton(self.__backgroundLitleWindows, width=35, height=35,
                                                              image=imgProjetOpen,
                                                              command=lambda: self.__winHelpFileAndProjet(3),
                                                              bg="#3b4bca", hoverbg="#051484")

        # Button

        btnSendLittle = self.__arrTK.createButton(self.__fBottomLitleWindows, image=imgSend,
                                                 width=40, height=40, command=self.__actionBTNRyley,
                                                 bg="#3b4bca", hoverbg="#051484")

        btnBigWindows = self.__arrTK.createButton(self.__fBottomLitleWindows,image=imgBTNBigWindows,
                                                     width=40,height=40,command=self.__modeBigWindows,
                                                     bg="#3b4bca", hoverbg="#051484")


        # Partie actu
        btnQuitActu = self.__arrTK.createButton(self.__backgroundActu, text="Retour",
                                                command=self.__backActu)

        # Label
        self.__lparoleRyley = self.__arrTK.createLabel(self.__topBackgrown,
                                                       bg="#041f75", fg="white",
                                                       ppolice="Arial", pstyle="bold",
                                                       ptaille=18, justify="left", pwraplength=400)

        self.__lparoleCodehelp = self.__arrTK.createLabel(self.__backgroundTopCodehelp,
                                                       bg="#041f75", fg="white",
                                                       ppolice="Arial", pstyle="bold",
                                                       ptaille=18, justify="left", pwraplength=400)

        self.__lparoleLittle = self.__arrTK.createLabel(self.__backgroundLitleWindows,
                                                        bg="#041f75", fg="white",
                                                        ppolice="Arial", pstyle="bold",
                                                        ptaille=18, justify="left", pwraplength=350)

        self.__labelActu = self.__arrTK.createLabel(self.__backgroundActu,
                                                    bg="#041f75", fg="white",
                                                    ppolice="Arial", pstyle="bold",
                                                    ptaille=18, justify="left", pwraplength=400)

        self.__labelFirstBoot = self.__arrTK.createLabel(self.__backgroundFirstboot,pwraplength=300,
                                                        bg="#041f75", fg="white",ptaille=20,
                                                        ppolice="Arial", pstyle="bold",justify="left")

        # Affichage des widgets
        self.__entryUserRyley.place(relx=0.40, rely=0.3, anchor="center")
        btnSendRyley.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparoleRyley.place(x=55, y=280)

        self.__arrTK.placeBottomLeft(btnParaRyley)
        self.__arrTK.placeBottomRight(btnCodehelp)

        self.__entryUserCodehelp.place(relx=0.40, rely=0.3, anchor="center")
        btnSendCodehelp.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparoleCodehelp.place(x=55, y=280)

        self.__entryUserLittle.place(relx=0.40, rely=0.3, anchor="center")
        btnSendLittle.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparoleLittle.place(x=95, y=10)

        self.__arrTK.placeBottomCenter(btnBigWindows)

        self.__arrTK.placeBottomLeft(btnParaCodehelp)
        self.__arrTK.placeBottomRight(btnRyley)
        self.__arrTK.placeBottomCenter(btnLittleWindows)

        self.__labelActu.place(x=70, y=75)
        self.__labelFirstBoot.place(x=70, y=190)
        self.__arrTK.placeBottomRight(btnQuitActu)

        self.__arrTK.placeRightBottom(btnCHColorSelecteur)
        self.__arrTK.placeBottomCenter(btnCHOrgaVar)

        self.__arrTK.placeBottomLeft(btnCHGestGit)
        self.__arrTK.placeBottomCenter(btnCHLibrairy)

        self.__arrTK.placeBottomRight(fDockCodeHelpAppRight)
        self.__arrTK.placeBottomLeft(fDockCodeHelpAppleft)
        self.__arrTK.placeBottomCenter(fDockCodeHelpApp)
        # Bind
        self.__keyboard()


    def active(self, firstStart: bool):
        if firstStart :
            thboot = th.Thread(target=self.__sequenceFirstBoot)
        else :
            thboot = th.Thread(target=self.__sequenceBoot)

        thboot.start()
        self.__arrTK.view()

    def __sequenceBoot(self):
        self.__disableAllFrame()
        self.__backgroudBoot1.pack()
        time.sleep(0.2)
        self.__backgroudBoot1.pack_forget()
        self.__backgroudBoot2.pack()
        time.sleep(0.2)
        self.__backgroudBoot2.pack_forget()
        self.__backgroudBoot3.pack()
        time.sleep(0.2)
        self.__backgroudBoot3.pack_forget()
        self.__backgroudBoot4.pack()
        time.sleep(0.2)
        self.__backgroudBoot4.pack_forget()
        self.__backgroudBoot5.pack()
        time.sleep(0.2)
        self.__backgroudBoot5.pack_forget()
        self.__paroleRyley(self.__assistantRyley.boot(2))
        self.__viewNormal()
        self.setButtonOpen()

    def __sequenceFirstBoot(self):
        self.__disableAllFrame()
        self.__backgroudBoot1.pack()
        time.sleep(0.2)
        self.__backgroudBoot1.pack_forget()
        self.__backgroudBoot2.pack()
        time.sleep(0.2)
        self.__backgroudBoot2.pack_forget()
        self.__backgroudBoot3.pack()
        time.sleep(0.2)
        self.__backgroudBoot3.pack_forget()
        self.__backgroudBoot4.pack()
        time.sleep(0.2)
        self.__backgroudBoot4.pack_forget()
        self.__backgroudBoot5.pack()
        time.sleep(0.2)
        self.__backgroudBoot5.pack_forget()
        self.__backgroundFirstboot.pack()
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(1))
        time.sleep(3)
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(2))
        time.sleep(3)
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(3))
        time.sleep(3)
        self.__paroleRyley(self.__assistantRyley.boot(2))
        self.__disableAllFrame()
        self.__viewNormal()
        self.setButtonOpen()

    def __sequenceStop(self):
        self.__screen.configure(bg_color="#081ec7", fg_color="#081ec7")
        self.__paroleRyley(self.__assistantRyley.shutdown())
        time.sleep(3)
        self.__screen.configure(bg_color="white", fg_color="white")
        self.__disableAllFrame()
        self.__backgroudBoot5.pack()
        time.sleep(0.2)
        self.__backgroudBoot5.pack_forget()
        self.__backgroudBoot4.pack()
        time.sleep(0.2)
        self.__backgroudBoot4.pack_forget()
        self.__backgroudBoot3.pack()
        time.sleep(0.2)
        self.__backgroudBoot3.pack_forget()
        self.__backgroudBoot2.pack()
        time.sleep(0.2)
        self.__backgroudBoot2.pack_forget()
        self.__backgroudBoot1.pack()
        if (self.__windowsOS==True) and (self.__linuxOS==False) :
            os.kill(os.getpid(), signal.SIGINT)
        else :
            if (self.__windowsOS==False) and (self.__linuxOS==True) :
                os.kill(os.getpid(), signal.SIGKILL)


    def __disableAllFrame(self):
        self.__topBackgrown.pack_forget()
        self.__bottomBackgrown.pack_forget()
        self.__frameBackgroud.pack_forget()
        self.__bottomBackgrownOpen.pack_forget()
        self.__backgroundActu.pack_forget()
        self.__backgroundFirstboot.pack_forget()
        self.__backgroundTopCodehelp.pack_forget()
        self.__backgroundBottomCodehelp.pack_forget()
        self.__frameBackgroudCodehelp.pack_forget()
        self.__backgroundLitleWindows.pack_forget()
        self.__fBottomLitleWindows.pack_forget()

    def __viewNormal(self):
        self.__topBackgrown.pack()
        self.__bottomBackgrown.pack()
        self.__frameBackgroud.pack()

    def __viewOpen(self):
        self.__topBackgrown.pack()
        self.__bottomBackgrownOpen.pack()
        self.__frameBackgroud.pack()

    def __viewCodehelp(self):
        self.__backgroundTopCodehelp.pack()
        self.__backgroundBottomCodehelp.pack()
        self.__frameBackgroudCodehelp.pack()

    def __modeRyley(self):
        self.__codeHelpActived = False
        self.__disableAllFrame()
        self.__viewNormal()
        self.setButtonOpen()

    def __modeCodehelp(self):
        self.__codeHelpActived = True
        if self.__litleWindowsActived:
            self.__modeBigWindows()
        self.__disableAllFrame()
        self.__paroleCodehelp(self.__language.getPhActiveCodehelp())
        self.__viewCodehelp()
        self.setButtonOpen()

    def __paroleRyley(self, text: str):
        if text != "":
            self.__lparoleRyley.configure(text=text)
            self.__entryUserRyley.delete(0, END)

    def __paroleCodehelp(self, text: str):
        if text != "":
            self.__lparoleCodehelp.configure(text=text)
            self.__entryUserCodehelp.delete(0, END)

    def __paroleLittle(self, text: str):
        if text != "":
            self.__lparoleLittle.configure(text=text)
            self.__entryUserLittle.delete(0, END)

    def __quitRyley(self):
        if (askyesno("Atention", "Voulez-vous vraiment fermer Ryley")):
            self.__close()

    def __close(self):
        if self.__litleWindowsActived:
            self.__modeBigWindows()
        self.__disableAllFrame()
        self.__viewNormal()
        self.__frameBackgroud.pack_forget()
        thSTop = th.Thread(target=self.__sequenceStop)
        thSTop.start()

    def __apropos(self):
        self.__arrTK.aproposWindows(
            nameSoft=self.__nameSoft,
            iconFile=self.__emplacementIcon,
            version=self.__version,
            copyright="Copyright Arrera Software by Baptiste P 2023-2025",
            linkSource="https://github.com/Arrera-Software/Ryley",
            linkWeb="https://arrera-software.fr/")

    def __actionBTNRyley(self):
        texte = self.__entryUserRyley.get().lower()
        self.__entryUserRyley.delete(0, END)
        self.__paroleRyley(self.__sendAssistant(texte))

    def __actionBTNCodehelp(self):
        texte = self.__entryUserCodehelp.get().lower()
        self.__entryUserCodehelp.delete(0, END)
        self.__paroleCodehelp(self.__sendAssistant(texte))

    def __actionBTNLitleWindows(self):
        texte = self.__entryUserLittle.get().lower()
        self.__entryUserLittle.delete(0, END)
        self.__paroleLittle(self.__sendAssistant(texte))

    def __sendAssistant(self, texte:str):
        out = ""
        texte = texte.lower()
        if ("mode normal" in texte and self.__litleWindowsActived == True):
            self.__modeBigWindows()
            return
        else :
            if ("mode petit" in texte or "mode discret" in texte and self.__litleWindowsActived == False):
                self.__modeLittleWindows()
                return
            else :
                if ("parametre" in texte):
                    self.__viewParametre()
                else:
                    if ("codehelp" in texte):
                        self.__modeCodehelp()
                        return
                    else:
                        self.__assistantRyley.neuron(texte)
                        nbSortie = self.__assistantRyley.getValeurSortie()
                        listSortie = self.__assistantRyley.getListSortie()
                        match nbSortie:
                            case 0:
                                out = listSortie[0]
                            case 1:
                                out =listSortie[0]
                            case 2:
                                out = "error"
                            case 3:
                                out = self.__language.getPhOpenActu()
                                self.__viewResumer(listSortie, 2)
                            case 4:
                                out = listSortie[0]
                            case 5:
                                out = listSortie[0]
                            case 6:
                                out = self.__language.getPhErreurActu()
                            case 7:
                                out = listSortie[0]
                                self.setButtonOpen()
                            case 8:
                                out = listSortie[0]
                                self.setButtonOpen()
                            case 9:
                                out = self.__language.getPhReadWord()
                                self.__windowsReadFile(listSortie, 2)
                            case 10:
                                out = listSortie[0]
                                self.setButtonOpen()
                            case 11:
                                 out = self.__language.getPhErreurResumerActu()
                            case 12:
                                out = self.__language.getPhResumerActu()
                                self.__viewResumer(listSortie, 1)
                            case 13:
                                out = self.__language.getPhReadTableur()
                                self.__windowsReadFile(listSortie, 1)
                            case 14:
                                out = listSortie[0]
                                self.setButtonOpen()
                            case 15:
                                self.__close()
                            case 16:
                                out = self.__assistantRyley.shutdown()
                            case 17:
                                out = ""
                                self.__windowsHelp(listSortie)
                            case 18:
                                out = self.__language.getPhResumerAgenda()
                                self.__viewResumer(listSortie, 3)
                            case 19:
                                out = self.__language.getPhResumerAll()
                                self.__viewResumer(listSortie, 4)
                            case 20:
                                out = self.__language.getPhErreurResumerAll()
                            case 21:
                                out = listSortie[0]
                                self.setButtonOpen()
                            case other:
                                out = ""
            return out

    def __keyboard(self):
        def anychar(event):
            if self.__windowsOS:
                if event.keycode == 13:
                    self.__actionBTNRyley()
                    self.__actionBTNCodehelp()
                    self.__actionBTNLitleWindows()
            else:
                if event.keycode == 36:
                    self.__actionBTNRyley()
                    self.__actionBTNCodehelp()
                    self.__actionBTNLitleWindows()
        self.__screen.bind("<Key>", anychar)

    def setButtonOpen(self):
        tableur = self.__assistantRyley.getTableur()
        word = self.__assistantRyley.getWord()
        projet = self.__assistantRyley.getProject()

        if tableur :
            self.__arrTK.placeTopRight(self.__btnTableurOpenRyley)
            self.__arrTK.placeBottomRight(self.__btnTableurOpenCodehelp)
            self.__arrTK.placeBottomLeft(self.__btnTableurOpenLittle)
        else :
            self.__btnTableurOpenRyley.place_forget()
            self.__btnTableurOpenCodehelp.place_forget()
            self.__btnTableurOpenLittle.place_forget()

        if word:
            self.__arrTK.placeTopLeft(self.__btnWordOpenRyley)
            self.__arrTK.placeBottomLeft(self.__btnWordOpenCodehelp)
            self.__arrTK.placeBottomRight(self.__btnWordOpenLitte)
        else :
            self.__btnWordOpenRyley.place_forget()
            self.__btnWordOpenCodehelp.place_forget()
            self.__btnWordOpenLitte.place_forget()

        if projet:
            self.__arrTK.placeTopCenter(self.__btnProjetOpenRyley)
            self.__arrTK.placeBottomCenter(self.__btnProjetOpenCodehelp)
            self.__arrTK.placeBottomLeft(self.__btnProjetOpenLitte)
        else :
            self.__btnProjetOpenRyley.place_forget()
            self.__btnProjetOpenCodehelp.place_forget()
            self.__btnProjetOpenLitte.place_forget()

        if self.__codeHelpActived == False:
            if tableur or word or projet :
                self.__disableAllFrame()
                self.__viewOpen()
            else :
                self.__disableAllFrame()
                self.__viewNormal()

    def __winHelpFileAndProjet(self, mode: int):
        """
        :param mode:
            1. Tableur
            2. Word
            3. Projet
        :return:
        """
        winHelp = self.__arrTK.aTopLevel(width=500, height=600,
                                         resizable=False,
                                         icon=self.__emplacementIcon)

        labelTitleHelp = self.__arrTK.createLabel(winHelp, ppolice="Arial", ptaille=25, pstyle="bold")
        aideView = self.__arrTK.createTextBox(winHelp, width=475, height=500,
                                              wrap="word", ppolice="Arial",
                                              ptaille=20, pstyle="normal")
        match mode:
            case 1:
                winHelp.title("Arrera Ryley : Aide Tableur")
                labelTitleHelp.configure(text="Aide Tableur")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpTableur()))
            case 2:
                winHelp.title("Arrera Ryley : Aide Traitement de texte")
                labelTitleHelp.configure(text="Aide Traitement de texte")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpWord()))
            case 3:
                winHelp.title("Arrera Ryley : Aide Arrera Projet")
                labelTitleHelp.configure(text="Aide Arrera Projet")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpProjet()))

        self.__arrTK.placeTopCenter(labelTitleHelp)
        self.__arrTK.placeCenter(aideView)

    def __traitementTextHelpFileAndProjet(self, liste:list):
        newText = ""
        for i in range(0, len(liste)):
            text = liste[i]
            if text[0] == "-" :
                text = text.replace("-", "").strip().lstrip()
                newText += "\n"+text+"\n"
            else :
                if text[0]== "*":
                    text = text.replace("*","").strip().lstrip()
                    newText += "    "+text+"\n"

        return newText.strip()

    def __viewResumer(self, listSortie:list, mode:int):
        """
        1 : Resumer actualités
        2 : actuliés
        3 : Resumer agenda
        4 : Resumer totale
        """
        self.__disableAllFrame()
        self.__backgroundActu.pack()
        match mode :
            case 1 :
                self.__labelActu.configure(text=listSortie[0]+
                                        "\n"+listSortie[1]+
                                        "\n"+listSortie[2]+
                                        "\n"+listSortie[3]+
                                        "\n"+listSortie[4]+
                                        "\n"+listSortie[5],
                                        justify="left",
                                        wraplength=400)
            case 2 :
                self.__labelActu.configure(text=listSortie[0]+
                                        "\n"+listSortie[1]+
                                        "\n"+listSortie[2],
                                        justify="left",
                                        wraplength=400)
            case 3 :
                self.__labelActu.configure(text=listSortie[0]+"\n"+listSortie[1],
                                        justify="left",
                                        wraplength=400)
            case 4 :
                self.__labelActu.configure(text=listSortie[0] + "\n" + listSortie[1]+"\n"
                                                +listSortie[2] + "\n" + listSortie[3]+"\n"
                                                +listSortie[4] + "\n" + listSortie[5]+"\n"
                                                +listSortie[7] + "\n" + listSortie[8],
                                           justify="left",
                                           wraplength=400)

    def __backActu(self):
        self.__disableAllFrame()
        self.__viewNormal()

    def __windowsHelp(self, list: list):
        winHelp = self.__arrTK.aTopLevel(width=500, height=600,
                                         title="Arrera RYLEY : Aide",
                                         resizable=False,
                                         icon=self.__emplacementIcon)
        labelTitleHelp = self.__arrTK.createLabel(winHelp, ppolice="Arial", ptaille=25, pstyle="bold")
        aideView = self.__arrTK.createTextBox(winHelp, width=450, height=500,
                                              wrap="word", ppolice="Arial",
                                              ptaille=20, pstyle="normal")
        self.__arrTK.insertTextOnTextBox(aideView, list[0])

        textSpeak = ""

        match list[1]:
            case "tableur":
                textSpeak = self.__language.getPhOpenAideTableur()
                labelTitleHelp.configure(text="Aide Tableur")
            case "word":
                textSpeak = self.__language.getPhOpenAideWord()
                labelTitleHelp.configure(text="Aide Traitement de texte")
            case "fichier":
                textSpeak = self.__language.getPhOpenAideFichier()
                labelTitleHelp.configure(text="Types créables par Arrera RYLEY")
            case "radio":
                textSpeak = self.__language.getPhOpenAideRadio()
                labelTitleHelp.configure(text="Radio disponible avec Arrera RYLEY")
            case "projet" :
                textSpeak = self.__language.getPhOpenAideProjet()
                labelTitleHelp.configure(text="Aide Arrera Projet")
            case "work" :
                textSpeak = self.__language.getPhOpenAideWork()
                labelTitleHelp.configure(text="Aide fonction Arrera Work")

        self.__arrTK.placeTopCenter(labelTitleHelp)
        self.__arrTK.placeCenter(aideView)
        self.__paroleRyley(textSpeak)

    def __windowsReadFile(self, liste:list, mode:int):
        """
        :param mode:
        1. Tableur
        2. Word
        :return:
        """
        winRead = self.__arrTK.aTopLevel(width=500, height=600,
                                         resizable=False,
                                         icon=self.__emplacementIcon)

        labelTitleRead = self.__arrTK.createLabel(winRead, ppolice="Arial", ptaille=25, pstyle="bold")

        content = self.__arrTK.createTextBox(winRead, width=475, height=500,
                                             wrap="word", ppolice="Arial",
                                             ptaille=20, pstyle="normal")


        match mode :
            case 1 :
                winRead.title("Arrera RYLEY : Lecture Tableur")
                labelTitleRead.configure(text="Lecture : Tableur")
                textContent = ""
                for i in range(0, len(liste)):
                    textContent = textContent+str(liste[i]) + "\n"
                self.__arrTK.insertTextOnTextBox(content, textContent)

            case 2 :
                winRead.title("Arrera RYLEY : Lecture Traitement de texte")
                labelTitleRead.configure(text="Lecture : Traitement de texte")
                self.__arrTK.insertTextOnTextBox(content, liste[0])

        self.__arrTK.placeCenter(content)
        self.__arrTK.placeTopCenter(labelTitleRead)

    def __viewParametre(self):
        self.__disableAllFrame()
        self.__arrGazelle.active()
        self.__arrGazelle.passQUITFNC(self.__quitParametre)

    def __quitParametre(self):
        self.__screen.protocol("WM_DELETE_WINDOW", self.__quitRyley)
        self.__screen.maxsize(500, 600)
        self.__viewNormal()
        self.__paroleRyley(self.__language.getPhParametre())

    def __activeOrgaVar(self):
        self.__paroleCodehelp(self.__sendAssistant("ouvre orga var"))

    def __activeColorSelecteur(self):
        self.__paroleCodehelp(self.__sendAssistant("ouvre color selecteur"))

    def __activeGestGit(self):
        self.__paroleCodehelp(self.__sendAssistant("ouvre gest github"))

    def __activeLibrairy(self):
        self.__paroleCodehelp(self.__sendAssistant("ouvre librairy"))

    def __modeLittleWindows(self):
        self.__disableAllFrame()
        self.__screen.maxsize(500, 200)
        self.__screen.minsize(500, 200)
        self.__paroleLittle(self.__language.getPhActiveModeLitle())
        self.__backgroundLitleWindows.pack()
        self.__fBottomLitleWindows.pack()
        self.__litleWindowsActived = True

    def __modeBigWindows(self):
        self.__disableAllFrame()
        self.__screen.maxsize(500, 600)
        self.__screen.minsize(500, 600)
        self.__paroleRyley(self.__language.getPhActiveModeNormal())
        self.__viewNormal()
        self.__litleWindowsActived = False