import sys
from datetime import datetime, timedelta
import pytz
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from yahoo_finance import Share, yql
from MainWindow import Ui_MainWindow

class runApplication(Ui_MainWindow):
    def __init__(self):
        self._translate = QtCore.QCoreApplication.translate
        self.data=""
        self.run()
        self.Quit()  
    def run(self):
        self.app=QApplication(sys.argv)
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.buttonActions()
        self.window.show()
        self.Quit()
    def buttonActions(self):
        self.ui.pushButtonStockdata.clicked.connect(self.getData)        
    def update(self,obj,text):
        self.obj=obj
        self.text=text
        self.obj.setText(self._translate("MainWindow", self.text))
    def getData(self):
        ''' Get stock data '''
        self.amount=0
        self.count=0
        self.yahoo = Share(self.ui.Symbol.text())
        self.yahoo.refresh()
        try:
            self.name=self.yahoo.get_name()
            self.price=float(self.yahoo.get_price())
            try:
                self.div=float(self.yahoo.get_dividend_share())
            except:
                self.div=0.0
            try:
                self.div_yield=float(self.yahoo.get_dividend_yield())
            except:
                self.div_yield=0.0
            self.getAmount()
            self.setData()
        except:
            self.data="Error:" 
            self.data+="\n"
            self.data+="This symbol does not exist."
            self.data+="\n"
            self.data+="Try another one."
            self.update(obj=self.ui.lblStockdata,text=self.data)
    def getAmount(self):
        if self.div_yield!=0.0 and self.div!=0.0:
            while self.amount < self.price:
              self.amount+=self.div
              self.count+=1
        self.amount=self.count
    def setData(self):
        if self.div==0.0:
            self.div="No data"
            self.div_yield="No data"
        self.data="Name: " + self.name
        self.data+="\n"
        self.data+="Price: " + str(self.price)
        self.data+="\n"
        if self.div!="No data":
            self.data+="Dividend: " + str(self.div)
            self.data+="\n"
            self.data+="Dividend yield: " + str(self.div_yield) + "%"
            self.data+="\n"
            self.data+="Stocks needed: " + str(round(self.amount))
            self.data+="\n"
            self.data+="This will give " + str(round(self.amount)*self.div) + " in dividends."
            self.data+="\n"
            self.data+="Total investment needed: " + str(int(self.amount*self.price)) + " US$"
        else:
            self.data+="This stock does not pay out dividends."
        self.update(obj=self.ui.lblStockdata,text=self.data)
    def Quit(self):
        sys.exit(self.app.exec_())

if __name__=="__main__":
    runApplication()
