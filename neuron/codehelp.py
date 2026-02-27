from neuron.CNeuronBase import neuronBase,gestionnaire


class neuroneCodehelp(neuronBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fncCodeHelp = self._gestionnaire.getGestFNC().getFNCCodeHelp()

    def neurone(self,requette:str):
        self._valeurOut = 0
        self._listSortie = ["",""]
        if not self._keyword.checkUtils(requette,"question-fonction"):
            if self._keyword.checkSearch(requette,"search"):
                if self._keyword.checkCodeHelp(requette,"devdoc"):
                    for word in self._keyword.getListKeyword("codehelp","devdoc"):
                        requette = requette.replace(word,"")

                    for word in self._keyword.getListKeyword("search","search"):
                        requette = requette.replace(word,"")

                    requette = requette.strip()

                    if self.__fncCodeHelp.searchDocInDevDoc(requette):
                        self._listSortie = [self._language.getPhraseCodehelp("6"),
                                            ""]
                    else :
                        self._listSortie = [self._language.getPhraseCodehelp("7"),
                                            ""]

                    self._valeurOut = 1
                elif self._keyword.checkCodeHelp(requette,"microsoft"):
                    for word in self._keyword.getListKeyword("codehelp","microsoft"):
                        requette = requette.replace(word,"")

                    for word in self._keyword.getListKeyword("search","search"):
                        requette = requette.replace(word,"")

                    requette = requette.strip()

                    if self.__fncCodeHelp.searchDocInMicrosoft(requette):
                        self._listSortie = [self._language.getPhraseCodehelp("8"),
                                            ""]
                    else :
                        self._listSortie = [self._language.getPhraseCodehelp("9"),
                                            ""]

                    self._valeurOut = 1
                elif self._keyword.checkCodeHelp(requette,"python"):
                    for word in self._keyword.getListKeyword("codehelp","python"):
                        requette = requette.replace(word,"")

                    for word in self._keyword.getListKeyword("search","search"):
                        requette = requette.replace(word,"")

                    requette = requette.strip()

                    if self.__fncCodeHelp.searchDocInPython(requette):
                        self._listSortie = [self._language.getPhraseCodehelp("10"),
                                            ""]
                    else :
                        self._listSortie = [self._language.getPhraseCodehelp("11"),
                                            ""]

                    self._valeurOut = 1
                elif self._keyword.checkCodeHelp(requette,"github"):
                    for word in self._keyword.getListKeyword("codehelp","github"):
                        requette = requette.replace(word,"")

                    for word in self._keyword.getListKeyword("search","search"):
                        requette = requette.replace(word,"")

                    requette = requette.strip()

                    if self.__fncCodeHelp.searchGithub(requette):
                        self._listSortie = [self._language.getPhraseCodehelp("12"),
                                            ""]
                    else :
                        self._listSortie = [self._language.getPhraseCodehelp("13"),
                                            ""]

                    self._valeurOut = 1
            elif self._keyword.checkOpen(requette,"open"):
                if self._keyword.checkCodeHelp(requette,"orga-var"):
                    self.__fncCodeHelp.setGUICodeHelp("GUIOrgaVar")
                    self._listSortie = [self._language.getPhraseCodehelp("1"),
                                        ""]
                    self._valeurOut = 23
                elif self._keyword.checkCodeHelp(requette,"color-select"):
                    self.__fncCodeHelp.setGUICodeHelp("GUIColorSelector")
                    self._listSortie = [self._language.getPhraseCodehelp("2"),
                                        ""]
                    self._valeurOut = 23
                elif self._keyword.checkCodeHelp(requette,"github") and  not self._keyword.checkCodeHelp(requette,"gestion"):

                    self.__fncCodeHelp.openSiteGithub()
                    self._listSortie = [self._language.getPhraseCodehelp("3"),
                                        ""]
                    self._valeurOut = 5
                elif self._keyword.checkCodeHelp(requette,"gestion") and self._keyword.checkCodeHelp(requette,"github"):
                    self.__fncCodeHelp.setGUICodeHelp("GUIGithubGestion")
                    self._listSortie = [self._language.getPhraseCodehelp("4"),
                                        ""]
                    self._valeurOut = 23
                elif self._keyword.checkCodeHelp(requette,"librairie"):
                    self.__fncCodeHelp.setGUICodeHelp("GUILibrairy")
                    self._listSortie = [self._language.getPhraseCodehelp("5"),
                                        ""]
                    self._valeurOut = 23