from gui.guibase import GuiBase,gestionnaire

class GUIView(GuiBase):
    def __init__(self,gestionnaire:gestionnaire,title):
        super().__init__(gestionnaire,title)
        self._textRead = ""

    def _mainframe(self):
        self._screen.minsize(500, 620)
        self._screen.maxsize(500, 620)

        self._screen.grid_columnconfigure(0, weight=1)
        self._screen.grid_rowconfigure(0, weight=0, minsize=25)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_rowconfigure(2, weight=0, minsize=25)

        # Frame
        topFrame = self._arrtk.createFrame(self._screen)
        labelFrame = self._arrtk.createFrame(self._screen)
        btnFrame = self._arrtk.createFrame(self._screen)

        # Conf frame
        labelFrame.grid_rowconfigure(0, weight=1)
        labelFrame.grid_columnconfigure(0, weight=1)

        # IMG
        imgLogo = self._arrtk.createImage(pathDark=self._gestionnaire.getConfigFile().icon,
                                          pathLight=self._gestionnaire.getConfigFile().icon,
                                          tailleX=50,tailleY=50)
        # Widgets
        logoLabel = self._arrtk.createLabel(topFrame,image=imgLogo)
        self._titleLabel = self._arrtk.createLabel(topFrame, text="", ppolice="Arial",
                                                   ptaille=35, pstyle="bold")

        btnRead = self._arrtk.createButton(btnFrame,text="Lire",
                                           bg=self._btnColor,fg=self._btnTexteColor,
                                           ppolice="Arial",ptaille=20,pstyle="bold")
        btnQuit = self._arrtk.createButton(btnFrame,text="Quitter",
                                           bg=self._btnColor,fg=self._btnTexteColor,
                                           ppolice="Arial",ptaille=20,pstyle="bold",
                                           command=self._screen.destroy)
        wTextBox,self._textBox = self._arrtk.createTextBoxScrolled(labelFrame)
        # Affichage
        logoLabel.pack(side="left", anchor="center", padx=(6, 10), pady=6)
        self._titleLabel.pack(side="left", anchor="center", pady=6)

        btnRead.pack(side="left", anchor="center", padx=(6, 10), pady=6)
        btnQuit.pack(side="right", anchor="center", pady=6)

        wTextBox.grid(row=0, column=0, sticky="nsew")

        topFrame.grid(row=0, column=0, sticky="nsew")
        labelFrame.grid(row=1, column=0, sticky="nsew")
        btnFrame.grid(row=2, column=0, sticky="nsew")