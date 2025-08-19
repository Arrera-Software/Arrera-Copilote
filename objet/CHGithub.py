from tkinter import*
import webbrowser as w
from github import Github
from ObjetsNetwork.gestion import*
from librairy.asset_manage import  resource_path

class CHGithub:
    def __init__(self,ConfigNeuron:jsonWork,gestion:gestionNetwork):
        self.__mainColor = ConfigNeuron.lectureJSON("interfaceColor")
        self.__mainTextColor = ConfigNeuron.lectureJSON("interfaceTextColor")
        self.__iconAssistant = resource_path(ConfigNeuron.lectureJSON("iconAssistant"))
        self.__name = ConfigNeuron.lectureJSON("name")
        self.__tokenGithub = gestion.getTokenGithub()
        self.__listDepo = []

    def GUI(self):
        self.__screenGH = Toplevel()
        self.__screenGH.title(self.__name+" : Codehelp Github")
        self.__screenGH.configure(bg=self.__mainColor)
        self.__screenGH.iconphoto(False,PhotoImage(file=self.__iconAssistant))
        self.__screenGH.maxsize(500,500)
        self.__screenGH.minsize(500,500)
        #Frame
        self.__mainFrame = Frame(self.__screenGH,bg=self.__mainColor,width=500,height=500)
        self.__frameSearch = Frame(self.__screenGH,bg=self.__mainColor,width=500,height=500)
        self.__frameError = Frame(self.__screenGH,bg=self.__mainColor,width=500,height=500)
        self.__frameList = Frame(self.__screenGH,bg=self.__mainColor,width=500,height=500)
        #scrollbar
        self.__scroll = Scrollbar(self.__frameList,orient="vertical")
        #widget
        labelAcceuil = Label(self.__mainFrame,text="GitHub",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","25"))
        btnList = Button(self.__mainFrame,text="Vos depot",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","15"),command=self.__GUIListDepos)
        btnRecherche = Button(self.__mainFrame,text="Recherche",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","15"),command=self.__GUISearch)
        self.__entrySeach = Entry(self.__frameSearch,font=("arial","15"),relief=SOLID)
        labelSearch = Label(self.__frameSearch,text="Recherche sur Github",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","25"))
        btnSearch = Button(self.__frameSearch,text="Valider",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","15"),command=self.__search)
        labelError = Label(self.__frameError,text="Aucun token enregistrer\nRendez-vous\ndans les parametre pour\nl'enregistrer",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","25"))
        btnError = Button(self.__frameError,text="Quitter",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","15"),command=self.__backMain)
        btnListQuit = Button(self.__frameList,text="Quitter",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","15"),width=self.__frameList.winfo_reqwidth(),command=self.__backMain)
        self.boxlistDepot = Listbox(self.__frameList,width=500,height=500)
        #Affichage
        labelAcceuil.place(x=((self.__mainFrame.winfo_reqwidth()-labelAcceuil.winfo_reqwidth())//2),y=0)
        btnList.place(x=((self.__mainFrame.winfo_reqwidth()-btnList.winfo_reqwidth())-15),y=((self.__mainFrame.winfo_reqheight()-btnList.winfo_reqheight())//2))
        btnRecherche.place(x=15,y=((self.__mainFrame.winfo_reqheight()-btnRecherche.winfo_reqheight())//2))
        labelSearch.place(x=((self.__frameSearch.winfo_reqwidth()-labelSearch.winfo_reqwidth())//2),y=0)
        self.__entrySeach.place(relx=0.5,rely=0.5,anchor="center")
        btnSearch.place(x=((self.__frameSearch.winfo_reqwidth()-btnSearch.winfo_reqwidth())//2),y=self.__frameSearch.winfo_reqheight()-btnSearch.winfo_reqheight())
        labelError.place(relx=0.5,rely=0.5,anchor="center")
        btnError.place(x=((self.__frameError.winfo_reqwidth()-btnError.winfo_reqwidth())//2),y=((self.__frameError.winfo_reqheight()-btnError.winfo_reqheight())))
        btnListQuit.place(x=((self.__frameList.winfo_reqwidth()-btnListQuit.winfo_reqwidth())//2),y=((self.__frameList.winfo_reqheight()-btnListQuit.winfo_reqheight())))
        self.boxlistDepot.place(relx=0, rely=0, relwidth=0.95, relheight=1)
        self.__scroll.place(relx=0.95, rely=0, relwidth=0.05, relheight=1)
        self.__mainFrame.place(relx=0.5,rely=0.5,anchor="center")

    def search(self,requette:str):
        urllink = requests.get("https://github.com/search?q="+requette)
        urllink = urllink.url
        w.open(urllink)
    
    def __GUISearch(self):
        self.__mainFrame.place_forget()
        self.__frameSearch.place(relx=0.5,rely=0.5,anchor="center")
    
    def __search(self):
        self.__mainFrame.place(relx=0.5,rely=0.5,anchor="center")
        self.__frameSearch.place_forget()
        self.search(str(self.__entrySeach.get()))
        self.__entrySeach.delete("0",END)

    def __setListDepos(self)->bool:
        if self.__tokenGithub :
            access = Github(self.__tokenGithub)
            for repo in access.get_user().get_repos():
                self.__listDepo.append(str(repo.name))
            return True
        else :
            return False
    
    def __backMain(self):
        self.__frameList.place_forget()
        self.__frameError.place_forget()
        self.__frameSearch.place_forget()
        self.__mainFrame.place(relx=0.5,rely=0.5,anchor="center")
        
    def __GUIListDepos(self):
        self.__mainFrame.place_forget()
        if self.__setListDepos() == False :
            self.__frameError.place(relx=0.5,rely=0.5,anchor="center")
        else :
            self.__frameList.place(relx=0.5,rely=0.5,anchor="center")
            for i in range(0,(len(self.__listDepo)-1)) :
                self.boxlistDepot.insert(END,self.__listDepo[i])
            self.__scroll.configure(command=self.boxlistDepot.yview)