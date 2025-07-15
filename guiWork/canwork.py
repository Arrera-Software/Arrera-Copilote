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
        # Variables d'interface
        self.__var = None
        self.__nameProjet = None

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
        btnCloseAcceuilDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                        height=60, image =imgAnnulerDock,
                                                        command=self.__closeDock)

        # Widgets du frame Tableur
        labelTitleNoOpenTableur = self.__arrTk.createLabel(self.__fTableurNoOpen, text="Travail sur un tableur",
                                                           ppolice="Arial",ptaille=25)
        btnOpenTableur = self.__arrTk.createButton(self.__fTableurNoOpen,width=90,height=90,
                                                   image=imgOpenTableur,command=self.__openTableur)
        labelTitleTableur = self.__arrTk.createLabel(self.__fTableur, text="Travail sur un tableur",
                                                     ppolice="Arial",ptaille=25)
        btnOpenTableurWithComputer = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                               image=imgOpenTableurCoputerSoft,
                                                               command=self.__openTableurCoputerSoft)
        btnCloseTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                    image=imgCloseTableur,command=self.__closeTableur)
        btnReadTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                   image=imgReadTableur,command=self.__addValeurTableur())
        btnAddValeurTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                        image=imgAddValeur,command=self.__addValeurTableur)
        btnAddMoyenneTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                         image=imgAddMoyenne,command=self.__addMoyenneTableur)
        btnAddSommeTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                       image=imgAddSomme,command=self.__addSommeTableur)
        btnAddComptageTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                          image=imgAddComptage,command=self.__addComptageTableur)
        btnAddMinimumTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                         image=imgAddMinimum,command=self.__addMinimumTableur)
        btnAddMaximumTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                         image=imgAddMaxmum,command=self.__addMaximumTableur)
        btnAffichageTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                        image=imgViewTableur,command=self.__viewTableur)
        btnSupprDataTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,
                                                        image=imgSupprValeur,
                                                        command=self.__supprValeurTableur)

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
                                                  image=imgOpenProjet
                                                  ,command=self.__openProjet)

        btnCreateProjet = self.__arrTk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                    image=imgCreateProject,
                                                    command=self.__windowsNameNewProjet)

        # OPEN
        labelTitleProjet = self.__arrTk.createLabel(self.__fProjet, text="Travail sur un projet",
                                                    ppolice="Arial", ptaille=25)
        btnAddTypeProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,
                                                     image=imgSetTypeProjet,command=self.__windowsTypeFileProjet)
        btnCreateFileProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgCreateFileProjet,
                                                        command=self.__windowsCreateFileProjet)
        btnOpenFileProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgOpenFileProjet,
                                                      command=self.__openFileProjet)
        btnViewTaskProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgTaskViewProjet,
                                                      command=self.__openTaskProjet)
        btnSayAllTaskProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90, image=imgTaskSayProjet)

        btnCloseProjet = self.__arrTk.createButton(self.__fProjet, width=90, height=90,image=imgCloseProjet,
                                                   command=self.__closeProjet)

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
        btnCloseAcceuilDock.grid(row=0, column=4, padx=5, pady=5)

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
        btnCreateFileProjet.grid(row=2, column=1, padx=5, pady=5)
        btnOpenFileProjet.grid(row=2, column=2, padx=5, pady=5)
        btnViewTaskProjet.grid(row=3, column=0, padx=5, pady=5)
        btnSayAllTaskProjet.grid(row=3, column=1, padx=5, pady=5)
        btnCloseProjet.grid(row=3, column=2, padx=5, pady=5)


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

    # Dock

    def __closeDock(self):
        if self.__projectOpen :
            self.__closeProjet()
        elif self.__tableurOpen :
            self.__closeTableur()
        elif self.__wordOpen :
            pass
        else :
            self.__activeAcceuil()

    def updateEtat(self):
        """
        Met à jour l'état des frames en fonction de l'ouverture des outils.
        """
        self.__wordOpen = self.__arrNeuron.getWord()
        self.__tableurOpen = self.__arrNeuron.getTableur()
        self.__projectOpen = self.__arrNeuron.getProject()

    # Partie Tableur
    def __openTableur(self):
        """
        Ouvre le tableur.
        """
        self.__arrNeuron.neuron("Ouvre un tableur")
        self.updateEtat()
        self.__activeTableur()

    def __openTableurCoputerSoft(self):
        """
        Ouvre le tableur avec un logiciel de tableur.
        """
        self.__arrNeuron.neuron("Ouvre le fichier tableur avec le logiciel de l'ordinateur")

    def __closeTableur(self):
        self.__arrNeuron.neuron("Ferme le tableur")
        self.updateEtat()
        self.__activeTableur()

    def __addValeurTableur(self):
        self.__arrNeuron.neuron("Ajoute une valeur au tableur")

    def __addMoyenneTableur(self):
        self.__arrNeuron.neuron("Ajout une moyenne au tableur")

    def __addSommeTableur(self):
        self.__arrNeuron.neuron("Ajoute une somme au tableur")

    def __addComptageTableur(self):
        self.__arrNeuron.neuron("Ajoute un comptage au tableur")

    def __addMinimumTableur(self):
        self.__arrNeuron.neuron("Ajout un minimun au tableur")

    def __addMaximumTableur(self):
        self.__arrNeuron.neuron("Ajout un maximun au tableur")

    def __viewTableur(self):
        self.__arrNeuron.neuron("Montre le tableur")

    def __supprValeurTableur(self):
        self.__arrNeuron.neuron("Supprime une valeur du tableur")


    # Partie Word
    def __openWord(self):
        """
        Ouvre le document Word.
        """
        self.__arrNeuron.neuron("Ouvre un document Word")
        self.updateEtat()
        self.__activeWord()

    # Partie Projet

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
        self.__nameProjet = dossier

    def __windowsTexteProjet(self,title:str, texte:str,fnc:callable):
        screen = ctk.CTkToplevel()
        screen.title(title)
        screen.geometry("225x100")
        screen.resizable(False, False)
        self.__arrTk.placeTopCenter(self.__arrTk.createLabel(screen, text=texte,
                                                             ppolice="Arial", ptaille=15))
        self.__entryNameProjet = self.__arrTk.createEntry(screen)
        self.__arrTk.placeCenter(self.__entryNameProjet)
        self.__arrTk.placeBottomCenter(self.__arrTk.createButton(screen,text="Valider",
                                                                 command= lambda :fnc(screen)))

    def __windowsNameNewProjet(self):
        """
        Crée un nouveau projet.
        """
        self.__windowsTexteProjet("Création d'un projet","Nom du nouveau projet",self.__createNewProjet)


    def __createNewProjet(self,screen:ctk.CTkToplevel):
        name = self.__entryNameProjet.get()
        screen.destroy()
        if not name:
            showerror("Erreur", "Le nom du projet ne peut pas être vide.")
            return

        self.__arrNeuron.neuron("cree un nouveau projet nomme "+name)
        self.updateEtat()
        self.__activeProjet()
        self.__nameProjet = name

    def __windowsTypeFileProjet(self):
        """
        Ouvre une fenêtre pour définir le type de fichier du projet.
        """
        self.__windowsTexteProjet("Type de fichier du projet",
                                  "Definir le type du projet",
                                  self.__setTypeFileProjet)

    def __setTypeFileProjet(self, screen: ctk.CTkToplevel):
        """
        Définit le type de fichier du projet.
        """
        type_file = self.__entryNameProjet.get()
        screen.destroy()
        if not type_file:
            showerror("Erreur", "Le type du projet ne peut pas être vide.")
            return

        self.__arrNeuron.neuron("Le type est "+type_file)

    def __windowsCreateFileProjet(self):
        """
        Ouvre une fenêtre pour créer un fichier de projet.
        """
        listType = [" word","odt","txt",
                    "python","en tete","json",
                    "html","css","md","cpp",
                    "language c++","language c",
                    "exel","php","js","java","kt"]
        screen = ctk.CTkToplevel()
        screen.title("Création d'un fichier de projet")
        screen.geometry("300x200")
        screen.resizable(False, False)

        self.__var = StringVar(screen)

        self.__arrTk.placeTopCenter(self.__arrTk.createLabel(screen, text="Creation d'un fichier dans le projet",
                                                             ppolice="Arial", ptaille=15))
        self.__entryNameFile = self.__arrTk.createEntry(screen)
        self.__arrTk.placeLeftCenter(self.__entryNameFile)
        self.__arrTk.placeRightCenter(self.__arrTk.createOptionMenu(screen, value=listType,var=self.__var))
        self.__var.set(listType[0])
        self.__arrTk.placeBottomCenter(self.__arrTk.createButton(screen, text="Valider",
                                                                 command=lambda: self.__createFileProjet(screen)))

    def __createFileProjet(self, screen: ctk.CTkToplevel):
        name_file = self.__entryNameFile.get()
        if not name_file:
            showerror("Erreur", "Imposible de créer un fichier sans nom.")
            return

        type_file = self.__var.get()
        screen.destroy()
        self.__arrNeuron.neuron("cree un fichier "+type_file+" nommer "+name_file)

    def __openFileProjet(self):
        """
        Ouvre un fichier de projet.
        """
        emplacementProjects = self.__fileUser.lectureJSON("wordFolder")+"/"+self.__nameProjet
        file_path = filedialog.askopenfilename(initialdir=emplacementProjects,
                                               title="Selection du fichier du projet",
                                               filetypes=[("All files", "*.*")])
        if file_path:
            file_name = file_path.split("/")[-1]
            self.__arrNeuron.neuron("ouvre le fichier "+file_name)
            self.updateEtat()
            self.__activeProjet()

    def __openTaskProjet(self):
        """
        Ouvre une tâche dans le projet.
        """
        self.__arrNeuron.neuron("ouvre une tache du projet")

    def __closeProjet(self):
        """
        Ferme le projet.
        """
        self.__arrNeuron.neuron("Ferme le projet")
        self.updateEtat()
        self.__activeAcceuil()
        self.__nameProjet = None