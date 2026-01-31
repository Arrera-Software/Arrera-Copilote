from gui.guibase import GuiBase,gestionnaire
from tkinter.filedialog import askdirectory,askopenfilename
import customtkinter as ctk
from tkinter.messagebox import showerror, showinfo
from tkinter import StringVar
from gui.GUITaskProject import GUITaskProject

class GUIWork(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Arrera Work")
        # Attributs
        self.__tableurOpen = False
        self.__wordOpen = False
        self.__projectOpen = False
        # Variables d'interface
        self.__var = None
        self.__nameProjet = None
        # asset
        self.__emplacementAsset = self._gestionnaire.getConfigFile().asset+"work/"
        # GUI
        self.__guiTaskProject = None


    def _mainframe(self):
        # var
        self.__listFormule = self._gestionnaire.getGestFNC().getFNCWork().getListFormuleTableur()
        self.__varFormule = StringVar(self._screen)
        # Conf de la fenetre
        self._screen.rowconfigure(0, weight=1)
        self._screen.rowconfigure(1, weight=0)
        self._screen.columnconfigure(0, weight=1)
        self._screen.columnconfigure(1, weight=2)
        self._screen.columnconfigure(2, weight=1)

        # Recuperation des image
        imgTableurAcceuil = self._arrtk.createImage(self.__emplacementAsset + "acceuil/tableur.png",
                                                    tailleX=100, tailleY=100)
        imgWordAcceuil = self._arrtk.createImage(self.__emplacementAsset + "acceuil/word.png",
                                                 tailleX=100, tailleY=100)
        imgProjectAcceuil = self._arrtk.createImage(self.__emplacementAsset + "acceuil/project.png",
                                                    tailleX=100, tailleY=100)

        imgTableurDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/tableur.png",
                                                 tailleX=50, tailleY=50)
        imgWordDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/word.png",
                                              tailleX=50, tailleY=50)
        imgProjectDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/project.png",
                                                 tailleX=50, tailleY=50)
        imgAnnulerDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/annuler.png",
                                                 tailleX=50, tailleY=50)

        # Images pour la frame Tableur
        imgAddComptage = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-comptagexcf.png",
                                                 tailleX=90, tailleY=90)
        imgAddMaxmum = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-maxmum.png",
                                               tailleX=90, tailleY=90)
        imgAddMinimum = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-minimum.png",
                                                tailleX=90, tailleY=90)
        imgAddMoyenne = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-moyenne.png",
                                                tailleX=90, tailleY=90)
        imgAddSomme = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-somme.png"
                                              , tailleX=90, tailleY=90)
        imgAddValeur = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-valeur.png"
                                               , tailleX=90, tailleY=90)
        imgCloseTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/close-tableur.png"
                                                  , tailleX=90, tailleY=90)
        imgOpenTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/open-tableur.png"
                                                 , tailleX=90, tailleY=90)
        imgOpenTableurCoputerSoft = self._arrtk.createImage(self.__emplacementAsset + "tableur/open-tableur-coputer-soft.png"
                                                            , tailleX=90, tailleY=90)

        imgSupprValeur = self._arrtk.createImage(self.__emplacementAsset + "tableur/suppr-valeur.png"
                                                 , tailleX=90, tailleY=90)
        imgViewTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/view-tableur.png"
                                                 , tailleX=90, tailleY=90)

        # Images pour la frame Word
        imgOpenWord = self._arrtk.createImage(self.__emplacementAsset + "word/open-word.png",
                                              tailleX=90, tailleY=90)
        imgOpenWordWithComputer = self._arrtk.createImage(self.__emplacementAsset + "word/open-word-coputer-soft.png",
                                                          tailleX=90, tailleY=90)
        imgCloseWord = self._arrtk.createImage(self.__emplacementAsset + "word/close-word.png",
                                               tailleX=90, tailleY=90)
        imgReadWord = self._arrtk.createImage(self.__emplacementAsset + "word/read-word.png",
                                              tailleX=90, tailleY=90)

        imgWriteWord = self._arrtk.createImage(self.__emplacementAsset + "word/write-word.png",
                                               tailleX=90, tailleY=90)

        # Images pour la frame Projet
        imgCreateFileProjet = self._arrtk.createImage(self.__emplacementAsset + "project/create-file-project.png",
                                                      tailleX=90, tailleY=90)
        imgCreateProject = self._arrtk.createImage(self.__emplacementAsset + "project/create-projet.png",
                                                   tailleX=90, tailleY=90)
        imgOpenFileProjet = self._arrtk.createImage(self.__emplacementAsset + "project/open-file-project.png",
                                                    tailleX=90, tailleY=90)
        imgOpenProjet = self._arrtk.createImage(self.__emplacementAsset + "project/open-project.png",
                                                tailleX=90, tailleY=90)
        imgSetTypeProjet = self._arrtk.createImage(self.__emplacementAsset + "project/setType-project.png",
                                                   tailleX=90, tailleY=90)
        imgTaskSayProjet = self._arrtk.createImage(self.__emplacementAsset + "project/task-say.png",
                                                   tailleX=90, tailleY=90)
        imgTaskViewProjet = self._arrtk.createImage(self.__emplacementAsset + "project/view-task-project.png",
                                                    tailleX=90, tailleY=90)
        imgCloseProjet = self._arrtk.createImage(self.__emplacementAsset + "project/close-project.png",
                                                 tailleX=90, tailleY=90)

        # Frames
        self.__fAcceuil = self._arrtk.createFrame(self._screen)
        self.__fDock = self._arrtk.createFrame(self._screen, bg="grey", height=70)
        self.__fTableur = self._arrtk.createFrame(self._screen)
        self.__fTableurNoOpen = self._arrtk.createFrame(self._screen)
        self.__fWord = self._arrtk.createFrame(self._screen)
        self.__fWordNoOpen = self._arrtk.createFrame(self._screen)
        self.__fProjet = self._arrtk.createFrame(self._screen)
        self.__fProjetNoOpen = self._arrtk.createFrame(self._screen)

        self.__frameManageTableur = self._arrtk.createFrame(self._screen)
        self.__frameAddValeur = self._arrtk.createFrame(self.__frameManageTableur)
        self.__frameAddFormule = self._arrtk.createFrame(self.__frameManageTableur)
        self.__frameReadTableur = self._arrtk.createFrame(self.__frameManageTableur)
        self.__frameDelValeurTableur = self._arrtk.createFrame(self.__frameManageTableur)

        self.__frameManageWord = self._arrtk.createFrame(self._screen)
        self.__fReadWord = self._arrtk.createFrame(self.__frameManageWord)
        self.__fWriteWord = self._arrtk.createFrame(self.__frameManageWord)

        # Widgets dans la frame d'accueil
        labelTitleAcceuil = self._arrtk.createLabel(self.__fAcceuil, text=self._gestionnaire.getConfigFile().name + " : Arrera Work",
                                                    ppolice="Arial", ptaille=25)
        btnArreraTableurAcceuil = self._arrtk.createButton(self.__fAcceuil, width=100,bg=self._btnColor,fg=self._btnTexteColor,
                                                           height=100, image=imgTableurAcceuil,
                                                           command=self.__activeTableur)
        btnArreraWordAcceuil = self._arrtk.createButton(self.__fAcceuil, width=100,bg=self._btnColor,fg=self._btnTexteColor,
                                                        height=100, image=imgWordAcceuil,
                                                        command=self.__activeWord)
        btnArreraProjectAcceuil = self._arrtk.createButton(self.__fAcceuil, width=100,bg=self._btnColor,fg=self._btnTexteColor,
                                                           height=100, image=imgProjectAcceuil,
                                                           command=self.__activeProjet)

        # Widgets dans la frame dock
        btnArreraTableurDock = self._arrtk.createButton(self.__fDock, width=60,bg=self._btnColor,fg=self._btnTexteColor,
                                                        height=60, image=imgTableurDock,
                                                        command=self.__activeTableur)
        btnArreraWordDock = self._arrtk.createButton(self.__fDock, width=60,bg=self._btnColor,fg=self._btnTexteColor,
                                                     height=60, image=imgWordDock,
                                                     command=self.__activeWord)
        btnArreraProjectDock = self._arrtk.createButton(self.__fDock, width=60,bg=self._btnColor,fg=self._btnTexteColor,
                                                        height=60, image=imgProjectDock,
                                                        command=self.__activeProjet)
        btnCloseAcceuilDock = self._arrtk.createButton(self.__fDock, width=60,bg=self._btnColor,fg=self._btnTexteColor,
                                                       height=60, image =imgAnnulerDock,
                                                       command=self.__closeDock)

        # Widgets du frame Tableur
        labelTitleNoOpenTableur = self._arrtk.createLabel(self.__fTableurNoOpen, text="Travail sur un tableur",
                                                          ppolice="Arial", ptaille=25)
        btnOpenTableur = self._arrtk.createButton(self.__fTableurNoOpen, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                  image=imgOpenTableur, command=self.__openTableur)
        labelTitleTableur = self._arrtk.createLabel(self.__fTableur, text="Travail sur un tableur",
                                                    ppolice="Arial", ptaille=25)
        btnOpenTableurWithComputer = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                              image=imgOpenTableurCoputerSoft,
                                                              command=self.__openTableurCoputerSoft)
        btnCloseTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                   image=imgCloseTableur, command=self.__closeTableur)

        btnAddValeurTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                       image=imgAddValeur, command=self.__viewAddValeurTableur)
        btnAddMoyenneTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                        image=imgAddMoyenne, command=self.__viewMoyenneTableur)
        btnAddSommeTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                      image=imgAddSomme, command=self.__viewSommeTableur)
        btnAddComptageTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                         image=imgAddComptage, command=self.__viewComptageTableur)
        btnAddMinimumTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                        image=imgAddMinimum, command=self.__viewMinimumTableur)
        btnAddMaximumTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                        image=imgAddMaxmum, command=self.__viewMaximumTableur)
        btnAffichageTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                       image=imgViewTableur, command=self.__readTableur)
        btnSupprDataTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                       image=imgSupprValeur,
                                                       command=self.__viewDelValeurTableur)

        # Widgets dans la frame Word
        labelTitleNoOpenWord = self._arrtk.createLabel(self.__fWordNoOpen, text="Travail sur un document Word",
                                                       ppolice="Arial", ptaille=25)
        btnOpenWord = self._arrtk.createButton(self.__fWordNoOpen, width=90, height=90, image=imgOpenWord,bg=self._btnColor,fg=self._btnTexteColor,
                                               command=self.__openWord)

        labelTitleWord = self._arrtk.createLabel(self.__fWord, text="Travail sur un document Word",
                                                 ppolice="Arial", ptaille=25)
        btnOpenWordWithComputer = self._arrtk.createButton(self.__fWord, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                           image=imgOpenWordWithComputer, command=self.__openWordCoputerSoft)
        btnEditWord = self._arrtk.createButton(self.__fWord, width=90, height=90, image=imgWriteWord, bg=self._btnColor, fg=self._btnTexteColor,
                                               command=self.__viewEditWord)
        btnViewReadWord = self._arrtk.createButton(self.__fWord, width=90, height=90, bg=self._btnColor, fg=self._btnTexteColor,
                                               image=imgReadWord, command=self.__viewReadWord)

        btnCloseWord = self._arrtk.createButton(self.__fWord, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                image=imgCloseWord, command=self.__closeWord)

        # Manage Word
        labelTitleReadWord = self._arrtk.createLabel(self.__fReadWord, text="Lecture du document Word",
                                                        ppolice="Arial", ptaille=25, pstyle="bold")
        wScrollText,self.__textReadWord = self._arrtk.createTextBoxScrolled(self.__fReadWord)
        btnQuitReadWord = self._arrtk.createButton(self.__fReadWord, ppolice="Arial", ptaille=20, pstyle="bold",
                                                   text="Quitter", bg=self._btnColor, fg=self._btnTexteColor,
                                                   command=self.__quitReadWord)
        btnReadWord = self._arrtk.createButton(self.__fReadWord, ppolice="Arial", ptaille=20, pstyle="bold",
                                                text="Lire", bg=self._btnColor, fg=self._btnTexteColor,
                                               command=self.__readWord)

        labelEditWord = self._arrtk.createLabel(self.__fWriteWord, text="Ecriture dans le document Word",
                                                    ppolice="Arial", ptaille=25, pstyle="bold")
        wScrollEditText, self.__textEditWord = self._arrtk.createTextBoxScrolled(self.__fWriteWord)
        btnQuitEditWord = self._arrtk.createButton(self.__fWriteWord, ppolice="Arial", ptaille=20, pstyle="bold",
                                                    text="Quitter", bg=self._btnColor, fg=self._btnTexteColor,
                                                    command=self.__quitEditWord)
        btnWriteWord = self._arrtk.createButton(self.__fWriteWord, ppolice="Arial", ptaille=20, pstyle="bold",
                                                    text="Ecrire", bg=self._btnColor, fg=self._btnTexteColor,
                                                command=self.__writeWord)



        # Widget dans la frame Projet
        # No OPEN
        labelTitleNoOpenProjet = self._arrtk.createLabel(self.__fProjetNoOpen, text="Travail sur un projet",
                                                         ppolice="Arial", ptaille=25)

        btnOpenProjet = self._arrtk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                 image=imgOpenProjet,bg=self._btnColor,fg=self._btnTexteColor,
                                                 command=self.__openProjet)

        btnCreateProjet = self._arrtk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                   image=imgCreateProject,bg=self._btnColor,fg=self._btnTexteColor,
                                                   command=self.__windowsNameNewProjet)

        # OPEN
        labelTitleProjet = self._arrtk.createLabel(self.__fProjet, text="Travail sur un projet",
                                                   ppolice="Arial", ptaille=25)
        btnAddTypeProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                    image=imgSetTypeProjet, command=self.__windowsTypeFileProjet)
        btnCreateFileProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgCreateFileProjet,
                                                       command=self.__windowsCreateFileProjet,bg=self._btnColor,fg=self._btnTexteColor)
        btnOpenFileProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgOpenFileProjet,
                                                     command=self.__openFileProjet,bg=self._btnColor,fg=self._btnTexteColor)
        btnViewTaskProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgTaskViewProjet,
                                                     command=self.openTaskProjet, bg=self._btnColor, fg=self._btnTexteColor)
        btnSayAllTaskProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90,bg=self._btnColor,fg=self._btnTexteColor,
                                                       image=imgTaskSayProjet, command=self.__sayTaskProjet)

        btnCloseProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgCloseProjet,
                                                  command=self.__closeProjet,bg=self._btnColor,fg=self._btnTexteColor)

        # frameTableurAdd
        # frameAddValeur
        labelTitleAddValeur = self._arrtk.createLabel(self.__frameAddValeur, text="Ajout d'une valeur",
                                                        ppolice="Arial", ptaille=25,pstyle="bold")
        wECaseValeur,self.__eCaseAddValeur = self._arrtk.createEntryLegend(self.__frameAddValeur,text="Case de la valeur : ",
                                                     ptaille=20,ppolice="Arial",gridUsed=True)
        wEValueValeur,self.__eValueAddValeur = self._arrtk.createEntryLegend(self.__frameAddValeur,text="Valeur : ",
                                                        ptaille=20,ppolice="Arial",gridUsed=True)
        btnAddValeur = self._arrtk.createButton(self.__frameAddValeur,ppolice="Arial",ptaille=25,pstyle="bold",
                                                  text="Ajouter la valeur",bg=self._btnColor,fg=self._btnTexteColor,
                                                command=self.__addValeurTableur)
        btnCancelAddValeur = self._arrtk.createButton(self.__frameAddValeur, ppolice="Arial", ptaille=25, pstyle="bold",
                                                      text="Annuler", bg=self._btnColor, fg=self._btnTexteColor,
                                                      command=self.__disableManageTableur)
        # frameAddFormule
        lTitleAddFormule = self._arrtk.createLabel(self.__frameAddFormule, text="Ajout d'une formule",
                                                            ppolice="Arial", ptaille=25, pstyle="bold")
        menuChoixFormule = self._arrtk.createOptionMenu(self.__frameAddFormule,value=self.__listFormule,
                                                        var=self.__varFormule,bg=self._btnColor,fg=self._btnTexteColor,
                                                        police="Arial",taille=20)
        wECaseStart,self.__eCaseStartFormule = self._arrtk.createEntryLegend(self.__frameAddFormule,text="Case de debut : ",
                                                        ptaille=20,ppolice="Arial",gridUsed=True)
        wECaseEnd,self.__eCaseEndFormule = self._arrtk.createEntryLegend(self.__frameAddFormule,text="Case de fin : ",
                                                        ptaille=20,ppolice="Arial",gridUsed=True)
        wECaseDest,self.__eCaseDestFormule = self._arrtk.createEntryLegend(self.__frameAddFormule,text="Case de destination : ",
                                                        ptaille=20,ppolice="Arial",gridUsed=True)
        btnAddFormule = self._arrtk.createButton(self.__frameAddFormule,ppolice="Arial",ptaille=20,pstyle="bold",
                                                    text="Ajouter la formule",bg=self._btnColor,fg=self._btnTexteColor,
                                                 command=self.__addFormuleTableur)
        btnCancelAddFormule = self._arrtk.createButton(self.__frameAddFormule, ppolice="Arial", ptaille=20, pstyle="bold",
                                                       text="Annuler", bg=self._btnColor, fg=self._btnTexteColor,
                                                       command=self.__disableManageTableur)
        # frameReadTableur
        labelTitleReadTableur = self._arrtk.createLabel(self.__frameReadTableur, text="Lecture du tableur",
                                                         ppolice="Arial", ptaille=25, pstyle="bold")
        self.__fScrolledRead = self._arrtk.createScrollFrame(self.__frameReadTableur)
        btnQuitReadTableur = self._arrtk.createButton(self.__frameReadTableur, ppolice="Arial", ptaille=20, pstyle="bold",
                                                      text="Quitter", bg=self._btnColor, fg=self._btnTexteColor,
                                                      command=self.__disableManageTableur)
        # frameDelValeurTableur
        labelTitleDelTableur = self._arrtk.createLabel(self.__frameDelValeurTableur, text="Suppression de valeur",
                                                        ppolice="Arial", ptaille=25, pstyle="bold")
        wECaseDel,self.__eCaseDel = self._arrtk.createEntryLegend(self.__frameDelValeurTableur,text="Case a supprimer : ",
                                                                    ptaille=20,ppolice="Arial",gridUsed=True)
        btnDelTableur = self._arrtk.createButton(self.__frameDelValeurTableur, ppolice="Arial", ptaille=20, pstyle="bold",
                                                 text="Supprimer la valeur", bg=self._btnColor, fg=self._btnTexteColor,
                                                 command=self.__delValeurTableur)
        btnCancelDebTableur = self._arrtk.createButton(self.__frameDelValeurTableur, ppolice="Arial", ptaille=20, pstyle="bold",
                                                         text="Annuler", bg=self._btnColor, fg=self._btnTexteColor,
                                                            command=self.__disableManageTableur)

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

        self.__frameManageTableur.grid_rowconfigure(0, weight=1)
        self.__frameManageTableur.grid_columnconfigure(0, weight=1)

        self.__frameAddValeur.columnconfigure(0, weight=1)
        self.__frameAddValeur.columnconfigure(1, weight=1)
        self.__frameAddValeur.rowconfigure(1, minsize=5)
        self.__frameAddValeur.rowconfigure(4, weight=1)

        self.__frameAddFormule.columnconfigure(0, weight=1)
        self.__frameAddFormule.columnconfigure(1, weight=1)
        self.__frameAddFormule.rowconfigure(5, weight=1)

        self.__frameReadTableur.columnconfigure(0, weight=1)
        self.__frameReadTableur.rowconfigure(1, weight=1)

        self.__frameDelValeurTableur.columnconfigure(0, weight=1)
        self.__frameDelValeurTableur.columnconfigure(1, weight=1)
        self.__frameDelValeurTableur.rowconfigure(1, weight=1)
        self.__frameDelValeurTableur.rowconfigure(3, weight=1)

        self.__frameManageWord.grid_rowconfigure(0, weight=1)
        self.__frameManageWord.grid_columnconfigure(0, weight=1)

        self.__fReadWord.grid_columnconfigure(0, weight=1, uniform="buttons")
        self.__fReadWord.grid_columnconfigure(1, weight=1, uniform="buttons")
        self.__fReadWord.grid_rowconfigure(0, weight=0)
        self.__fReadWord.grid_rowconfigure(1, weight=1)
        self.__fReadWord.grid_rowconfigure(2, weight=0)

        self.__fWriteWord.grid_columnconfigure(0, weight=1, uniform="buttons")
        self.__fWriteWord.grid_columnconfigure(1, weight=1, uniform="buttons")
        self.__fWriteWord.grid_rowconfigure(0, weight=0)
        self.__fWriteWord.grid_rowconfigure(1, weight=1)
        self.__fWriteWord.grid_rowconfigure(2, weight=0)


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


        btnAddValeurTableur.grid(row=1, column=1, padx=20, pady=20)
        btnAddMoyenneTableur.grid(row=1, column=2, padx=20, pady=20)
        btnAddSommeTableur.grid(row=2, column=0, padx=20, pady=20)
        btnAddComptageTableur.grid(row=2, column=1, padx=20, pady=20)
        btnAddMinimumTableur.grid(row=2, column=2, padx=20, pady=20)
        btnAddMaximumTableur.grid(row=3, column=0, padx=20, pady=20)
        btnAffichageTableur.grid(row=3, column=1, padx=20, pady=20)
        btnSupprDataTableur.grid(row=3, column=2, padx=20, pady=20)
        btnCloseTableur.grid(row=4, column=0, padx=20, pady=20)
        #btnReadTableur.grid(row=4, column=1, padx=20, pady=20)

        labelTitleNoOpenWord.grid(row=0, column=1, sticky="n")
        btnOpenWord.grid(row=2, column=1, sticky="n")

        labelTitleWord.grid(row=0, column=0, columnspan=3, sticky='ew')
        btnViewReadWord.grid(row=1, column=0, padx=20, pady=20)
        btnEditWord.grid(row=1, column=1, padx=20, pady=20)
        btnOpenWordWithComputer.grid(row=1, column=2, padx=20, pady=20)
        btnCloseWord.grid(row=2, column=0, padx=20, pady=20)

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

        labelTitleAddValeur.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 20))
        wECaseValeur.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 10))
        wEValueValeur.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20)
        btnCancelAddValeur.grid(row=5, column=0, sticky="sw", padx=10, pady=10)
        btnAddValeur.grid(row=5, column=1, sticky="se", padx=10, pady=10)

        lTitleAddFormule.grid(row=0, column=0, columnspan=2, sticky="n", padx=10, pady=(10, 6))
        menuChoixFormule.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=(0, 10))
        wECaseStart.grid(row=2, column=0, columnspan=2, sticky="ew", padx=12, pady=(0, 6))
        wECaseEnd.grid(row=3, column=0, columnspan=2, sticky="ew", padx=12, pady=(0, 6))
        wECaseDest.grid(row=4, column=0, columnspan=2, sticky="ew", padx=12)
        btnCancelAddFormule.grid(row=6, column=0, sticky="sw", padx=10, pady=10)
        btnAddFormule.grid(row=6, column=1, sticky="se", padx=10, pady=10)

        labelTitleReadTableur.grid(row=0, column=0, sticky="new", padx=10, pady=(10, 8))
        self.__fScrolledRead.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
        btnQuitReadTableur.grid(row=2, column=0, sticky="sew", padx=10, pady=10)

        labelTitleDelTableur.grid(row=0, column=0, columnspan=2, sticky="n", padx=10, pady=(10, 8))
        wECaseDel.grid(row=2, column=0, columnspan=2, padx=12, pady=6)
        btnCancelDebTableur.grid(row=4, column=0, sticky="sw", padx=10, pady=10)
        btnDelTableur.grid(row=4, column=1, sticky="se", padx=10, pady=10)

        labelTitleReadWord.grid(row=0, column=0, columnspan=2, sticky="ew",padx=8, pady=(8, 4))
        wScrollText.grid(row=1, column=0, columnspan=2, sticky="nsew",padx=8, pady=4)
        btnQuitReadWord.grid(row=2, column=0, sticky="ew",padx=(8, 4), pady=(4, 8))
        btnReadWord.grid(row=2, column=1, sticky="ew",padx=(4, 8), pady=(4, 8))

        labelEditWord.grid(row=0, column=0, columnspan=2, sticky="ew",padx=8, pady=(8, 4))
        wScrollEditText.grid(row=1, column=0, columnspan=2, sticky="nsew",padx=8, pady=4)
        btnQuitEditWord.grid(row=2, column=0, sticky="ew",padx=(8, 4), pady=(4, 8))
        btnWriteWord.grid(row=2, column=1, sticky="ew",padx=(4, 8), pady=(4, 8))


    def activeProjet(self):
        self.active()
        self._mainframe()
        self.__activeProjet()

    def activeTableur(self):
        self.active()
        self._mainframe()
        self.__activeTableur()

    def activeWord(self):
        self.active()
        self._mainframe()
        self.__activeWord()

    def activeAcceuil(self):
        self.active()
        self._mainframe()
        self.__activeAcceuil()

    # Active pour le tableur

    def activeManageTableur(self,mode:int):
        """
        1. Add Valeur
        2. Add Somme
        3. Add Moyenne
        4. Add Comptage
        5. Add Minimum
        6. Add Maximum
        7. Suppr valeur
        """
        self.active()
        self.updateEtat()
        if not self.__tableurOpen:
            return False

        match mode :
            case 1 :
                self.__viewAddValeurTableur()
                return True
            case 2 :
                self.__viewSommeTableur()
                return True
            case 3 :
                self.__viewMoyenneTableur()
                return True
            case 4 :
                self.__viewComptageTableur()
                return True
            case 5 :
                self.__viewMinimumTableur()
                return True
            case 6 :
                self.__viewMaximumTableur()
                return True
            case 7 :
                self.__viewDelValeurTableur()
                return True
            case _ :
                return False

    def activeReadWord(self):
        self.active()
        self.updateEtat()
        if not self.__wordOpen:
            return False
        self.__viewReadWord()
        return True

    def activeWriteWord(self):
        self.active()
        self.updateEtat()
        if not self.__wordOpen:
            return False
        self.__viewEditWord()
        return True

    def activeReadTableur(self):
        self.active()
        self.updateEtat()
        if not self.__tableurOpen:
            return False
        self.__readTableur()
        return True

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
        self._screen.update()

    def __activeTableur(self):
        self.__disabelFrame()
        if not self.__tableurOpen:
            self.__fTableurNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self._screen.update()

    def __activeWord(self):
        self.__disabelFrame()
        if not self.__wordOpen:
            self.__fWordNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fWord.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self._screen.update()

    def __activeProjet(self):
        self.__disabelFrame()

        if not self.__projectOpen:
            self.__fProjetNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fProjet.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self._screen.update()

    # Partie fonctionnelle de l'application

    # Dock

    def __closeDock(self):
        if self.__projectOpen :
            self.__closeProjet()
        elif self.__tableurOpen :
            self.__closeTableur()
        elif self.__wordOpen :
            self.__closeWord()
        else :
            self.__activeAcceuil()

    def updateEtat(self):
        """
        Met à jour l'état des frames en fonction de l'ouverture des outils.
        """
        self.__wordOpen = self._gestionnaire.getGestFNC().getFNCWork().getEtatWord()
        self.__tableurOpen = self._gestionnaire.getGestFNC().getFNCWork().getEtatTableur()
        self.__projectOpen = self._gestionnaire.getGestFNC().getFNCWork().getEtatProject()
        if self.__projectOpen:
            self.__nameProjet = self._gestionnaire.getGestFNC().getFNCWork().getNameProjet()
            self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                   self.__nameProjet,
                                                   self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())
        else :
            self.__nameProjet = None
            self.__guiTaskProject = None

    # Partie Tableur
    def __openTableur(self):
        """
        Ouvre le tableur.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openTableur()
        self.updateEtat()
        self.__activeTableur()

    def __openTableurCoputerSoft(self):
        """
        Ouvre le tableur avec un logiciel de tableur.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openTableurOs()

    def __closeTableur(self):
        self.__disableManageTableur()
        self._gestionnaire.getGestFNC().getFNCWork().closeTableur()
        self.updateEtat()
        self.__activeTableur()

    def __viewAddValeurTableur(self):
        self.__disabelFrame()
        self.__disableManageTableur()
        self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__frameAddValeur.grid(row=0, column=0, sticky="nsew")
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.__eCaseAddValeur.delete(0,ctk.END)
        self.__eValueAddValeur.delete(0,ctk.END)
        self._screen.update()

    def __addValeurTableur(self):
        case = self.__eCaseAddValeur.get()
        valeur = self.__eValueAddValeur.get()
        if not case or not valeur:
            showerror("Erreur", "La case et la valeur ne peuvent pas être vide.")
            return
        if self._gestionnaire.getGestFNC().getFNCWork().addValeurOnTableur(case,valeur):
            showinfo("Succès", f"La valeur {valeur} a été ajoutée à la case {case}.")
            self.__disableManageTableur()
        else:
            showerror("Erreur", "Une erreur est survenue lors de l'ajout de la valeur.")
            self.__disableManageTableur()

    def __viewAddFormuleTableur(self):
        self.__disabelFrame()
        self.__disableManageTableur()
        self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__frameAddFormule.grid(row=0, column=0, sticky="nsew")
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.__eCaseDestFormule.delete(0,ctk.END)
        self.__eCaseEndFormule.delete(0,ctk.END)
        self.__eCaseStartFormule.delete(0,ctk.END)

    def __viewMoyenneTableur(self):
        self.__viewAddFormuleTableur()
        self.__varFormule.set(self.__listFormule[1])
        self._screen.update()

    def __viewSommeTableur(self):
        self.__viewAddFormuleTableur()
        self.__varFormule.set(self.__listFormule[0])
        self._screen.update()

    def __viewComptageTableur(self):
        self.__viewAddFormuleTableur()
        self.__varFormule.set(self.__listFormule[2])
        self._screen.update()

    def __viewMinimumTableur(self):
        self.__viewAddFormuleTableur()
        self.__varFormule.set(self.__listFormule[3])
        self._screen.update()

    def __viewMaximumTableur(self):
        self.__viewAddFormuleTableur()
        self.__varFormule.set(self.__listFormule[4])
        self._screen.update()

    def __addFormuleTableur(self):
        caseDest = self.__eCaseDestFormule.get()
        caseEnd = self.__eCaseEndFormule.get()
        caseStart = self.__eCaseStartFormule.get()
        formule = self.__varFormule.get()

        if not caseDest or not caseEnd or not caseStart or not formule:
            showerror("Erreur", "Les cases et la formule ne peuvent pas être vide.")
            return

        if formule == self.__listFormule[0]:
            if self._gestionnaire.getGestFNC().getFNCWork().addSommeOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule SOMME a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout de la somme.")
        elif formule == self.__listFormule[1]:
            if self._gestionnaire.getGestFNC().getFNCWork().addMoyenneOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule MOYENNE a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout de la moyenne.")
        elif formule == self.__listFormule[2]:
            if self._gestionnaire.getGestFNC().getFNCWork().addComptageOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule COMPTAGE a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout du comptage.")
        elif formule == self.__listFormule[3]:
            if self._gestionnaire.getGestFNC().getFNCWork().addMinimumOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule MINIMUM a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout du minimum.")
        elif formule == self.__listFormule[4]:
            if self._gestionnaire.getGestFNC().getFNCWork().addMaximumOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule MAXIMUM a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout du maximum.")
        else :
            showerror("Erreur", "La formule sélectionnée n'est pas valide.")

        self.__disableManageTableur()


    def __readTableur(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readTableur():
            self.__disabelFrame()
            self.__disableManageTableur()
            self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
            self.__frameReadTableur.grid(row=0, column=0, sticky="nsew")
            self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

            for w in self.__fScrolledRead.winfo_children():
                w.destroy()

            data = self._gestionnaire.getGestFNC().getFNCWork().getReadTableur()
            if not data:
                lbl = self._arrtk.createLabel(self.__fScrolledRead, text="Le tableur est vide.",
                                              ppolice="Arial", ptaille=15)
                lbl.pack(pady=10)
            else:
                for row in data:
                    lbl = self._arrtk.createLabel(self.__fScrolledRead, text=row+"\n",
                                                  ppolice="Arial", ptaille=15,justify="left")
                    lbl.configure(anchor="w")
                    lbl.pack(side="top", anchor="w", fill="x", padx=5, pady=2)

        else :
            self.__disabelFrame()
            self.__disableManageTableur()




    def __viewDelValeurTableur(self):
        self.__disabelFrame()
        self.__disableManageTableur()
        self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__frameDelValeurTableur.grid(row=0, column=0, sticky="nsew")
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.__eCaseDel.delete(0,ctk.END)
        self._screen.update()

    def __delValeurTableur(self):
        case = self.__eCaseDel.get()
        if not case:
            showerror("Erreur", "La case ne peut pas être vide.")
            return
        if self._gestionnaire.getGestFNC().getFNCWork().delValeur(case):
            showinfo("Succès", f"La valeur de la case {case} a été supprimée.")

        self.__disableManageTableur()

    def __disableManageTableur(self):
        self.__frameManageTableur.grid_forget()
        self.__frameAddValeur.grid_forget()
        self.__frameAddFormule.grid_forget()
        self.__frameReadTableur.grid_forget()
        self.__frameDelValeurTableur.grid_forget()
        self.__fDock.grid_forget()
        self.__disabelFrame()
        self.__activeTableur()


    # Partie Word
    def __openWord(self):
        """
        Ouvre le document Word.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openWord()
        self.updateEtat()
        self.__activeWord()

    def __openWordCoputerSoft(self):
        """
        Ouvre le document Word avec un logiciel de traitement de texte.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openWordOs()

    def __closeWord(self):
        """
        Ferme le document Word.
        """
        self.__disableManageWord()
        self._gestionnaire.getGestFNC().getFNCWork().closeWord()
        self.updateEtat()
        self.__activeWord()

    def __viewEditWord(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readWord():

            self.__disabelFrame()
            self.__disableManageWord()
            self.__frameManageWord.grid(row=0, column=0, columnspan=3, sticky='nsew')
            self.__fWriteWord.grid(row=0, column=0, sticky="nsew")
            self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
            self.__textEditWord.configure(state="normal")

            text = self._gestionnaire.getGestFNC().getFNCWork().getReadWord()
            if text :
                self.__textEditWord.delete(1.0, ctk.END)
                self.__textEditWord.insert(ctk.END, text)
        else :
            showinfo("Erreur", "Une erreur est survenue.")

    def __writeWord(self):
        newTexte = self.__textEditWord.get(1.0, ctk.END)
        if self._gestionnaire.getGestFNC().getFNCWork().writeWordEcrase(newTexte):
            showinfo("Succès", "Le document a été mis à jour.")
        else :
            showerror("Erreur", "Une erreur est survenue lors de la mise à jour du document.")
        self.__disableManageWord()

    def __quitEditWord(self):
        self.__disableManageWord()

    def __viewReadWord(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readWord():
            text = self._gestionnaire.getGestFNC().getFNCWork().getReadWord()
            if text :
                self.__disabelFrame()
                self.__disableManageWord()
                self.__frameManageWord.grid(row=0, column=0, columnspan=3, sticky='nsew')
                self.__fReadWord.grid(row=0, column=0, sticky="nsew")
                self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
                self.__textReadWord.configure(state="normal")
                self.__textReadWord.delete(1.0, ctk.END)
                self.__textReadWord.insert(ctk.END, text)
                self.__textReadWord.configure(state="disabled")
            else :
                showinfo("Info", "Le document est vide.")
        else :
            showinfo("Erreur", "Une erreur est survenue lors de la lecture du document.")

    def __quitReadWord(self):
        self.__disableManageWord()

    def __readWord(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readWord():
            text = self._gestionnaire.getGestFNC().getFNCWork().getReadWord()
            if text :
                self._gestionnaire.getArrVoice().say(text)
            else :
                showinfo("Info", "Le document est vide.")
        else :
            showinfo("Erreur", "Une erreur est survenue lors de la lecture du document.")

    def __disableManageWord(self):
        self.__frameManageWord.grid_forget()
        self.__fReadWord.grid_forget()
        self.__fWriteWord.grid_forget()
        self.__fDock.grid_forget()
        self.__disabelFrame()
        self.__activeWord()


    # Partie Projet

    def __openProjet(self):
        """
        Ouvre le projet.
        """
        emplacementProjects = self._gestionnaire.getUserConf().getWorkFolder()

        dossier = askdirectory(initialdir=emplacementProjects,
                                          title="Selection du projet")
        dossier = (dossier.replace
                   (emplacementProjects,"").replace
                   ("/","").replace("\\","")).strip()
        self._gestionnaire.getGestFNC().getFNCWork().openProjet(dossier)
        self.updateEtat()
        self.__activeProjet()
        self.__nameProjet = dossier
        self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                  self.__nameProjet,
                                                  self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())

    def __windowsTexteProjet(self,title:str, texte:str,fnc:callable):
        screen = self._arrtk.aTopLevel(width=225, height=100,resizable=False,title=title)
        self._arrtk.placeTopCenter(self._arrtk.createLabel(screen, text=texte,
                                                           ppolice="Arial", ptaille=15))
        self.__entryNameProjet = self._arrtk.createEntry(screen)
        self._arrtk.placeCenter(self.__entryNameProjet)
        self._arrtk.placeBottomCenter(self._arrtk.createButton(screen, text="Valider",
                                                               command= lambda :fnc(screen)))

    def __windowsNameNewProjet(self):
        """
        Crée un nouveau projet.
        """
        self.__windowsTexteProjet("Création d'un projet","Nom du nouveau projet",self.__createNewProjet)


    def __sayTaskProjet(self):
        """
        Ouvre une fenêtre pour dire une tâche dans le projet.
        """
        pass

    def __createNewProjet(self,screen:ctk.CTkToplevel):
        name = self.__entryNameProjet.get()
        screen.destroy()
        if not name:
            showerror("Erreur", "Le nom du projet ne peut pas être vide.")
            return

        self._gestionnaire.getGestFNC().getFNCWork().createProjet(name)
        self.updateEtat()
        self.__activeProjet()
        self.__nameProjet = name
        self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                               self.__nameProjet,
                                               self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())

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

        self._gestionnaire.getGestFNC().getFNCWork().addTypeProjet(type_file)

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

        self._arrtk.placeTopCenter(self._arrtk.createLabel(screen, text="Creation d'un fichier dans le projet",
                                                           ppolice="Arial", ptaille=15))
        self.__entryNameFile = self._arrtk.createEntry(screen)
        self._arrtk.placeLeftCenter(self.__entryNameFile)
        self._arrtk.placeRightCenter(self._arrtk.createOptionMenu(screen, value=listType, var=self.__var))
        self.__var.set(listType[0])
        self._arrtk.placeBottomCenter(self._arrtk.createButton(screen, text="Valider",
                                                               command=lambda: self.__createFileProjet(screen)))

    def __createFileProjet(self, screen: ctk.CTkToplevel):
        name_file = self.__entryNameFile.get()
        if not name_file:
            showerror("Erreur", "Imposible de créer un fichier sans nom.")
            return

        type_file = self.__var.get()
        screen.destroy()


    def __openFileProjet(self):
        """
        Ouvre un fichier de projet.
        """
        emplacementProjects = self._gestionnaire.getUserConf().getWorkFolder()+self.__nameProjet+"/"
        file_path = askopenfilename(initialdir=emplacementProjects,
                                               title="Selection du fichier du projet",
                                               filetypes=[("All files", "*.*")])
        if file_path:
            file_name = file_path.split("/")[-1]
            self.updateEtat()
            self.__activeProjet()
            self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                   self.__nameProjet,
                                                   self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())

    def openTaskProjet(self):
        """
        Ouvre une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.active()
            return True
        else :
            return False

    def openTaskProjetAdd(self):
        """
        Ouvre une fenêtre pour ajouter une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.activeAdd()
            return True
        else :
            return False


    def openTaskProjetdel(self):
        """
        Ouvre une fenêtre pour ajouter une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.activeDel()
            return True
        else :
            return False

    def openTaskProjetfinish(self):
        """
        Ouvre une fenêtre pour ajouter une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.activeFinish()
            return True
        else :
            return False


    def __closeProjet(self):
        """
        Ferme le projet.
        """
        self._gestionnaire.getGestFNC().getFNCWork().closeProjet()
        self.__activeAcceuil()
        self.__nameProjet = None
        del self.__guiTaskProject
        self.__guiTaskProject = None
        self.updateEtat()