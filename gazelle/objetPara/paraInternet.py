from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingInternet :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #variable 
        self.__config = config
        self.__varType = StringVar(windows)
        self.__varSuppr = StringVar(windows)
        self.__listType = ["Autre",
                         "Stokage en ligne"]
        #declaration cadre 
        self.__mainFrame = cadre 
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__addFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__supprFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = [
            Label(self.__acceuilFrame,text="Paramétre d'internet",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__addFrame,text="Ajouter un site",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__supprFrame,text="Supprimer un site",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.__addFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.__supprFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil)
        ]
        #acceuilFrame
        btnAdd = Button(self.__acceuilFrame,text="Ajouter un site",bg=color,fg=textColor,font=("arial","15"),command=self.addView)
        btnSuppr = Button(self.__acceuilFrame,text="Supprimer un site",bg=color,fg=textColor,font=("arial","15"),command=self.supprView)
        #frame addFrame
        self.__menuType = OptionMenu(self.__addFrame,self.__varType,*self.__listType)
        self.__edtName = Entry(self.__addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        self.__edtLien = Entry(self.__addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnValiderAdd = Button(self.__addFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self.add)
        #frame supprFrame
        btnValiderSuppr = Button(self.__supprFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self.suppr)
        #calcule 
        hauteurCadre = self.__acceuilFrame.winfo_reqheight()
        largeurCadre = self.__acceuilFrame.winfo_reqwidth()
        #affichage 
        #acceuilFrame
        labelTitre[0].place(x=((largeurCadre-(labelTitre[0].winfo_reqwidth()))//2),y=0)
        btnAdd.place(x=((largeurCadre-(btnAdd.winfo_reqwidth()))//2),y=200)
        btnSuppr.place(x=((largeurCadre-(btnSuppr.winfo_reqwidth()))//2),y=275)
        #addFrame
        labelTitre[1].place(x=((largeurCadre-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.__menuType.place(x=0,y=((labelTitre[1].winfo_reqheight()+self.__menuType.winfo_reqheight())+10))
        self.__edtName.place(x=((largeurCadre-self.__edtName.winfo_reqwidth())//2),y=200)
        self.__edtLien.place(x=((largeurCadre-self.__edtLien.winfo_reqwidth())//2),y=275)
        btnValiderAdd.place(x=0,y=(hauteurCadre-btnValiderAdd.winfo_reqheight()))
        btnRetour[0].place(x=(largeurCadre-btnRetour[0].winfo_reqwidth()),y=(hauteurCadre-btnRetour[0].winfo_reqheight()))
        #supprFrame
        labelTitre[2].place(x=((largeurCadre-labelTitre[2].winfo_reqwidth())//2),y=0)
        btnValiderSuppr.place(x=0,y=(hauteurCadre-btnValiderSuppr.winfo_reqheight()))
        btnRetour[1].place(x=(largeurCadre-btnRetour[1].winfo_reqwidth()),y=(hauteurCadre-btnRetour[1].winfo_reqheight()))
        
    def _backAcceuil(self)->bool:
        self.__addFrame.place_forget()
        self.__supprFrame.place_forget()
        self.__acceuilFrame.place(x=0,y=0)
        return True
    
    def view(self)->bool:
        self.__mainFrame.pack(side="left")
        self._backAcceuil()
        return True
    
    def addView(self)->bool:
        self.__acceuilFrame.place_forget()
        self.__varType.set(self.__listType[0])
        self.__addFrame.place(x=0,y=0)
        return True
        
    
    def add(self)->bool:
        name = self.__edtName.get()
        lien = self.__edtLien.get()
        varType = self.__varType.get()
        if varType == self.__listType[1]: 
            if lien:
                self.__config.EcritureJSON("lienCloud",lien)
                self.__edtName.delete("0",END)
                self.__edtLien.delete("0",END)
                self._backAcceuil()
                return True
            else :
                messagebox.showerror("Erreur","Veuiller ecrire le lien de votre stokage could")
                self.__edtName.delete("0",END)
                self.__edtLien.delete("0",END)
                self._backAcceuil()
                return False
        else :
            if name and lien : 
                self.__config.EcritureJSONDictionnaire("dictSite",name,lien)
                self.__edtName.delete("0",END)
                self.__edtLien.delete("0",END)
                self._backAcceuil()
                return True
            else :
                messagebox.showerror("Erreur","Veuiller ecrire le lien et le nom du site")
                self.__edtName.delete("0",END)
                self.__edtLien.delete("0",END)
                self._backAcceuil()
                return False
    
    def supprView(self)->bool:
        listSite = list((self.__config.lectureJSONDict("dictSite").keys()))
        if self.__config.lectureJSON("lienCloud") :
            listSite.append("Lien cloud")
        if not listSite :
            messagebox.showerror("Erreur","Aucun site n'est enregistrer")
            return False
        else :        
            self.__acceuilFrame.place_forget()
            self.menuSite = OptionMenu(self.__supprFrame,self.__varSuppr,*listSite)
            self.__supprFrame.place(x=0,y=0)
            self.menuSite.place(relx=0.5,rely=0.5,anchor="center")
            return True
            
    def suppr(self)->bool:
        site = self.__varSuppr.get()
        if (site == "Lien cloud"):
            self.__config.suppressionJson("lienCloud")
        else :
            nb=int(self.__config.lectureJSON("nbSite"))
            self.__config.EcritureJSON("nbSite",str(nb-1))
            self.__config.supprJSONList("dictSite",site)
            messagebox.showinfo("Site supprimer","Le site a ete supprimer")
        self._backAcceuil()
        return True