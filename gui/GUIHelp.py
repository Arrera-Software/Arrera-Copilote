from gui.GUIView import GUIView,gestionnaire

class GUIHelp(GUIView):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Aide")

    def activeHelp(self, texte:str):
        self.active()
        self._textBox.configure(state="normal")
        self._textBox.delete(1.0, "end")
        self._textBox.insert("end", texte)
        self._textBox.configure(state="disabled", font=("Arial", 20, "normal"))
        self._titleLabel.configure(text="Aide")
        self._textRead = texte