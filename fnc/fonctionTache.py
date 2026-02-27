from fnc.fncBase import fncBase, gestionnaire
import json
from librairy.arrera_date import*

class fncArreraTache(fncBase) :
    def __init__(self,gestionnaire:gestionnaire, fncDate:CArreraDate, taskFile:str):
        super().__init__(gestionnaire)
        self.__taskFile = taskFile
        self.__objDate = fncDate
        self.__content = {}

    def __readTaskFile(self):
        try:
            with open(self.__taskFile, 'r', encoding='utf-8') as jsonFile:
                self.__content = json.load(jsonFile)
                return True
        except Exception as e:
            return False

    def addTask(self, name: str, date: datetime = None, description: str = None):
        # Vérifie le nom
        if not name:
            return False

        self.__readTaskFile()

        # Vérifie si la tâche existe déjà
        if name in self.__content:
            return False

        baseDict = {
            "description": description if description else "none",
            "date": date.isoformat() if date else "none",
            "fini": False  # Booléen, pas une chaîne !
        }

        self.__content[name] = baseDict

        # On sauvegarde le fichier
        with open(self.__taskFile, 'w', encoding='utf-8') as jsonFile:
            json.dump(self.__content, jsonFile, ensure_ascii=False, indent=4)

        return True

    def delTask(self, name:str):
        if not name :
            return False

        self.__readTaskFile()

        if name in self.__content:
            del self.__content[name]
            with open(self.__taskFile, 'w', encoding='utf-8') as jsonFile:
                json.dump(self.__content, jsonFile, ensure_ascii=False, indent=4)

            return True
        else :
            return False


    def finishTask(self, name:str):
        if not name:
            return False
        else :
            self.__readTaskFile()

            if name in self.__content:
                self.__content[name]["fini"] = True
                with open(self.__taskFile, 'w', encoding='utf-8') as jsonFile:
                    json.dump(self.__content, jsonFile, ensure_ascii=False, indent=4)
                return True
            else :
                return False

    def unfinishTask(self, name:str):
        if not name:
            return False
        else :
            self.__readTaskFile()

            if name in self.__content:
                self.__content[name]["fini"] = False
                with open(self.__taskFile, 'w', encoding='utf-8') as jsonFile:
                    json.dump(self.__content, jsonFile, ensure_ascii=False, indent=4)
                return True
            else :
                return False

    def getNbTaskNoFinish(self):
        if self.getNoFinishTask() is not None:
            return len(self.getNoFinishTask())
        else :
            return 0

    def getNoFinishTask(self):
        if self.__readTaskFile() :
            listTask = list(self.__content.keys())
            outList = []
            for i in listTask:
                if not self.__content[i]["fini"]:
                    outList.append(i)
            return outList
        else :
            return None

    def getNbTaskFinish(self):
        if self.getFinishTask() is not None:
            return len(self.getFinishTask())
        else :
            return 0

    def getFinishTask(self):
        if self.__readTaskFile() :
            listTask = list(self.__content.keys())
            outList = []
            for i in listTask:
                if self.__content[i]["fini"]:
                    outList.append(i)
            return list(outList)
        else :
            return None

    def getAllTask(self):
        if self.__readTaskFile() :
            return list(self.__content.keys())
        else :
            return None

    def getNbAllTask(self):
        if self.getAllTask() is not None:
            return len(self.getAllTask())
        else :
            return 0

    def checkDateTask(self,name:str):
        self.__objDate.rafraichisement()
        today = f"{self.__objDate.annes()}-{self.__objDate.nbMois()}-{self.__objDate.jour()}"
        self.__readTaskFile()
        if name in self.__content and not self.__content[name]["fini"]:
            task_date = self.__content[name]["date"]
            if task_date == "none":
                return False
            elif task_date == today:
                return True
            else:
                return False
        else:
            return False

    def getListTaskToday(self):
        self.__readTaskFile()
        listFlag = list(self.__content.keys())
        listToday = []
        for i in listFlag:
            if self.checkDateTask(i):
               listToday.append(i)

        return listToday

    def getNbTaskToday(self):
        return len(self.getListTaskToday())

    def checkDateTaskTowmorow(self,name:str):
        towmorow = datetime.today() + timedelta(days=1)
        towmorow = f"{towmorow.year}-{towmorow.month}-{towmorow.day}"
        self.__readTaskFile()
        if name in self.__content and not self.__content[name]["fini"]:
            task_date = str(self.__content[name]["date"])
            if task_date == "none":
                return False
            elif task_date == towmorow:
                return True
            else:
                return False
        else:
            return False

    def getListTaskTowmorow(self):
        self.__readTaskFile()
        listFlag = list(self.__content.keys())
        listToday = []
        for i in listFlag:
            if self.checkDateTaskTowmorow(i):
               listToday.append(i)

        return listToday

    def getNbTaskTowmorow(self):
        return len(self.getListTaskTowmorow())

    def checkTaskLate(self,name):
        today = datetime.today()
        today = f"{today.year}-{today.month}-{today.day}"
        today = datetime.strptime(today, "%Y-%m-%d")
        self.__readTaskFile()
        if name in self.__content and not self.__content[name]["fini"]:
            task_date = self.__content[name]["date"]
            task_date = datetime.strptime(task_date, "%Y-%m-%d")
            if task_date == "none":
                return False
            elif task_date < today:
                return True
            else:
                return False
        else:
            return False

    def getListTaskLate(self):
        self.__readTaskFile()
        listFlag = list(self.__content.keys())
        listToday = []
        for i in listFlag:
            if self.checkTaskLate(i):
                listToday.append(i)

        return listToday

    def getNbTaskLate(self):
        return len(self.getListTaskLate())