from tkinter import END
import pyperclip
from tkinter.scrolledtext import*
from gui.guibase import GuiBase,gestionnaire
from tkinter import WORD
from tkinter.messagebox import showinfo

class GUIOrthographe(GuiBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Correcteur de texte")
        self.__corrector = self._gestionnaire.getGestFNC().getFNCOrthographe()
        self.__originalText = ""

    def _mainframe(self):
        # Parametrage de la fenetre
        self._screen.rowconfigure(0, weight=1)
        self._screen.columnconfigure(0, weight=1)
        # Frame
        self.__frameErreur =  self._arrtk.createFrame(self._screen)
        self.__frameCorrect =  self._arrtk.createFrame(self._screen)
        self.__frameOut =  self._arrtk.createFrame(self._screen)
        # Widget
        # Label
        labelTitle = self._arrtk.createLabel(self.__frameCorrect,text="Correcteur d'orthographe",
                                             ptaille=20,ppolice="Arial",pstyle="bold")
        labelTitleOut = self._arrtk.createLabel(self.__frameOut,text="Texte corrigé",
                                                ptaille=20,ppolice="Arial",pstyle="bold")
        self.__labelOutCorrect = self._arrtk.createLabel(self.__frameOut,justify="left",
                                                       ptaille=20,ppolice="Arial",pstyle="bold")
        self.__labelOutViewCorrect = self._arrtk.createLabel(self.__frameOut,justify="left",
                                                             ptaille=20,ppolice="Arial",pstyle="bold")
        # ScrolledText
        self.__zoneSortie = ScrolledText(self.__frameCorrect, wrap=WORD, width=80, height=15)
        # Bouton
        self.__btnCorrect = self._arrtk.createButton(self.__frameCorrect,text="",
                                                     ptaille=20,ppolice="Arial",pstyle="bold"
                                                     ,bg=self._btnColor,fg=self._btnTexteColor)
        btnCopyOut = self._arrtk.createButton(self.__frameOut,text="Copier le texte",
                                              ptaille=20,ppolice="Arial",pstyle="bold"
                                              ,bg=self._btnColor,fg=self._btnTexteColor,
                                              command=self.__copyText)

        # Parametrage des grid
        # Frame Correct
        self.__frameCorrect.rowconfigure(0, weight=0)
        self.__frameCorrect.rowconfigure(1, weight=1)
        self.__frameCorrect.rowconfigure(2, weight=0)
        self.__frameCorrect.columnconfigure(0, weight=1)
        self.__frameCorrect.columnconfigure(1, weight=1)
        self.__frameCorrect.columnconfigure(2, weight=1)

        self.__frameOut.grid_columnconfigure(0, weight=1)
        self.__frameOut.grid_columnconfigure(1, weight=1)
        self.__frameOut.grid_columnconfigure(2, weight=1)
        self.__frameOut.grid_rowconfigure(0, weight=1)
        self.__frameOut.grid_rowconfigure(1, weight=1)
        self.__frameOut.grid_rowconfigure(2, weight=1)

        # Placement
        # Frame
        self.__frameCorrect.grid(row=0, column=0, sticky="nsew")
        # Widget
        labelTitle.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))
        self.__zoneSortie.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
        self.__btnCorrect.grid(row=2, column=1, pady=(10, 0))

        labelTitleOut.grid(row=0, column=1)
        self.__labelOutCorrect.grid(row=1, column=0,sticky="nsew")
        self.__labelOutViewCorrect.grid(row=1, column=2,sticky="nsew")
        btnCopyOut.grid(row=2, column=1)

    def setTexte(self,texte:str):
        self.__zoneSortie.delete(1.0,END)
        self.__zoneSortie.insert(END,texte)
        self.__btnCorrect.configure(text="Corriger",command=self.__checkTexte)

    def __checkTexte(self):
        text = self.__zoneSortie.get(1.0, END)
        self.__originalText = text
        if self.__corrector.check(text) and self.__corrector.correctionText():
            self.__labelOutCorrect.configure(text="Mots incorrects:\n" + "\n".join(map(str, self.__corrector.getMotsIncorrects())))
            self.__textCorrected = self.__corrector.getCorrections()
            self.__labelOutViewCorrect.configure(text=self.__textCorrected,wraplength=100)
            self.__frameCorrect.grid_forget()
            self.__frameOut.grid(row=0, column=0, sticky="nsew")
        else :
            self.__frameCorrect.grid_forget()
            self.__frameErreur.grid(row=0, column=0, sticky="nsew")

    def __copyText(self):
        pyperclip.copy(self.__textCorrected)
        self._screen.destroy()
        showinfo("Info","Texte corriger copier")