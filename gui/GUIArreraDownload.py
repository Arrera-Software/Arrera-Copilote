from librairy.arrera_tk import *
from fnc.fonctionArreraDownload import *
from tkinter.messagebox import showerror,showinfo
import threading as th
from gui.guibase import GuiBase,gestionnaire


class GUIArreraDownload(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Arrera Download")
        # Mise en place de objet
        self.__objetArrera = CArreraDownload()

    def _mainframe(self):
        self._screen.geometry("450x450")
        self._screen.resizable(False,False)
        # Initilisation du theard
        self.__tDownload = th.Thread()
        # Var
        self.__listMode = ["Vidéo simple", "Juste son", "Juste vidéo"]
        self.__varGetMode = StringVar(self._screen)
        # Frame
        # main
        self.__fMain = self._arrtk.createFrame(self._screen, width=450, height=450)
        # Download
        self.__fDownload = self._arrtk.createFrame(self._screen, width=450, height=450)
        # Widget
        # fmain
        labelTitle = self._arrtk.createLabel(self.__fMain, text="Arrera Download",
                                             ppolice="Arial", ptaille=30,
                                             pstyle="bold")

        self.__entryURL = self._arrtk.createEntry(self.__fMain, ppolice="Arial", ptaille=20, width=400)
        btnDownload = self._arrtk.createButton(self.__fMain, text="Telecharger", command=self.__downlaodView,
                                               ppolice="Arial", ptaille=20)
        modeSelection = self._arrtk.createOptionMenu(self.__fMain,
                                                     var=self.__varGetMode,
                                                     value=self.__listMode,
                                                     police="Arial", taille=20)

        # fDownload
        self.__labelDownload = self._arrtk.createLabel(self.__fDownload, text="", ppolice="Arial", ptaille=20)
        # fmain
        self._arrtk.placeTopCenter(labelTitle)
        modeSelection.place(x=10, y=60)
        self._arrtk.placeBottomCenterNoStick(btnDownload)
        self._arrtk.placeCenter(self.__entryURL)
        # fDonwload
        self._arrtk.placeCenter(self.__labelDownload)
        # Mise d'une valeur sur l'option menu
        self.__varGetMode.set(self.__listMode[0])

        self._arrtk.placeCenter(self.__fMain)

    def __backMain(self):
        self._arrtk.placeCenter(self.__fMain)

    def __downlaodView(self):
        url = self.__entryURL.get()
        self.__entryURL.delete(0, END)
        folder = self._gestionnaire.getUserConf().getVideoDownloadFolder()
        if folder == "":
            showerror("Download", "Aucun dossier de telechargement enregistrer")
            return
        else:
            self.__objetArrera.setDownloadFolderDur(folder)

        # Recuperation du mode
        mode = self.__varGetMode.get()

        if mode == self.__listMode[0]:
            self.__objetArrera.setMode(1)
        elif mode == self.__listMode[1]:
            self.__objetArrera.setMode(2)
        elif mode == self.__listMode[2]:
            self.__objetArrera.setMode(3)
        if url == "":
            showerror("Download", "Aucun URL")
            return
        self.__objetArrera.setURL(url)
        self.__tDownload = th.Thread(target=self.__objetArrera.download)

        self.__fMain.place_forget()
        self._arrtk.placeCenter(self.__fDownload)
        self.__labelDownload.configure(text="Telechargement en cours...")
        self.__tDownload.start()
        self._screen.after(500, self.__downloadCheck)

    def __downloadCheck(self):
        if self.__tDownload.is_alive():
            text1 = "Telechargement en cours..."
            text2 = "Telechargement en cours......"
            text3 = "Telechargement en cours........."

            textLabel = self.__labelDownload.cget("text")

            if textLabel == text1:
                self.__labelDownload.configure(text=text2)
            elif textLabel == text2:
                self.__labelDownload.configure(text=text3)
            else:
                self.__labelDownload.configure(text=text1)

            self._screen.after(500, self.__downloadCheck)
        else:
            showinfo("Download", "Telechargement terminer")
            self.__fDownload.place_forget()
            self.__tDownload = th.Thread()
            self._arrtk.placeCenter(self.__fMain)
            self._screen.update()

    def __downloadNewVersion(self):
        wb.open("https://github.com/Arrera-Software/Arrera-VideoDownload/releases")
        self._screen.quit()