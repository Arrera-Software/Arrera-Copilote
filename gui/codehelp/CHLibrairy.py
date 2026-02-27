from tkinter import StringVar

from gui.codehelp.CCHguiBase import CCHguiBase,gestionnaire
import webbrowser as w
import requests


class CHLibrairy(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Librairie")
        self.__lienLibrairy = "https://github.com/Arrera-Software/Arrera-librairy"
        self.__lienReadme =  "https://github.com/Arrera-Software/Arrera-librairy/blob/main/README.md"
        self.__lienObjetPython = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/python"
        self.__lienObjetCPP = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/C%2B%2B"
        self.__varName = None
        self.__listLib = []
        self.__dictURLName = {}

    def __testConnection(self):
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            try:
                response = requests.get(
                    "https://raw.githubusercontent.com/Arrera-Librairy/index-codehelp/refs/heads/main/index.json")
                response.raise_for_status()
                contenuJson = response.json()
                nb = len(contenuJson) + 1

                for i in range(1,nb):
                    self.__listLib.append(contenuJson[str(i)]['name'])
                    self.__dictURLName[contenuJson[str(i)]['name']] = contenuJson[str(i)]['url']

                return True

            except requests.exceptions.RequestException as e:
                print(f"Erreur lors de la récupération de l'index : {e}")
                return False
        else:
            print("Pas de connexion internet")
            return False

    def _mainframe(self):
        # Var
        self.__varName = StringVar(self._screen)
        # Frame
        self.__welcomeFrame = self._arrtk.createFrame(self._screen,width=700, height=500)
        self.__errorFrame = self._arrtk.createFrame(self._screen,width=700, height=500)

        # Widget
        # welcome Frame
        labelAcceuilTop = self._arrtk.createLabel(self.__welcomeFrame,text="Arrera librairie"
                                                  ,ppolice="arial",ptaille=25)
        self.__optionName = None
        btnView = self._arrtk.createButton(self.__welcomeFrame, text="Consulter", bg=self._btnColor,
                                           fg=self._btnTexteColor,ppolice="Arial",ptaille=25)
        # Error Frame
        labelError = self._arrtk.createLabel(self.__errorFrame,text="Impossible de récuper l'index",
                                             ppolice="arial",ptaille=25)

        # Affichage
        self._arrtk.placeTopCenter(labelAcceuilTop)
        self._arrtk.placeBottomCenter(btnView)

        self._arrtk.placeCenter(labelError)

        # Teste de la connection
        if self.__testConnection():
            # Option
            self.__optionName = self._arrtk.createOptionMenu(self.__welcomeFrame, var=self.__varName,value=self.__listLib)
            self._arrtk.placeCenter(self.__optionName)
            # Bouton
            btnView.configure(command= lambda : w.open(self.__dictURLName[self.__varName.get()]))
            # Affichage Frame
            self._arrtk.placeCenter(self.__welcomeFrame)
        else :
            self._arrtk.placeCenter(self.__errorFrame)