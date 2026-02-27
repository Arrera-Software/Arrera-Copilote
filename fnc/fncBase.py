from gestionnaire.gestion import gestionnaire

class fncBase:
    def __init__(self, gestionnaire:gestionnaire):
        self._gestionnaire = gestionnaire
        self._gestSocket = self._gestionnaire.getSocketObjet()
        self._gestLang = self._gestionnaire.getLanguageObjet()
        # Librairy
        self._dectOS = self._gestionnaire.getOSObjet()
