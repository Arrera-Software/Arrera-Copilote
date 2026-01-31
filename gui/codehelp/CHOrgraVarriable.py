from tkinter import StringVar,Text,Menu
from tkinter.messagebox import *
from tkinter.filedialog import *
from librairy.arrera_tk import *
import json

from gui.codehelp.CCHguiBase import CCHguiBase,gestionnaire

class CHOrgraVarriable(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Organisateur de varriable")
        self.__docOpen = False
        self.__file = ""
        self.__objetOS = self._gestionnaire.getOSObjet()
        # Var
        self.__listSuppr = ["", "", ""]
        self.__listType = ["int", "bool", "char", "string",
                           "float", "list", "tuple", "dict",
                           "set", "bytes", "date", "time",
                           "enum", "object"]
        self.__varType = None
        self.__varSuppr = None

    
    def _mainframe(self):
        self.__docOpen = False
        self.__file = ""
        #var
        self.__varType = StringVar(self._screen)
        self.__varSuppr = StringVar(self._screen)

        # Modif sur le screen
        self._screen.minsize(1000, 700)
        self._screen.maxsize(1000, 700)
        self._screen.resizable(FALSE, FALSE)
        #Frame
        self.__frameNoOpenDoc = self._arrtk.createFrame(self._screen, width=900, height=700)
        self.__frameAdd = self._arrtk.createFrame(self._screen, width=500, height=350)
        self.__frameSuppr = self._arrtk.createFrame(self._screen, width=500, height=350)
        frameEntry = self._arrtk.createFrame(self.__frameAdd, width=485, height=70)
        #Widget
        self.__zoneEcriture = Text(self._screen)
        #Menu
        self.__menuediteur = Menu(self._screen)
        self.__fichiermenu = Menu(self.__menuediteur, tearoff=0)
        self.__fichiermenu.add_command(label="Enregistrer", command=self.__saveOnFile)
        self.__fichiermenu.add_command(label="Nouveau", command=self.__newDoc)
        self.__fichiermenu.add_command(label="Ouvrir", command=self.__openDoc)
        self.__menuediteur.add_cascade(label="Fichier", menu=self.__fichiermenu)
        self._screen.config(menu=self.__menuediteur)
        #frameNoOpenDoc
        labelNoDoc = self._arrtk.createLabel(self.__frameNoOpenDoc,ppolice="arial",ptaille=35,text="Pas de document\nouvert")
        #Widget frameAdd
        btnOpenNoDoc = self._arrtk.createButton(self.__frameNoOpenDoc,text="Ouvrir un document",
                                                bg=self._btnColor,fg=self._btnTexteColor,
                                                ppolice="arial",ptaille=25,command=self.__openDoc)
        labelAdd = self._arrtk.createLabel(self.__frameAdd,text="Ajouter une varriable",
                                           ppolice="arial",ptaille=25)
        btnAdd = self._arrtk.createButton(self.__frameAdd,text="Valider",ppolice="arial",ptaille=25,
                                          bg=self._btnColor,fg=self._btnTexteColor,
                                         command=self.__addValeur)
        # Entry
        self.__entryName = self._arrtk.createEntry(frameEntry,ptaille=20)
        self.__entryValeur = self._arrtk.createEntry(frameEntry,ptaille=20)
        # OptionMenu
        menuType = self._arrtk.createOptionMenu(frameEntry,var=self.__varType,value=self.__listType,
                                                bg=self._btnColor,fg=self._btnTexteColor)
        #Widget frameSuppr
        labelSuppr = self._arrtk.createLabel(self.__frameSuppr,text="Supprimer une varriable",ppolice="arial",ptaille=25)
        btnSuppr = self._arrtk.createButton(self.__frameSuppr,text="Valider",ppolice="arial",ptaille=25,
                                            bg=self._btnColor,fg=self._btnTexteColor,command=self.__supprValeur)
        self.__menuSuppr = self._arrtk.createOptionMenu(self.__frameSuppr,var = self.__varSuppr,value = self.__listSuppr,
                                                        bg=self._btnColor,fg=self._btnTexteColor)
        #Affichage
        self._arrtk.placeCenter(self.__frameNoOpenDoc)
        #frameAdd
        self._arrtk.placeTopCenter(labelAdd)
        self._arrtk.placeBottomCenter(btnAdd)
        self._arrtk.placeCenter(frameEntry)
        self._arrtk.placeLeftCenter(self.__entryName)
        self._arrtk.placeCenter(menuType)
        self._arrtk.placeRightCenter(self.__entryValeur)
        #frameSuppr
        labelSuppr.place(x=((self.__frameSuppr.winfo_reqwidth()-labelSuppr.winfo_reqwidth())//2),y=0)
        self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
        self._arrtk.placeBottomCenter(btnSuppr)
        #frameNoOpenDoc
        self._arrtk.placeCenter(labelNoDoc)
        self._arrtk.placeBottomCenter(btnOpenNoDoc)
        #Ajout de menu a la fenetre
        self.__varType.set(self.__listType[0])


    def __openDoc(self):
        if self.__docOpen:
            showwarning("Document ouvert","Un document est encore ouvert fermer le avant d'ouvrir un autre")
        else :
            self.__file = askopenfilename(defaultextension=".chov", filetypes=[("Fichier Codehelp Orga Var", ".chov")])
            if self.__file :
                self.__docOpen = True 
                self.__fichiermenu.entryconfigure("Ouvrir",label="Fermer",command=self.__closeDoc)
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
                    self._arrtk.placeTopRight(self.__frameAdd)
                    self._arrtk.placeBottomRight(self.__frameSuppr)
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
            self.__fichiermenu.entryconfigure("Ouvrir",label="Fermer",command=self.__closeDoc)
            self.__frameNoOpenDoc.place_forget()
            self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
            self._arrtk.placeTopRight(self.__frameAdd)
            self._arrtk.placeBottomRight(self.__frameSuppr)
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
            self.__frameAdd.place_forget()
            self.__frameSuppr.place_forget()
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
                self.__entryName.delete("1", END)
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
        self.__menuSuppr = self._arrtk.createOptionMenu(self.__frameSuppr,var = self.__varSuppr,value=self.__listSuppr
                                                        ,bg=self._btnColor,fg=self._btnTexteColor)
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
        self.__menuSuppr = self._arrtk.createOptionMenu(self.__frameSuppr,var = self.__varSuppr,value=self.__listSuppr,
                                                        bg=self._btnColor,fg=self._btnTexteColor)
        self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")