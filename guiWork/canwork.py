from librairy.arrera_tk import *
from ObjetsNetwork.arreraNeuron import *

class CAnWorkGUI:
    def __init__(self, arrtk : CArreraTK,nameAssistant : str,asset:str,arrNeuron:ArreraNetwork,fileUserAssistant:str):
        # Attributs
        self.__tableurOpen = False
        self.__wordOpen = False
        self.__projectOpen = False
        # Attributs de l'interface
        self.__arrTk = arrtk
        self.__emplacementAsset = asset+"/"
        self.__nameAssistant = nameAssistant
        # Recuperation du neurone
        self.__arrNeuron = arrNeuron
        self.__fileUser = jsonWork(fileUserAssistant)

    def __createWindows(self):
        self.__screen = self.__arrTk.aTopLevel(width=500, height=650,
                                               title=self.__nameAssistant + " : Arrera Work",
                                               resizable=True)
        self.__screen.rowconfigure(0, weight=1)
        self.__screen.rowconfigure(1, weight=0)
        self.__screen.columnconfigure(0, weight=1)
        self.__screen.columnconfigure(1, weight=2)
        self.__screen.columnconfigure(2, weight=1)

        # Recuperation des image
        imgTableurAcceuil = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/tableur.png",tailleX=100, tailleY=100)
        imgWordAcceuil = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/word.png",tailleX=100, tailleY=100)
        imgProjectAcceuil = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/project.png",tailleX=100, tailleY=100)

        imgTableurDock = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/tableur.png",tailleX=50, tailleY=50)
        imgWordDock = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/word.png",tailleX=50, tailleY=50)
        imgProjectDock = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/project.png",tailleX=50, tailleY=50)
        imgAnnulerDock = self.__arrTk.createImage(self.__emplacementAsset + "acceuil/annuler.png",tailleX=50, tailleY=50)

        # Images pour la frame Tableur
        imgAddComptage = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-comptagexcf.png",
                                                  tailleX=90, tailleY=90)
        imgAddMaxmum = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-maxmum.png",
                                                tailleX=90, tailleY=90)
        imgAddMinimum = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-minimum.png",
                                                 tailleX=90, tailleY=90)
        imgAddMoyenne = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-moyenne.png",
                                                 tailleX=90, tailleY=90)
        imgAddSomme = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-somme.png"
                                               ,tailleX=90, tailleY=90)
        imgAddValeur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-valeur.png"
                                                ,tailleX=90, tailleY=90)
        imgCloseTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/close-tableur.png"
                                                   ,tailleX=90, tailleY=90)
        imgOpenTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/open-tableur.png"
                                                  ,tailleX=90, tailleY=90)
        imgOpenTableurCoputerSoft = self.__arrTk.createImage(self.__emplacementAsset + "tableur/open-tableur-coputer-soft.png"
                                                             ,tailleX=90, tailleY=90)
        imgReadTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/read-tableur.png"
                                                  ,tailleX=90, tailleY=90)
        imgSupprValeur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/suppr-valeur.png"
                                                  ,tailleX=90, tailleY=90)
        imgViewTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/view-tableur.png"
                                                  ,tailleX=90, tailleY=90)

        # Images pour la frame Word
        imgOpenWord = self.__arrTk.createImage(self.__emplacementAsset + "word/open-word.png",
                                               tailleX=90, tailleY=90)
        imgOpenWordWithComputer = self.__arrTk.createImage(self.__emplacementAsset + "word/open-word-coputer-soft.png",
                                                           tailleX=90, tailleY=90)
        imgCloseWord = self.__arrTk.createImage(self.__emplacementAsset + "word/close-word.png",
                                                tailleX=90, tailleY=90)
        imgReadWord = self.__arrTk.createImage(self.__emplacementAsset + "word/read-word.png",
                                               tailleX=90, tailleY=90)
        imgWriteWord = self.__arrTk.createImage(self.__emplacementAsset + "word/write-word.png",
                                                tailleX=90, tailleY=90)

        # Images pour la frame Projet
        imgCreateFileProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/create-file-project.png",
                                                       tailleX=90, tailleY=90)
        imgCreateProject = self.__arrTk.createImage(self.__emplacementAsset + "project/create-projet.png",
                                                    tailleX=90, tailleY=90)
        imgOpenFileProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/open-file-project.png",
                                                     tailleX=90, tailleY=90)
        imgOpenProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/open-project.png",
                                                 tailleX=90, tailleY=90)
        imgSetTypeProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/setType-project.png",
                                                    tailleX=90, tailleY=90)
        imgTaskSayProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/task-say.png",
                                                    tailleX=90, tailleY=90)
        imgTaskViewProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/view-task-project.png",
                                                     tailleX=90, tailleY=90)
        imgViewTypeFileProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/view-type.png",
                                                         tailleX=90, tailleY=90)
        imgCloseProjet = self.__arrTk.createImage(self.__emplacementAsset + "project/close-project.png",
                                                  tailleX=90, tailleY=90)

        # Frames
        self.__fAcceuil = self.__arrTk.createFrame(self.__screen)
        self.__fDock = self.__arrTk.createFrame(self.__screen, bg="grey", height=70)
        self.__fTableur = self.__arrTk.createFrame(self.__screen)
        self.__fTableurNoOpen = self.__arrTk.createFrame(self.__screen)
        self.__fWord = self.__arrTk.createFrame(self.__screen)
        self.__fWordNoOpen = self.__arrTk.createFrame(self.__screen)
        self.__fProjet = self.__arrTk.createFrame(self.__screen)
        self.__fProjetNoOpen = self.__arrTk.createFrame(self.__screen)

        # Widgets dans la frame d'accueil
        labelTitleAcceuil = self.__arrTk.createLabel(self.__fAcceuil, text=self.__nameAssistant + " : Arrera Work",
                                                     ppolice="Arial",ptaille=25)
        btnArreraTableurAcceuil = self.__arrTk.createButton(self.__fAcceuil,width=100,
                                                            height=100, image=imgTableurAcceuil,
                                                            command=self.__activeTableur)
        btnArreraWordAcceuil = self.__arrTk.createButton(self.__fAcceuil, width=100,
                                                         height=100, image=imgWordAcceuil,
                                                         command=self.__activeWord)
        btnArreraProjectAcceuil = self.__arrTk.createButton(self.__fAcceuil, width=100,
                                                            height=100, image=imgProjectAcceuil,
                                                            command=self.__activeProjet)

        # Widgets dans la frame dock
        btnArreraTableurDock = self.__arrTk.createButton(self.__fDock,width=60,
                                                         height=60, image=imgTableurDock,
                                                         command=self.__activeTableur)
        btnArreraWordDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                      height=60, image=imgWordDock,
                                                      command=self.__activeWord)
        btnArreraProjectDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                         height=60, image=imgProjectDock,
                                                         command=self.__activeProjet)
        btnArreraBackAcceuilDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                             height=60,image =imgAnnulerDock,
                                                             command=self.__activeAcceuil)

        # Widgets du frame Tableur
        labelTitleNoOpenTableur = self.__arrTk.createLabel(self.__fTableurNoOpen, text="Travail sur un tableur",
                                                           ppolice="Arial",ptaille=25)
        btnOpenTableur = self.__arrTk.createButton(self.__fTableurNoOpen,width=90,height=90,
                                                   image=imgOpenTableur,command=self.__openTableur)
        labelTitleTableur = self.__arrTk.createLabel(self.__fTableur, text="Travail sur un tableur",
                                                     ppolice="Arial",ptaille=25)
        btnOpenTableurWithComputer = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgOpenTableurCoputerSoft,)
        btnCloseTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgCloseTableur)
        btnReadTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgReadTableur)
        btnAddValeurTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddValeur)
        btnAddMoyenneTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddMoyenne)
        btnAddSommeTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddSomme)
        btnAddComptageTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddComptage)
        btnAddMinimumTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddMinimum)
        btnAddMaximumTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddMaxmum)
        btnAffichageTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgViewTableur)
        btnSupprDataTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgSupprValeur)

        # Widgets dans la frame Word
        labelTitleNoOpenWord = self.__arrTk.createLabel(self.__fWordNoOpen, text="Travail sur un document Word",
                                                        ppolice="Arial",ptaille=25)
        btnOpenWord = self.__arrTk.createButton(self.__fWordNoOpen,width=90,height=90,image=imgOpenWord,
                                                command=self.__openWord)

        labelTitleWord = self.__arrTk.createLabel(self.__fWord, text="Travail sur un document Word",
                                                  ppolice="Arial",ptaille=25)
        btnOpenWordWithComputer = self.__arrTk.createButton(self.__fWord,width=90,height=90,image=imgOpenWordWithComputer)
        btnCloseWord = self.__arrTk.createButton(self.__fWord,width=90,height=90,image=imgCloseWord)
        btnReadWord = self.__arrTk.createButton(self.__fWord,width=90,height=90,image=imgReadWord)
        btnWriteWord = self.__arrTk.createButton(self.__fWord,width=90,height=90,image=imgWriteWord)

        # Widget dans la frame Projet
        # No OPEN
        labelTitleNoOpenProjet = self.__arrTk.createLabel(self.__fProjetNoOpen, text="Travail sur un projet",
                                                          ppolice="Arial", ptaille=25)

        btnOpenProjet = self.__arrTk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                  image=imgOpenProjet,command=self.__openProjet)

        btnCreateProjet = self.__arrTk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                    image=imgCreateProject)

        # OPEN
        labelTitleProjet = self.__arrTk.createLabel(self.__fProjet, text="Travail sur un projet",
                                                    ppolice="Arial", ptaille=25)
        btnAddTypeProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgSetTypeProjet)
        btnShowTypeFile = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgViewTypeFileProjet)
        btnCreateFileProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgCreateFileProjet)
        btnOpenFileProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgOpenFileProjet)
        btnViewTaskProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgTaskViewProjet)
        btnSayAllTaskProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90, image=imgTaskSayProjet)

        btnCloseProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgCloseProjet)

        # Grille des frame
        self.__fAcceuil.rowconfigure(0, weight=1)
        self.__fAcceuil.rowconfigure(1, weight=0)
        self.__fAcceuil.rowconfigure(2, weight=1)

        # Colonnes pareil pour leur largeur
        self.__fAcceuil.columnconfigure(0, weight=1)
        self.__fAcceuil.columnconfigure(1, weight=2)
        self.__fAcceuil.columnconfigure(2, weight=1)

        self.__fDock.grid_columnconfigure(0, weight=1)
        self.__fDock.grid_columnconfigure(5, weight=1)

        self.__fTableurNoOpen.grid_rowconfigure(0, weight=1)
        self.__fTableurNoOpen.grid_rowconfigure(1, weight=0)
        self.__fTableurNoOpen.grid_rowconfigure(2, weight=0)
        self.__fTableurNoOpen.grid_rowconfigure(3, weight=1)

        self.__fTableurNoOpen.grid_columnconfigure(0, weight=1)
        self.__fTableurNoOpen.grid_columnconfigure(1, weight=0)
        self.__fTableurNoOpen.grid_columnconfigure(2, weight=1)

        self.__fTableur.grid_columnconfigure(0, weight=1)
        self.__fTableur.grid_columnconfigure(1, weight=1)
        self.__fTableur.grid_columnconfigure(2, weight=1)

        self.__fWordNoOpen.grid_rowconfigure(0, weight=1)
        self.__fWordNoOpen.grid_rowconfigure(1, weight=0)
        self.__fWordNoOpen.grid_rowconfigure(2, weight=0)
        self.__fWordNoOpen.grid_rowconfigure(3, weight=1)

        self.__fWordNoOpen.grid_columnconfigure(0, weight=1)
        self.__fWordNoOpen.grid_columnconfigure(1, weight=0)
        self.__fWordNoOpen.grid_columnconfigure(2, weight=1)

        self.__fWord.grid_columnconfigure(0, weight=1)
        self.__fWord.grid_columnconfigure(1, weight=1)
        self.__fWord.grid_columnconfigure(2, weight=1)

        self.__fProjetNoOpen.grid_rowconfigure(0, weight=1)
        self.__fProjetNoOpen.grid_rowconfigure(1, weight=0)
        self.__fProjetNoOpen.grid_rowconfigure(2, weight=0)
        self.__fProjetNoOpen.grid_rowconfigure(3, weight=1)

        self.__fProjetNoOpen.grid_columnconfigure(0, weight=1)
        self.__fProjetNoOpen.grid_columnconfigure(1, weight=0)
        self.__fProjetNoOpen.grid_columnconfigure(2, weight=1)

        # Centrage vertical par lignes vides
        self.__fProjet.grid_rowconfigure(0, weight=1)
        self.__fProjet.grid_rowconfigure(5, weight=1)

        # Centrage horizontal
        self.__fProjet.grid_columnconfigure(0, weight=1)
        self.__fProjet.grid_columnconfigure(1, weight=0)
        self.__fProjet.grid_columnconfigure(2, weight=1)


        # Affichage des frames
        labelTitleAcceuil.grid(row=0, column=0, columnspan=3, sticky='new', pady=20)  # En haut, centré, espacé en haut

        # Placement des boutons sur la même ligne et centrés
        btnArreraTableurAcceuil.grid(row=1, column=0, padx=10, pady=60)
        btnArreraWordAcceuil.grid(row=1, column=1, padx=10, pady=60)
        btnArreraProjectAcceuil.grid(row=1, column=2, padx=10, pady=60)

        # PLacement des boutons dans le dock
        btnArreraTableurDock.grid(row=0, column=1, padx=5, pady=5)
        btnArreraWordDock.grid(row=0, column=2, padx=5, pady=5)
        btnArreraProjectDock.grid(row=0, column=3, padx=5, pady=5)
        btnArreraBackAcceuilDock.grid(row=0, column=4, padx=5, pady=5)

        # Placement widget des frame Tableur
        labelTitleNoOpenTableur.grid(row=0, column=1, sticky="n")
        btnOpenTableur.grid(row=2, column=1, sticky="n")

        labelTitleTableur.grid(row=0, column=0, columnspan=3, sticky='ew')

        btnOpenTableurWithComputer.grid(row=1, column=0, padx=20, pady=20)

        btnReadTableur.grid(row=1, column=1, padx=20, pady=20)
        btnAddValeurTableur.grid(row=1, column=2, padx=20, pady=20)
        btnAddMoyenneTableur.grid(row=2, column=0, padx=20, pady=20)
        btnAddSommeTableur.grid(row=2, column=1, padx=20, pady=20)
        btnAddComptageTableur.grid(row=2, column=2, padx=20, pady=20)
        btnAddMinimumTableur.grid(row=3, column=0, padx=20, pady=20)
        btnAddMaximumTableur.grid(row=3, column=1, padx=20, pady=20)
        btnAffichageTableur.grid(row=3, column=2, padx=20, pady=20)
        btnSupprDataTableur.grid(row=4, column=0, padx=20, pady=20)
        btnCloseTableur.grid(row=4, column=1, padx=20, pady=20)

        labelTitleNoOpenWord.grid(row=0, column=1, sticky="n")
        btnOpenWord.grid(row=2, column=1, sticky="n")

        labelTitleWord.grid(row=0, column=0, columnspan=3, sticky='ew')
        btnOpenWordWithComputer.grid(row=1, column=0, padx=20, pady=20)
        btnCloseWord.grid(row=1, column=1, padx=20, pady=20)
        btnReadWord.grid(row=1, column=2, padx=20, pady=20)
        btnWriteWord.grid(row=2, column=0, padx=20, pady=20)

        # Placement des widgets dans la frame Projet
        labelTitleProjet.grid(row=0, column=0, columnspan=3, sticky='new')
        labelTitleNoOpenProjet.grid(row=0, column=1, sticky="n")
        btnOpenProjet.grid(row=2, column=0, sticky="n")
        btnCreateProjet.grid(row=2, column=2, sticky="n")

        # labelTitleProjet.grid(row=1, column=0, columnspan=3, pady=(10, 30))
        btnAddTypeProjet.grid(row=2, column=0, padx=5, pady=5)
        btnShowTypeFile.grid(row=2, column=1, padx=5, pady=5)
        btnCreateFileProjet.grid(row=2, column=2, padx=5, pady=5)
        btnOpenFileProjet.grid(row=3, column=0, padx=5, pady=5)
        btnViewTaskProjet.grid(row=3, column=1, padx=5, pady=5)
        btnSayAllTaskProjet.grid(row=3, column=2, padx=5, pady=5)
        btnCloseProjet.grid(row=4, column=1, padx=5, pady=(5, 20))


    def activeAcceuil(self):
        self.__createWindows()
        self.__activeAcceuil()

    def activeProjet(self):
        self.__createWindows()
        self.__activeProjet()

    def activeTableur(self):
        self.__createWindows()
        self.__activeTableur()

    def activeWord(self):
        self.__createWindows()
        self.__activeWord()

    def __disabelFrame(self):
        self.__fAcceuil.grid_forget()
        self.__fDock.grid_forget()
        self.__fTableur.grid_forget()
        self.__fWord.grid_forget()
        self.__fProjet.grid_forget()
        self.__fTableurNoOpen.grid_forget()
        self.__fWordNoOpen.grid_forget()
        self.__fProjetNoOpen.grid_forget()

    def __activeAcceuil(self):
        self.__disabelFrame()
        self.__fAcceuil.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__screen.update()

    def __activeTableur(self):
        self.__disabelFrame()
        if not self.__tableurOpen:
            self.__fTableurNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.__screen.update()

    def __activeWord(self):
        self.__disabelFrame()
        if not self.__wordOpen:
            self.__fWordNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fWord.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.__screen.update()

    def __activeProjet(self):
        self.__disabelFrame()

        if not self.__projectOpen:
            self.__fProjetNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fProjet.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.__screen.update()

    # Partie fonctionnelle de l'application

    def updateEtat(self):
        """
        Met à jour l'état des frames en fonction de l'ouverture des outils.
        """
        self.__wordOpen = self.__arrNeuron.getWord()
        self.__tableurOpen = self.__arrNeuron.getTableur()
        self.__projectOpen = self.__arrNeuron.getProject()

    def __openTableur(self):
        """
        Ouvre le tableur.
        """
        self.__arrNeuron.neuron("Ouvre un tableur")
        self.updateEtat()
        self.__activeTableur()

    def __openWord(self):
        """
        Ouvre le document Word.
        """
        self.__arrNeuron.neuron("Ouvre un document Word")
        self.updateEtat()
        self.__activeWord()

    def __openProjet(self):
        """
        Ouvre le projet.
        """
        emplacementProjects = self.__fileUser.lectureJSON("wordFolder")

        dossier = filedialog.askdirectory(initialdir=emplacementProjects,
                                          title="Selection du projet")
        dossier = (dossier.replace
                   (emplacementProjects,"").replace
                   ("/","").replace("\\","")).strip()
        self.__arrNeuron.neuron("ouvre le projet nommer "+dossier)
        self.updateEtat()
        self.__activeProjet()