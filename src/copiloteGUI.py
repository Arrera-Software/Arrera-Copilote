from ObjetsNetwork.arreraNeuron import *
from guiWork.canwork import *
from src.CLanguageCopilote import *
import signal
from setting.CArreraGazelleUIRyleyCopilote import *
from src.arrera_voice import *
import threading as th

VERSION = "I2025-1.00"

class guiCopilote:
    def __init__(self, neuronConfigFileRyley: str, neuronConfigFileSix: str, version: str):
        # Varriable
        self.__nameSoft = "Arrera Copilote"
        self.__version = version
        # Argument pour l'interface
        self.__codeHelpActived = False
        self.__litleWindowsActived = 0
        self.__fileOpen = False
        # arguments sons micro 
        self.__soundState = False
        self.__microState = False
        self.__microTrigger = False
        self.__is_listening = False

        # Boot ArreraTK
        self.__arrTK = CArreraTK()

        # Arrera Voice
        self.__arrVoice = CArreraVoice(jsonWork("fichierJSON/copiloteConfig.json"))

        #Theard de parole
        self.__threadParoleCopilote = th.Thread()
        self.__theardMicrophone = th.Thread()
        self.__threadSpeaking = False

        # Demarage Neuron Network
        self.__assistantRyley = ArreraNetwork(neuronConfigFileRyley)
        self.__assistantSix = ArreraNetwork(neuronConfigFileSix)

        # Atribut pour les sortie des neuron
        self.__listSortieRyley = []
        self.__listSortieSix = []
        self.__outSpecial= ""

        self.__neuronUsedSix = ""
        self.__neuronUsedRyley = ""

        self.__nbSortieSix = 0
        self.__nbSortieRyley = 0

        # Demarage objet language Ryley
        self.__language = CLanguageCopilote("language/copilote/paroleCopilote.json",
                                            "language/copilote/paroleSix.json",
                                            "language/copilote/paroleRyley.json",
                                              "fichierJSON/aideRyley.json",
                                              "fichierJSON/firstBootCopilote.json",
                                            "fichierJSON/configUser.json")

        # Teste sur de l'OS hote
        objOS = OS()
        self.__windowsOS = objOS.osWindows()
        self.__linuxOS = objOS.osLinux()
        self.__macOS = objOS.osMac()
        del objOS

        # Demarage de l'interface

        if self.__windowsOS and not self.__linuxOS:
            self.__emplacementIcon = "asset/icon.ico"
        elif not self.__windowsOS and self.__linuxOS :
            self.__emplacementIcon = "asset/icon.png"
        elif self.__macOS :
            self.__emplacementIcon = "asset/icon-macos.png"

        self.__screen = self.__arrTK.aTK(0,title=self.__nameSoft, resizable=False,
                                         width=500, height=600,icon=self.__emplacementIcon)

        self.__screen.protocol("WM_DELETE_WINDOW", self.__quitCopilote)

        # Demage de l'objet parametre

        self.__arrGazelle = CArreraGazelleUIRyleyCopilote(self.__arrTK, self.__screen,
                                                          "fichierJSON/configUser.json",
                                                          "fichierJSON/configNeuron.json",
                                                          "fichierJSON/copiloteConfig.json",
                                                          "fichierJSON/configSetting.json")
        self.__arrGazelle.passApropos(self.__apropos)

        # Definition des images
        emplacementLight = "asset/GUI/light/"
        emplacementDark = "asset/GUI/dark/"

        # Interface aide pour Arrera Work
        self.__guiWork = CAnWorkGUI(self.__arrTK,
                                    self.__nameSoft,
                                    "asset/work",
                                    self.__assistantSix,
                                    jsonWork(neuronConfigFileSix).lectureJSON("fileUser"))

        # Creation des images

        imgSend = self.__arrTK.createImage(pathLight=emplacementLight + "send.png",
                                           pathDark=emplacementDark + "send.png",
                                           tailleX=30, tailleY=30)
        imgPara = self.__arrTK.createImage(pathLight=emplacementLight + "settings.png",
                                             pathDark=emplacementDark + "settings.png",
                                             tailleX=30, tailleY=30)

        imgCodehelp = self.__arrTK.createImage(pathLight=emplacementLight + "iconRyleyCodehelp.png",
                                             pathDark=emplacementDark + "iconRyleyCodehelp.png",
                                             tailleX=30, tailleY=30)

        imgCopilote = self.__arrTK.createImage(pathLight=self.__emplacementIcon,
                                               pathDark=self.__emplacementIcon,
                                               tailleX=30, tailleY=30)

        imgSix = self.__arrTK.createImage(pathLight="asset/six.png",pathDark="asset/six.png",
                                          tailleX=75, tailleY=75)
        imgRyley = self.__arrTK.createImage(pathLight="asset/ryley.png",pathDark="asset/ryley.png",
                                            tailleX=75, tailleY=75)
        imgCancel = self.__arrTK.createImage(pathLight=emplacementLight +"cancel.png",
                                             pathDark=emplacementDark +"cancel.png",
                                             tailleX=75, tailleY=75)

        imgTableurOpen = self.__arrTK.createImage(pathLight=emplacementLight + "tableur.png",
                                                    pathDark=emplacementDark + "tableur.png",
                                                    tailleX=30, tailleY=30)
        imgWordOpen = self.__arrTK.createImage(pathLight=emplacementLight + "word.png",
                                                    pathDark=emplacementDark + "word.png",
                                                    tailleX=30, tailleY=30)
        imgProjetOpen = self.__arrTK.createImage(pathLight=emplacementLight + "projet.png",
                                                    pathDark=emplacementDark + "projet.png",
                                                    tailleX=30, tailleY=30)
        imgBTNGUIWork = self.__arrTK.createImage(pathLight=emplacementLight + "work.png",
                                                    pathDark=emplacementDark + "work.png",
                                                    tailleX=30, tailleY=30)

        imgCHColorSelector = self.__arrTK.createImage(pathLight=emplacementLight + "btnColorSelector.png",
                                                    pathDark=emplacementDark + "btnColorSelector.png",
                                                    tailleX=30, tailleY=30)

        imgCHGestGithub = self.__arrTK.createImage(pathLight=emplacementLight + "btnGestGithub.png",
                                                     pathDark=emplacementDark + "btnGestGithub.png",
                                                     tailleX=30, tailleY=30)

        imgCHLibrairy = self.__arrTK.createImage(pathLight=emplacementLight + "btnLibrairy.png",
                                                   pathDark=emplacementDark + "btnLibrairy.png",
                                                   tailleX=30, tailleY=30)

        imgCHOrgaVar = self.__arrTK.createImage(pathLight=emplacementLight + "btnOrgaVar.png",
                                                   pathDark=emplacementDark + "btnOrgaVar.png",
                                                   tailleX=30, tailleY=30)

        imgBTNBigWindows = self.__arrTK.createImage(pathLight=emplacementLight + "btnbigwindows.png",
                                                pathDark=emplacementDark + "btnbigwindows.png",
                                                tailleX=30, tailleY=30)

        imgBTNLittleWindows = self.__arrTK.createImage(pathLight=emplacementLight + "btnlittlewindows.png",
                                                pathDark=emplacementDark + "btnlittlewindows.png",
                                                tailleX=30, tailleY=30)

        self.__imgBtnSoundOff = self.__arrTK.createImage(pathLight=emplacementLight + "soundOff.png",
                                               pathDark=emplacementDark + "soundOff.png",
                                               tailleX=30, tailleY=30)

        self.__imgBtnMicroOff = self.__arrTK.createImage(pathLight=emplacementLight + "microOff.png",
                                               pathDark=emplacementDark + "microOff.png",
                                               tailleX=30, tailleY=30)

        self.__imgBtnSoundOn = self.__arrTK.createImage(pathLight=emplacementLight + "soundOn.png",
                                                 pathDark=emplacementDark + "soundOn.png",
                                                 tailleX=30, tailleY=30)

        self.__imgBtnMicroOn = self.__arrTK.createImage(pathLight=emplacementLight + "microOn.png",
                                                 pathDark=emplacementDark + "microOn.png",
                                                 tailleX=30, tailleY=30)
        self.__imgBtnMicroTiger = self.__arrTK.createImage(pathLight=emplacementLight + "microTriger.png",
                                                    pathDark=emplacementDark + "microTriger.png",
                                                    tailleX=30, tailleY=30)


        # Frame
        self.__homeBackgroud = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementLight + "homeScree.png",
                                                                       imageDark=emplacementDark + "homeScree.png",
                                                                       width=500, height=470)

        self.__homeBackgroudFileOpen = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                               imageLight=emplacementLight + "homeScreenOpen.png",
                                                                               imageDark=emplacementDark + "homeScreenOpen.png",
                                                                               width=500, height=470)

        self.__copiloteSpeak = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + "copiloteSpeak.png",
                                                                      imageDark=emplacementDark + "copiloteSpeak.png",
                                                                      width=500, height=470)

        self.__backgroundActu = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "actu.png",
                                                                        imageDark=emplacementDark + "actu.png",
                                                                        width=500, height=600)

        self.__backgroundLitleWindowsRyley = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                                     imageLight=emplacementLight + "litlewindows-ryley.png",
                                                                                     imageDark=emplacementDark + "litlewindows-ryley.png",
                                                                                     width=500, height=110)

        self.__backgroundLitleWindowsSix = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                                     imageLight=emplacementLight + "litlewindows-six.png",
                                                                                     imageDark=emplacementDark + "litlewindows-six.png",
                                                                                     width=500, height=110)

        self.__fChoiceLitleWindows = self.__arrTK.createFrame(self.__screen,
                                                              width=500, height=200,
                                                              bg="#482c4a", corner_radius=0)

        self.__fBottomLitleWindows = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=90,
                                                         bg="#482c4a", corner_radius=0)

        self.__frameBackgroud = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=130,
                                                         bg="#482c4a",corner_radius=0)

        self.__backgroundFirstboot = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "firstBoot.png",
                                                                        imageDark=emplacementDark + "firstBoot.png",
                                                                        width=500, height=600)



        self.__backgroudBoot1 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "booting1.png",
                                                                        imageDark=emplacementDark + "booting1.png",
                                                                        width=500, height=600)

        self.__backgroudBoot2 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "booting2.png",
                                                                        imageDark=emplacementDark + "booting2.png",
                                                                        width=500, height=600)
        self.__backgroudBoot3 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "booting3.png",
                                                                        imageDark=emplacementDark + "booting3.png",
                                                                        width=500, height=600)
        self.__backgroudBoot4 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "booting4.png",
                                                                        imageDark=emplacementDark + "booting4.png",
                                                                        width=500, height=600)
        self.__backgroudBoot5 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                        imageLight=emplacementLight + "booting5.png",
                                                                        imageDark=emplacementDark + "booting5.png",
                                                                        width=500, height=600)

        self.__backgroundTopCodehelp = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + "topCodehelp.png",
                                                                      imageDark=emplacementDark + "topCodehelp.png",
                                                                      width=500, height=400)
        self.__backgroundBottomCodehelp = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                             imageLight=emplacementLight + "bottomCodeHelp.png",
                                                                             imageDark=emplacementDark + "bottomCodeHelp.png",
                                                                             width=500, height=70)
        self.__frameBackgroudCodehelp = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=130,
                                                         bg="#656565", corner_radius=0)

        fDockCodeHelpApp = self.__arrTK.createFrame(self.__frameBackgroudCodehelp, width=350, height=45, bg="#656565")
        fDockCodeHelpAppRight = self.__arrTK.createFrame(fDockCodeHelpApp, width=175, height=45, bg="#656565")
        fDockCodeHelpAppleft = self.__arrTK.createFrame(fDockCodeHelpApp, width=175, height=45, bg="#656565")


        # Widget
        # Entry
        self.__entryUserCopilote = self.__arrTK.createEntry(self.__frameBackgroud,
                                                            ppolice="Arial", ptaille=25, width=350)

        self.__entryUserCodehelp = self.__arrTK.createEntry(self.__frameBackgroudCodehelp,
                                                         ppolice="Arial", ptaille=25, width=350)

        self.__entryUserLittle = self.__arrTK.createEntry(self.__fBottomLitleWindows,
                                                        ppolice="Arial", ptaille=25, width=350)

        # Bouton
        # Partie Ryley
        btnSendCopilote = self.__arrTK.createButton(self.__frameBackgroud, image=imgSend,
                                                 width=40, height=40, command=self.__actionBTNAcceuil,
                                                 bg="#694d6b", hoverbg="#1d1020")

        btnParaCopilote = self.__arrTK.createButton(self.__frameBackgroud,image=imgPara,
                                            width=40, height=40,command=self.__viewParametre,
                                            bg="#694d6b",hoverbg="#1d1020")

        btnCodehelp = self.__arrTK.createButton(self.__frameBackgroud,image=imgCodehelp,
                                                width=40,height=40,command=self.__modeCodehelp,
                                                bg="#694d6b", hoverbg="#1d1020")

        btnLittleWindows = self.__arrTK.createButton(self.__frameBackgroud,image=imgBTNLittleWindows,
                                                       width=40,height=40,command=self.__modeLittleWindows,
                                                       bg="#694d6b", hoverbg="#1d1020")

        btnWorkGUI = self.__arrTK.createButton(self.__frameBackgroud, image=imgBTNGUIWork,
                                                width=40, height=40, command= lambda: self.__guiWork.activeAcceuil(),
                                                bg="#694d6b", hoverbg="#1d1020")

        self.__btnSoundNormal = self.__arrTK.createButton(self.__frameBackgroud, image=self.__imgBtnSoundOff,
                                                          width=40, height=40, command = self.__actionSound,
                                                          bg="#694d6b", hoverbg="#1d1020")
        self.__btnMicroNormal = self.__arrTK.createButton(self.__frameBackgroud, image=self.__imgBtnMicroOff,
                                                          width=40, height=40,command=self.__actionMicro,
                                                          bg="#694d6b", hoverbg="#1d1020")

        btnChoiceSixLitleWin = self.__arrTK.createButton(self.__fChoiceLitleWindows,
                                                         image=imgSix,width=80,height=80
                                                         ,command=self.__modeLittleWindowsSix
                                                         ,bg="#694d6b", hoverbg="#1d1020")
        btnChoiceRyleyLitleWin = self.__arrTK.createButton(self.__fChoiceLitleWindows,
                                                           image=imgRyley,width=80,height=80
                                                           ,command=self.__modeLittleWindowsRyley
                                                           ,bg="#694d6b", hoverbg="#1d1020")
        btnChoiceCancelLitleWin = self.__arrTK.createButton(self.__fChoiceLitleWindows,
                                                            image=imgCancel,width=80,height=80
                                                            ,command=self.__cancelLittleWindows
                                                            ,bg="#694d6b", hoverbg="#1d1020")

        # Btn open

        self.__btnTableurOpenCopilote = self.__arrTK.createButton(self.__homeBackgroudFileOpen, width=35, height=35,
                                                                  image=imgTableurOpen,
                                                                  command=lambda: self.__winHelpFileAndProjet(1),
                                                                  bg="#d1d1d1", hoverbg="#585858")

        self.__btnWordOpenCopilote = self.__arrTK.createButton(self.__homeBackgroudFileOpen, width=35, height=35,
                                                               image=imgWordOpen,
                                                               command=lambda: self.__winHelpFileAndProjet(2),
                                                               bg="#d1d1d1", hoverbg="#585858")

        self.__btnProjetOpenCopilote = self.__arrTK.createButton(self.__homeBackgroudFileOpen, width=35, height=35,
                                                                 image=imgProjetOpen,
                                                                 command=lambda: self.__winHelpFileAndProjet(3),
                                                                 bg="#d1d1d1", hoverbg="#585858")

        # Partie Codehelp
        btnSendCodehelp = self.__arrTK.createButton(self.__frameBackgroudCodehelp, image=imgSend,
                                                    width=40, height=40, command=self.__actionBTNCodehelp,
                                                    bg="#8c8c8c", hoverbg="#4e4e4e")

        btnParaCodehelp = self.__arrTK.createButton(self.__frameBackgroudCodehelp, image=imgPara,
                                                 width=40, height=40, command=self.__viewParametre,
                                                 bg="#8c8c8c", hoverbg="#4e4e4e")

        btnCopilote = self.__arrTK.createButton(self.__frameBackgroudCodehelp, image=imgCopilote,
                                                width=40, height=40, command=self.__modeNormal,
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
                                                                  bg="#aaaaaa", hoverbg="#434343")

        self.__btnWordOpenCodehelp = self.__arrTK.createButton(self.__backgroundBottomCodehelp, width=35, height=35,
                                                            image=imgWordOpen,
                                                            command=lambda: self.__winHelpFileAndProjet(2),
                                                               bg="#aaaaaa", hoverbg="#434343")

        self.__btnProjetOpenCodehelp = self.__arrTK.createButton(self.__backgroundBottomCodehelp, width=35, height=35,
                                                              image=imgProjetOpen,
                                                              command=lambda: self.__winHelpFileAndProjet(3),
                                                                 bg="#aaaaaa", hoverbg="#434343")

        # Partie litle windows

        # Bouton open

        self.__btnTableurOpenLittle = self.__arrTK.createButton(self.__fBottomLitleWindows, width=35, height=35,
                                                               image=imgTableurOpen,
                                                               command=lambda: self.__winHelpFileAndProjet(1),
                                                                bg="#694d6b", hoverbg="#1d1020")

        self.__btnWordOpenLitte = self.__arrTK.createButton(self.__fBottomLitleWindows, width=35, height=35,
                                                            image=imgWordOpen,
                                                            command=lambda: self.__winHelpFileAndProjet(2),
                                                            bg="#694d6b", hoverbg="#1d1020")

        self.__btnProjetOpenLitteRyley = self.__arrTK.createButton(self.__backgroundLitleWindowsRyley, width=35, height=35,
                                                                   image=imgProjetOpen,
                                                                   command=lambda: self.__winHelpFileAndProjet(3),
                                                                   bg="#aaaaaa", hoverbg="#434343")

        self.__btnProjetOpenLitteSix = self.__arrTK.createButton(self.__backgroundLitleWindowsSix, width=35, height=35,
                                                                   image=imgProjetOpen,
                                                                   command=lambda: self.__winHelpFileAndProjet(3),
                                                                 bg="#aaaaaa", hoverbg="#434343")

        # Button

        btnSendLittle = self.__arrTK.createButton(self.__fBottomLitleWindows, image=imgSend,
                                                  width=40, height=40, command=self.__actionBTNLitleWindows,
                                                  bg="#694d6b", hoverbg="#1d1020")

        btnBigWindows = self.__arrTK.createButton(self.__fBottomLitleWindows,image=imgBTNBigWindows,
                                                     width=40,height=40,command=self.__modeBigWindows,
                                                     bg="#694d6b", hoverbg="#1d1020")

        self.__btnSoundLitle = self.__arrTK.createButton(self.__fBottomLitleWindows, image=self.__imgBtnSoundOff,
                                                          width=40, height=40, command = self.__actionSound,
                                                          bg="#694d6b", hoverbg="#1d1020")
        self.__btnMicroLitle = self.__arrTK.createButton(self.__fBottomLitleWindows, image=self.__imgBtnMicroOff,
                                                          width=40, height=40,command=self.__actionMicro,
                                                          bg="#694d6b", hoverbg="#1d1020")


        # Partie actu
        btnQuitActu = self.__arrTK.createButton(self.__backgroundActu, text="Retour",
                                                command=self.__backActu)

        # Label
        self.__lparoleRyleyNormal = self.__arrTK.createLabel(self.__homeBackgroud,
                                                             bg="#041f75", fg="white",
                                                             ppolice="Arial", pstyle="bold",
                                                             ptaille=18, justify="left", pwraplength=350)

        self.__lparoleSixNormal = self.__arrTK.createLabel(self.__homeBackgroud,
                                                           bg="#0018ff", fg="white",
                                                           ppolice="Arial", pstyle="bold",
                                                           ptaille=18, justify="left", pwraplength=350)

        self.__lparoleSixFileOpen = self.__arrTK.createLabel(self.__homeBackgroudFileOpen,
                                                             bg="#0018ff", fg="white",
                                                             ppolice="Arial", pstyle="bold",
                                                             ptaille=18, justify="left", pwraplength=350)

        self.__lparoleRyleyFileOpen = self.__arrTK.createLabel(self.__homeBackgroudFileOpen,
                                                               bg="#041f75", fg="white",
                                                               ppolice="Arial", pstyle="bold",
                                                               ptaille=18, justify="left", pwraplength=350)

        self.__lparoleCopilote = self.__arrTK.createLabel(self.__copiloteSpeak,
                                                         bg="#482c4a", fg="white",
                                                         ppolice="Arial", pstyle="bold",
                                                         ptaille=18, justify="left", pwraplength=350)

        self.__lparoleCodehelp = self.__arrTK.createLabel(self.__backgroundTopCodehelp,
                                                       bg="#482c4a", fg="white",
                                                       ppolice="Arial", pstyle="bold",
                                                       ptaille=18, justify="left", pwraplength=400)

        self.__lparoleLittleRyley = self.__arrTK.createLabel(self.__backgroundLitleWindowsRyley,
                                                             bg="#041f75", fg="white",
                                                             ppolice="Arial", pstyle="bold",
                                                             ptaille=18, justify="left", pwraplength=350)

        self.__lparoleLittleSix = self.__arrTK.createLabel(self.__backgroundLitleWindowsSix,
                                                             bg="#0018ff", fg="white",
                                                             ppolice="Arial", pstyle="bold",
                                                             ptaille=18, justify="left", pwraplength=350)

        self.__labelActu = self.__arrTK.createLabel(self.__backgroundActu,
                                                    bg="#041f75", fg="white",
                                                    ppolice="Arial", pstyle="bold",
                                                    ptaille=18, justify="left", pwraplength=400)

        self.__labelFirstBoot = self.__arrTK.createLabel(self.__backgroundFirstboot,pwraplength=300,
                                                        bg="#3c2144", fg="white",ptaille=20,
                                                        ppolice="Arial", pstyle="bold",justify="left")

        # Affichage des widgets

        self.__entryUserCopilote.place(relx=0.40, rely=0.50, anchor="center")
        btnSendCopilote.place(relx=0.90, rely=0.50, anchor="center")

        self.__lparoleRyleyNormal.place(x=120, y=160)
        self.__lparoleSixNormal.place(x=120, y=340)

        self.__lparoleRyleyFileOpen.place(x=120, y=110)
        self.__lparoleSixFileOpen.place(x=120, y=290)

        self.__lparoleCopilote.place(x=75,y=260)

        self.__arrTK.placeBottomLeft(btnParaCopilote)
        self.__arrTK.placeBottomRight(btnCodehelp)

        self.__entryUserCodehelp.place(relx=0.40, rely=0.3, anchor="center")
        btnSendCodehelp.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparoleCodehelp.place(x=55, y=280)

        self.__entryUserLittle.place(relx=0.40, rely=0.3, anchor="center")
        btnSendLittle.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparoleLittleRyley.place(x=95, y=10)
        self.__lparoleLittleSix.place(x=95, y=10)

        self.__arrTK.placeBottomCenter(btnBigWindows)

        self.__arrTK.placeBottomLeft(btnParaCodehelp)
        self.__arrTK.placeBottomRight(btnCopilote)
        self.__arrTK.placeBottomCenter(btnLittleWindows)
        self.__arrTK.placeWidgetCenteredAtBottom(self.__btnSoundNormal, -125)
        self.__arrTK.placeWidgetCenteredAtBottom(self.__btnMicroNormal, 125)

        self.__arrTK.placeTopCenter(btnWorkGUI)

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

        self.__arrTK.placeCenterLeft(btnChoiceSixLitleWin)
        self.__arrTK.placeCenterRight(btnChoiceRyleyLitleWin)
        self.__arrTK.placeCenter(btnChoiceCancelLitleWin)
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
        time.sleep(0.4)
        self.__backgroudBoot1.pack_forget()
        self.__backgroudBoot2.pack()
        time.sleep(0.4)
        self.__backgroudBoot2.pack_forget()
        self.__backgroudBoot3.pack()
        time.sleep(0.4)
        self.__backgroudBoot3.pack_forget()
        self.__backgroudBoot4.pack()
        time.sleep(0.4)
        self.__backgroudBoot4.pack_forget()
        self.__backgroudBoot5.pack()
        time.sleep(0.2)
        self.__backgroudBoot5.pack_forget()
        self.__paroleRyley(self.__assistantRyley.boot(2))
        self.__paroleSix(self.__assistantSix.boot(2))
        self.__viewNormal()

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
        self.__arrVoice.say(self.__language.getFirstBoot(1))
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(2))
        self.__arrVoice.say(self.__language.getFirstBoot(2))
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(3))
        self.__arrVoice.say(self.__language.getFirstBoot(3))
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(4))
        self.__arrVoice.say(self.__language.getFirstBoot(4))
        self.__labelFirstBoot.configure(text=self.__language.getFirstBoot(5))
        self.__arrVoice.say(self.__language.getFirstBoot(5))
        self.__paroleRyley(self.__assistantRyley.boot(2))
        self.__paroleSix(self.__assistantSix.boot(2))
        self.__disableAllFrame()
        self.__viewNormal()
        self.__setButtonOpen()

    def __sequenceStop(self):
        self.__disableAllFrame()
        self.__screen.maxsize(500, 600)
        self.__screen.minsize(500, 600)
        self.__viewNormal()
        self.__soundState = False
        self.__screen.configure(bg_color="#482c4a", fg_color="#482c4a")
        self.__paroleRyley(self.__assistantRyley.shutdown())
        self.__paroleSix(self.__assistantSix.shutdown())
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
        if self.__windowsOS and not self.__linuxOS and not self.__macOS:
            os.kill(os.getpid(), signal.SIGINT)
        elif not self.__windowsOS and self.__linuxOS or self.__macOS :
            os.kill(os.getpid(), signal.SIGKILL)


    def __disableAllFrame(self):
        self.__copiloteSpeak.pack_forget()
        self.__homeBackgroud.pack_forget()
        self.__frameBackgroud.pack_forget()
        self.__homeBackgroudFileOpen.pack_forget()
        self.__backgroundActu.pack_forget()
        self.__backgroundFirstboot.pack_forget()
        self.__backgroundTopCodehelp.pack_forget()
        self.__backgroundBottomCodehelp.pack_forget()
        self.__frameBackgroudCodehelp.pack_forget()
        self.__backgroundLitleWindowsRyley.pack_forget()
        self.__fBottomLitleWindows.pack_forget()
        self.__fChoiceLitleWindows.pack_forget()
        self.__backgroundLitleWindowsSix.pack_forget()

    def __viewNormal(self):
        self.__screen.focus_set()
        self.__homeBackgroud.pack()
        self.__frameBackgroud.pack()

    def __viewOpen(self):
        self.__disableAllFrame()
        self.__screen.focus_set()
        self.__homeBackgroudFileOpen.pack()
        self.__frameBackgroud.pack()

    def __viewCodehelp(self):
        self.__screen.focus_set()
        self.__backgroundTopCodehelp.pack()
        self.__backgroundBottomCodehelp.pack()
        self.__frameBackgroudCodehelp.pack()

    def __modeNormal(self):
        self.__screen.focus_set()
        self.__codeHelpActived = False
        self.__disableAllFrame()
        self.__viewNormal()
        self.__setButtonOpen()

    def __modeCodehelp(self):
        self.__screen.focus_set()
        self.__codeHelpActived = True
        if self.__litleWindowsActived != 0:
            self.__modeBigWindows()
        self.__disableAllFrame()
        self.__paroleCodehelp(self.__language.getPhActiveCodehelp())
        self.__viewCodehelp()
        self.__setButtonOpen()

    def __paroleRyley(self, text: str):
        if text != "":
            self.__lparoleRyleyNormal.configure(text=text)
            self.__lparoleRyleyFileOpen.configure(text=text)
            self.__entryUserCopilote.delete(0, END)

    def __paroleCopilote(self,text: str):
        if text != "":
            self.__disableAllFrame()
            self.__copiloteSpeak.pack()
            self.__frameBackgroud.pack()
            self.__lparoleCopilote.configure(text=text)
            self.__screen.update()
            time.sleep(0.8)

    def __paroleSix(self, text: str):
        if text != "":
            self.__lparoleSixNormal.configure(text=text)
            self.__lparoleSixFileOpen.configure(text=text)
            self.__entryUserCopilote.delete(0, END)
            if self.__soundState :
                self.__ttsSpeak(text)

    def __paroleCodehelp(self, text: str):
        if text != "":
            self.__lparoleCodehelp.configure(text=text)
            self.__entryUserCodehelp.delete(0, END)

    def __paroleLittle(self, text: str):
        if text != "":
            self.__entryUserLittle.delete(0, END)
            if self.__litleWindowsActived == 1:
                self.__lparoleLittleRyley.configure(text=text)
            elif self.__litleWindowsActived == 2:
                self.__lparoleLittleSix.configure(text=text)
                if self.__soundState:
                    self.__ttsSpeak(text)

    def __quitCopilote(self):
        if (askyesno("Atention", "Voulez-vous vraiment fermer Arrera Copilote ?")):
            self.__close()

    def __close(self):
        if self.__litleWindowsActived != 0:
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
            linkSource="https://github.com/Arrera-Software/Arrera-Copilote",
            linkWeb="https://arrera-software.fr/")

    def __actionBTNAcceuil(self):
        if (self.__litleWindowsActived == 0 or self.__litleWindowsActived == 1 or self.__litleWindowsActived == 2) and self.__codeHelpActived == False:
            texte = self.__entryUserCopilote.get().lower()
            self.__entryUserCopilote.delete(0, END)
            self.__screen.focus_set()
            self.__sendCopilote(texte)


    def __actionBTNCodehelp(self):
        if self.__codeHelpActived:
            texte = self.__entryUserCodehelp.get().lower()
            self.__entryUserCodehelp.delete(0, END)
            self.__screen.focus_set()
            self.__sendCopilote(texte)

    def __actionBTNLitleWindows(self):
        if self.__litleWindowsActived == 1 or self.__litleWindowsActived == 2:
            texte = self.__entryUserLittle.get().lower()
            self.__entryUserLittle.delete(0, END)
            self.__screen.focus_set()
            self.__sendCopilote(texte)

    def __copiloteBrain(self, texte: str):
        if "mode normal" in texte and self.__litleWindowsActived != 0:
            self.__modeBigWindows()
            return
        elif "mode petit" in texte or "mode discret" in texte and self.__litleWindowsActived == 0:
            self.__modeLittleWindows()
            return
        elif "parametre" in texte:
            self.__viewParametre()
        elif "codehelp" in texte:
            self.__modeCodehelp()

    def __ryleyBrain(self, texte):
        self.__assistantRyley.neuron(texte)
        self.__nbSortieRyley = self.__assistantRyley.getValeurSortie()
        self.__listSortieRyley = self.__assistantRyley.getListSortie()
        self.__neuronUsedRyley = self.__assistantRyley.getNeuronUsed()
        return self.__traimentNeuronal(self.__nbSortieRyley, self.__listSortieRyley)

    def __sixBrain(self, texte):
        self.__assistantSix.neuron(texte)
        self.__nbSortieSix = self.__assistantSix.getValeurSortie()
        self.__listSortieSix = self.__assistantSix.getListSortie()
        self.__neuronUsedSix = self.__assistantSix.getNeuronUsed()
        return self.__traimentNeuronal(self.__nbSortieSix, self.__listSortieSix)

    def __traitementSpecial(self):
        if self.__nbSortieRyley == 3 and self.__nbSortieSix == 3:
            self.__outSpecial = self.__language.getPhOpenActu()
            self.__paroleCopilote(self.__outSpecial)
            self.__viewResumer(self.__listSortieRyley, 2)
            return True

        elif self.__nbSortieRyley == 9 and self.__nbSortieSix == 9:
            self.__outSpecial = self.__language.getPhReadWord()
            self.__windowsReadFile(self.__listSortieRyley, 2)
            self.__paroleCopilote(self.__outSpecial)
            return True

        elif self.__nbSortieRyley == 12 and self.__nbSortieSix == 12:
            self.__outSpecial = self.__language.getPhResumerActu()
            self.__viewResumer(self.__listSortieRyley, 1)
            self.__paroleCopilote(self.__outSpecial)
            return True

        elif self.__nbSortieRyley == 13 and self.__nbSortieSix == 13:
            self.__outSpecial = self.__language.getPhReadTableur()
            self.__windowsReadFile(self.__listSortieRyley, 1)
            self.__paroleCopilote(self.__outSpecial)
            return True

        elif self.__nbSortieRyley == 17 and self.__nbSortieSix == 17:
            self.__windowsHelp(self.__listSortieRyley)

        elif self.__nbSortieRyley == 18 and self.__nbSortieSix == 18:
            self.__outSpecial = self.__language.getPhResumerAgenda()
            self.__viewResumer(self.__listSortieRyley, 3)
            self.__paroleCopilote(self.__outSpecial)
            return True

        elif self.__nbSortieRyley == 19 and self.__nbSortieSix == 19:
            self.__outSpecial = self.__language.getPhResumerAll()
            self.__viewResumer(self.__listSortieRyley, 4)
            self.__paroleCopilote(self.__outSpecial)
            return True

        else :
            return False

    def __reponseRyley(self,outRyley:str,nUsedSix:str,nUsedRyley:str):

        if nUsedSix == "software" and  nUsedRyley == "none":
            return self.__language.getRyleyPhOpenArrera()
        elif nUsedSix == "open" and  nUsedRyley == "none":
            return self.__language.getRyleyPhOpen()
        elif nUsedSix == "word" and  nUsedRyley == "none":
            return self.__language.getRyleyPhWork()
        if nUsedSix == "search" and  nUsedRyley == "none":
            return self.__language.getRyleyPhSearch()
        else :
            return outRyley

    def __reponseSix(self,outSix:str,nUsedSix:str,nUsedRyley:str):
        if nUsedRyley == "codehelp" and  nUsedSix == "none":
            return self.__language.getSixPhOpenCodehelp()
        elif nUsedRyley == "service" and  nUsedSix == "none":
            return self.__language.getSixPhService()
        else :
            return outSix

    def __sendCopilote(self, texte:str):
        self.__outSpecial = ""
        outRyley = self.__ryleyBrain(texte)
        outSix = self.__sixBrain(texte)

        outRyley = self.__reponseRyley(outRyley, self.__neuronUsedSix, self.__neuronUsedRyley)
        outSix = self.__reponseSix(outSix, self.__neuronUsedSix, self.__neuronUsedRyley)

        specialFnc = self.__traitementSpecial()

        if specialFnc:
            if self.__codeHelpActived:
                self.__paroleCodehelp(self.__outSpecial)

            elif self.__litleWindowsActived == 1 or self.__litleWindowsActived == 2:
                self.__paroleLittle(self.__outSpecial)

            else :
                self.__paroleSix(self.__outSpecial)
                self.__paroleRyley(self.__outSpecial)
        else :
            if self.__codeHelpActived:
                self.__paroleCodehelp(outRyley)

            elif self.__litleWindowsActived == 1:
                self.__paroleLittle(outRyley)

            elif self.__litleWindowsActived == 2 :
                self.__paroleLittle(outSix)

            else :
                self.__paroleSix(outSix)
                self.__paroleRyley(outRyley)

    def __traimentNeuronal(self, nb:int, liste:list):
        match nb:
            case 0:
                return liste[0]
            case 1:
                return liste[0]
            case 2:
                return "error"
            case 4:
                return liste[0]
            case 5:
                return liste[0]
            case 6:
                return self.__language.getPhErreurActu()
            case 7:
                self.__setButtonOpen()
                return liste[0]
            case 8:
                self.__setButtonOpen()
                return liste[0]
            case 10:
                self.__setButtonOpen()
                return liste[0]
            case 11:
                return self.__language.getPhErreurResumerActu()
            case 14:
                self.__setButtonOpen()
                return liste[0]
            case 15:
                self.__close()
                return ""
            case 16:
                return self.__assistantRyley.shutdown()
            case 17 :
                return self.__windowsHelp(liste)
            case 20:
                return self.__language.getPhErreurResumerAll()
            case 21:
                self.__setButtonOpen()
                return liste[0]
            case other:
                return ""

    def __keyboard(self):
        def anychar(event):
            if self.__windowsOS:
                if event.keycode == 13:
                    if not self.__codeHelpActived and self.__litleWindowsActived == 0:
                        self.__actionBTNAcceuil()
                    elif self.__codeHelpActived:
                        self.__actionBTNCodehelp()
                    elif self.__litleWindowsActived == 1 or self.__litleWindowsActived == 2:
                        self.__actionBTNLitleWindows()
            elif self.__linuxOS :
                if event.keycode == 36:
                    if not self.__codeHelpActived and self.__litleWindowsActived == 0:
                        self.__actionBTNAcceuil()
                    elif self.__codeHelpActived:
                        self.__actionBTNCodehelp()
                    elif self.__litleWindowsActived == 1 or self.__litleWindowsActived == 2:
                        self.__actionBTNLitleWindows()
            elif self.__macOS:
                if event.keycode == 603979789:
                    if not self.__codeHelpActived and self.__litleWindowsActived == 0:
                        self.__actionBTNAcceuil()
                    elif self.__codeHelpActived:
                        self.__actionBTNCodehelp()
                    elif self.__litleWindowsActived == 1 or self.__litleWindowsActived == 2:
                        self.__actionBTNLitleWindows()
        self.__screen.bind("<Key>", anychar)

    def __setButtonOpen(self):
        self.__guiWork.updateEtat()

        tableur = (self.__assistantSix.getTableur())
        word = self.__assistantSix.getWord()
        projet = self.__assistantSix.getProject()

        if tableur :
            self.__arrTK.placeRightBottomNoStick(self.__btnTableurOpenCopilote)
            self.__arrTK.placeRightBottomNoStick(self.__btnTableurOpenCodehelp)
            self.__arrTK.placeBottomLeft(self.__btnTableurOpenLittle)
        else :
            self.__btnTableurOpenCopilote.place_forget()
            self.__btnTableurOpenCodehelp.place_forget()
            self.__btnTableurOpenLittle.place_forget()

        if word:
            self.__arrTK.placeLeftBottomNoStick(self.__btnWordOpenCopilote)
            self.__arrTK.placeLeftBottomNoStick(self.__btnWordOpenCodehelp)
            self.__arrTK.placeBottomRight(self.__btnWordOpenLitte)
        else :
            self.__btnWordOpenCopilote.place_forget()
            self.__btnWordOpenCodehelp.place_forget()
            self.__btnWordOpenLitte.place_forget()

        if projet:
            self.__arrTK.placeBottomCenterNoStick(self.__btnProjetOpenCopilote)
            self.__arrTK.placeBottomCenterNoStick(self.__btnProjetOpenCodehelp)
            self.__arrTK.placeLeftBottomNoStick(self.__btnProjetOpenLitteRyley)
            self.__arrTK.placeLeftBottomNoStick(self.__btnProjetOpenLitteSix)
        else :
            self.__btnProjetOpenCopilote.place_forget()
            self.__btnProjetOpenCodehelp.place_forget()
            self.__btnProjetOpenLitteRyley.place_forget()
            self.__btnProjetOpenLitteSix.place_forget()

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
                                         title="Arrera Copilote : Aide",
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
        return textSpeak

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
                winRead.title("Arrera COPILOTE : Lecture Tableur")
                labelTitleRead.configure(text="Lecture : Tableur")
                textContent = ""
                for i in range(0, len(liste)):
                    textContent = textContent+str(liste[i]) + "\n"
                self.__arrTK.insertTextOnTextBox(content, textContent)

            case 2 :
                winRead.title("Arrera COPILOTE : Lecture Traitement de texte")
                labelTitleRead.configure(text="Lecture : Traitement de texte")
                self.__arrTK.insertTextOnTextBox(content, liste[0])

        self.__arrTK.placeCenter(content)
        self.__arrTK.placeTopCenter(labelTitleRead)

    def __viewParametre(self):
        self.__screen.focus_set()
        self.__disableAllFrame()
        self.__arrGazelle.active()
        self.__arrGazelle.passQUITFNC(self.__quitParametre)

    def __quitParametre(self):
        self.__screen.focus_set()
        self.__screen.protocol("WM_DELETE_WINDOW", self.__quitCopilote)
        self.__screen.maxsize(500, 600)
        self.__viewNormal()
        self.__paroleRyley(self.__language.getPhParametre())

    def __activeOrgaVar(self):
        self.__assistantRyley.neuron("ouvre orga var")
        self.__paroleCodehelp(self.__assistantRyley.getListSortie()[0])

    def __activeColorSelecteur(self):
        self.__assistantRyley.neuron("ouvre color selecteur")
        self.__paroleCodehelp(self.__assistantRyley.getListSortie()[0])

    def __activeGestGit(self):
        self.__assistantRyley.neuron("ouvre gest github")
        self.__paroleCodehelp(self.__assistantRyley.getListSortie()[0])

    def __activeLibrairy(self):
        self.__assistantRyley.neuron("ouvre librairy")
        self.__paroleCodehelp(self.__assistantRyley.getListSortie()[0])

    def __modeLittleWindows(self):
        self.__screen.focus_set()
        self.__disableAllFrame()
        self.__screen.maxsize(500, 200)
        self.__screen.minsize(500, 200)
        self.__fChoiceLitleWindows.pack()

    def __modeLittleWindowsRyley(self):
        self.__screen.focus_set()
        self.__disableAllFrame()
        self.__btnSoundLitle.place_forget()
        self.__btnMicroLitle.place_forget()
        self.__backgroundLitleWindowsRyley.pack()
        self.__fBottomLitleWindows.pack()
        self.__litleWindowsActived = 1
        self.__paroleLittle(self.__language.getPhActiveModeLitleRyley())

    def __modeLittleWindowsSix(self):
        self.__screen.focus_set()
        self.__disableAllFrame()
        self.__backgroundLitleWindowsSix.pack()
        self.__fBottomLitleWindows.pack()
        self.__litleWindowsActived = 2
        self.__arrTK.placeWidgetCenteredAtBottom(self.__btnSoundLitle, -125)
        self.__arrTK.placeWidgetCenteredAtBottom(self.__btnMicroLitle, 125)
        self.__paroleLittle(self.__language.getPhActiveModelitleSix())

    def __modeBigWindows(self):
        self.__screen.focus_set()
        self.__disableAllFrame()
        self.__screen.maxsize(500, 600)
        self.__screen.minsize(500, 600)
        self.__paroleRyley(self.__language.getPhActiveModeNormalRyley())
        self.__paroleSix(self.__language.getPhActiveModeNormalSix())
        self.__viewNormal()
        self.__litleWindowsActived = 0
        self.__setButtonOpen()

    def __ttsSpeak(self,text:str):
        """
        Fonction pour faire parler le TTS
        :param text: Texte à faire parler
        """
        if not self.__threadSpeaking :
            self.__threadParoleCopilote = th.Thread(target=self.__arrVoice.say,args=(text,))
            self.__threadParoleCopilote.start()
            self.__screen.after(1000, self.__updateSpeak)

    def __updateSpeak(self):
        """
        Fonction pour mettre à jour le texte de parole
        """
        if self.__threadParoleCopilote.is_alive():
            self.__screen.update()
            self.__screen.after(1000, self.__updateSpeak)
        else :
            self.__threadSpeaking = False

    def __actionSound(self):
        if not self.__soundState:
            self.__soundState = True
            if self.__litleWindowsActived == 2 :
                self.__paroleLittle(self.__language.getPhActiveSoundLitle())
            else :
                self.__paroleSix(self.__language.getPhActiveSound())

            self.__btnSoundNormal.configure(image=self.__imgBtnSoundOn)
            self.__btnSoundLitle.configure(image=self.__imgBtnSoundOn)

        else :

            if self.__litleWindowsActived == 2 :
                self.__paroleLittle(self.__language.getPhDesactiveSound(2))
            else :
                self.__paroleSix(self.__language.getPhDesactiveSound(1))
            self.__soundState = False
            self.__btnSoundNormal.configure(image=self.__imgBtnSoundOff)
            self.__btnSoundLitle.configure(image=self.__imgBtnSoundOff)

    def __cancelLittleWindows(self):
        self.__disableAllFrame()
        self.__viewNormal()
        self.__litleWindowsActived = 0
        self.__screen.maxsize(500, 600)
        self.__screen.minsize(500, 600)
        self.__setButtonOpen()

    def __enableMicro(self):
        if not self.__microState:
            self.__theardMicrophone = th.Thread(target=self.__copiloteListen)
            self.__microState = True
            self.__btnMicroNormal.configure(image=self.__imgBtnMicroOn)
            self.__btnMicroLitle.configure(image=self.__imgBtnMicroOn)
            self.__theardMicrophone.start()
            self.__screen.after(1000, self.__updateMicro)

    def __updateMicro(self):
        if self.__theardMicrophone.is_alive():
            self.__screen.update()
            self.__btnMicroNormal.configure(image=self.__imgBtnMicroOn)
            self.__btnMicroLitle.configure(image=self.__imgBtnMicroOn)
            self.__screen.after(1000, self.__updateMicro)
        else :
            self.__btnMicroNormal.configure(image=self.__imgBtnMicroOff)
            self.__btnMicroLitle.configure(image=self.__imgBtnMicroOff)
            self.__theardMicrophone = th.Thread()
            self.__microState = False

    def __actionMicro(self):
         if not self.__microState:
            if self.__arrVoice.getNbWord() == 0:
                self.__enableMicro()
            else :
                if not self.__is_listening:
                    self.__is_listening = True
                    self.listen_thread = th.Thread(target=self.__tigerloop, daemon=True)
                    self.listen_thread.start()
                else:
                    self.__is_listening = False
                    self.__btnMicroNormal.configure(image=self.__imgBtnMicroOff)
                    self.__btnMicroLitle.configure(image=self.__imgBtnMicroOff)


    def __copiloteListen(self):
        sortie = self.__arrVoice.listen()
        if sortie == 0 :
            if self.__litleWindowsActived == 2 or self.__litleWindowsActived == 1:
                self.__entryUserLittle.delete(0, END)
                self.__entryUserLittle.insert(0, self.__arrVoice.getTextMicro())
                time.sleep(0.4)
                self.__actionBTNLitleWindows()
            elif self.__codeHelpActived :
                self.__entryUserCodehelp.delete(0, END)
                self.__entryUserCodehelp.insert(0, self.__arrVoice.getTextMicro())
                time.sleep(0.4)
                self.__actionBTNCodehelp()
            else:
                self.__entryUserCopilote.delete(0, END)
                self.__entryUserCopilote.insert(0, self.__arrVoice.getTextMicro())
                time.sleep(0.4)
                self.__actionBTNAcceuil()


    def __tigerloop(self):
        while self.__is_listening:
            self.__btnMicroLitle.configure(image=self.__imgBtnMicroTiger)
            self.__btnMicroNormal.configure(image=self.__imgBtnMicroTiger)
            result = self.__arrVoice.trigerWord()
            if result == 1 :
                self.__enableMicro()