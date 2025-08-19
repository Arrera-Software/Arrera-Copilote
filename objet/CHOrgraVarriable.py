from tkinter import*
from tkinter.filedialog import*
from tkinter.messagebox import*
from ObjetsNetwork.gestion import*
from librairy.asset_manage import resource_path

class CHOrgraVarriable:
    def __init__(self,ConfigNeuron:jsonWork,dectOS:OS):
        self.__mainColor = ConfigNeuron.lectureJSON("interfaceColor")
        self.__mainTextColor = ConfigNeuron.lectureJSON("interfaceTextColor")
        self.__iconAssistant = resource_path(ConfigNeuron.lectureJSON("iconAssistant"))
        self.__name = ConfigNeuron.lectureJSON("name")
        self.__docOpen = False
        self.__file = ""
        self.__objetOS = dectOS
    
    def bootOrganisateur(self):
        self.__docOpen = False
        self.__file = ""
        self.__screenOrganisateurVar = Toplevel()
        self.__screenOrganisateurVar.minsize(1000,700)
        self.__screenOrganisateurVar.maxsize(1000,700)
        self.__screenOrganisateurVar.title(self.__name+" : Codehelp varriable organisateur")
        self.__screenOrganisateurVar.iconphoto(False,PhotoImage(file=self.__iconAssistant))
        self.__screenOrganisateurVar.config(bg="red")
        #var
        self.__varType = StringVar(self.__screenOrganisateurVar)
        self.__varSuppr = StringVar(self.__screenOrganisateurVar)
        self.__listSuppr = ["","",""]
        self.__listType = ["int", "bool", "char", "string", 
                            "float", "list", "tuple", "dict", 
                            "set", "bytes", "date", "time", 
                            "enum", "object"]
        #Frame
        self.__frameNoOpenDoc = Frame(self.__screenOrganisateurVar,width=500,height=700,bg=self.__mainColor)
        frameAdd = Frame(self.__screenOrganisateurVar,width=500,height=350,bg=self.__mainColor,relief=GROOVE,bd=5)
        self.__frameSuppr = Frame(self.__screenOrganisateurVar,width=500,height=350,bg=self.__mainColor,relief=GROOVE,bd=5)
        #Widget
        self.__zoneEcriture = Text(self.__screenOrganisateurVar)
        #Menu
        self.__menuediteur = Menu(self.__screenOrganisateurVar,bg=self.__mainColor,fg=self.__mainTextColor)
        self.__menuediteur.add_command(label="Enregistrer",command=self.__saveOnFile)
        self.__menuediteur.add_command(label="Nouveau",command=self.__newDoc)
        self.__menuediteur.add_command(label="Ouvrir",command=self.__openDoc)
        #frameNoOpenDoc
        labelNoDoc = Label(self.__frameNoOpenDoc,font=("arial","35"),bg=self.__mainColor,fg=self.__mainTextColor,text="Pas de document\nouvert")
        #Widget frameAdd
        labelAdd = Label(frameAdd,text="Ajouter une varriable",font=("arial","25"),bg=self.__mainColor,fg=self.__mainTextColor)
        btnAdd = Button(frameAdd,text="Valider",font=("arial","15"),bg=self.__mainColor,fg=self.__mainTextColor,command=self.__addValeur)
        frameEntry = Frame(frameAdd,bg=self.__mainColor,width=485,height=70)
        self.__entryName = Entry(frameEntry,font=("arial","13"),relief=SOLID)
        self.__entryValeur = Entry(frameEntry,font=("arial","13"),relief=SOLID)
        menuType = OptionMenu(frameEntry,self.__varType,*self.__listType)
        #Widget frameSuppr
        labelSuppr = Label(self.__frameSuppr,text="Supprimer une varriable",font=("arial","25"),bg=self.__mainColor,fg=self.__mainTextColor)
        btnSuppr = Button(self.__frameSuppr,text="Valider",font=("arial","15"),bg=self.__mainColor,fg=self.__mainTextColor,command=self.__supprValeur)
        self.__menuSuppr = OptionMenu(self.__frameSuppr,self.__varSuppr,*self.__listSuppr)
        #Affichage
        self.__frameNoOpenDoc.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        if (self.__objetOS.osWindows()==True):
            frameAdd.place(x=(self.__screenOrganisateurVar.winfo_width()/2), y=0)
            self.__frameSuppr.place(x=self.__screenOrganisateurVar.winfo_width()/2, y=self.__screenOrganisateurVar.winfo_height()/2)
        else :
            if (self.__objetOS.osLinux()==True):
                frameAdd.place(x=500, y=0)
                self.__frameSuppr.place(x=500, y=350)
        #frameAdd
        labelAdd.place(x=((frameAdd.winfo_reqwidth()-labelAdd.winfo_reqwidth())//2),y=2)
        btnAdd.place(x=((frameAdd.winfo_reqwidth()-btnAdd.winfo_reqwidth())//2),y=(frameAdd.winfo_reqheight()-btnAdd.winfo_reqheight()-2))
        frameEntry.place(relx=0.5,rely=0.5,anchor="center")
        self.__entryName.place(x=2,y=((frameEntry.winfo_reqheight()-self.__entryName.winfo_reqheight())//2))
        menuType.place(relx=0.5,rely=0.5,anchor="center")
        self.__entryValeur.place(x=((frameEntry.winfo_reqwidth()-self.__entryValeur.winfo_reqwidth())-2),y=((frameEntry.winfo_reqheight()-self.__entryValeur.winfo_reqheight())//2))
        #frameSuppr
        labelSuppr.place(x=((self.__frameSuppr.winfo_reqwidth()-labelSuppr.winfo_reqwidth())//2),y=0)
        self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
        if (self.__objetOS.osWindows()==True):
            btnSuppr.place(x=((self.__frameSuppr.winfo_reqwidth()-btnSuppr.winfo_reqwidth())//2),y=(self.__frameSuppr.winfo_reqheight()-btnSuppr.winfo_reqheight()-10))
        else :
            if (self.__objetOS.osLinux()==True):
                btnSuppr.place(x=((self.__frameSuppr.winfo_reqwidth()-btnSuppr.winfo_reqwidth())//2),y=(self.__frameSuppr.winfo_reqheight()-btnSuppr.winfo_reqheight()-40))
        #frameNoOpenDoc
        labelNoDoc.place(relx=0.5,rely=0.5,anchor="center")
        #Ajout de menu a la fenetre
        self.__varType.set(self.__listType[0])
        self.__screenOrganisateurVar.config(menu=self.__menuediteur)

    def __openDoc(self):
        if self.__docOpen == True :
            showwarning("Document ouvert","Un document est encore ouvert fermer le avant d'ouvrir un autre")
        else :
            self.__file = askopenfilename(defaultextension=".chov", filetypes=[("Fichier Codehelp Orga Var", ".chov")])
            if self.__file :
                self.__docOpen = True 
                self.__menuediteur.entryconfigure("Ouvrir",label="Fermer",command=self.__closeDoc)
                self.__frameNoOpenDoc.place_forget()
                self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                with open(self.__file, "r") as f:
                    data = json.load(f)
                    self.__zoneEcriture.config(state="normal")
                    self.__zoneEcriture.delete("1.0", END)
                    for key, value in data.items():
                        self.__zoneEcriture.config(state="normal")
                        self.__zoneEcriture.insert(END, f"{key}:{value}\n")
                        self.__zoneEcriture.config(state="disable")
                    self.__refreshSuppr()
            else :
                showwarning("Aucun document selectionner","Veuillez selectionner un document")

    def __newDoc(self):
        self.__file = asksaveasfilename(defaultextension=".chov", filetypes=[("Fichier Codehelp Orga Var", ".chov")])
        if self.__file :
            #Initialisation de zoneEcriture
            self.__zoneEcriture.config(state="normal")
            self.__zoneEcriture.delete("1.0",END)
            self.__zoneEcriture.insert("1.0","Type name : valeur")
            self.__zoneEcriture.config(state="disable")
            self.__docOpen = True 
            self.__menuediteur.entryconfigure("Ouvrir",label="Fermer",command=self.__closeDoc)
            self.__frameNoOpenDoc.place_forget()
            self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
            self.__refreshSuppr()
            self.__saveOnFile()
        else :
            showwarning("Aucun document enregister","Veuillez enregister un document")

    def __closeDoc(self):
        if self.__docOpen == True :
            self.__file = ""
            self.__docOpen = False
            self.__menuediteur.entryconfigure("Fermer",label="Ouvrir",command=self.__openDoc)
            self.__zoneEcriture.place_forget()
            self.__frameNoOpenDoc.place(relx=0, rely=0, relwidth=0.5, relheight=1)
            self.__clearMenuSuppr()
        else :
            showwarning("Aucun document ouvert","Aucun document n'est ouvert")

    def __addValeur(self):
        if self.__docOpen == True :
            self.__zoneEcriture.config(state="normal")
            name = self.__entryName.get()
            value = self.__entryValeur.get()
            typeVar = self.__varType.get()
            if name and value and typeVar :
                key = typeVar+" "+name
                self.__entryName.delete(0, END)
                self.__entryValeur.delete(0, END)
                d = self.__zoneEcriture.get("1.0", "end")
                d = dict(map(str, item.split(':')) for item in d.strip().split('\n'))
                d[key] = value
                self.__zoneEcriture.delete("1.0", END)
                for key, value in d.items():
                    self.__zoneEcriture.insert(END, f"{key}:{value}\n")
                self.__zoneEcriture.place_forget()
                self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                self.__zoneEcriture.config(state="disable")
                self.__saveOnFile()
                self.__refreshSuppr()
            else:
                showwarning("Erreur ecriture","Veuillez entrer tout la valeur pour ajouter une varriable")
        else :
            showwarning("Aucun document ouvert","Veuillez ouvrir un document")

    def __saveOnFile(self):
        if self.__docOpen == True :
            data = self.__zoneEcriture.get("1.0", "end")
            data = dict(map(str, item.split(':')) for item in data.strip().split('\n'))
            with open(self.__file, "w") as f:
                json.dump(data, f)
        else :
            showwarning("Imposible d'enregistrer","Aucun document ouvert")

    def __refreshSuppr(self):
        self.__menuSuppr.place_forget()
        self.__menuSuppr.destroy()
        data = self.__zoneEcriture.get("1.0", "end")
        data = dict(map(str, item.split(':')) for item in data.strip().split('\n'))
        del data["Type name "]
        if not data :
            self.__listSuppr = ["","",""]
        else :
            self.__listSuppr = list(data.keys())
        self.__menuSuppr = OptionMenu(self.__frameSuppr,self.__varSuppr,*self.__listSuppr)
        self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
    
    def __supprValeur(self):
        valeur = self.__varSuppr.get()
        if valeur :
            d = self.__zoneEcriture.get("1.0", "end")
            d = dict(map(str, item.split(':')) for item in d.strip().split('\n'))
            del d[valeur]
            self.__zoneEcriture.config(state="normal")
            self.__zoneEcriture.delete("1.0", END)
            for key, value in d.items():
                self.__zoneEcriture.insert(END, f"{key}:{value}\n")
            self.__zoneEcriture.place_forget()
            self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
            self.__zoneEcriture.config(state="disable")
            self.__saveOnFile()
            self.__refreshSuppr()
        else :
            showwarning("Imposible de supprimer une varriable","Aucun varriable selectionner")
    
    def __clearMenuSuppr(self):
        self.__menuSuppr.place_forget()
        self.__menuSuppr.destroy()
        self.__listSuppr = ["","",""]
        self.__menuSuppr = OptionMenu(self.__frameSuppr,self.__varSuppr,*self.__listSuppr)
        self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")