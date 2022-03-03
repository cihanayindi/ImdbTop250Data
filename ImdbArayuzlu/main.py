#-------------------KÜTÜPHANE------------------#
#----------------------------------------------#

import sys
from sqlite3 import Cursor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfaUI import *
import requests
from bs4 import BeautifulSoup

#---------------UYGULAMA OLUSTUR---------------#
#----------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

#---------------SİTEYE BAĞLAN---------------#
#-------------------------------------------#

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

if response.status_code == 200:
    ui.statusbar.showMessage("Bağlantı başarılı!",10000)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi, "html.parser")

#---------------LİSTELE BUTONU---------------#
#--------------------------------------------#

def LISTELE():

    ui.tblwVeriler.clear()
    _altyil = len(ui.lneAltYil.text())
    _ustyil = len(ui.lneUstYil.text())
    _rating = len(ui.lneEnAzRating.text())
    basliklar = soup.find_all("td", {"class": "titleColumn"})
    ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})
    isimler = []
    ratinglistesi = []
    for baslik in basliklar:
        baslik = baslik.text
        baslik = baslik.strip()
        baslik = baslik.replace("\n", "")
        baslik = baslik.split(" ")
        deneme = ''
        for i in range(6,len(baslik)):
            deneme += baslik[i] + " "
        isimler.append(deneme)

    for rating in ratingler:
        rating = rating.text
        ratinglistesi.append(rating)

    sonuc = zip(isimler,ratinglistesi)

    if (_altyil != 0 and _ustyil != 0):
        altyil = int(ui.lneAltYil.text())
        ustyil = int(ui.lneUstYil.text())
        if (_rating != 0):
            str = ui.lneEnAzRating.text()
            str = str.replace(",",".")
            str = float(str)
            names = []
            ratings = []
            for isim,deger in sonuc:
                if (float(deger) >= str):
                    yil = isim[-6:-2]
                    yil = int(yil)
                    if (altyil < yil < ustyil):
                        names.append(isim)
                        ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
        else:
            names = []
            ratings = []
            for isim,deger in sonuc:
                yil = isim[-6:-2]
                yil = int(yil)
                if (altyil < yil < ustyil):
                    names.append(isim)
                    ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
    elif (_altyil != 0 and _ustyil == 0):
        altyil = int(ui.lneAltYil.text())
        if (_rating != 0):
            str = ui.lneEnAzRating.text()
            str = str.replace(",", ".")
            str = float(str)
            names = []
            ratings = []
            for isim,deger in sonuc:
                if (float(deger) >= str):
                    yil = isim[-6:-2]
                    yil = int(yil)
                    if (yil > altyil):
                        names.append(isim)
                        ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
        else:
            names = []
            ratings = []
            for isim, deger in sonuc:
                yil = isim[-6:-2]
                yil = int(yil)
                if (altyil < yil):
                    names.append(isim)
                    ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
    elif (_altyil == 0 and _ustyil != 0):
        ustyil = int(ui.lneUstYil.text())
        if (_rating != 0):
            str = ui.lneEnAzRating.text()
            str = str.replace(",", ".")
            str = float(str)
            names = []
            ratings = []
            for isim,deger in sonuc:
                if (float(deger) >= str):
                    yil = isim[-6:-2]
                    yil = int(yil)
                    if (yil < ustyil):
                        names.append(isim)
                        ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
        else:
            names = []
            ratings = []
            for isim, deger in sonuc:
                yil = isim[-6:-2]
                yil = int(yil)
                if (yil < ustyil):
                    names.append(isim)
                    ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
    elif (_altyil == 0 and _ustyil == 0):
        if (_rating != 0):
            str = ui.lneEnAzRating.text()
            str = str.replace(",",".")
            str = float(str)
            names = []
            ratings = []
            for isim,deger in sonuc:
                if (float(deger) >= str):
                    names.append(isim)
                    ratings.append(deger)
            son = list(zip(names,ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))
        else:
            names = []
            ratings = []
            for isim, deger in sonuc:
                names.append(isim)
                ratings.append(deger)
            son = list(zip(names, ratings))
            for satirIndeks, satirVeri in enumerate(son):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwVeriler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem((sutunVeri)))

#---------------ÇIKIŞ---------------#
#-----------------------------------#

def CIKIS():
    cevap = QMessageBox.question(penAna, "ÇIKIŞ", "Programdan çıkmak istediğinize emin misiniz?",\
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        sys.exit(Uygulama.exec_())
    else:
        penAna.show()



#---------------SİNYAL-SLOT---------------#
#-----------------------------------------#

ui.btnListele.clicked.connect(lambda : LISTELE())
ui.btnCikis.clicked.connect(lambda : CIKIS())

sys.exit(Uygulama.exec_())
