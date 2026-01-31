from datetime import datetime, timedelta

class CArreraDate :
    def __init__(self):
        self.__date= datetime.now()
    
    def rafraichisement(self):
        self.__date= datetime.now()
        
    def heure(self):
        return str(self.__date.time().hour)

    def minute(self):
        return str(self.__date.time().minute)
    
    def second(self):
        return str(self.__date.time().second)
    
    def jour(self):
        jour = self.__date.day
        if jour < 10 :
            return "0"+str(jour)
        else :
            return str(jour)
    
    def jourSimple(self):
        return str(self.__date.day)
    
    def nbMois(self):
        mois = self.__date.month
        if mois < 10 :
            return "0"+str(mois)
        else :
            return str(mois)

    def nbMoisSimple(self):
        return str(self.__date.month)
           
    
    def mois(self):
        mois = int(self.__date.month)
        if mois == 1 :
            monthSTR = "Janvier"
        else :
            if mois == 2 :
                monthSTR = "Fevrier"
            else :
                if mois == 3 :
                    monthSTR = "Mars"
                else :
                    if mois == 4 :
                        monthSTR = "Avril"
                    else :
                        if mois == 5 :
                            monthSTR = "Mai"
                        else:
                            if mois == 6 :
                                monthSTR = "Juin"
                            else:
                                if mois == 7 :
                                    monthSTR = "Juillet"
                                else :
                                    if mois == 8 :
                                        monthSTR = "Aout"
                                    else :
                                        if mois == 9 :
                                            monthSTR = "Septembre"
                                        else :
                                            if mois == 10 :
                                                monthSTR = "Octobre"
                                            else:
                                                if mois == 11 :
                                                    monthSTR = "Novembre"
                                                else :
                                                    monthSTR = "Décembre"
        return monthSTR
    
    def annes(self):
        return str(self.__date.year)

    def getDateToday(self):
        date = self.__date
        return str(str(date.year)+"-"+str(date.month)+"-"+str(date.day))

    def dateTowmoro(self):
        dateHier = self.__date - timedelta(days=1)
        return str(dateHier.strftime("%Y-%m-%d"))

    def otherPastDate(self,delta:int):
        date = self.__date - timedelta(days=delta)
        return str(str(date.year)+"-"+str(date.month)+"-"+str(date.day))

    def otherAfterDate(self,delta:int):
        date = self.__date + timedelta(days=delta)
        return str(str(date.year)+"-"+str(date.month)+"-"+str(date.day))
