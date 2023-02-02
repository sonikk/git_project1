import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from map import Ui_MainWindow
from io import BytesIO
import requests
from PIL import Image

address = ''


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.map.clicked.connect(self.display_image)

    def display_image(self):
        global address
        address = self.lineEdit.text()

        proxies = {'http':
                       'http://s2021010002:Ypower986-@proxy.volgatech.net:3128/',
                   'https':
                       'https://s2021010002:Ypower986-@proxy.volgatech.net:3128/'}



        map_params = {
            "ll": address,
            'spn': '0.00821099999999575,0.004622000000004789',
            'pt': address,
            "l": "map"
        }

        map_api_server = "http://static-maps.yandex.ru/1.x/"

        response = requests.get(map_api_server, params=map_params, proxies=proxies)


        self.pixmap = QPixmap()
        self.pixmap.loadFromData(response.content)
        self.map_2.setPixmap(self.pixmap)






app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())