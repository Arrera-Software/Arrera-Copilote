from neuron.CNeuronBase import neuronBase,gestionnaire

class neuroneSearch(neuronBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fncSearch = self._gestFNC.getFNCSearch()

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if not self._keyword.checkUtils(requette,"question-fonction"):
            if self._keyword.checkSearch(requette,"bigsearch"):
                search = requette.replace("bigsearch","").replace("grand recherche","").strip()
                state = self.__fncSearch.bigRecherche(search)
                if state:
                    self._listSortie = [self._language.getPhraseSearch("1"), ""]
                else :
                    self._listSortie = [self._language.getPhraseSearch("3"), ""]
                self._valeurOut = 1
            elif self._keyword.checkSearch(requette,"search"):
                search = requette.replace("recherche","").replace("search","").strip()
                state = self.__fncSearch.search(search)
                if state:
                    self._listSortie = [self._language.getPhraseSearch("4"), ""]
                else :
                    self._listSortie = [self._language.getPhraseSearch("2"), ""]
                self._valeurOut = 1