from tkinter import StringVar

from gui.guibase import GuiBase,gestionnaire

class GuiTraducteur(GuiBase):
    def __init__(self, gestionnaire: gestionnaire):
        super().__init__(gestionnaire, "Traducteur")
        self._fncTrad = self._gestionnaire.getGestFNC().getFNCTraduction()
        self.__listLang = self._fncTrad.getLang()
        self.__dictLang = self._fncTrad.getLangAndLangCode()

    def _mainframe(self):
        # Variables
        self.__varLangIn = StringVar(self._screen)
        self.__varLangOut = StringVar(self._screen)
        # Frame
        frameTop = self._arrtk.createFrame(self._screen)
        frameTrad = self._arrtk.createFrame(self._screen)
        # Config Fenetre
        self._screen.grid_columnconfigure(0, weight=1)
        self._screen.grid_rowconfigure(0, weight=0, minsize=60)  # hauteur fixe/mini pour le bandeau haut
        self._screen.grid_rowconfigure(1, weight=1)
        # config frame
        frameTrad.grid_columnconfigure(0, weight=1, uniform="halves")
        frameTrad.grid_columnconfigure(1, weight=1, uniform="halves")
        frameTrad.grid_columnconfigure(2, weight=1, uniform="halves")
        frameTrad.grid_columnconfigure(3, weight=1, uniform="halves")
        frameTrad.grid_rowconfigure(0, weight=0)
        frameTrad.grid_rowconfigure(1, weight=1)
        frameTrad.grid_rowconfigure(2, weight=0)
        # Widgets
        labelTitle = self._arrtk.createLabel(frameTop,text=self._gestionnaire.getName()+" : Traducteur",
                                             ppolice="Arial",ptaille=30,pstyle="bold")
        self.__textBoxIn = self._arrtk.createTextBox(frameTrad,enableKeyboard=True,
                                                     ppolice="Arial",ptaille=25)
        self.__textBoxOut = self._arrtk.createTextBox(frameTrad,enableKeyboard=True,
                                                      ppolice="Arial",ptaille=25)
        btnTrad = self._arrtk.createButton(frameTrad,text="Traduire",ppolice="Arial",
                                           ptaille=25,pstyle="bold",bg=self._btnColor,
                                           fg=self._btnTexteColor,command=self.__translate)
        labelIndicationIn = self._arrtk.createLabel(frameTrad,text="Langue d'entrée :",
                                                    ppolice="Arial",ptaille=20,pstyle="bold")
        labelIndicationOut = self._arrtk.createLabel(frameTrad,text="Langue de sortie :",
                                                     ppolice="Arial",ptaille=20,pstyle="bold")
        menuLangIn = self._arrtk.createOptionMenu(frameTrad,var=self.__varLangIn,value=self.__listLang
                                                  ,taille=20,police="Arial")
        menuLangOut = self._arrtk.createOptionMenu(frameTrad,var=self.__varLangOut,value=self.__listLang
                                                        ,taille=20,police="Arial")

        # Placement
        frameTop.grid(row=0, column=0, sticky="ew")
        frameTrad.grid(row=1, column=0, sticky="nsew")

        labelTitle.pack(side="left", anchor="nw", padx=10, pady=5)

        labelIndicationIn.grid(row=0, column=0, sticky="w", padx=(10,5), pady=(10,5))
        menuLangIn.grid(row=0, column=1, sticky="w", padx=(0,10), pady=(10,5))

        labelIndicationOut.grid(row=0, column=2, sticky="e", padx=(10,5), pady=(10,5))
        menuLangOut.grid(row=0, column=3, sticky="e", padx=(0,10), pady=(10,5))

        self.__textBoxIn.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=(10,5), pady=(0,10))
        self.__textBoxOut.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=(5,10), pady=(0,10))

        btnTrad.grid(row=2, column=0, columnspan=4, sticky="ew", padx=10, pady=(0,10))

        self.__clear()

    def __clear(self):
        self.__textBoxIn.delete("1.0","end")
        self.__textBoxOut.delete("1.0","end")
        self.__varLangIn.set("Langue d'entrée")
        self.__varLangOut.set("Langue de sortie")

    def __translate(self):
        langIn = self.__varLangIn.get()
        langOut = self.__varLangOut.get()
        texte = self.__textBoxIn.get("1.0","end").strip()
        self.__textBoxIn.delete("1.0","end")

        if langIn == "Langue d'entrée":
            return

        if langOut == "Langue de sortie":
            return

        if langIn == langOut:
            return

        if not texte:
            return

        codeIn = self.__dictLang.get(langIn)
        codeOut = self.__dictLang.get(langOut)

        if self._fncTrad.setTranlator(codeOut,codeIn):
            traduction = self._fncTrad.tranlate(texte)
            if traduction:
                self.__textBoxOut.delete("1.0","end")
                self.__textBoxOut.insert("1.0",traduction)