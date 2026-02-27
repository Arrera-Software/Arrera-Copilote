from fnc.fncBase import fncBase,gestionnaire
from datetime import datetime, timedelta
from meteofrance_api import MeteoFranceClient
from fnc.fonctionGPS import fncGPS

class fncMeteo(fncBase) :
    def __init__(self,gestionnaire:gestionnaire,gpsFnc:fncGPS):
        super().__init__(gestionnaire)
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            self.__client = MeteoFranceClient()
            self.__dictWarning = self.__client.get_warning_dictionary("fr")
        self.__fncGPS = gpsFnc
        self.__nameTown = None
        self.__temperature = None
        self.__humidity = None
        self.__description = None
        self.__date = None
        self.__icon = None
        self.__redAlert = []
        self.__orangeAlert = []
        self.__yellowAlert = []
        self.__greenAlert = []


    def getMeteoCurrentHour(self,town:str="",latitude:str="",longitude:str=""):
        """
        Récupère la météo actuelle pour une ville ou des coordonnées géographiques.
        :param town: Nom de la ville (optionnel)
        :param latitude: Latitude (optionnel)
        :param longitude: Longitude (optionnel)
        :return: True si les données sont récupérées avec succès, False sinon.
        """
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            if town:
                try:
                    townWeather = self.__client.search_places(town)
                    departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                    place = townWeather[0]
                    if not place:
                        return False
                except Exception as e:
                    # print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif latitude and longitude:
                try:
                    town = self.__fncGPS.getTownWithLatitudeAndLongitude(latitude,longitude)
                    if town is None:
                        return False
                    else:
                        townWeather = self.__client.search_places(town)
                        place = townWeather[0]
                        departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                        if not place:
                            return False
                except Exception as e:
                    # print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif self.__fncGPS.locate():
                    try :
                        town = self.__fncGPS.getTown()
                        townWeather = self.__client.search_places(town)
                        departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                        place = townWeather[0]
                        if not place:
                            return False
                    except Exception as e:
                        # print(f"Erreur lors de la récupération des données météo : {e}")
                        return False
            else :
                return False

            try :
                weather = self.__client.get_forecast_for_place(place)
                dictMeteo = weather.current_forecast
                self.__nameTown = place.name
                self.__temperature = dictMeteo['T']['value']
                self.__humidity = dictMeteo["humidity"]
                self.__description = dictMeteo['weather']['desc']
                self.__icon = dictMeteo['weather']['icon']
                alertes = self.__client.get_warning_current_phenomenons(departement).phenomenons_max_colors
                self.__rankingAlert(alertes)
                return True
            except Exception as e:
                # print(f"Erreur lors de la récupération des données météo : {e}")
                return False
        else :
            return False

    def getMeteoTowmorowMorning(self,town:str="",departement:str="75",latitude:str="",longitude:str=""):
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            if town:
                try:
                    townWeather = self.__client.search_places(town)
                    place = townWeather[0]
                    if not place:
                        return False
                    departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                except Exception as e:
                    print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif latitude and longitude:
                try:
                    town = self.__fncGPS.getTownWithLatitudeAndLongitude(latitude,longitude)
                    if town is None:
                        return False
                    else:
                        townWeather = self.__client.search_places(town)
                        place = townWeather[0]
                        if not place:
                            return False
                    departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                except Exception as e:
                    print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif self.__fncGPS.locate():
                    try :
                        townWeather = self.__client.search_places(self.__fncGPS.getTown())
                        place = townWeather[0]
                        if not place:
                            return False
                    except Exception as e:
                        print(f"Erreur lors de la récupération des données météo : {e}")
                        return False
            else :
                return False

            try :
                weather = self.__client.get_forecast_for_place(place)
                now = datetime.now()
                tomorrow_morning = (now + timedelta(days=1)).replace(hour=6, minute=0, second=0, microsecond=0)
                for dictMeteo in weather.forecast:
                    forecast_time = datetime.fromtimestamp(dictMeteo["dt"])
                    if forecast_time == tomorrow_morning:
                        self.__nameTown = place.name
                        self.__temperature = dictMeteo['T']['value']
                        self.__humidity = dictMeteo["humidity"]
                        self.__description = dictMeteo['weather']['desc']
                        self.__icon = dictMeteo['weather']['icon']
                        alertes = self.__client.get_warning_current_phenomenons(departement).phenomenons_max_colors
                        self.__rankingAlert(alertes)
                        return True
                else:
                    return False
            except Exception as e:
                # print(f"Erreur lors de la récupération des données météo : {e}")
                return False
        else :
            return False

    def getMeteoTowmorowNoon(self,town:str="",departement:str="75",latitude:str="",longitude:str=""):
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            if town:
                try:
                    townWeather = self.__client.search_places(town)
                    place = townWeather[0]
                    if not place:
                        return False
                    departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                except Exception as e:
                    # print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif latitude and longitude:
                try:
                    town = self.__fncGPS.getTownWithLatitudeAndLongitude(latitude,longitude)
                    if town is None:
                        return False
                    else:
                        townWeather = self.__client.search_places(town)
                        place = townWeather[0]
                        if not place:
                            return False
                    departement = self.__fncGPS.getFrenchDepartementWithTown(town)
                except Exception as e:
                    # print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif self.__fncGPS.locate():
                    try :
                        townWeather = self.__client.search_places(self.__fncGPS.getTown())
                        place = townWeather[0]
                        if not place:
                            return False
                    except Exception as e:
                        # print(f"Erreur lors de la récupération des données météo : {e}")
                        return False
            else :
                return False

            try :
                weather = self.__client.get_forecast_for_place(place)
                now = datetime.now()
                tomorrow_morning = (now + timedelta(days=1)).replace(hour=13, minute=0, second=0, microsecond=0)
                for dictMeteo in weather.forecast:
                    forecast_time = datetime.fromtimestamp(dictMeteo["dt"])
                    if forecast_time == tomorrow_morning:
                        self.__nameTown = place.name
                        self.__temperature = dictMeteo['T']['value']
                        self.__humidity = dictMeteo["humidity"]
                        self.__description = dictMeteo['weather']['desc']
                        self.__icon = dictMeteo['weather']['icon']
                        alertes = self.__client.get_warning_current_phenomenons(departement).phenomenons_max_colors
                        self.__rankingAlert(alertes)
                        return True
                else:
                    return False
            except Exception as e:
                # print(f"Erreur lors de la récupération des données météo : {e}")
                return False
        else :
            return False

    def __rankingAlert(self,alertes:list):
        self.__redAlert = []
        self.__orangeAlert = []
        self.__yellowAlert = []
        self.__greenAlert = []
        for alerte in alertes:
            idColor = int(alerte.get('phenomenon_max_color_id'))
            nameWarning = self.__dictWarning.get_phenomenon_by_id(int(alerte.get('phenomenon_id')))['name']
            if idColor == 1:
                self.__greenAlert.append(nameWarning)
            elif idColor == 2:
                self.__yellowAlert.append(nameWarning)
            elif idColor == 3:
                self.__orangeAlert.append(nameWarning)
            elif idColor == 4:
                self.__redAlert.append(nameWarning)

    def getNameTown(self):
        return self.__nameTown

    def getTemperature(self):
        return self.__temperature

    def getHumidity(self):#permet de recuperé le taux d'humiditer en %
        return self.__humidity

    def getDescription(self):
        return self.__description

    def getIcon(self):
        return self._gestionnaire.getConfigFile().asset+"meteo/"+self.__icon+".png"

    def getRedAlert(self):
        return self.__redAlert

    def getOrangeAlert(self):
        return self.__orangeAlert

    def getYellowAlert(self):
        return self.__yellowAlert

    def getGreenAlert(self):
        return self.__greenAlert