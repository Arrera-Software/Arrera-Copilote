from ObjetsNetwork.historique import *

class formule:
    def __init__(self, gestionnaireNeuron: gestionNetwork, fncHist: CHistorique):
        self.__fncHist = fncHist
        self.__calanguage = gestionnaireNeuron.getLanguageObjet()

    def nocomprehension(self):
        return self.__calanguage.getNoComprehension()

    def bootNoHist(self, hour):
        nbrand = random.randrange(0, 1)
        if hour >= 0 and hour < 3:
            formule = self.__calanguage.getPhraseBootNormale("1")
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                formule = self.__calanguage.getPhraseBootNormale("2")
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    formule = self.__calanguage.getPhraseBootNormale("3")
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        formule = self.__calanguage.getPhraseBootNormale("4")
                        return formule[nbrand]
                    else:
                        if hour >= 13 and hour <= 14:
                            formule = self.__calanguage.getPhraseBootNormale("5")
                            return formule[nbrand]
                        else:
                            if hour >= 15 and hour <= 18:
                                formule = self.__calanguage.getPhraseBootNormale("6")
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    formule = self.__calanguage.getPhraseBootNormale("7")
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        formule = self.__calanguage.getPhraseBootNormale("8")
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            formule = self.__calanguage.getPhraseBootNormale("9")
                                            return formule[nbrand]
                                        else:
                                            formule = self.__calanguage.getPhraseBootNormale("10")
                                            return formule

    def aurevoir(self, hour):
        nbrand = random.randrange(0, 1)
        if hour >= 0 and hour < 3:
            formule = self.__calanguage.getPhraseAurevoir("1")
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                formule = self.__calanguage.getPhraseAurevoir("2")
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    formule = self.__calanguage.getPhraseAurevoir("3")
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        formule = self.__calanguage.getPhraseAurevoir("4")
                        return formule[nbrand]
                    else:
                        if hour >= 13 and hour <= 16:
                            formule = self.__calanguage.getPhraseAurevoir("5")
                            return formule[nbrand]
                        else:
                            if hour >= 16 and hour <= 18:
                                formule = self.__calanguage.getPhraseAurevoir("6")
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    formule = self.__calanguage.getPhraseAurevoir("7")
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        formule = self.__calanguage.getPhraseAurevoir("8")
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            formule = self.__calanguage.getPhraseAurevoir("9")
                                            return formule[nbrand]
                                        else:
                                            formule = self.__calanguage.getPhraseAurevoir("10")
                                            return formule[nbrand]

    def bootWithHist(self, hour):

        sortie = self.__fncHist.verfiHist()
        if (sortie == True):
            self.__fncHist.startHistAction()

            if hour >= 0 and hour < 3:
                formule = self.__calanguage.getPhraseBootHist("1")
                return formule
            else:
                if hour >= 3 and hour <= 6:
                    formule = self.__calanguage.getPhraseBootHist("2")
                    return formule
                else:
                    if hour >= 6 and hour <= 10:
                        formule = self.__calanguage.getPhraseBootHist("3")
                        return formule
                    else:
                        if hour >= 10 and hour <= 12:
                            formule = self.__calanguage.getPhraseBootHist("4")
                            return formule
                        else:
                            if hour >= 13 and hour <= 14:
                                formule = self.__calanguage.getPhraseBootHist("5")
                                return formule
                            else:
                                if hour >= 15 and hour <= 18:
                                    formule = self.__calanguage.getPhraseBootHist("6")
                                    return formule
                                else:
                                    if hour >= 18 and hour <= 20:
                                        formule = self.__calanguage.getPhraseBootHist("7")
                                        return formule
                                    else:
                                        if hour >= 20 and hour <= 23:
                                            formule = self.__calanguage.getPhraseBootHist("8")
                                            return formule
                                        else:
                                            if hour >= 0 and hour < 3:
                                                formule = self.__calanguage.getPhraseBootHist("9")
                                                return formule
                                            else:
                                                formule = self.__calanguage.getPhraseBootHist("10")
                                                return formule

        else :
            return self.bootNoHist(hour)