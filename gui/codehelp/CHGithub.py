from tkinter import*
import webbrowser as w
from github import Github
import requests
from gui.codehelp.CCHguiBase import CCHguiBase,gestionnaire

class CHGithub(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Github")
        self.__tokenGithub = self._gestionnaire.getUserConf().getTokenGithub()
        self.__listDepo = []

    def _mainframe(self):
        #Frame
        self.__frameWelcome = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__frameSearch = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__frameError = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__frameList = self._arrtk.createFrame(self._screen, width=500, height=500)
        # Label
        labelWelcome = self._arrtk.createLabel(self.__frameWelcome, text="GitHub", ppolice="Arial", ptaille=35)
        labelError = self._arrtk.createLabel(self.__frameError,
                                             text="Aucun token enregistrer\nRendez-vous\ndans les parametre pour\nl'enregistrer",
                                             ppolice="Arial", ptaille=25)
        labelSearch = self._arrtk.createLabel(self.__frameSearch, text="Recherche sur Github", ppolice="Arial",
                                              ptaille=25)
        # BTN
        btnWelcomeDirectory = self._arrtk.createButton(self.__frameWelcome, text="Vos depot", bg=self._btnColor,
                                           fg=self._btnTexteColor, ppolice="Arial", ptaille=25,
                                           command=self.__GUIListDepos)
        btnWelcomeSearch = self._arrtk.createButton(self.__frameWelcome, text="Recherche", bg=self._btnColor,
                                                fg=self._btnTexteColor, ppolice="Arial", ptaille=25,
                                                command=self.__GUISearch)
        btnValidateSearch = self._arrtk.createButton(self.__frameSearch, text="Valider", bg=self._btnColor,
                                             fg=self._btnTexteColor, ppolice="Arial", ptaille=15, command=self.__search)
        btnBackSearch = self._arrtk.createButton(self.__frameSearch, text="Retour", bg=self._btnColor,
                                                 fg=self._btnTexteColor, ppolice="Arial", ptaille=15,command=self.__backMain)
        btnErrorDirectory = self._arrtk.createButton(self.__frameError, text="Quitter", bg=self._btnColor,
                                            fg=self._btnTexteColor, ppolice="Arial", ptaille=15,
                                            command=self.__backMain)
        btnListQuit = self._arrtk.createButton(self.__frameList, text="Quitter", bg=self._btnColor,
                                               fg=self._btnTexteColor, ppolice="Arial", ptaille=15,
                                               width=self.__frameList.winfo_reqwidth(), command=self.__backMain)
        #scrollbar
        self.__scroll = Scrollbar(self.__frameList,orient="vertical")
        #Entry
        self.__entrySearch = self._arrtk.createEntry(self.__frameSearch, ppolice="Arial", ptaille=25, width=400)
        # Listbox
        self.__boxlistDepot = Listbox(self.__frameList, width=500, height=500)
        #Affichage
        self._arrtk.placeTopCenter(labelWelcome)
        self._arrtk.placeLeftCenter(btnWelcomeDirectory)
        self._arrtk.placeRightCenter(btnWelcomeSearch)
        self._arrtk.placeTopCenter(labelSearch)
        self._arrtk.placeCenter(self.__entrySearch)
        self._arrtk.placeBottomRight(btnValidateSearch)
        self._arrtk.placeBottomLeft(btnBackSearch)
        self._arrtk.placeCenter(labelError)
        self._arrtk.placeBottomCenter(btnErrorDirectory)
        self._arrtk.placeBottomCenter(btnListQuit)
        self.__boxlistDepot.place(relx=0, rely=0, relwidth=0.95, relheight=1)
        self.__scroll.place(relx=0.95, rely=0, relwidth=0.05, relheight=1)
        self._arrtk.placeCenter(self.__frameWelcome)

    def search(self,requette:str):
        urllink = requests.get("https://github.com/search?q="+requette)
        urllink = urllink.url
        w.open(urllink)
    
    def __GUISearch(self):
        self.__frameWelcome.place_forget()
        self.__frameSearch.place(relx=0.5,rely=0.5,anchor="center")
    
    def __search(self):
        self.__frameWelcome.place(relx=0.5, rely=0.5, anchor="center")
        self.__frameSearch.place_forget()
        self.search(str(self.__entrySearch.get()))
        self.__entrySearch.delete("0", END)

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
        self._arrtk.placeCenter(self.__frameWelcome)
        
    def __GUIListDepos(self):
        self.__frameWelcome.place_forget()
        if not self.__setListDepos():
            self.__frameError.place(relx=0.5,rely=0.5,anchor="center")
        else :
            self.__frameList.place(relx=0.5,rely=0.5,anchor="center")
            for i in range(0,(len(self.__listDepo)-1)) :
                self.__boxlistDepot.insert(END, self.__listDepo[i])
            self.__scroll.configure(command=self.__boxlistDepot.yview)