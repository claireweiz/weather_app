import tkinter
from tkinter import ttk
from tkinter.constants import *
from tkinter import StringVar, IntVar
from tkinter.ttk import *
from PIL import ImageTk, Image

class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.geometry("400x350")
        self.title("Tkinter Weather App 🌤")
        #self.configure(bg ='#27445C')

        self.controller = controller
        self.bind('<Return>', self.controller.handleButtonSearch)

        #---- Variables ----
        self.varSearch = StringVar()
        self.varTemp = StringVar()
        self.varLocation = StringVar()
        self.varCondition = StringVar()
        self.varIcon = StringVar()
        self.varFeelsLike = StringVar()
        self.varWindSpeed = StringVar()
        self.varWindDir = StringVar()
        self.varPrecip = IntVar()
        self.varUnits = IntVar()

        #---- Frames ----
        self.mainframe = Frame(self)
        self.mainframe.grid(pady=(500, 0))
        
        self.mainframe.pack()
        self._createFrameSearchBar()
        self._createFrameInfo()
        self._createFrameDetails()
        self._createFrameControls()
        

    def _createFrameSearchBar(self):
        self.frameSearchBar = Frame(self.mainframe)

        self.comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        # comboSearch.insert(0, 'Enter City Name')
        self.buttonSearch = Button(self.frameSearchBar, text="SEARCH", command=self.controller.handleButtonSearch)
        
        #self.comboSearch.bind('<KeyRelease>', self.controller.handleButtonSearch)

        self.comboSearch.pack(padx=10, pady=10, side=LEFT)
        self.buttonSearch.pack(padx=10, pady=10, side=RIGHT)
        self.frameSearchBar.pack(pady=5)


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)
        labelTemp = Label(self.frameInfo, textvariable=self.varTemp, font=('bold', 30))
        labelLocation = Label(self.frameInfo, textvariable=self.varLocation, font=('bold', 15))
        #labelIcon = Label(self.frameInfo, textvariable=self.varIcon)

        labelTemp.pack(pady=5)
        labelLocation.pack(pady=5)
        #labelIcon.pack(pady=5)
        self.frameInfo.pack()

    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        labelConditionLeft = Label(self.frameDetails, text='Current Condition:')
        labelFeelsLikeLeft = Label(self.frameDetails, text='Feels Like:')
        labelWindSpeedLeft = Label(self.frameDetails, text='Wind Speed:')
        labelWindDirLeft = Label(self.frameDetails, text='Wind Direction:')
        labelPrecipLeft = Label(self.frameDetails, text='Precipitation:')

        #s = ttk.Style()
        #s.configure('my.TFrame', bg='#27445C')
        labelConditionRight = Label(self.frameDetails, textvariable=self.varCondition)
        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike)
        labelWindSpeedRight = Label(self.frameDetails, textvariable=self.varWindSpeed)
        labelWindDirRight = Label(self.frameDetails, textvariable=self.varWindDir)
        labelPrecipRight = Label(self.frameDetails, textvariable=self.varPrecip)

        labelConditionLeft.grid(row=0, column=0, pady=5, sticky=W)
        labelConditionRight.grid(row=0, column=1, pady=5, sticky=E)
        labelFeelsLikeLeft.grid(row=1, column=0, pady=5, sticky=W)
        labelFeelsLikeRight.grid(row=1, column=1, pady=5, sticky=E)
        labelWindSpeedLeft.grid(row=2, column=0, pady=5, sticky=W)
        labelWindSpeedRight.grid(row=2, column=1, pady=5, sticky=E)
        labelWindDirLeft.grid(row=3, column=0, pady=5, sticky=W)
        labelWindDirRight.grid(row=3, column=1, pady=5, sticky=E)
        labelPrecipLeft.grid(row=4, column=0, pady=5,sticky=W)
        labelPrecipRight.grid(row=4, column=1, pady=5, sticky=E)
        self.frameDetails.pack()


    def _createFrameControls(self):
        self.frameControls = Frame(self.mainframe)

        radioC = Radiobutton(self.frameControls, text='Celcius', variable=self.varUnits, value=1, command=self.controller.updateGUI)
        radioF = Radiobutton(self.frameControls, text='Fahrenheit', variable=self.varUnits, value=2, command=self.controller.updateGUI)

        radioC.invoke()

        radioC.pack(side=LEFT, padx=15, pady=10)
        radioF.pack(side=RIGHT, padx=15, pady=10)
        self.frameControls.pack()
 
        
    def main(self):
        self.mainloop()