import json

class jsonWork:
    def __init__(self, file):
        self.fichier = file

    def getJSONDict(self):
        """
        Retourne un dictionnaire un json
        :return : contenu du fichier json complet
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                dict = json.load(openfile)
            return dict
        except:
            return None

    def getContentJsonFlag(self, flag:str):
        """
        Lire un flag du fichier json
        :param flag: Flag qui contient la valeur que vous voulez lire
        :return: Contenu du flag
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                dict = json.load(openfile)[flag]
            return str(dict)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier JSON : {e}")
            return None

    def getContentJsonMultiFlag(self, flag1, flag2):
        """
         Lire un flag qui se trouve un un dictionnaire stoker dans le JSON
        :param flag1: Flag ou se trouve le dictionnaire secondaie
        :param flag2: Flag ou se trouve la valeur
        :return: Valeur contenu du flag
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                dict = json.load(openfile)[flag1][flag2]
            return str(dict)
        except:
            return None

    def getFlagListJson(self, flag):
        """
         Lire un flag qui contient une liste
        :param flag: Flag ou se trouve la liste que vous voulez lire
        :return: retourne La liste
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                liste = json.load(openfile)[flag]
            return list(liste)
        except:
            return None

    def getFlagDictJson(self, flag):
        """
        Lire un flag qui contient un dictionnaire
        :param flag: Flag ou se trouve le dictionnaire que vous voulez lire
        :return: Retourne le dictionnaire
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                dictionnaire = json.load(openfile)[flag]
            return dict(dictionnaire)
        except:
            return None

    def setValeurJson(self, flag, valeur):  # Permet d'ecrire une nouvelle valeur a flag definie
        """
        Ecrire une valeur dans un flag choisi
        :param flag: Flag ou vous voulez ecrire votre valeur
        :param valeur: Valeur que vous voulez ecrire
        """
        try :
            openfile = open(self.fichier, 'r', encoding='utf-8')
            dict = json.load(openfile)
            openfile.close()
            writeFile = open(self.fichier, 'w', encoding='utf-8')
            dict[flag] = valeur
            json.dump(dict, writeFile, indent=2)
            return True
        except Exception as e:
            # print(f"Erreur lors de l'écriture dans le fichier JSON : {e}")
            return False

    def setListJson(self, flag, valeur: list):
        """
        Ecrire une liste dans le flag choisie
        :param flag: Flag ou vous voulez ecrire votre liste
        :param valeur: liste que vous voulez ecrire
        """
        try :
            # Chargez le fichier JSON
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                data = json.load(openfile)
            # Vérifiez si le champ (flag) existe et est une liste
            if flag in data and isinstance(data[flag], list):
                # Ajoutez la nouvelle valeur à la liste
                data[flag].append(valeur)
                # Écrivez le fichier JSON mis à jour
                with open(self.fichier, 'w', encoding='utf-8') as writeFile:
                    json.dump(data, writeFile, indent=2)

            return True
        except Exception as e:
            # print(f"Erreur lors de l'écriture dans le fichier JSON : {e}")
            return False

    def setDictJson(self, flag, cle, valeur):
        """
        Ecrire un dictionnaire dans le flag choisie
        :param flag: Flag ou vous voulez ecrire votre dictionnaire
        :param cle: Cles de votre dictionnaire
        :param valeur: Valeur que vous voulez erire dans dictionnaire a cette cles
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
                data = json.load(fichier_json)

            if flag in data and isinstance(data[flag], dict):
                data[flag][cle] = valeur  # Met à jour le dictionnaire
                with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                    json.dump(data, fichier_modifie, indent=2)
            return True
        except Exception as e:
            # print(f"Erreur lors de l'écriture dans le fichier JSON : {e}")
            return False

    def unsetDictJson(self, flag, cle):
        """
         Supprimer un cles choisi dans dictionnaire stoker dans un JSON
        :param flag: Flag ou se trouve le dictionnaire
        :param cle: Cle du dictionnaire que vous voulez supprimer
        """
        try:
            with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
                data = json.load(fichier_json)

            if flag in data and isinstance(data[flag], dict):
                if cle in data[flag]:
                    del data[flag][cle]  # Supprime la clé spécifiée du dictionnaire
                    with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                        json.dump(data, fichier_modifie, indent=2)
            return True
        except Exception as e:
            # print(f"Erreur lors de la suppression de la clé dans le fichier JSON : {e}")
            return False

    def unsetValeurJson(self, flag: str):
        """
        Supprimer la valeur du flag selectionner
        :param flag: Flag ou vous voulez supprimer la valeur
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
                data = json.load(fichier_json)
            if flag in data:
                data[flag] = ""  # Supprime le champ spécifié
                with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                    json.dump(data, fichier_modifie, indent=2)
            return True
        except Exception as e:
            # print(f"Erreur lors de la suppression de la valeur dans le fichier JSON : {e}")
            return False

    def unsetListJson(self, flag, valeur):
        """
        Supprimer un valeur dans un liste stoker dans un JSON
        :param flag: Flag ou se touve la liste
        :param valeur: valeur de la liste que vous voulez supprimer
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
                data = json.load(fichier_json)
            if flag in data and isinstance(data[flag], list):
                liste = data[flag]

                if valeur in liste:
                    liste.remove(valeur)  # Supprime la valeur spécifiée de la liste
                    with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                        json.dump(data, fichier_modifie, indent=2)
            return True
        except Exception as e:
            # print(f"Erreur lors de la suppression de la valeur dans le fichier JSON : {e}")
            return False

    def unsetDictReorg(self, flag):
        """
        Supprimer un flag du fichier JSON tout en reoganisant le fichier
        :param flag: Flag que vous voulez supprimer
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as openfile:
                dict = json.load(openfile)
                del dict[flag]
                newDict = {}
                newKey = 0
                for cle in sorted(dict.keys(), key=lambda x: int(x)):
                    newDict[str(newKey)] = dict[cle]
                    newKey += 1
                writeFile = open(self.fichier, 'w', encoding='utf-8')
                json.dump(newDict, writeFile, indent=2)
                writeFile.close()
            return True
        except Exception as e:
            # print(f"Erreur lors de la suppression du flag dans le fichier JSON : {e}")
            return False

    def unsetDictByFlag(self, flag, name):
        """
         Supprimer un valeur avec sa cles dans un dictionnaire stoker dans le JSON juste avec la valeur
        :param flag: Flag du dictionnaire
        :param name: Valeur de la cles que vous voulez supprimer
        """
        try :
            with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
                data = json.load(fichier_json)

            for key, value in data.items():
                if value.get(flag) == name:
                    self.unsetDictReorg(key)
            return True
        except Exception as e:
            # print(f"Erreur lors de la suppression de la valeur dans le fichier JSON : {e}")
            return False

    def setDictOnJson(self, dict: dict):
        """
        ECrire un dictionnaire python dans le fichier json
        :param dict: Dictionnaire que vous voulez ecrire dans votre fichier json
        """
        try :
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(dict, fichier_modifie, indent=2)
            return True
        except Exception as e:
            # print(f"Erreur lors de l'écriture du dictionnaire dans le fichier JSON : {e}")
            return False