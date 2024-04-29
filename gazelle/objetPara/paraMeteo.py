
from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingMeteo :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #varriable
        self.__varSuppr = StringVar(windows)
        self.__varChoixLieu = StringVar(windows)
        self.__configFile = config
        self.__listChoixLieu = ["Simple","Domicile","Travail"]
        #declaration cadre
        self.__mainFrame = cadre
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__listFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__addFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__supprFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        labelTitre = [
            Label(self.__acceuilFrame,text="Parametre Meteo",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__listFrame,text="Liste de ville enregistrer",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__addFrame,text="Ecrivez la ville\nque vous voulez rajouter",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__supprFrame,text="Selectionner la ville\nque vous voulez supprimer",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.__listFrame,text="Retour",bg=color,fg=textColor,command=self._backAcceuil,font=("arial","15")),
            Button(self.__addFrame,text="Annuler",bg=color,fg=textColor,command=self._backAcceuil,font=("arial","15")),
            Button(self.__supprFrame,text="Annuler",bg=color,fg=textColor,command=self._backAcceuil,font=("arial","15"))
        ]
        #Frame acceuilFrame
        btnListMeteo =  Button(self.__acceuilFrame,text="      Liste meteo      ",bg=color,fg=textColor,font=("arial","15"),command=self.viewListMeteo)
        btnAddVille =   Button(self.__acceuilFrame,text="   Ajouter une ville   ",bg=color,fg=textColor,font=("arial","15"),command=self.addView)
        btnSupprVille = Button(self.__acceuilFrame,text="   Supprimer une ville ",bg=color,fg=textColor,font=("arial","15"),command=self.supprView)
        #frame listFrame
        self.__labelListe = Label(self.__listFrame,bg=color,fg=textColor,font=("arial","15"))
        #frame addFrame
        menuChoixLieu = OptionMenu(self.__addFrame,self.__varChoixLieu,*self.__listChoixLieu)
        self.__entryVille = Entry(self.__addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnAddValidate = Button(self.__addFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self._add)
        #frame supprFrame
        btnSupprValidate = Button(self.__supprFrame,font=("arial","15"),text="Valider",bg=color,fg=textColor,command=self._suppr)
        #recuperartion valeur 
        centrageAcceuil = self.__acceuilFrame.winfo_reqwidth()
        centrageAddVille = self.__addFrame.winfo_reqwidth()
        hauteurRetour = btnRetour[0].winfo_reqheight()
        largeurRetour = btnRetour[0].winfo_reqwidth()
        hauteurCadre = self.__acceuilFrame.winfo_reqheight()
        largeurCadre = self.__acceuilFrame.winfo_reqwidth()
        #affichage
        # acceuilFrame
        labelTitre[0].place(x=((centrageAcceuil-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnListMeteo.place(x=((centrageAcceuil-btnListMeteo.winfo_reqwidth())//2),y=200)
        btnAddVille.place(x=((centrageAcceuil-btnAddVille.winfo_reqwidth())//2),y=275)
        btnSupprVille.place(x=((centrageAcceuil-btnSupprVille.winfo_reqwidth())//2),y=350)
        # listFrame
        labelTitre[1].place(x=((self.__listFrame.winfo_reqwidth()-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.__labelListe.place(x=0,y=(labelTitre[1].winfo_reqheight()+10))
        btnRetour[0].place(x=(largeurCadre-largeurRetour),y=(hauteurCadre-hauteurRetour))
        # addVilleFrame
        labelTitre[2].place(x=((centrageAddVille-labelTitre[2].winfo_reqwidth())//2),y=0)
        menuChoixLieu.place(x=15,y=((labelTitre[2].winfo_reqheight()+menuChoixLieu.winfo_reqheight())+15))
        self.__entryVille.place(relx=0.5,rely=0.5,anchor="center")
        btnAddValidate.place(x=0,y=(hauteurCadre-btnAddValidate.winfo_reqheight()))
        btnRetour[1].place(x=(largeurCadre-largeurRetour),y=(hauteurCadre-hauteurRetour))
        # supprFrame
        labelTitre[3].place(x=((centrageAddVille-labelTitre[3].winfo_reqwidth())//2),y=0)
        btnSupprValidate.place(x=0,y=(hauteurCadre-btnSupprValidate.winfo_reqheight()))
        btnRetour[2].place(x=(largeurCadre-largeurRetour),y=(hauteurCadre-hauteurRetour))
        
        
    def view(self)->bool:
        self.__mainFrame.pack(side="left")
        self.__acceuilFrame.place(x=0,y=0)
        self._backAcceuil()
        return True
    
    def _backAcceuil(self)->bool:
        self.__listFrame.place_forget()
        self.__addFrame.place_forget()
        self.__supprFrame.place_forget()
        self.__acceuilFrame.place(x=0,y=0)
        self.__acceuilFrame.update()
        return True 
    
    def viewListMeteo(self) ->bool:
        self.__acceuilFrame.place_forget()
        self.__listFrame.place(x=0,y=0)
        if self.__labelListe.cget("text"):
            self.__listFrame.config(text="")
        listeVille = []
        if not self.__configFile.lectureJSON("lieuDomicile")  :
            listeVille.append("Pas de lieu domicile enregistrer")
        else :
            listeVille.append("Lieu domicile enregistrer")
        if not self.__configFile.lectureJSON("lieuTravail") :
            listeVille.append("Pas de lieu travail enregistrer")
        else :
            listeVille.append("Lieu travail enregistrer")   
        listeVille = listeVille + self.__configFile.lectureJSONList("listVille")
        for i in range(0,len(listeVille)):
            self.__labelListe.configure(text=self.__labelListe.cget("text")+listeVille[i]+"\n")
        return True
            
    def addView(self)->bool:
        self.__acceuilFrame.place_forget()
        self.__entryVille.delete(0,"end")
        self.__varChoixLieu.set(self.__listChoixLieu[0])
        self.__addFrame.place(x=0,y=0)
        return True
    
    def _add(self)->bool:
        typeVille  = self.__varChoixLieu.get()
        if (typeVille == self.__listChoixLieu[0]):
            self.__configFile.EcritureJSONList("listVille",str(self.__entryVille.get()))
        else :
            if (typeVille == self.__listChoixLieu[1]):
                self.__configFile.EcritureJSON("lieuDomicile",str(self.__entryVille.get()))
            else :
                if (typeVille == self.__listChoixLieu[2]):
                    self.__configFile.EcritureJSON("lieuTravail",str(self.__entryVille.get()))
        self._backAcceuil()
        messagebox.showinfo("Ecriture terminer","Votre ville a été enregister")
        return True
    
    def supprView(self)->bool:
        if (len(str(self.__configFile.lectureJSON("lieuDomicile")))==0 ) and (len(str(self.__configFile.lectureJSON("lieuTravail")))==0) and (len(self.__configFile.lectureJSONList("listVille"))==0) :
            self._backAcceuil()
            messagebox.showerror("Aucun donner enregister","Ajouter des villes dans la meteo avant d'en supprimer")
        else :
            self.__supprFrame.place(x=0,y=0)
            listeVille = []
            if len(str(self.__configFile.lectureJSON("lieuDomicile")))>0 :
                listeVille.append("Domicile")
            if len(str(self.__configFile.lectureJSON("lieuTravail")))>0 :
                listeVille.append("Travail")
            listeVille = listeVille + self.__configFile.lectureJSONList("listVille")
            print(listeVille)
            self.menuVille = OptionMenu(self.__supprFrame,self.__varSuppr,*listeVille)
            self.menuVille.place(relx=0.5,rely=0.5,anchor="center")
            self.__varSuppr.set(listeVille[0])
            self.menuVille.update()
        return True
    
    def _suppr(self)->bool:
        valeur = self.__varSuppr.get()
        if valeur == "Domicile" :
            self.__configFile.suppressionJson("lieuDomicile")
        else :
            if valeur == "Travail" :
                self.__configFile.suppressionJson("lieuTravail")
            else :
                self.__configFile.suppressionJsonList("listVille",valeur)
        self.menuVille.destroy()
        self._backAcceuil() 