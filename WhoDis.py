import sys
import json
import requests
from PyQt5 import QtWidgets
import gui


class Ui(gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.label.setText("IP Address:")
        self.go_button.clicked.connect(self.search_function)

    def search_function(self):
        print("works")
        country = self.country
        region = self.region
        domain = self.ip_address
        lat = self.latitude
        lon = self.longitude
        isp = self.isp
        status = self.status

        ip = self.input_line
        request = requests.get("http://ip-api.com/json/" + ip.text())
        response = json.loads(request.text)

        country.setText(str(response['country']))
        region.setText(str(response['region']))
        domain.setText(str(response['query']))
        lat.setText(str(response['lat']))
        lon.setText(str(response['lon']))
        isp.setText(str(response['isp']))
        status.setText(str(response['status']))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
