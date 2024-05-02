from fonctionnalites.arreratableur import*
from tkinter import*
from tkinter import filedialog, messagebox
import re


class CArreraCopiloteTableur :
    def __init__(self) :
        self.__color = "white"
        self.__textColor = "black"
        self.__caseSelect = str
        self.__actionSelect = str
    
    def active(self):
        file = ""
        result = messagebox.askquestion(
            "Choix de l'action", 
            "Voulez-vous créer un nouveau fichier ou ouvrir un fichier existant ?")
        if (result=="yes"):
            while (file=="") :
                file = filedialog.asksaveasfilename(
                    defaultextension='.xlsx', 
                    filetypes=[("Fichiers Excel", "*.xlsx"),("Fichiers ODF", "*.ods")])
        else :
            while (file=="") :
                file = filedialog.askopenfilename(
                    filetypes=[("Fichiers Excel", "*.xlsx"),("Fichiers ODF", "*.ods")])
        
        self.__tableur = CArreraTableur(file)
        screen = Toplevel()
        screen.title("Copilote : Tableur")
        screen.iconphoto(False,PhotoImage(file="asset/icon/copilote/icon.png"))
        screen.maxsize(700,700)
        screen.minsize(700,700)
        # Varriable
        self.__action = StringVar(screen)
        listAction = ["ecrire une valeur","faire une moyenne","faire une somme",
                    "faire un comptage","faire un minimun","faire un maximun","supprimer un valeur"]
        #Cadre principal
        self.__mainFrame = Frame(screen,width=350,height=700,bg="red")
        # Label Affichage contenu tableur 
        self.__labelTableurView = Label(screen,font=("arial",12),
                                      fg=self.__textColor,bg=self.__color,
                                      )
        #Cadre secondaire
        self.__frameCase = Frame(self.__mainFrame,bg=self.__color)
        self.__frameAction =  Frame(self.__mainFrame,bg=self.__color)
        # widget mainframe
        labelIndication = Label(self.__mainFrame,text="Modifier le tableur",
                                font=("arial",15),fg=self.__textColor,bg=self.__color)
        self.__labelCaseSelect = Label(self.__mainFrame,font=("arial",15),
                                       fg=self.__textColor,bg=self.__color)
        self.__labelfncSelect = Label(self.__mainFrame,font=("arial",15),
                                       fg=self.__textColor,bg=self.__color)
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
        self.__frameCase.place(x=15,y=35)
        self.__frameAction.place(x=15,y=85)
        # Affichage principale
        self.__mainFrame.pack(side="left")
        self.__labelTableurView.pack(side="left",anchor="n")
    
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
                self.__caseSelect = case 
                self.__labelCaseSelect.configure(text="Case selectionner : "+case)
                self.__frameCase.place_forget()
                self.__labelCaseSelect.place(x=15,y=35)

            else :
                messagebox.showerror("Case invalide","La case n'est pas valide")
        self.__entryCase.delete(0,END)
    
    def __setAction(self):
        action = self.__action.get()
        self.__actionSelect = action
        self.__frameAction.place_forget()
        self.__labelfncSelect.configure(text="Action : "+action)
        self.__labelfncSelect.place(x=15,y=85)