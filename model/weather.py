import requests

API_KEY = 'a1656844bbda456d9fd153632232203'

class Weather:
    
    def __init__(self, location:str='Taipei'):
        self.weatherData = {}
        self.fetch(location)
    
   #---- Location ----

    def getLocationData(self, name):
        data = self.weatherData['location'][name]
        return str(data)
    
    def getCity(self):
        return self.getLocationData('name')


    def getState(self):
        return self.getLocationData('region')


    def getCountry(self):
        return self.getLocationData('country')


    def getTimeZone(self):
        return self.getLocationData('tz_id')


    def getLocation(self):
        if 'America' in self.getTimeZone():
            return f'{self.getCity()}, {self.getState()}' 
        else:
            return f'{self.getCity()}, {self.getCountry()}'


    #---- Current

    def getCurrentData(self, name):
        data = self.weatherData['current'][name]
        return data if name == 'condition' else str(data)


    def getCurrentTempC(self):
        return self.getCurrentData('temp_c') + '\u00B0C'
    
    
    def getCurrentTempF(self):
        return self.getCurrentData('temp_f')+ '\u00B0F'


    def getConditionText(self):
        condition = self.getCurrentData('condition')
        return str(condition['text'])


    def getConditionIcon(self):
        condition = self.getCurrentData('condition')
        icon = str(condition['icon'])
        return icon


    def getFeelsLikeF(self):
        return self.getCurrentData('feelslike_f') + '\u00B0F'


    def getFeelsLikeC(self):
        return self.getCurrentData('feelslike_c') + '\u00B0C'


    def getWindSpeedMPH(self):
        return self.getCurrentData('wind_mph') + ' mph'

    
    def getWindDirection(self):
        return self.getCurrentData('wind_dir')


    def getPrecip(self):
        return self.getCurrentData('precip_mm') + ' mm'
    
    #---- fetch ----
    
    def fetch(self, query):
        try:    
            url = f'http://api.weatherapi.com/v1/current.json' + \
                f'?key={API_KEY}&q={query}&aqi=no'
            self.weatherData = requests.get(url).json()
        except:
            self.weatherData = {'error': []}
