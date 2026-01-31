from gui.codehelp.CCHguiBase import CCHguiBase,gestionnaire
from tkinter import colorchooser

class CCHcolorSelector(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Selecteur de couleur")

    def _mainframe(self):
        self._screen.maxsize(800, 500)
        self._screen.minsize(800, 500)
        self._screen.resizable(False, False)
        #fonction
        #cadre
        cadreNoir = self._arrtk.createFrame(self._screen, bg="black", width=325, height=325)
        self.__cadreColor = self._arrtk.createFrame(cadreNoir,bg="#ffffff",width=310,height=310)
        #label
        self.__labelIndicationCode = self._arrtk.createLabel(self._screen, text="Code HTML : #ffffff \nCode RGB : (255,255,255)",
                                                             ppolice="Arial",ptaille=25, justify="left")
        #declaration des bouton
        buttonSelection = self._arrtk.createButton(self._screen, text="Selectionner la couleur",
                                                   bg=self._btnColor, fg=self._btnTexteColor,
                                                   ppolice="Arial",ptaille=15, command=self.__selecteur)
        self.__buttonCopiHTLM = self._arrtk.createButton(self._screen, text="Copier le code HTML",
                                                         bg=self._btnColor, fg=self._btnTexteColor,
                                                         ppolice="Arial",ptaille=15)
        self.__buttonCopiRGB = self._arrtk.createButton(self._screen, text="Copier le code RGB",
                                                        bg=self._btnColor, fg=self._btnTexteColor,
                                                        ppolice="Arial",ptaille=15)
        #affichage
        self._arrtk.placeCenter(self.__cadreColor)
        cadreNoir.pack(side="right")
        self.__labelIndicationCode.place(x=15,y=15)
        buttonSelection.place(x=15,y=135)
        self.__buttonCopiHTLM.place(x=15,y=235)
        self.__buttonCopiRGB.place(x=15,y=335)
        
    def __selecteur(self):
        self.__color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur")
        self.__colorHTLM = str(self.__color[1])
        self.__colorRGB = str(self.__color[0])
        self.__cadreColor.configure(fg_color=self.__colorHTLM)
        self.__buttonCopiHTLM.configure(command=self.__copieHTLM)
        self.__buttonCopiRGB.configure(command=self.__copieRGB)
        self.__labelIndicationCode.configure(text="Code HTML : "+self.__colorHTLM+"\nCode RGB : "+self.__colorRGB)
    
    def __copieHTLM(self):
        self._screen.clipboard_clear()
        self._screen.clipboard_append(self.__colorHTLM)
    
    def __copieRGB(self):
        self._screen.clipboard_clear()
        self._screen.clipboard_append(self.__colorRGB)