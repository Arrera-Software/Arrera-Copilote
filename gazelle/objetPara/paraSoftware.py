from tkinter import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingSoftware :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,settingConfig:jsonWork,neuronFile:jsonWork,textColor:str,color:str):
        #varriable
        self.__config = config
        self.__assistantFile = neuronFile
        self.__varType = StringVar(windows)
        self.__varSuppr = StringVar(windows)
        self.__varSupprSpe = StringVar(windows)
        self.__listTypeSoft = [
            "Autre",
            "Traitement de texte",
            "Tableur",
            "Presentation",
            "Navigateur Internet",
            "Note",
            "Musique"
        ]
        self.__listTypeSoftSpe = [
            "Traitement de texte",
            "Tableur",
            "Presentation",
            "Navigateur Internet",
            "Note",
            "Musique"
        ]
        #declaration cadre
        self.__mainFrame = cadre
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__addFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__supprFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__addLinuxFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__supprSpeFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #objet detction 
        self.__dectOS = OS()
        #widget
        labelTitre = [
            Label(self.__acceuilFrame,text="Gestion logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__addFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__supprFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__addLinuxFrame,text="Entrer la commande\npour lancer le logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__supprSpeFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","20")),
            ]
        btnRetour = [
            Button(self.__addFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.__supprFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.__addLinuxFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.__supprSpeFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil)
        ]
        #acceuilFrame
        btnAjout=Button(self.__acceuilFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","15"),command=self.addView) 
        btnSuppr=Button(self.__acceuilFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","15"),command=self.supprSoft)
        btnSupprSpe =Button(self.__acceuilFrame,text="Supprimer logiciel speciaux",bg=color,fg=textColor,font=("arial","15"),command=self._supprSpeciauxViev)
        btnSetEmplacement = Button(self.__acceuilFrame,text="Definir emplacement",bg=color,fg=textColor,font=("arial","15"),command=self._setEmplacementWindows)
        #supprFrame
        btnValiderSuppr = Button(self.__supprFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"),command=self._suppr) 
        #addFrame
        self.__entryNameSoft = Entry(self.__addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        menuTypeSoft = OptionMenu(self.__addFrame,self.__varType,*self.__listTypeSoft)
        self.__varType.set(self.__listTypeSoft[0])
        btnValiderAdd = Button(self.__addFrame,text="Ajouter",bg=color,fg=textColor,font=("arial","15")) 
        #addLinuxFram
        self.__entryCommandSoft = Entry(self.__addLinuxFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnSaveLinux = Button(self.__addLinuxFrame,text="Enregistrer",bg=color,fg=textColor,font=("arial","15"),command=self._saveSoftLinux) 
        #supprSpe
        menuSupprSpe = OptionMenu(self.__supprSpeFrame,self.__varSupprSpe,*self.__listTypeSoftSpe)
        btnValiderSupprSpe = Button(self.__supprSpeFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"),command=self._supprSpeciaux)
        if (self.__dectOS.osLinux()==True):
            btnValiderAdd.configure(command=self._addLinuxView)
        else :
            if (self.__dectOS.osWindows() == True) :
                btnValiderAdd.configure(command=self._addSoftWindows)
                self.__softWin  = gestionSoftWindows(neuronFile.lectureJSON("emplacementSoftWindows"))
        #calcule affichage
        largeurFrame=self.__acceuilFrame.winfo_reqwidth()
        hauteurFrame=self.__acceuilFrame.winfo_reqheight()
        #Affichage
        #acceuilFrame
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnAjout.place(x=((largeurFrame-btnAjout.winfo_reqwidth())//2),y=175)
        btnSuppr.place(x=((largeurFrame-btnSuppr.winfo_reqwidth())//2),y=250)
        btnSupprSpe.place(x=((largeurFrame-btnSupprSpe.winfo_reqwidth())//2),y=325)
        if (self.__dectOS.osWindows()==True):
            btnSetEmplacement.place(x=((largeurFrame-btnSetEmplacement.winfo_reqwidth())//2),y=400)
        #addFrame
        labelTitre[1].place(x=((largeurFrame-labelTitre[1].winfo_reqwidth())//2),y=0)
        menuTypeSoft.place(x=10,y=((labelTitre[1].winfo_reqheight()+menuTypeSoft.winfo_reqheight())+5))
        self.__entryNameSoft.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderAdd.place(x=0,y=(hauteurFrame-btnValiderAdd.winfo_reqheight()))
        btnRetour[0].place(x=(largeurFrame-btnRetour[0].winfo_reqwidth()),y=(hauteurFrame-btnRetour[0].winfo_reqheight()))
        #suppr Frame
        labelTitre[2].place(x=((largeurFrame-labelTitre[2].winfo_reqwidth())//2),y=0)
        btnValiderSuppr.place(x=0,y=(hauteurFrame-btnValiderSuppr.winfo_reqheight()))
        btnRetour[1].place(x=(largeurFrame-btnRetour[1].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
        #addLinuxFrame
        labelTitre[3].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        self.__entryCommandSoft.place(relx=0.5,rely=0.5,anchor="center")
        btnSaveLinux.place(x=0,y=(hauteurFrame-btnSaveLinux.winfo_reqheight()))
        btnRetour[2].place(x=(largeurFrame-btnRetour[2].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
        #varSupprSpe
        labelTitre[4].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        menuSupprSpe.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderSupprSpe.place(x=0,y=(hauteurFrame-btnValiderSupprSpe.winfo_reqheight()))
        btnRetour[3].place(x=(largeurFrame-btnRetour[3].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
    
    def view(self)->bool:
        self.__mainFrame.pack(side="left")
        self._backAcceuil()
        return True
    
    def _backAcceuil(self)->bool:
        self.__addFrame.place_forget()
        self.__supprFrame.place_forget()
        self.__addLinuxFrame.place_forget()
        self.__supprSpeFrame.place_forget()
        self.__acceuilFrame.place(x=0,y=0)
        return True
        
    
    def addView(self)->bool:
        self.__entryNameSoft.delete(0,END)
        self.__varType.set(self.__listTypeSoft[0])
        self.__acceuilFrame.place_forget()
        self.__addFrame.place(x=0,y=0)
        return True
    
    def _saveSoftWindows(self,name:str,flag:str,dict:bool)->bool:
        if name:
            self.__softWin.setName(name)
            sortie = self.__softWin.saveSoftware()
            if sortie == True :
                if dict == True :
                    self.__config.EcritureJSONDictionnaire(flag,name,self.__softWin.getName())
                else :
                    self.__config.EcritureJSON(flag,self.__softWin.getName())
                messagebox.showinfo("Logiciel sauvegarder","Le logiciel a bien etais enregister")
                return True
            else :
                messagebox.showerror("Erreur emplacement","Une erreur c'est produit lors de la selection de l'emplacement")
                return False
        else :
            messagebox.showerror("Erreur nom","Vous pouver pas enregister un logiciel sans nom")
            return False
    
    def _setEmplacementWindows(self)->bool:
        messagebox.showinfo("Infomation","Vous devait selectionner un dossier deja crée")
        sortie = self.__softWin.setEmplacementSoft()
        self.__assistantFile.EcritureJSON("emplacementSoftWindows",sortie)
        return True
    
    def _addSoftWindows(self)->bool:
        typeSoft = self.__varType.get()
        if typeSoft == self.__listTypeSoft[0]:
            self._saveSoftWindows(self.__entryNameSoft.get(),"dictSoftWindows",True)
            nbSoft = int(self.__config.lectureJSON("nbSoft"))
            self.__config.EcritureJSON("nbSoft",str(nbSoft+1))
        else :
            if typeSoft == self.__listTypeSoft[1]:
                self._saveSoftWindows("TTexte","wordWindows",False)
            else :
                if typeSoft == self.__listTypeSoft[2]:
                    self._saveSoftWindows("tableur","exelWindows",False)
                else :
                    if typeSoft == self.__listTypeSoft[3]:
                        self._saveSoftWindows("presentation","diapoWindows",False)
                    else :
                        if typeSoft == self.__listTypeSoft[4]:
                            self._saveSoftWindows("internet","browserWindows",False)
                        else :
                            if typeSoft == self.__listTypeSoft[5]:
                                self._saveSoftWindows("note","noteWindows",False)
                            else :
                                if typeSoft == self.__listTypeSoft[6]:
                                    self._saveSoftWindows("musique","musicWindows",False)
        self.__entryNameSoft.delete(0,END)
        self._backAcceuil() 
        return bool
        
    def supprSoft(self)->bool:
        if (self.__dectOS.osWindows()==True):
            listSoft= list(self.__config.lectureJSONDict("dictSoftWindows").keys())
        else :
            listSoft= list(self.__config.lectureJSONDict("dictSoftLinux").keys())
        if not listSoft :
            messagebox.showerror("Erreur","Aucun logiciel n'est enregistrer")
        else :
            self.__acceuilFrame.place_forget()
            self.__supprFrame.place(x=0,y=0)
            self.menuSuppr = OptionMenu(self.__supprFrame,self.__varSuppr,*listSoft)
            self.menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
        return True
            
    def _suppr(self)-> bool:
        if (self.__dectOS.osWindows()==True):
            name = self.__varSuppr.get()
            self.__config.supprJSONList("dictSoftWindows",name)
            self.__softWin.supprSoft(name)
            nbSoft = int(self.__config.lectureJSON("nbSoft"))
            self.__config.EcritureJSON("nbSoft",str(nbSoft-1))
        else :
            if (self.__dectOS.osLinux()==True):
                self.__config.supprJSONList("dictSoftLinux",self.__varSuppr.get())
                nbSoft = int(self.__config.lectureJSON("nbSoft"))
                self.__config.EcritureJSON("nbSoft",str(nbSoft-1))
        self._backAcceuil()
        self.menuSuppr.destroy() 
        return True 
        
        
    def _addLinuxView(self)-> bool:
        self.__addFrame.place_forget()
        self.__addLinuxFrame.place(x=0,y=0)
        return True 
        
    def _saveSoftLinux(self)-> bool:
        command = self.__entryCommandSoft.get()
        typeSoft = self.__varType.get()
        if typeSoft == self.__listTypeSoft[0]:
            name = self.__entryNameSoft.get()
            self.__config.EcritureJSONDictionnaire("dictSoftLinux",name,command)
            nbSoft = int(self.__config.lectureJSON("nbSoft"))
            self.__config.EcritureJSON("nbSoft",str(nbSoft+1))
        else :
            if typeSoft == self.__listTypeSoft[1]:
                self.__config.EcritureJSON("wordLinux",command)
            else :
                if typeSoft == self.__listTypeSoft[2]:
                    self.__config.EcritureJSON("exelLinux",command)
                else :
                    if typeSoft == self.__listTypeSoft[3]:
                        self.__config.EcritureJSON("diapoLinux",command)
                    else :
                        if typeSoft == self.__listTypeSoft[4]:
                            self.__config.EcritureJSON("browserLinux",command)
                        else :
                            if typeSoft == self.__listTypeSoft[5]:
                                self.__config.EcritureJSON("noteLinux",command)
                            else :
                                if typeSoft == self.__listTypeSoft[6]:
                                    self.__config.EcritureJSON("musicLinux",command)
        self._backAcceuil()
        self.__entryNameSoft.delete("0",END)
        self.__entryCommandSoft.delete("0",END)
        return True 
    
    def _supprSpeciauxViev(self)->bool:
        self.__acceuilFrame.place_forget()
        self.__varSupprSpe.set(self.__listTypeSoftSpe[0])
        self.__supprSpeFrame.place(x=0,y=0)
        return bool
    
    def _supprSpeciaux(self)->bool:
        typeSoft = self.__varSupprSpe.get()
        if typeSoft == self.__listTypeSoftSpe[0]:
            if (self.__dectOS.osWindows()==True):
                if not self.__config.lectureJSON("wordWindows") :
                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                else :
                    self.__softWin.supprSoft("TTexte")
                    self.__config.suppressionJson("wordWindows")
            else :
                if not self.__config.lectureJSON("wordLinux") :
                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                else :
                    self.__config.suppressionJson("wordLinux")
        else :
            if typeSoft == self.__listTypeSoftSpe[1]:

                if (self.__dectOS.osWindows()==True):
                    if not self.__config.lectureJSON("exelWindows") :
                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                    else :
                        self.__softWin.supprSoft("tableur")
                        self.__config.suppressionJson("exelWindows")
                else :
                    if not self.__config.lectureJSON("exelLinux") :
                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                    else :
                        self.__config.suppressionJson("exelLinux")
            else :
                if typeSoft == self.__listTypeSoftSpe[2]:
                    if (self.__dectOS.osWindows()==True):
                        if not self.__config.lectureJSON("diapoWindows") :
                            messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                        else :
                            self.__softWin.supprSoft("presentation")
                            self.__config.suppressionJson("diapoWindows")
                    else :
                        if not self.__config.lectureJSON("diapoLinux") :
                            messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                        else :
                            self.__config.suppressionJson("diapoLinux")
                else :
                    if typeSoft == self.__listTypeSoftSpe[3]:
                        if (self.__dectOS.osWindows()==True):
                            if not self.__config.lectureJSON("browserWindows") :
                                messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                            else :
                                self.__softWin.supprSoft("internet")
                                self.__config.suppressionJson("browserWindows")
                        else :
                            if not self.__config.lectureJSON("browserLinux") :
                                messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                            else :
                                self.__config.suppressionJson("browserLinux")
                    else :
                        if typeSoft == self.__listTypeSoftSpe[4]:
                            if (self.__dectOS.osWindows()==True):
                                if not self.__config.lectureJSON("noteWindows") :
                                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                else :
                                    self.__softWin.supprSoft("note")
                                    self.__config.suppressionJson("noteWindows")
                            else :
                                if not self.__config.lectureJSON("noteLinux") :
                                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                else :
                                    self.__config.suppressionJson("noteLinux")
                        else :
                            if typeSoft == self.__listTypeSoftSpe[5]:
                                if (self.__dectOS.osWindows()==True):
                                    if not self.__config.lectureJSON("musicWindows") :
                                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                    else :
                                        self.__softWin.supprSoft("musique")
                                        self.__config.suppressionJson("musicWindows")
                                else :
                                    if not self.__config.lectureJSON("musicLinux") :
                                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                    else :
                                        self.__config.suppressionJson("musicLinux")
        self._backAcceuil()
        return True