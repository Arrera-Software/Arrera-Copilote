from fnc.fncBase import fncBase,gestionnaire
import requests
import webbrowser
import urllib.parse

class fncGPS(fncBase):
    def __init__(self,gestionnaire: gestionnaire):
        super().__init__(gestionnaire)
        self.__latitude = None
        self.__longitude = None
        self.__region = None

    def locate(self):
        api_url = 'https://ipinfo.io/json'
        if self._gestionnaire.getNetworkObjet().getEtatInternet() :
            try:
                response = requests.get(api_url, timeout=5)
                response.raise_for_status()
                data = response.json()
                loc = tuple(map(float, data['loc'].split(',')))
                self.__region = self.__getDepartementWithPostalCode(data['postal'])
                self.__latitude = loc[0]
                self.__longitude = loc[1]
                return True
            except Exception as e:
                # print(e)
                return False
        else :
            return False

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getRegion(self):
        return self.__region

    def getTown(self):
        url = 'https://nominatim.openstreetmap.org/reverse'
        params = {
            'lat': str(self.__latitude),
            'lon': str(self.__longitude),
            'format': 'json',
            'zoom': 10,  # Niveau de détail (10 = ville)
            'addressdetails': 1,
        }
        headers = {
            'User-Agent': 'my-geocoder'
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        city = data.get('address', {}).get('city') \
               or data.get('address', {}).get('town') \
               or data.get('address', {}).get('village')
        return city

    def launchGoogleMapItinerary(self, depart: str, arrivee: str):
        if depart != "" and arrivee != "":
            base_url = "https://www.google.com/maps/dir/?api=1"
            params = {
                "origin": depart,
                "destination": arrivee
            }

            # Encoder les paramètres pour les inclure dans l'URL
            url_params = urllib.parse.urlencode(params)
            full_url = f"{base_url}&{url_params}"

            # Ouvrir l'URL dans le navigateur par défaut
            return webbrowser.open(full_url)
        else:
            return False

    def getTownWithLatitudeAndLongitude(self,latitude:str,longitude:str):
        if self._gestionnaire.getNetworkObjet().getEtatInternet() :
            url = 'https://nominatim.openstreetmap.org/reverse'
            params = {
                'lat': str(latitude),
                'lon': str(longitude),
                'format': 'json',
                'zoom': 10,  # Niveau de détail (10 = ville)
                'addressdetails': 1,
            }
            headers = {
                'User-Agent': 'my-geocoder'
            }
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            city = data.get('address', {}).get('city') \
                   or data.get('address', {}).get('town') \
                   or data.get('address', {}).get('village')
            return city
        else :
            return None

    def __getDepartementWithPostalCode(self, postal_code):
        # Code postal en string pour éviter les erreurs avec les zéros
        str_code = str(postal_code)
        # Les 2 premiers chiffres du code postal correspondent au département (sauf exceptions)
        if str_code[:2] == "20":
            # La Corse a deux départements : 2A et 2B.
            if int(str_code) < 20200:
                return "2A"
            else:
                return "2B"
        if str_code[:2] in ["97", "98"]:
            # Outre-mer: retournez les 3 premiers chiffres
            return str_code[:3]
        return str_code[:2]

    def getFrenchDepartementWithTown(self,town:str):
        url = f"https://geo.api.gouv.fr/communes?nom={town.lower()}&fields=departement&format=json"
        result = requests.get(url).json()
        if result:
            return result[0]['departement']['code']
        else:
            return None