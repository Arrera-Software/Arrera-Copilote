from fonctionnalites.arreratableur import*
from tkinter import*
from tkinter import filedialog, messagebox


class CArreraCopiloteTableur :
    def __init__(self) :
        self.__color = "white"
        self.__textColor = "black"
        self.__caseSelect = str
    
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
        self.__type = StringVar(screen)
        listAction = ["ecrire une valeur","faire une moyenne","faire une somme",
                    "faire un comptage","faire un minimun","faire un maximun","supprimer un valeur"]
        #Cadre principal
        self.__mainFrame = Frame(screen,width=350,height=700,bg="red")
        # Label Affichage contenu tableur 
        self.labelTableurView = Label(screen,font=("arial",12),
                                      fg=self.__textColor,bg=self.__color,
                                      )
        #Cadre secondaire
        frameCase = Frame(self.__mainFrame,bg=self.__color)
        frameAction =  Frame(self.__mainFrame,bg=self.__color)
        # widget mainframe
        labelIndication = Label(self.__mainFrame,text="Modifier le tableur",
                                font=("arial",15),fg=self.__textColor,bg=self.__color)
        # widget frameCase
        labelCase = Label(frameCase,text="Case :",font=("arial",15),
                          fg=self.__textColor,bg=self.__color)
        self.__entryCase = Entry(frameCase,font=("arial","15"),width=5,relief=SOLID)
        btnSetCase = Button(frameCase,text="Valider",
                            bg=self.__color,fg=self.__textColor,font=("arial","15"))
        # widget mainFrame 
        labelAction = Label(frameAction,text="Action :",font=("arial",15),
                          fg=self.__textColor,bg=self.__color)
        choixAction = OptionMenu(frameAction,self.__type,*listAction)
        btnSetAction = Button(frameAction,text="Valider",
                            bg=self.__color,fg=self.__textColor,font=("arial","15"))
        #set option menu 
        self.__type.set(listAction[0])
        
        self.updateTableur()
        #Affichage 
        
        
        labelIndication.place(x=0,y=0)
        labelCase.pack(side="left")
        self.__entryCase.pack(side="left")
        btnSetCase.pack(side="right")
        labelAction.pack(side="left")
        choixAction.pack(side="left")
        btnSetAction.pack(side="right")
        frameCase.place(x=15,y=35)
        frameAction.place(x=15,y=85)
        self.__mainFrame.pack(side="left")
        self.labelTableurView.pack(side="left",anchor="n")
    
    def updateTableur(self):
        sortie = self.__tableur.read()
        self.labelTableurView.configure(text="Contenu du fichier tableur", justify="left")
        for cell_position, cell_value in sortie.items():
            text = self.labelTableurView.cget("text")
            self.labelTableurView.configure(text=text+"\n"+f"Cellule {cell_position} : {cell_value}", justify="left")

        