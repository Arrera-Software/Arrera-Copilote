from fonctionnalites.arreratableur import*
from tkinter import*
from tkinter import filedialog, messagebox
import re


class CArreraCopiloteTableurGUI :
    def __init__(self) :
        self.__color = "white"
        self.__textColor = "black"
        self.__caseSelected = str
        self.__actionSelected = str
        self.__tableur = None
        self.__selectCase = False
        self.__selectAction = False
    
    def activeGUI(self):
        file = ""
        result = messagebox.askquestion(
            "Choix de l'action", 
            "Voulez-vous crée un fichier ?")
        if (result=="yes"):
            file = filedialog.asksaveasfilename(
                defaultextension='.xlsx', 
                filetypes=[("Fichiers Excel", "*.xlsx"),("Fichiers ODF", "*.ods")])
        else :
            file = filedialog.askopenfilename(
                filetypes=[("Fichiers Excel", "*.xlsx"),("Fichiers ODF", "*.ods")])
        if (file!=""):
            self.__tableur = CArreraTableur(file)
            screen = Toplevel()
            screen.title("Copilote : Tableur")
            screen.iconphoto(False,PhotoImage(file="asset/icon/copilote/icon.png"))
            screen.maxsize(700,700)
            screen.minsize(700,700)
            screen.configure(bg=self.__color)
            # Varriable
            self.__action = StringVar(screen)
            listAction = ["ecrire une valeur","faire une moyenne","faire une somme",
                        "faire un comptage","faire un minimun","faire un maximun","supprimer un valeur"]
            #Cadre principal
            self.__mainFrame = Frame(screen,width=350,height=700,bg=self.__color)
            # Label Affichage contenu tableur 
            self.__labelTableurView = Label(screen,font=("arial",12),
                                        fg=self.__textColor,bg=self.__color)
            #Cadre secondaire
            self.__frameCase = Frame(self.__mainFrame,bg=self.__color)
            self.__frameAction =  Frame(self.__mainFrame,bg=self.__color)
            # Cadre add 
            self.__addValeur = Frame(self.__mainFrame,width=350,height=150,bg=self.__color)
            self.__addMoyenne = Frame(self.__mainFrame,width=350,height=150,bg=self.__color)
            self.__addSomme = Frame(self.__mainFrame,width=350,height=150,bg=self.__color)
            self.__addComptage = Frame(self.__mainFrame,width=350,height=150,bg=self.__color)
            self.__addMinimun = Frame(self.__mainFrame,width=350,height=150,bg=self.__color)
            self.__addMaximun = Frame(self.__mainFrame,width=350,height=150,bg=self.__color)
            # widget mainframe
            labelIndication = Label(self.__mainFrame,text="Modifier le tableur",
                                    font=("arial",15),fg=self.__textColor,bg=self.__color)
            self.__labelCaseSelect = Label(self.__mainFrame,font=("arial",15),
                                        fg=self.__textColor,bg=self.__color)
            self.__labelfncSelect = Label(self.__mainFrame,font=("arial",15),
                                        fg=self.__textColor,bg=self.__color)
            self.__btnAnnuler = Button(self.__mainFrame,text="Annuler",font=("arial",15),width=25,
                                        fg=self.__textColor,bg=self.__color,command=self.__cancelSelect)
            # widget frameCase
            labelCase = Label(self.__frameCase,text="Case :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            self.__entryCase = Entry(self.__frameCase,font=("arial","15"),width=5,relief=SOLID)
            btnSetCase = Button(self.__frameCase,text="Valider",bg=self.__color,
                                fg=self.__textColor,font=("arial","15"),command=self.__setCase)
            # widget mainFrame 
            labelAction = Label(self.__frameAction,text="Action :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            choixAction = OptionMenu(self.__frameAction,self.__action,*listAction)
            btnSetAction = Button(self.__frameAction,text="Valider",bg=self.__color,
                                fg=self.__textColor,font=("arial","15"),command=self.__setAction)
            # widget addValeur
            labelAddValeur = Label(self.__addValeur,text="Ecriver la valeur",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            self.__entryAddValeur = Entry(self.__addValeur,font=("arial","15"),width=15,relief=SOLID)
            validerAddValeur = Button(self.__addValeur,text="Ajouter",font=("arial",15),
                            fg=self.__textColor,bg=self.__color,command=lambda:self.__ecritureFormule(1))
            # widget addMoyenne
            labelAddMoyenne = Label(self.__addMoyenne,text="Definissez les case pour votre moyenne",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            debutMoyenne = Frame(self.__addMoyenne)
            finMoyenne = Frame(self.__addMoyenne)
            self.__entryAddMoyenneDebut = Entry(debutMoyenne,font=("arial","15"),width=5,relief=SOLID)
            self.__entryAddMoyenneFin = Entry(finMoyenne,font=("arial","15"),width=5,relief=SOLID)
            labelMoyenneDebut  =Label(debutMoyenne,text="Debut :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            labelMoyenneFin  =Label(finMoyenne,text="Fin :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            validerAddMoyenne = Button(self.__addMoyenne,text="Ajouter",font=("arial",15),
                            fg=self.__textColor,bg=self.__color,command=lambda:self.__ecritureFormule(2))
            # widget addSomme
            labelAddSomme = Label(self.__addSomme,text="Definissez les case pour votre somme",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            debutSomme = Frame(self.__addSomme)
            finSomme = Frame(self.__addSomme)
            self.__entryAddSommeDebut = Entry(debutSomme,font=("arial","15"),width=5,relief=SOLID)
            self.__entryAddSommeFin = Entry(finSomme,font=("arial","15"),width=5,relief=SOLID)
            labelSommeDebut  =Label(debutSomme,text="Debut :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            labelSommeFin  =Label(finSomme,text="Fin :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            validerAddSomme = Button(self.__addSomme,text="Ajouter",font=("arial",15),
                            fg=self.__textColor,bg=self.__color,command=lambda:self.__ecritureFormule(3))
            # widget addComptage
            labelAddComptage = Label(self.__addComptage,text="Definissez les case pour compter\nle nombre de valeur",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            debutComptage = Frame(self.__addComptage)
            finComptage = Frame(self.__addComptage)
            self.__entryAddComptageDebut = Entry(debutComptage,font=("arial","15"),width=5,relief=SOLID)
            self.__entryAddComptageFin = Entry(finComptage,font=("arial","15"),width=5,relief=SOLID)
            labelComptageDebut  =Label(debutComptage,text="Debut :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            labelComptageFin  =Label(finComptage,text="Fin :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            validerAddComptage = Button(self.__addComptage,text="Ajouter",font=("arial",15),
                            fg=self.__textColor,bg=self.__color,command=lambda:self.__ecritureFormule(4))
            # widget addMinimun
            labelAddMinimun = Label(self.__addMinimun,text="Definissez les case pour\ntrouver votre valeur minimun",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            debutMinimun = Frame(self.__addMinimun)
            finMinimun = Frame(self.__addMinimun)
            self.__entryAddMinimunDebut = Entry(debutMinimun,font=("arial","15"),width=5,relief=SOLID)
            self.__entryAddMinimunFin = Entry(finMinimun,font=("arial","15"),width=5,relief=SOLID)
            labelMinimunDebut  =Label(debutMinimun,text="Debut :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            labelMinimunFin  =Label(finMinimun,text="Fin :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            validerAddMinimun = Button(self.__addMinimun,text="Ajouter",font=("arial",15),
                            fg=self.__textColor,bg=self.__color,command=lambda:self.__ecritureFormule(5))
            # widget addMaximun
            labelAddMaximun = Label(self.__addMaximun,text="Definissez les case pour\ntrouver votre valeur maximun",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            debutMaximun = Frame(self.__addMaximun)
            finMaximun = Frame(self.__addMaximun)
            self.__entryAddMaximunDebut = Entry(debutMaximun,font=("arial","15"),width=5,relief=SOLID)
            self.__entryAddMaximunFin = Entry(finMaximun,font=("arial","15"),width=5,relief=SOLID)
            labelMaximunDebut  =Label(debutMaximun,text="Debut :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            labelMaximunFin  =Label(finMaximun,text="Fin :",font=("arial",15),
                            fg=self.__textColor,bg=self.__color)
            validerAddMaximun = Button(self.__addMaximun,text="Ajouter",font=("arial",15),
                            fg=self.__textColor,bg=self.__color,command=lambda:self.__ecritureFormule(6))
            #set option menu 
            self.__action.set(listAction[0])
            # Affichage des valeur du tableur
            self.__updateTableur()
            # Affichage 
            # Affichage widget mainFrame
            labelIndication.place(x=0,y=0)
            labelCase.pack(side="left")
            self.__entryCase.pack(side="left")
            btnSetCase.pack(side="right")
            labelAction.pack(side="left")
            choixAction.pack(side="left")
            btnSetAction.pack(side="right")
            self.__frameCase.place(x=15,y=40)
            self.__frameAction.place(x=15,y=100)
            # Affichage widget AddValeur
            labelAddValeur.place(relx=0.5, rely=0, anchor="n")
            self.__entryAddValeur.place(relx=0.5,rely=0.5,anchor="center")
            validerAddValeur.place(relx=0.5, rely=1, anchor="s")
            # Affichage widget addMoyenne
            self.__entryAddMoyenneFin.pack(side="right")
            self.__entryAddMoyenneDebut.pack(side="right")
            labelMoyenneDebut.pack(side="left")
            labelMoyenneFin.pack(side="left")
            labelAddMoyenne.place(relx=0.5, rely=0, anchor="n")
            debutMoyenne.place(relx=0, rely=0.5, anchor="w")
            finMoyenne.place(relx=1, rely=0.5, anchor="e")
            validerAddMoyenne.place(relx=0.5, rely=1, anchor="s")
            # Affichage widget addSomme
            labelAddSomme.place(relx=0.5, rely=0, anchor="n")
            debutSomme.place(relx=0, rely=0.5, anchor="w")
            finSomme.place(relx=1, rely=0.5, anchor="e")
            self.__entryAddSommeDebut.pack(side="right")
            self.__entryAddSommeFin.pack(side="right")
            labelSommeDebut.pack(side="left")
            labelSommeFin.pack(side="left")
            validerAddSomme.place(relx=0.5, rely=1, anchor="s")
            # Affichage widget addComptage
            labelAddComptage.place(relx=0.5, rely=0, anchor="n")
            debutComptage.place(relx=0, rely=0.5, anchor="w")
            finComptage.place(relx=1, rely=0.5, anchor="e")
            self.__entryAddComptageDebut.pack(side="right")
            self.__entryAddComptageFin.pack(side="right")
            labelComptageDebut.pack(side="left")
            labelComptageFin.pack(side="left")
            validerAddComptage.place(relx=0.5, rely=1, anchor="s") 
            # Affichage widget addMinimun
            labelAddMinimun.place(relx=0.5, rely=0, anchor="n")
            debutMinimun.place(relx=0, rely=0.5, anchor="w")
            finMinimun.place(relx=1, rely=0.5, anchor="e")
            self.__entryAddMinimunDebut.pack(side="right")
            self.__entryAddMinimunFin.pack(side="right")
            labelMinimunDebut.pack(side="left")
            labelMinimunFin.pack(side="left")
            validerAddMinimun.place(relx=0.5, rely=1, anchor="s") 
            # Affichage widget addMaximun
            labelAddMaximun.place(relx=0.5, rely=0, anchor="n")
            debutMaximun.place(relx=0, rely=0.5, anchor="w")
            finMaximun.place(relx=1, rely=0.5, anchor="e")
            self.__entryAddMaximunDebut.pack(side="right")
            self.__entryAddMaximunFin.pack(side="right")
            labelMaximunDebut.pack(side="left")
            labelMaximunFin.pack(side="left")
            validerAddMaximun.place(relx=0.5, rely=1, anchor="s")
            # Affichage principale
            self.__mainFrame.pack(side="left")
            self.__labelTableurView.pack(side="left",anchor="n")
            return True
        else :
            return False
        
    def __verifChaine(self,chaine):
        # Expression régulière pour vérifier la chaîne
        regex = r"^[A-Z]\d$"

        # Vérification de la chaîne avec l'expression régulière
        if re.match(regex, chaine):
            return True
        else:
            return False

    def __updateTableur(self):
        sortie = self.__tableur.read()
        self.__labelTableurView.configure(text="Contenu du fichier tableur:\n", justify="left")
        for cell_position, cell_value in sortie.items():
            text = self.__labelTableurView.cget("text")
            self.__labelTableurView.configure(text=text
                                              +"\n"+f"Cellule {cell_position} : {cell_value}", 
                                              justify="left")
    
    def __setCase(self):
        case = self.__entryCase.get()
        if not case  :
            messagebox.showerror("Case est vide","Veillez entrez quelque chose dans la case")
        else :
            if (self.__verifChaine(case)==True):
                self.__caseSelected = case 
                self.__labelCaseSelect.configure(text="Case selectionner : "+case)
                self.__frameCase.place_forget()
                self.__labelCaseSelect.place(x=15,y=35)
                self.__selectCase = True
                self.__btnAnnuler.place(x=15,y=335)
                if ((self.__selectCase==True) and (self.__selectAction==True)):
                    self.__preecretureFormule()
            else :
                messagebox.showerror("Case invalide","La case n'est pas valide")
        self.__entryCase.delete(0,END)
    
    def __setAction(self):
        action = self.__action.get()
        self.__actionSelected = action
        self.__frameAction.place_forget()
        self.__labelfncSelect.configure(text="Action : "+action)
        self.__labelfncSelect.place(x=15,y=85)
        self.__selectAction = True
        self.__btnAnnuler.place(x=15,y=335)
        if ((self.__selectCase==True) and (self.__selectAction==True)):       
            self.__preecretureFormule()
    
    def __cancelSelect(self):
        self.__caseSelected = None
        self.__actionSelected = None
        self.__selectCase = False
        self.__selectAction = False
        self.__labelCaseSelect.place_forget()
        self.__frameCase.place(x=15,y=35)
        self.__labelfncSelect.place_forget()
        self.__frameAction.place(x=15,y=85)
        self.__btnAnnuler.place_forget()

        self.__addValeur.place_forget()
        self.__addMoyenne.place_forget()
        self.__addSomme.place_forget()
        self.__addComptage.place_forget()
        self.__addMinimun.place_forget()
        self.__addMaximun.place_forget()
    
    def __preecretureFormule(self):
        #self.__addMaximun.place(x=0,y=400)
        if (self.__actionSelected=="ecrire une valeur"):
            self.__addValeur.place(x=0,y=400)
        else :
            if (self.__actionSelected=="faire une moyenne"):
                self.__addMoyenne.place(x=0,y=400)
            else :
                if (self.__actionSelected=="faire une somme"):
                    self.__addSomme.place(x=0,y=400)
                else :
                    if (self.__actionSelected=="faire un comptage"):
                        self.__addComptage.place(x=0,y=400)
                    else :
                        if (self.__actionSelected=="faire un minimun"):
                            self.__addMinimun.place(x=0,y=400)
                        else :
                            if (self.__actionSelected=="faire un maximun"):
                                self.__addMaximun.place(x=0,y=400)
                            else :
                                if (self.__actionSelected=="supprimer un valeur"):
                                    self.__tableur.deleteValeur(self.__caseSelected)
                                    self.__tableur.saveFile()
                                    messagebox.showinfo("Copilote","Valeur Supprimer")
                                    self.__updateTableur()
        
    def __ecritureFormule(self,v:int):
        """
        1 : valeur 
        2 : moyenne
        3 : somme
        4 : comptage
        5 : minimun
        6 : maximun
        """
        if (v==1):
            valeur = self.__entryAddValeur.get()
            self.__entryAddValeur.delete(0,END)
            if (valeur.isdigit()==True):
                self.__tableur.write(self.__caseSelected,int(valeur))
            else : 
                self.__tableur.write(self.__caseSelected,valeur)
            self.__tableur.saveFile()
            self.__cancelSelect()
            messagebox.showinfo("Copilote","Valeur ajouter")
            self.__updateTableur()
        else :
            if (v==2):
                caseDebut  = self.__entryAddMoyenneDebut.get()
                caseFin = self.__entryAddMoyenneFin.get()
                self.__entryAddMoyenneDebut.delete(0,END)
                self.__entryAddMoyenneFin.delete(0,END)
                if((self.__verifChaine(caseDebut)==True)and(self.__verifChaine(caseFin)==True)):
                    self.__tableur.moyenne(self.__caseSelected,caseDebut,caseFin)
                    self.__tableur.saveFile()
                    messagebox.showinfo("Copilote","Moyenne ecrite")
                    self.__cancelSelect()
                    self.__updateTableur()
                else :
                    messagebox.showerror("Copilote","La moyenne n'a pas pu etre ajouter")
            else :
                if (v==3):
                    caseDebut = self.__entryAddSommeDebut.get()
                    caseFin = self.__entryAddSommeFin.get()
                    self.__entryAddSommeDebut.delete(0,END)
                    self.__entryAddSommeFin.delete(0,END)
                    if((self.__verifChaine(caseDebut)==True)and(self.__verifChaine(caseFin)==True)):
                        self.__tableur.somme(self.__caseSelected,caseDebut,caseFin)
                        self.__tableur.saveFile()
                        messagebox.showinfo("Copilote","Somme ecrite")
                        self.__cancelSelect()
                        self.__updateTableur()
                    else :
                        messagebox.showerror("Copilote","La somme n'a pas pu etre ajouter")
                else :
                    if (v==4):
                        caseDebut = self.__entryAddComptageDebut.get()
                        caseFin = self.__entryAddComptageFin.get()
                        self.__entryAddComptageDebut.delete(0,END)
                        self.__entryAddComptageFin.delete(0,END)
                        if((self.__verifChaine(caseDebut)==True)and(self.__verifChaine(caseFin)==True)):
                            self.__tableur.comptage(self.__caseSelected,caseDebut,caseFin)
                            self.__tableur.saveFile()
                            messagebox.showinfo("Copilote","Comptage ecrite")
                            self.__cancelSelect()
                            self.__updateTableur()
                        else :
                            messagebox.showerror("Copilote","Le comptage n'a pas pu etre ajouter")
                    else :
                        if (v==5):
                            caseDebut = self.__entryAddMinimunDebut.get()
                            caseFin = self.__entryAddMinimunFin.get()
                            self.__entryAddMinimunDebut.delete(0,END)
                            self.__entryAddMinimunFin.delete(0,END)
                            if((self.__verifChaine(caseDebut)==True)and(self.__verifChaine(caseFin)==True)):
                                self.__tableur.minimun(self.__caseSelected,caseDebut,caseFin)
                                self.__tableur.saveFile()
                                messagebox.showinfo("Copilote","Minimun ecrite")
                                self.__cancelSelect()
                                self.__updateTableur()
                            else :
                                messagebox.showerror("Copilote","Le minimun n'a pas pu etre ajouter")
                        else :
                            if (v==6):
                                caseDebut = self.__entryAddMaximunDebut.get()
                                caseFin = self.__entryAddMaximunFin.get()
                                self.__entryAddMaximunDebut.delete(0,END)
                                self.__entryAddMaximunFin.delete(0,END)
                                if((self.__verifChaine(caseDebut)==True)and(self.__verifChaine(caseFin)==True)):
                                    self.__tableur.maximun(self.__caseSelected,caseDebut,caseFin)
                                    self.__tableur.saveFile()
                                    messagebox.showinfo("Copilote","Maximun ecrite")
                                    self.__cancelSelect()
                                    self.__updateTableur()
                                else :
                                    messagebox.showerror("Copilote","Le maximun n'a pas pu etre ajouter")

    def activeEcritureDirect(self,case:str,tableur:CArreraTableur):
        self.__case = case 
        self.__tableur = tableur
        self.__screenEcritureDirect = Toplevel()
        self.__screenEcritureDirect.title("Copilote : Tableur")
        self.__screenEcritureDirect.iconphoto(False,PhotoImage(file="asset/icon/copilote/icon.png"))
        self.__screenEcritureDirect.maxsize(300,250)
        self.__screenEcritureDirect.minsize(300,250)
        self.__screenEcritureDirect.configure(bg=self.__color)
        # Varriable
        self.__action = StringVar(self.__screenEcritureDirect)
        listAction = ["ecrire une valeur","faire une moyenne","faire une somme",
                    "faire un comptage","faire un minimun","faire un maximun","supprimer un valeur"] 
        #Creation de cardre 
        self.__mainCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")
        self.__valeurCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")
        self.__moyenneCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")  
        self.__sommeCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")
        self.__comptageCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")
        self.__minumunCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")
        self.__maximunCadre = Frame(self.__screenEcritureDirect,width=300,height=250,bg="white")
        # Widget mainCadre
        labelInfomainCadre = Label(self.__mainCadre,text="Case selectionner :",font=("arial","15"),bg="white",fg="black")
        menu = OptionMenu(self.__mainCadre,self.__action,*listAction)
        buttonValidermainCadre = Button(self.__mainCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command= self.__choixEcritureDirect)
        # Widget valeurCadre 
        labelInfovaleurCadre = Label(self.__valeurCadre,text="Ecriver la valeur\nque vous voulez ecrire",font=("arial","15"),bg="white",fg="black")
        self.__entryValeur = Entry(self.__valeurCadre,font=("arial","15"),width=5,relief=SOLID)
        buttonValidervaleurCadre = Button(self.__valeurCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command=lambda : self.__validerEcritureDirect(1))
        # widget moyenneCadre
        labelInfomoyenneCadre = Label(self.__moyenneCadre,text="Ecriver la case du\ndebut et la case de\nla fin pour faire votre moyenne",font=("arial","15"),bg="white",fg="black")
        self.__entryMoyenneDebut = Entry(self.__moyenneCadre,font=("arial","15"),width=5,relief=SOLID)
        self.__entryMoyenneFin = Entry(self.__moyenneCadre,font=("arial","15"),width=5,relief=SOLID)
        buttonValidermoyenneCadre = Button(self.__moyenneCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command=lambda : self.__validerEcritureDirect(2))
        # widget sommeCadre
        labelInfosommeCadre = Label(self.__sommeCadre,text="Ecriver la case du debut et la case de\nla fin pour faire votre somme",font=("arial","15"),bg="white",fg="black")
        self.__entrySommeDebut = Entry(self.__sommeCadre,font=("arial","15"),width=5,relief=SOLID)
        self.__entrySommeFin = Entry(self.__sommeCadre,font=("arial","15"),width=5,relief=SOLID)
        buttonValidersommeCadre = Button(self.__sommeCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command=lambda : self.__validerEcritureDirect(3))
        # widget comptageCadre
        labelInfocomptageCadre = Label(self.__comptageCadre,text="Ecriver la case du debut et la case de\nla fin pour faire votre comptage de valeur",font=("arial","15"),bg="white",fg="black")
        self.__entrycomptageDebut = Entry(self.__comptageCadre,font=("arial","15"),width=5,relief=SOLID)
        self.__entrycomptageFin = Entry(self.__comptageCadre,font=("arial","15"),width=5,relief=SOLID)
        buttonValidercomptageCadre = Button(self.__comptageCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command=lambda : self.__validerEcritureDirect(4))
        # widget minumunCadre
        labelInfominumunCadre = Label(self.__minumunCadre,text="Ecriver la case du debut et la case de\nla fin pour faire votre minimun",font=("arial","15"),bg="white",fg="black")
        self.__entryminimunDebut = Entry(self.__minumunCadre,font=("arial","15"),width=5,relief=SOLID)
        self.__entryminimunFin = Entry(self.__minumunCadre,font=("arial","15"),width=5,relief=SOLID)
        buttonValiderminumunCadre = Button(self.__minumunCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command=lambda : self.__validerEcritureDirect(5))
        # widget maximunCadre
        labelInfomaximunCadre = Label(self.__maximunCadre,text="Ecriver la case du debut et la case de\nla fin pour faire votre maximun",font=("arial","15"),bg="white",fg="black")
        self.__entrymaximunDebut = Entry(self.__maximunCadre,font=("arial","15"),width=5,relief=SOLID)
        self.__entrymaximunFin = Entry(self.__maximunCadre,font=("arial","15"),width=5,relief=SOLID)
        buttonValidermaximunCadre = Button(self.__maximunCadre,text="Valider",font=("arial","15"),bg="white",fg="black",command=lambda : self.__validerEcritureDirect(6))
        # Affichage
        # Widget mainCadre
        labelInfomainCadre.place(relx=0.5, rely=0, anchor="n") 
        menu.place(relx=0.5, rely=0.5, anchor="center")
        buttonValidermainCadre.place(relx=0.5, rely=1, anchor="s")
        # Widget valeurCadre 
        labelInfovaleurCadre.place(relx=0.5, rely=0, anchor="n")
        self.__entryValeur.place(relx=0.5, rely=0.5, anchor="center")
        buttonValidervaleurCadre.place(relx=0.5, rely=1, anchor="s")
        # widget moyenneCadre
        labelInfomoyenneCadre.place(relx=0.5, rely=0, anchor="n") 
        self.__entryMoyenneDebut.place(relx=0.0, rely=0.5, anchor="w")
        self.__entryMoyenneFin.place(relx=1.0, rely=0.5, anchor="e")
        buttonValidermoyenneCadre.place(relx=0.5, rely=1, anchor="s")
        # widget sommeCadre
        labelInfosommeCadre.place(relx=0.5, rely=0, anchor="n") 
        self.__entrySommeDebut.place(relx=0.0, rely=0.5, anchor="w")
        self.__entrySommeFin.place(relx=1.0, rely=0.5, anchor="e")
        buttonValidersommeCadre.place(relx=0.5, rely=1, anchor="s")
        # widget comptageCadre
        labelInfocomptageCadre.place(relx=0.5, rely=0, anchor="n")
        self.__entrycomptageDebut.place(relx=0.0, rely=0.5, anchor="w")
        self.__entrycomptageFin.place(relx=1.0, rely=0.5, anchor="e")
        buttonValidercomptageCadre.place(relx=0.5, rely=1, anchor="s")
        # widget minumunCadre
        labelInfominumunCadre.place(relx=0.5, rely=0, anchor="n")
        self.__entryminimunDebut.place(relx=0.0, rely=0.5, anchor="w")
        self.__entryminimunFin.place(relx=1.0, rely=0.5, anchor="e")
        buttonValiderminumunCadre.place(relx=0.5, rely=1, anchor="s")
        # widget maximunCadre
        labelInfomaximunCadre.place(relx=0.5, rely=0, anchor="n")
        self.__entrymaximunDebut.place(relx=0.0, rely=0.5, anchor="w")
        self.__entrymaximunFin.place(relx=1.0, rely=0.5, anchor="e")
        buttonValidermaximunCadre.place(relx=0.5, rely=1, anchor="s")

        # Afficage principal 
        self.__action.set(listAction[0])
        self.__mainCadre.pack()

    def __choixEcritureDirect(self):
        listAction = ["ecrire une valeur","faire une moyenne","faire une somme",
                "faire un comptage","faire un minimun","faire un maximun","supprimer un valeur"] 
        retour = self.__action.get()
        self.__mainCadre.pack_forget()
        if(retour==listAction[0]):
            self.__valeurCadre.pack()
        else :
            if(retour==listAction[1]):
                self.__moyenneCadre.pack()
            else :
                if(retour==listAction[2]):
                    self.__sommeCadre.pack()
                else :
                    if(retour==listAction[3]):
                        self.__comptageCadre.pack()
                    else :
                        if(retour==listAction[4]):
                            self.__minumunCadre.pack()
                        else :
                            if(retour==listAction[5]):
                                self.__maximunCadre.pack()
                            else :
                                if(retour==listAction[6]):
                                    self.__tableur.deleteValeur(self.__case)
                                    self.__tableur.saveFile()
                                    self.__screenEcritureDirect.destroy()


            
    def __validerEcritureDirect(self,v:int):
        """
        1 : valeur
        2 : moyenne 
        3 : somme 
        4 : comptage
        5 : minimun
        6 : Maximun 
        """
        match(v):
            case 1 :
                case1 = self.__entryValeur.get()
                if (case1.isdigit()==True):
                    self.__tableur.write(self.__case,int(case1))
                else :
                    self.__tableur.write(self.__case,case1)
            case 2 :
                case1 = self.__entryMoyenneDebut.get()
                case2 = self.__entryMoyenneFin.get()
                if((self.__verifChaine(case1)==True)and(self.__verifChaine(case2)==True)):
                    self.__tableur.moyenne(self.__case,case1,case2)
                else :
                    messagebox.showerror("Copilote","Les deux case ne sont pas valide")
            case 3 :
                case1 = self.__entrySommeDebut.get()
                case2 = self.__entrySommeFin.get()
                if((self.__verifChaine(case1)==True)and(self.__verifChaine(case2)==True)):
                    self.__tableur.somme(self.__case,case1,case2)
                else :
                    messagebox.showerror("Copilote","Les deux case ne sont pas valide")
            case 4 :
                case1 = self.__entrycomptageDebut.get()
                case2 = self.__entrycomptageFin.get()
                if((self.__verifChaine(case1)==True)and(self.__verifChaine(case2)==True)):
                    self.__tableur.comptage(self.__case,case1,case2)
                else :
                    messagebox.showerror("Copilote","Les deux case ne sont pas valide")
            case 5 :
                case1 = self.__entryminimunDebut.get()
                case2 = self.__entryminimunFin.get()
                if((self.__verifChaine(case1)==True)and(self.__verifChaine(case2)==True)):
                    self.__tableur.minimun(self.__case,case1,case2)
                else :
                    messagebox.showerror("Copilote","Les deux case ne sont pas valide")
            case 6 :
                case1 = self.__entrymaximunDebut.get()
                case2 = self.__entrymaximunFin.get()
                if((self.__verifChaine(case1)==True)and(self.__verifChaine(case2)==True)):
                    self.__tableur.maximun(self.__case,case1,case2)
                else :
                    messagebox.showerror("Copilote","Les deux case ne sont pas valide")
            
        self.__tableur.saveFile()
        self.__screenEcritureDirect.destroy()
        
