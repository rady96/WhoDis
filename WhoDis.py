import sys
import json
import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import gui, about
import webbrowser



class Ui(gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.label.setText("IP Address:")
        self.go_button.clicked.connect(self.search_function)
        self.actionAbout.triggered.connect(self.showabout)
        self.actionGithub.triggered.connect(self.github)
        self.actionDonate.triggered.connect(self.donate)
        self.actionWebsite.triggered.connect(self.website)
        self.actionExit.triggered.connect(self.exit)

    def showabout(self):
        about_window.show()

    def github(self):
        webbrowser.open('https://github.com/rady96/WhoDis')

    def donate(self):
        webbrowser.open('http://rady.tech')

    def website(self):
        webbrowser.open('http://rady.tech')

    def exit(self):
        app.exit()

    def search_function(self):
        try:
            ip = window.input_line
            request = requests.get("http://ip-api.com/json/" + ip.text())
            response = json.loads(request.text)
            country = window.country
            region = window.region
            domain = window.ip_address
            lat = window.latitude
            lon = window.longitude
            isp = window.isp
            status = window.status

            country.setText(str(response['country']))
            region.setText(str(response['region']))
            domain.setText(str(response['query']))
            lat.setText(str(response['lat']))
            lon.setText(str(response['lon']))
            isp.setText(str(response['isp']))
            status.setText(str(response['status']))

        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Woooops")
            msg.setInformativeText('Something not right !')
            msg.setWindowTitle("Error")
            msg.exec_()


class about(about.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(about, self).__init__()
        self.setupUi(self)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    about_window = about()
    window.show()
    app.exec_()
