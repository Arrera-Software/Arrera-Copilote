from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingGPS:
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #variable
        self.__configFile = config
        #cadre
        self.__mainFrame = cadre
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__addresseDomicile = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__addresseWork = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #widget
        labelTitre = [
            Label(self.__acceuilFrame,text="Parametre GPS",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__addresseDomicile,text="Adresse de domicile",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__addresseWork,text="Adresse de travail",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.__addresseDomicile,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.__addresseWork,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil)
        ]
        btnSuppr = [
            Button(self.__addresseDomicile,text="Supprimer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._supprAdresse("domicile")),
            Button(self.__addresseWork,text="Supprimer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._supprAdresse("work"))
        ]
        btnValider = [
            Button(self.__addresseDomicile,text="Enregistrer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._addAdresse("domicile")),
            Button(self.__addresseWork,text="Enregistrer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._addAdresse("work"))
        ]
        self.__entryAdresse = [
            Entry(self.__addresseDomicile,font=("arial","15"),borderwidth=2,relief="solid"),
            Entry(self.__addresseWork,font=("arial","15"),borderwidth=2,relief="solid")
        ]
        #acceuil frame
        btnDomicile = Button(self.__acceuilFrame,text="Adresse de domicile",bg=color,fg=textColor,font=("arial","15"),command=self.domicileView)
        btnWork = Button(self.__acceuilFrame,text="Adresse de travail",bg=color,fg=textColor,font=("arial","15"),command=self.workView)
        #recuperartion valeur 
        centrageAcceuil = self.__acceuilFrame.winfo_reqwidth()
        hauteurCadre = self.__acceuilFrame.winfo_reqheight()
        largeurCadre = self.__acceuilFrame.winfo_reqwidth()
        #affichage 
        #acceuilFrame
        labelTitre[0].place(x=((centrageAcceuil-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnDomicile.place(x=((centrageAcceuil-btnDomicile.winfo_reqwidth())//2),y=175)
        btnWork.place(x=((centrageAcceuil-btnWork.winfo_reqwidth())//2),y=275)
        #addresseDomicile
        labelTitre[1].place(x=((centrageAcceuil-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.__entryAdresse[0].place(relx=0.5,rely=0.5,anchor="center")
        btnRetour[0].place(x=(largeurCadre-btnRetour[0].winfo_reqwidth()),y=(hauteurCadre-btnRetour[0].winfo_reqheight()))
        btnValider[0].place(x=((centrageAcceuil-btnValider[0].winfo_reqwidth())//2),y=325)
        btnSuppr[0].place(x=((centrageAcceuil-btnSuppr[0].winfo_reqwidth())//2),y=375)
        #addressWork
        labelTitre[2].place(x=((centrageAcceuil-labelTitre[2].winfo_reqwidth())//2),y=0)
        self.__entryAdresse[1].place(relx=0.5,rely=0.5,anchor="center")
        btnRetour[1].place(x=(largeurCadre-btnRetour[1].winfo_reqwidth()),y=(hauteurCadre-btnRetour[1].winfo_reqheight()))
        btnValider[1].place(x=((centrageAcceuil-btnValider[0].winfo_reqwidth())//2),y=325)
        btnSuppr[1].place(x=((centrageAcceuil-btnSuppr[0].winfo_reqwidth())//2),y=375)
     
    def _backAcceuil(self)->bool:
        self.__addresseDomicile.place_forget()
        self.__addresseWork.place_forget()
        self.__acceuilFrame.place(x=0,y=0)
        self.__acceuilFrame.update()
        return  True    
    
    def view(self)->bool:
        self._backAcceuil()
        self.__mainFrame.pack(side="left")
        self._backAcceuil()
        return True
        
    def domicileView(self) ->bool:
        self.__acceuilFrame.place_forget()
        self.__entryAdresse[0].delete(0,"end")
        self.__addresseDomicile.place(x=0,y=0)
        return True
    
    def workView(self) ->bool:
        self.__acceuilFrame.place_forget()
        self.__entryAdresse[1].delete(0,"end")
        self.__addresseWork.place(x=0,y=0)
        return True
    
    def _addAdresse(self,type:str)->bool:
        self._backAcceuil()
        if type == "domicile" :
            adresse = self.__entryAdresse[0].get()
            self.__configFile.EcritureJSON("adresseDomicile",adresse)
            self.__entryAdresse[0].delete(0,"end")
            messagebox.showinfo("Adresse enregistrer","L'adresse de votre domicile a ete enregistrer")
        else :
            if type == "work":
                adresse = self.__entryAdresse[1].get()
                self.__configFile.EcritureJSON("adresseTravail",adresse)
                self.__entryAdresse[1].delete(0,"end")
                messagebox.showinfo("Adresse enregistrer","L'adresse de votre lieu de travail a ete enregistrer")  
        return True 
    
    def _supprAdresse(self,type:str)->bool:
        self._backAcceuil()
        if type == "domicile" :
            self.__configFile.suppressionJson("adresseDomicile")
            self.__entryAdresse[0].delete(0,"end")
            messagebox.showinfo("Adresse supprimer","L'adresse de votre domicile a ete supprimer")
        else :
            if type == "work":
                self.__configFile.suppressionJson("adresseTravail")
                self.__entryAdresse[1].delete(0,"end")
                messagebox.showinfo("Adresse enregistrer","L'adresse de votre lieu de travail a ete supprimer")  
        return True  