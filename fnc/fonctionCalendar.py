import json
import os
from librairy.arrera_date import*
from fnc.fncBase import fncBase,gestionnaire

class fncCalendar(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__calendarFile = self._gestionnaire.getEmplacementFileAgenda()
        self.__contentCalendar = None

    def __updateDateToday(self):
        self.__today = datetime.today()

    def __loadCalendar(self):
        if not os.path.exists(self.__calendarFile):
            return False
        else :
            with open(self.__calendarFile, "r", encoding="utf-8") as f:
                self.__contentCalendar = json.loads(f.read())
            return True

    def __saveCalendar(self):
        if not os.path.exists(self.__calendarFile):
            return False
        else :
            with open(self.__calendarFile, "w", encoding="utf-8") as f:
                json.dump(self.__contentCalendar, fp=f, indent=4)
            return True

    def addEventToCalendar(self,name:str,date:datetime,heure:str = "",descrption:str = "",lieu:str="",repetition:bool = False):
        if not self.__loadCalendar() :
            return False

        if not self.__contentCalendar :
            id = 1
        else:
            id = max(ev["id"] for ev in self.__contentCalendar) + 1

        date_str = date.isoformat()


        dictNewEvent = {
            "id":id,
            "date": date_str,
            "heure": heure,
            "name": name,
            "description": descrption,
            "lieu": lieu,
            "repetition": repetition
        }
        self.__contentCalendar.append(dictNewEvent)

        return self.__saveCalendar()

    def getAllEvents(self):
        if not self.__loadCalendar() :
            return []

        if not self.__contentCalendar :
            return []

        listEvents = []
        for event in self.__contentCalendar:
            listEvents.append(event["name"])

        return listEvents

    def getInformationEvent(self,name:str):
        if not self.__loadCalendar() :
            return {}

        if not self.__contentCalendar :
            return {}

        for event in self.__contentCalendar:
            if event["name"] == name:
                return event

        return {}

    def checkDateHourEvent(self):
        if not self.__loadCalendar() :
            return []

        if not self.__contentCalendar :
            return []

        listEvent = []
        date_str = datetime.today().strftime("%Y-%m-%d")
        hour_str = datetime.today().strftime("%H:%M")


        for event in self.__contentCalendar:
            if event["date"] == date_str:
                if event["heure"] == "":
                    listEvent.append(event["name"])
                else :
                    if event["heure"] == hour_str:
                        listEvent.append(event["name"])

        return listEvent

    def checkDateDayEvent(self):
        if not self.__loadCalendar() :
            return []

        if not self.__contentCalendar :
            return []

        listEvent = []
        date_str = datetime.today().strftime("%Y-%m-%d")


        for event in self.__contentCalendar:
            if event["date"] == date_str:
                listEvent.append(event["name"])

        return listEvent

    def checkEventWithDate(self,date:str):
        """ date au format YYYY-MM-DD """
        if not self.__loadCalendar() :
            return []

        if not self.__contentCalendar :
            return []

        listEvent = []
        date_str = date


        for event in self.__contentCalendar:
            if event["date"] == date_str:
                listEvent.append(event["name"])

        return listEvent

    def delEvent(self,name:str):
        if not self.__loadCalendar() :
            return False

        if not self.__contentCalendar :
            return False

        for i, event in enumerate(self.__contentCalendar):
            if event["name"] == name:
                del self.__contentCalendar[i]
                return self.__saveCalendar()

        return False