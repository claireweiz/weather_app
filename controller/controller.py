from view.view import View
from model.weather import Weather
from tkinter import messagebox

class Controller:
    
    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()
        
        self.updateGUI()
    
    
    def main(self):
        self.view.main()
        
    def updateGUI(self):
        if 'error' not in self.weather.weatherData:
            self.view.varLocation.set(self.weather.getLocation())
            self.view.varCondition.set(self.weather.getConditionText())
            self.view.varIcon.set(self.weather.getConditionIcon())
            self.view.varWindSpeed.set(self.weather.getWindSpeedMPH())
            self.view.varWindDir.set(self.weather.getWindDirection())
            self.view.varPrecip.set(self.weather.getPrecip())
            
            if self.view.varUnits.get() == 1:
                self.view.varTemp.set(self.weather.getCurrentTempC())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeC())
            else:
                self.view.varTemp.set(self.weather.getCurrentTempF())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeF())
        else: 
            location = self.view.varSearch.get()
            messagebox.showerror('Error', 'Cannot find city "{}"'.format(location))    
    
    def handleButtonSearch(self, event=None):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.updateGUI()
               