from ObjetsNetwork.gestion import *
from arreraSoftware.fonctionTache import *
from tkinter import filedialog
from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from objet.arreradocument import *
from objet.arreratableur import *
from librairy.travailJSON import *
from librairy.dectectionOS import *
import subprocess
import re
import os
from pathlib import Path


class fncArreraWork:
    def __init__(self, fncDate: fncDate, gestion: gestionNetwork, neuronfile: jsonWork, dectOs: OS):
        # Objet 
        self.__dectOs = dectOs
        self.__fncDate = fncDate
        self.__configFile = neuronfile
        # Variable etat ouverture fichier
        self.__tableurOpen = False
        self.__wordOpen = False
        self.__projectOpen = False
        # Varriable des objet 
        self.__objTableur = None
        self.__objWord = None
        # File JSON Project
        self.__jsonFileProject = None
        # Varriable de nom du fichier
        self.__fileTableur = ""
        self.__fileWord = ""
        # Chargement des variable
        self.__nameAssistant = self.__configFile.lectureJSON("name")
        self.__iconAssistant = self.__configFile.lectureJSON("iconAssistant")
        self.__guiColor = self.__configFile.lectureJSON("interfaceColor")
        self.__textColor = self.__configFile.lectureJSON("interfaceTextColor")
        # Varriable Projet
        self.__folderProject = ""
        self.__lastCreateFile = ""
        self.__listFileProjet = []
        self.__fncTaskProjet = None  # Correspont au tache du projet
        self.__listTaskProjetToday = []
        self.__listTaskProjetTowmorow = []
        # Recupertion de l'emplacement de travail de assistant
        self.__gestionnaireNeuron = gestion

    def openTableur(self):
        if (self.__tableurOpen == False):
            # Demande de l'emplacement du fichier
            showinfo("Work", "Choisissez votre fichier exel")
            emplacementFile = filedialog.askopenfilename(
                defaultextension='.xlsx',
                filetypes=[("Fichiers Excel", "*.xlsx")])
            self.__fileTableur = emplacementFile
            if (emplacementFile == ""):
                showwarning("Work", "Aucun fichier selectionner")
                return False
            else:
                self.__objTableur = CArreraTableur(emplacementFile)
                showinfo("Work", "Exel ouvert")
                self.__tableurOpen = True
                return True
        else:
            return False

    def openTableurDirectly(self, file: str):
        if (self.__tableurOpen == False and file != ""):
            self.__fileTableur = file
            self.__objTableur = CArreraTableur(file)
            self.__tableurOpen = True
            return True
        else:
            return False

    def openWord(self):
        if (self.__wordOpen == False):
            # Demande de l'emplacement du fichier
            showinfo("Work", "Choisissez votre fichier word")
            emplacementFile = filedialog.askopenfilename(
                defaultextension='.xlsx',
                filetypes=[('Tout les fichier', '*.*'),
                           ('Fichiers Word', '*.docx'),
                           ("Texte OpenDocument", "*.odt")])
            self.__fileWord = emplacementFile
            if (emplacementFile == ""):
                showwarning("Work", "Aucun fichier selectionner")
                return False
            else:
                self.__objWord = CArreraDocx(emplacementFile)
                showinfo("Work", "Word ouvert")
                self.__wordOpen = True
                return True
        else:
            return False

    def openWordDirectly(self, file: str):
        if (self.__wordOpen == False and file != ""):
            self.__fileWord = file
            self.__objWord = CArreraDocx(file)
            self.__wordOpen = True
            return True
        else:
            return False

    def __setFormuleTableur(self, mode: int, case1: str, case2: str, caseDest: str):
        """
        1: Somme
        2: Moyenne
        3: Comptage
        4: Minimun
        5: Maximun
        """
        if (self.__tableurOpen == True):
            match mode:
                case 1:
                    self.__objTableur.somme(caseDest, case1, case1)
                    self.__objTableur.saveFile()
                    return True
                case 2:
                    self.__objTableur.moyenne(caseDest, case1, case2)
                    self.__objTableur.saveFile()
                    return True
                case 3:
                    self.__objTableur.comptage(caseDest, case1, case2)
                    self.__objTableur.saveFile()
                    return True
                case 4:
                    self.__objTableur.minimun(caseDest, case1, case2)
                    self.__objTableur.saveFile()
                    return True
                case 5:
                    self.__objTableur.maximun(caseDest, case1, case2)
                    self.__objTableur.saveFile()
                    return True
                case other:
                    return False
        else:
            return False

    def readTableur(self):
        if (self.__tableurOpen == True):
            listSorti = []
            contenu = self.__objTableur.read()
            for cell_position, cell_value in contenu.items():
                listSorti.append("Cellule " + str(cell_position) + " : " + str(cell_value))
            return listSorti
        else:
            return ["error", ""]

    def setValeurTableur(self, case: str, valeur):
        if ((self.__tableurOpen == True) and (case != "")):
            self.__objTableur.write(case, valeur)
            self.__objTableur.saveFile()
            return True
        else:
            return False

    def closeTableur(self):
        if (self.__tableurOpen == True):
            self.__objTableur.saveFile()
            self.__objTableur.closeFile()
            del self.__objTableur
            self.__objTableur = None
            self.__fileTableur = ""
            self.__tableurOpen = False
            return True
        else:
            return False

    def writeDocxFile(self):
        if self.__wordOpen:
            screen = Toplevel()
            screen.title("Ecriture dans un word")
            screen.geometry("500x200")
            screen.resizable(False, False)
            self.__entryTextWord = Entry(screen)
            self.__entryTextWord.place(relx=0.5, rely=0.5, anchor="center")
            Button(screen, text="Valider", command=lambda: self.__writeWord(screen)).place(relx=0.5, rely=1, anchor='s')
            return True
        else:
            return False

    def __writeWord(self, screen: Toplevel):
        text = self.__entryTextWord.get()
        screen.destroy()
        self.__entryTextWord.delete(0, END)
        if (self.__wordOpen == True):
            sortie = self.__objWord.writeEcrase(text)
            if (sortie == True):
                showinfo("Word", "Ecriture reussie")
                return True
            else:
                showerror("Word", "Ecriture non reussie")
                return False

    def readDocxFile(self):
        if (self.__wordOpen == True):
            return self.__objWord.read()
        else:
            return "error"

    def closeDocx(self):
        if (self.__wordOpen == True):
            del self.__objWord
            self.__objWord = None
            self.__fileWord = ""
            self.__wordOpen = False
            return True
        else:
            return False

    def getEtatTableur(self):
        return self.__tableurOpen

    def getEtatWord(self):
        return self.__wordOpen

    def getEtatProject(self):
        return self.__projectOpen

    def getNameFileTableur(self):
        return self.__fileTableur

    def getNameFileWord(self):
        return self.__fileWord

    def tkAddValeurParole(self):
        if (self.__tableurOpen == True):
            tab = Toplevel()
            tab.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant + " Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300, 100)
            tab.minsize(300, 100)
            frameCase = Frame(tab, bg=self.__guiColor)
            frameValeur = Frame(tab, bg=self.__guiColor)
            # Declaration des widget
            labelCase = Label(frameCase, text="Case :", font=("arial", "15"),
                              bg=self.__guiColor, fg=self.__textColor)
            entryCase = Entry(frameCase, font=("arial", "15"), relief=SOLID)
            labelValeur = Label(frameValeur, text="Valeur :", font=("arial", "15"),
                                bg=self.__guiColor, fg=self.__textColor)
            entryValeur = Entry(frameValeur, font=("arial", "15"), relief=SOLID)
            btnValider = Button(tab, text="Valider", font=("arial", "15"), bg=self.__guiColor,
                                fg=self.__textColor,
                                command=lambda: self.__fncAddValeurParole(tab, entryValeur, entryCase))
            # Affichage de widget
            labelCase.pack(side="left")
            labelValeur.pack(side="left")
            entryCase.pack(side="right")
            entryValeur.pack(side="right")

            frameCase.pack()
            frameValeur.pack()

            btnValider.pack(side="bottom")

            return True
        else:
            showerror("Work", "Il n'a pas de tableur ouvert")
            return False

    def tkSuppValeurParole(self):
        if (self.__tableurOpen == True):
            tab = Toplevel()
            tab.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant + " Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300, 100)
            tab.minsize(300, 100)
            frameCase = Frame(tab, bg=self.__guiColor)
            # Declaration des widget
            labelCase = Label(frameCase, text="Case :", font=("arial", "15"),
                              bg=self.__guiColor, fg=self.__textColor)
            entryCase = Entry(frameCase, font=("arial", "15"), relief=SOLID)
            btnValider = Button(tab, text="Valider", font=("arial", "15"), bg=self.__guiColor,
                                fg=self.__textColor, command=lambda: self.__fncSupprValeurParole(tab, entryCase))
            # Affichage de widget
            labelCase.pack(side="left")
            entryCase.pack(side="right")

            frameCase.pack()

            btnValider.pack(side="bottom")

            return True
        else:
            showerror("Work", "Il n'a pas de tableur ouvert")
            return False

    def __fncAddValeurParole(self, w: Toplevel, evaleur: Entry, ecase: Entry):
        valeur = evaleur.get()
        case = ecase.get()
        if (case == ""):
            showerror("Work", "Vous avez pas définie de case.")
        else:
            self.__addValeur(case, valeur)

        evaleur.delete(0, END)
        ecase.delete(0, END)
        w.destroy()

    def __fncSupprValeurParole(self, w: Toplevel, ecase: Entry):
        case = ecase.get()
        if (case == ""):
            showerror("Work", "Vous avez pas définie de case.")
        else:
            self.__supprValeur(case)

        ecase.delete(0, END)
        w.destroy()

    def __addValeur(self, case: str, valeur):
        if (self.__tableurOpen == True):
            if (self.__verifTableurCase(case) == True):
                if (str(valeur).isdigit() == True):
                    self.__objTableur.write(case, int(valeur))
                else:
                    self.__objTableur.write(valeur)
                self.__objTableur.saveFile()
                showinfo("Work", "Valeur ecrite")
            else:
                showerror("Work", "La case n'est pas valide")
        else:
            showerror("Work", "Il n'a pas de tableur ouvert")

    def __supprValeur(self, case: str):
        if (self.__tableurOpen == True):
            if (self.__verifTableurCase(case) == True):
                self.__objTableur.deleteValeur(case)
                self.__objTableur.saveFile()
                showinfo("Work", "Valeur supprimer")
            else:
                showerror("Work", "La case n'est pas valide")
        else:
            showerror("Work", "Il n'a pas de tableur ouvert")

    def __verifTableurCase(self, chaine):
        # Expression régulière pour vérifier la chaîne
        regex = r"^[A-Z]\d$"

        # Vérification de la chaîne avec l'expression régulière
        if re.match(regex, chaine):
            return True
        else:
            return False

    def tkAddFormuleParole(self, mode: int):
        """
        1: Somme
        2: Moyenne
        3: Comptage
        4: Minimun
        5: Maximun
        """
        if ((self.__tableurOpen == True) and (mode < 5)):
            tab = Toplevel()
            tab.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant + " Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300, 175)
            tab.minsize(300, 175)
            frameCaseDest = Frame(tab, bg=self.__guiColor)
            frameCaseDebut = Frame(tab, bg=self.__guiColor)
            frameCaseFin = Frame(tab, bg=self.__guiColor)
            # Declaration des widget
            # Indication
            labelIndication = Label(tab, font=("arial", "20"),
                                    bg=self.__guiColor, fg=self.__textColor)
            # Destination
            labelCaseDest = Label(frameCaseDest, text="Destination :", font=("arial", "15"),
                                  bg=self.__guiColor, fg=self.__textColor)
            entryCaseDest = Entry(frameCaseDest, font=("arial", "15"), relief=SOLID)
            # Debut
            labelCaseDebut = Label(frameCaseDebut, text="Debut :", font=("arial", "15"),
                                   bg=self.__guiColor, fg=self.__textColor)
            entryCaseDebut = Entry(frameCaseDebut, font=("arial", "15"), relief=SOLID)
            # Fin
            labelCaseFin = Label(frameCaseFin, text="Fin :", font=("arial", "15"),
                                 bg=self.__guiColor, fg=self.__textColor)
            entryCaseFin = Entry(frameCaseFin, font=("arial", "15"), relief=SOLID)
            # Valider
            btnValider = Button(tab, text="Valider", font=("arial", "15"), bg=self.__guiColor,
                                fg=self.__textColor,
                                command=lambda: self.__fncAddFormuleTableurTk(mode, tab, entryCaseDest, entryCaseDebut,
                                                                              entryCaseFin))

            # Definition du texte du label indication et de la bonne fnc
            match mode:
                case 1:
                    labelIndication.configure(text="Somme")
                case 2:
                    labelIndication.configure(text="Moyenne")
                case 3:
                    labelIndication.configure(text="Comptage")
                case 4:
                    labelIndication.configure(text="Minimun")
                case 5:
                    labelIndication.configure(text="Maximun")
            # Affichage
            # Widget in frame
            labelCaseDest.pack(side="left")
            entryCaseDest.pack(side="right")

            labelCaseDebut.pack(side="left")
            entryCaseDebut.pack(side="right")

            labelCaseFin.pack(side="left")
            entryCaseFin.pack(side="right")

            # Windows
            labelIndication.pack()
            frameCaseDest.pack()
            frameCaseDebut.pack()
            frameCaseFin.pack()
            btnValider.pack()
            return True
        else:
            return False

    def __fncAddFormuleTableurTk(self, mode: int, w: Toplevel, edest: Entry, edebut: Entry, eFin: Entry):
        dest = edest.get()
        debut = edebut.get()
        fin = eFin.get()

        if ((self.__verifTableurCase(dest) == True)
                and (self.__verifTableurCase(debut) == True)
                and (self.__verifTableurCase(fin) == True)):

            sortie = self.__setFormuleTableur(mode, debut, fin, dest)

            if (sortie == True):
                showinfo("Work", "Formule ajouter")
            else:
                showerror("Work", "Formule non ajouter")
        else:
            showerror("Work", "Les cases ne sont pas valide")

        edest.delete(0, END)
        edebut.delete(0, END)
        eFin.delete(0, END)
        w.destroy()

    def openTableurOs(self):
        if (self.__tableurOpen == True):
            if ((self.__dectOs.osLinux() == True)
                    and (self.__dectOs.osWindows() == False)):
                subprocess.call(["xdg-open", self.__fileTableur])
                return True
            else:
                if ((self.__dectOs.osLinux() == False)
                        and (self.__dectOs.osWindows() == True)):
                    os.startfile(self.__fileTableur)
                    return True
                else:
                    return False
        else:
            return False

    def openWordOs(self):
        if (self.__wordOpen == True):
            if ((self.__dectOs.osLinux() == True)
                    and (self.__dectOs.osWindows() == False)):
                subprocess.call(["xdg-open", self.__fileWord])
                return True
            else:
                if ((self.__dectOs.osLinux() == False)
                        and (self.__dectOs.osWindows() == True)):
                    os.startfile(self.__fileWord)
                    return True
                else:
                    return False
        else:
            return False

    def guiTableurWork(self):
        if (self.__tableurOpen == True):
            # Declaration de la fenetre
            tabGUI = Toplevel()
            tabGUI.title(self.__nameAssistant + " Work : Tableur")
            tabGUI.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            tabGUI.configure(bg=self.__guiColor)
            tabGUI.maxsize(800, 500)
            tabGUI.minsize(800, 500)
            # Frame
            frameGestion = Frame(tabGUI, bg=self.__guiColor, width=440, height=450)
            # Declaration widget
            viewTableur = ScrolledText(tabGUI, wrap=WORD, width=40, height=50)
            # Frame gestion
            labelTitre = Label(frameGestion, text="Gestion du tableur",
                               font=("arial", "25"), bg=self.__guiColor,
                               fg=self.__textColor)
            btnAddFormule = Button(frameGestion, text="Ajouter une Formule", font=("arial", "15"),
                                   fg=self.__textColor, bg=self.__guiColor, width=30,
                                   command=lambda: self.__tkAddFormuleGUI(viewTableur))
            btnAddValeur = Button(frameGestion, text="Ajouter une valeur", font=("arial", "15"),
                                  fg=self.__textColor, bg=self.__guiColor, width=30,
                                  command=lambda: self.__tkAddValeurGUI(viewTableur))
            btnSuppr = Button(frameGestion, text="Supprimer", font=("arial", "15"),
                              fg=self.__textColor, bg=self.__guiColor, width=30,
                              command=lambda: self.__tkSuppValeurGUI(viewTableur))
            # Recuperation des valeur du tableur
            self.__setValeurTableurGUI(viewTableur)
            # Affichage
            viewTableur.pack(side="left")
            frameGestion.pack(side="right")

            labelTitre.place(relx=0.5, rely=0.0, anchor="n")
            btnAddFormule.place(x=((frameGestion.winfo_reqwidth()
                                    - btnAddFormule.winfo_reqwidth()) // 2),
                                y=100)
            btnAddValeur.place(x=((frameGestion.winfo_reqwidth()
                                   - btnAddValeur.winfo_reqwidth()) // 2),
                               y=300)
            btnSuppr.place(relx=0.5, rely=0.5, anchor="center")

            return True
        else:
            return False

    def __setValeurTableurGUI(self, wText: ScrolledText):
        wText.configure(state="normal")
        wText.delete(1.0, END)
        listSortie = self.readTableur()
        texte = ""
        for i in range(0, len(listSortie)):
            texte = texte + listSortie[i] + "\n"
        wText.insert(INSERT, texte)
        wText.configure(state="disabled")

    def __fncAddValeurGUI(self, w: Toplevel, evaleur: Entry, ecase: Entry, wText: ScrolledText):
        valeur = evaleur.get()
        case = ecase.get()
        if (case == ""):
            showerror("Work", "Vous avez pas définie de case.")
        else:
            self.__addValeur(case, valeur)
            self.__setValeurTableurGUI(wText)
        evaleur.delete(0, END)
        ecase.delete(0, END)
        w.destroy()

    def __tkAddValeurGUI(self, wText: ScrolledText):
        if (self.__tableurOpen == True):
            tab = Toplevel()
            tab.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant + " Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300, 100)
            tab.minsize(300, 100)
            frameCase = Frame(tab, bg=self.__guiColor)
            frameValeur = Frame(tab, bg=self.__guiColor)
            # Declaration des widget
            labelCase = Label(frameCase, text="Case :", font=("arial", "15"),
                              bg=self.__guiColor, fg=self.__textColor)
            entryCase = Entry(frameCase, font=("arial", "15"), relief=SOLID)
            labelValeur = Label(frameValeur, text="Valeur :", font=("arial", "15"),
                                bg=self.__guiColor, fg=self.__textColor)
            entryValeur = Entry(frameValeur, font=("arial", "15"), relief=SOLID)
            btnValider = Button(tab, text="Valider", font=("arial", "15"), bg=self.__guiColor,
                                fg=self.__textColor,
                                command=lambda: self.__fncAddValeurGUI(tab, entryValeur, entryCase, wText))
            # Affichage de widget
            labelCase.pack(side="left")
            labelValeur.pack(side="left")
            entryCase.pack(side="right")
            entryValeur.pack(side="right")

            frameCase.pack()
            frameValeur.pack()

            btnValider.pack(side="bottom")

            return True
        else:
            showerror("Work", "Il n'a pas de tableur ouvert")
            return False

    def __tkSuppValeurGUI(self, wText: ScrolledText):
        if (self.__tableurOpen == True):
            tab = Toplevel()
            tab.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant + " Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300, 100)
            tab.minsize(300, 100)
            frameCase = Frame(tab, bg=self.__guiColor)
            # Declaration des widget
            labelCase = Label(frameCase, text="Case :", font=("arial", "15"),
                              bg=self.__guiColor, fg=self.__textColor)
            entryCase = Entry(frameCase, font=("arial", "15"), relief=SOLID)
            btnValider = Button(tab, text="Valider", font=("arial", "15"), bg=self.__guiColor,
                                fg=self.__textColor, command=lambda: self.__fncSupprValeurGUI(tab, entryCase, wText))
            # Affichage de widget
            labelCase.pack(side="left")
            entryCase.pack(side="right")

            frameCase.pack()

            btnValider.pack(side="bottom")

            return True
        else:
            showerror("Work", "Il n'a pas de tableur ouvert")
            return False

    def __fncSupprValeurGUI(self, w: Toplevel, ecase: Entry, wText: ScrolledText):
        case = ecase.get()
        if (case == ""):
            showerror("Work", "Vous avez pas définie de case.")
        else:
            self.__supprValeur(case)
            self.__setValeurTableurGUI(wText)

        ecase.delete(0, END)
        w.destroy()

    def __tkAddFormuleGUI(self, wText: ScrolledText):
        tab = Toplevel()
        tab.iconphoto(False, PhotoImage(file=self.__iconAssistant))
        tab.title(self.__nameAssistant + " Work : Tableur")
        tab.configure(background=self.__guiColor)
        tab.maxsize(300, 175)
        tab.minsize(300, 175)
        frameCaseDest = Frame(tab, bg=self.__guiColor)
        frameCaseDebut = Frame(tab, bg=self.__guiColor)
        frameCaseFin = Frame(tab, bg=self.__guiColor)
        # String var
        formuleVar = StringVar(tab)
        # List formule
        listFormule = ["Somme", "Moyenne", "Comptage", "Minimun", "Maximun"]
        # Declaration des widget
        # Indication
        menuFormule = OptionMenu(tab, formuleVar, *listFormule)
        # Destination
        labelCaseDest = Label(frameCaseDest, text="Destination :", font=("arial", "15"),
                              bg=self.__guiColor, fg=self.__textColor)
        entryCaseDest = Entry(frameCaseDest, font=("arial", "15"), relief=SOLID)
        # Debut
        labelCaseDebut = Label(frameCaseDebut, text="Debut :", font=("arial", "15"),
                               bg=self.__guiColor, fg=self.__textColor)
        entryCaseDebut = Entry(frameCaseDebut, font=("arial", "15"), relief=SOLID)
        # Fin
        labelCaseFin = Label(frameCaseFin, text="Fin :", font=("arial", "15"),
                             bg=self.__guiColor, fg=self.__textColor)
        entryCaseFin = Entry(frameCaseFin, font=("arial", "15"), relief=SOLID)
        # Valider
        btnValider = Button(tab, text="Valider", font=("arial", "15"), bg=self.__guiColor,
                            fg=self.__textColor, command=lambda: self.__fncaddFormuleGUI(tab, wText, formuleVar,
                                                                                         entryCaseDest,
                                                                                         entryCaseDebut,
                                                                                         entryCaseFin))
        # Affichage
        # Widget in frame
        labelCaseDest.pack(side="left")
        entryCaseDest.pack(side="right")

        labelCaseDebut.pack(side="left")
        entryCaseDebut.pack(side="right")

        labelCaseFin.pack(side="left")
        entryCaseFin.pack(side="right")
        # Set de la valeur
        formuleVar.set(listFormule[0])
        # Windows
        menuFormule.pack()
        frameCaseDest.pack()
        frameCaseDebut.pack()
        frameCaseFin.pack()
        btnValider.pack()

    def __fncaddFormuleGUI(self, w: Toplevel, wText: ScrolledText, var: StringVar,
                           eDest: Entry, eDebut: Entry, eFin: Entry):

        mode = var.get()

        caseDest = eDest.get()
        caseDebut = eDebut.get()
        caseFin = eFin.get()

        if ((self.__verifTableurCase(caseDest) == True)
                and (self.__verifTableurCase(caseFin) == True)
                and (self.__verifTableurCase(caseDebut) == True)):

            match mode:
                case "Somme":
                    self.__setFormuleTableur(1, caseDebut, caseFin, caseDest)
                case "Moyenne":
                    self.__setFormuleTableur(2, caseDebut, caseFin, caseDest)
                case "Comptage":
                    self.__setFormuleTableur(3, caseDebut, caseFin, caseDest)
                case "Minimun":
                    self.__setFormuleTableur(4, caseDebut, caseFin, caseDest)
                case "Maximun":
                    self.__setFormuleTableur(5, caseDebut, caseFin, caseDest)

            showinfo("Work", "Formule ajouter")
            w.destroy()
            self.__setValeurTableurGUI(wText)

    def guiWordWork(self):
        if (self.__wordOpen == True):
            gWord = Toplevel()
            gWord.title(self.__nameAssistant + " Work : Traitement de texte")
            gWord.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            gWord.configure(bg=self.__guiColor)
            gWord.maxsize(650, 650)
            gWord.minsize(650, 650)
            # Frame
            fBottom = Frame(gWord, width=650, height=50, bg=self.__guiColor)
            # Widget
            viewWord = ScrolledText(gWord, wrap=WORD, width=75, height=60)
            # Widget frame bottom
            btnSave = Button(fBottom, text="Sauvegarder",
                             font=("arial", "15"), command=lambda: self.__fncSaveGUIWord(viewWord),
                             bg=self.__guiColor, fg=self.__textColor)
            btnQuitter = Button(fBottom, text="Quitter",
                                font=("arial", "15"), command=lambda: self.__fncQuitGUIWord(viewWord, gWord),
                                bg=self.__guiColor, fg=self.__textColor)
            # Recuperation du contenu du word
            sortie = self.readDocxFile()
            viewWord.delete(1.0, END)
            viewWord.insert(INSERT, sortie)
            # Affichage
            btnSave.place(relx=0.0, rely=0.5, anchor="w")
            btnQuitter.place(relx=1.0, rely=0.5, anchor="e")
            fBottom.pack(side="bottom")
            viewWord.pack()
            return True
        else:
            return False

    def __fncSaveGUIWord(self, wText: ScrolledText):
        content = wText.get(1.0, END)
        sortie = self.__objWord.writeEcrase(content)
        if (sortie == True):
            showinfo("Word", "Document sauvegarder")
        else:
            showerror("Word", "Le document ne c'est pas sauvergarder")

    def __fncQuitGUIWord(self, wText: Scrollbar, w: Toplevel):
        content = wText.get(1.0, END)
        self.__objWord.writeEcrase(content)
        w.destroy()

    def openProjet(self, project: str):
        if (self.__projectOpen == False):
            wordEmplacement = self.__gestionnaireNeuron.getWorkEmplacement()
            repertoir = Path(wordEmplacement)
            dossier = [dossier.name for dossier in repertoir.iterdir() if dossier.is_dir()]
            for i in range(0, len(dossier)):
                if (project == dossier[i]):
                    # Ecriture de l'emplacement du projet
                    self.__folderProject = wordEmplacement + "/" + project
                    # Ouverture du fichier de config
                    self.__jsonFileProject = jsonWork(
                        os.path.join(self.__folderProject + "/.arreraProjet", project + ".apr"))
                    # Mise de la var a true
                    self.__projectOpen = True
                    # Ouverture fichier de tache
                    self.__fncTaskProjet = fncArreraTache(self.__fncDate, self.__configFile,
                                                          self.__folderProject + "/.arreraProjet/TaskProjet.json",
                                                          True, self.getNameProjet())
                    return True
            return False
        else:
            return False

    def createProject(self, name: str):
        wordEmplacement = self.__gestionnaireNeuron.getWorkEmplacement()
        if ((self.__projectOpen == False) and (wordEmplacement != "")):
            dataJson = {"name": "", "type": ""}
            folder = (wordEmplacement + "/" + name)
            dataJson["name"] = name
            try:
                # Creation du projet
                os.makedirs(folder, exist_ok=True)
                # Creation du sous dossier de config du projet
                os.makedirs(folder + "/.arreraProjet")
                # Enregistrement de l'emplacement du projet
                self.__folderProject = folder
                # Creation du fichier de config
                configPath = os.path.join(folder + "/.arreraProjet", name + ".apr")
                # Creation du fichier de tache
                taskPath = os.path.join(folder + "/.arreraProjet", "TaskProjet.json")
                try:
                    # Ecriture dans les deux fichier
                    with open(configPath, "w", encoding="utf-8") as file:
                        json.dump(dataJson, file, ensure_ascii=False, indent=4)
                    with open(taskPath, "w", encoding="utf-8") as file:
                        json.dump({}, file, ensure_ascii=False, indent=4)
                    # Ouverture du fichier de config
                    self.__jsonFileProject = jsonWork(configPath)
                    # Mise a true de la var de projet ouvert
                    self.__projectOpen = True
                    # Ouverture fichier de tache
                    self.__fncTaskProjet = fncArreraTache(self.__fncDate, self.__configFile, taskPath,
                                                          True, self.getNameProjet())
                    return True
                except Exception as e:
                    return False
            except Exception as e:
                return False
        else:
            return False

    def setTypeProject(self, type: str):
        if ((type != "") and (self.__projectOpen == True)):
            self.__jsonFileProject.EcritureJSON("type", type)
            return True
        else:
            return False

    def closeProject(self):
        if (self.__projectOpen == True):
            self.__projectOpen = False
            self.__folderProject = ""
            self.__lastCreateFile = ""
            self.__jsonFileProject = None
            self.__fncTaskProjet = None
            self.__listFileProjet = []
            self.__listTaskProjetToday = []
            self.__listTaskProjetTowmorow = []
            return True
        else:
            return False

    def createFileProject(self, mode: int, nameFile: str):
        """
        in :
            1 : exel
            2 : word
            3 : odt
            4 : txt
            5 : python
            6 : h
            7 : json
            8 : html
            9 : css
            10 : md
            11 : cpp
            12 : c
            13 : php
            14 : js
            15 : java
            16 : kt (kotlin)
        """
        if ((self.__projectOpen == True) and (nameFile != "")):
            emplacementFile = self.__folderProject + "/"
            match mode:
                case 1:  # Exel
                    self.__lastCreateFile = nameFile + ".xlsx"
                    wb = Workbook()
                    ws = wb.active
                    ws.title = nameFile
                    ws['A1'] = ""
                    wb.save(emplacementFile + self.__lastCreateFile)
                    del ws
                    wb.close()
                    del wb
                    return True
                case 2:  # word
                    self.__lastCreateFile = nameFile + '.docx'
                    doc = Document()
                    doc.add_paragraph("")
                    doc.save(emplacementFile + self.__lastCreateFile)
                    return True
                case 3:  # Odt
                    self.__lastCreateFile = nameFile + ".odt"
                    doc = OpenDocumentText()
                    p1 = P(text="")
                    doc.text.addElement(p1)
                    doc.save(emplacementFile + self.__lastCreateFile)
                    return True
                case 4:  # txt
                    self.__lastCreateFile = nameFile + ".txt"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("Texte file named " + nameFile)
                    return True
                case 5:  # python
                    self.__lastCreateFile = nameFile + ".py"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("# Python file named " + nameFile)
                    return True
                case 6:  # h
                    self.__lastCreateFile = nameFile + ".h"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// hearder file create named " + nameFile)
                    return True
                case 7:  # json
                    self.__lastCreateFile = nameFile + ".json"
                    dataJson = {}
                    jsonPath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(jsonPath, "w", encoding="utf-8") as file:
                        json.dump(dataJson, file, ensure_ascii=False, indent=4)
                    return True
                case 8:  # html
                    self.__lastCreateFile = nameFile + ".html"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">'
                                   + '\n<meta name="viewport" content="width=device-width, initial-scale=1.0">' +
                                   '\n<title>html Page</title>\n</head>\n<body></body>\n</html>')
                    return True
                case 9:  # css
                    self.__lastCreateFile = nameFile + ".css"
                    filePath = os.path.join(emplacementFile, )
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("/* CSS file named " + nameFile + " */")
                    return True
                case 10:  # md
                    self.__lastCreateFile = nameFile + ".md"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("File readme named " + nameFile)
                    return True
                case 11:  # cpp
                    self.__lastCreateFile = nameFile + ".cpp"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// C++ file named " + nameFile)
                    return True
                case 12:  # c
                    self.__lastCreateFile = nameFile + ".c"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// C file named " + nameFile)
                    return True
                case 13:  # php
                    self.__lastCreateFile = nameFile + ".php"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// PHP file named " + nameFile)
                    return True
                case 14:  # javascript
                    self.__lastCreateFile = nameFile + ".js"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// JavaScript file named " + nameFile)
                    return True
                case 15:  # java
                    self.__lastCreateFile = nameFile + ".java"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// Java file named " + nameFile)
                    return True
                case 16:  # kt
                    self.__lastCreateFile = nameFile + ".kt"
                    filePath = os.path.join(emplacementFile, self.__lastCreateFile)
                    with open(filePath, "w", encoding="utf-8") as file:
                        file.write("// Kotlin file named " + nameFile)
                    return True
                case other:
                    return False
        else:
            return False

    def getNameProjet(self):
        if (self.__projectOpen == True):
            return self.__jsonFileProject.lectureJSON("name")
        else:
            return ""

    def getNameLastFileCreate(self):
        return self.__lastCreateFile

    def openFileProjet(self, file: str):
        """
        0 : Error
        1 : Open by os
        2 : Open by ArreraDocx
        3 : Open bu ArreraTableur
        """
        if ((self.__projectOpen == True) and (file != "")):
            if (("docx" in file) or ("odt" in file)):
                self.__objWord = CArreraDocx(self.__folderProject + "/" + file)
                self.__fileWord = self.__folderProject + "/" + self.__lastCreateFile
                self.__wordOpen = True
                return 2
            else:
                if ("xlsx" in file):
                    self.__objTableur = CArreraTableur(self.__folderProject + "/" + file)
                    self.__fileTableur = self.__folderProject + "/" + file
                    self.__tableurOpen = True
                    return 3
                else:
                    if ((self.__dectOs.osLinux() == True)
                            and (self.__dectOs.osWindows() == False)):
                        subprocess.call(["xdg-open", self.__folderProject + "/" + file])
                        return 1
                    else:
                        if ((self.__dectOs.osLinux() == False)
                                and (self.__dectOs.osWindows() == True)):
                            os.startfile(self.__folderProject + "/" + file)
                            return 1
                        else:
                            return 0

    def openLastFileCreate(self):
        """
        0 : Error
        1 : Open by os
        2 : Open by ArreraDocx
        3 : Open bu ArreraTableur
        """
        if ((self.__lastCreateFile != "")):
            sortie = self.openFileProjet(self.__lastCreateFile)
            self.__lastCreateFile = ""
            return sortie
        else:
            return 0

    def setlistFileProject(self):
        if (self.__projectOpen == True):
            try:
                # Liste les fichiers et dossiers dans le répertoire
                self.__listFileProjet = os.listdir(self.__folderProject)
                self.__listFileProjet.remove(".arreraProjet")
                return True
            except FileNotFoundError:
                return False
            except PermissionError:
                return False
            except Exception as e:
                return False
        else:
            return False

    def getListFileProjet(self):
        return self.__listFileProjet

    def openFileOtherProjet(self, file: str):
        """
        0 : Error
        1 : Open by os
        2 : Open by ArreraDocx
        3 : Open bu ArreraTableur
        """
        if ((self.__projectOpen == True) and (self.setlistFileProject() == True)
                and ("." in file) and (file != "")):
            listFile = self.getListFileProjet()
            nbFile = len(listFile)

            for i in range(0, nbFile):
                if (listFile[i] == file):
                    return self.openFileProjet(listFile[i])

            return 0

        else:
            return 0

    def showTacheProjet(self):
        if (self.__projectOpen == True):
            self.__fncTaskProjet.activeViewTask()
            return True
        else:
            return False

    def addTacheProjet(self):
        if (self.__projectOpen == True):
            self.__fncTaskProjet.activeViewAdd()
            return True
        else:
            return False

    def supprTacheProjet(self):
        if (self.__projectOpen == True):
            self.__fncTaskProjet.activeViewSuppr()
            return True
        else:
            return False

    def checkTacheProjet(self):
        if (self.__projectOpen == True):
            self.__fncTaskProjet.activeViewCheck()
            return True
        else:
            return False

    def getNbTacheProjet(self):
        """
        -1 : Error
        """
        if (self.__projectOpen == True):
            return self.__fncTaskProjet.getNbTache()
        else:
            return -1

    def getNBTacheToday(self):
        """
        -1 : error
        """
        if (self.__projectOpen == True):
            return self.__fncTaskProjet.getNbTacheToday()
        else:
            return -1

    def setListTacheTodayProjet(self):
        if (self.__projectOpen == True):
            self.__listTaskProjetToday = self.__fncTaskProjet.getTacheToday()
            return True
        else:
            return False

    def getListTacheTodayProjet(self):
        return self.__listTaskProjetToday

    def setListTacheTowmorowProjet(self):
        if (self.__projectOpen == True):
            self.__listTaskProjetTowmorow = self.__fncTaskProjet.getTacheTowmorow()
            return True
        else:
            return False

    def getListTacheTowmorowProjet(self):
        return self.__listTaskProjetTowmorow

    def getListProjetCreated(self):
        wordEmplacement = self.__gestionnaireNeuron.getWorkEmplacement()
        project_list = []
        if wordEmplacement:
            for folder in os.listdir(wordEmplacement):
                folder_path = os.path.join(wordEmplacement, folder)
                if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, ".arreraProjet")):
                    project_list.append(folder)
        return project_list
