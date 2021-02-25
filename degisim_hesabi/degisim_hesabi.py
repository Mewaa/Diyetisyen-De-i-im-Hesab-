import sys
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Değişim Hesabı"
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #----menu bar kategori----#
       # exitButton = QAction(QIcon('close.png'),'Exit',self)
       # exitButton.setShortcut('Ctrl+Q')
       # exitButton.setStatusTip('Exit applicaiton')
       # exitButton.triggered.connect(self.close)

        #-------Hesaplama Kısmı------#

        metin2 = QLabel(self)
        metin2.setText("Süt:")
        metin2.move(30,50)

        metin3 = QLabel(self)
        metin3.setText("Süt (YY):")
        metin3.move(30,100)

        metin0 = QLabel(self)
        metin0.setText("Et:")
        metin0.move(30,150)

        metin4 = QLabel(self)
        metin4.setText("EYG:")
        metin4.move(30,200)

        metin5 = QLabel(self)
        metin5.setText("Sebze:")
        metin5.move(30,250)

        metin6 = QLabel(self)
        metin6.setText("Meyve:")
        metin6.move(30,300)

        metin7 = QLabel(self)
        metin7.setText("Yağ:")
        metin7.move(30,350)

        metin8 = QLabel(self)
        metin8.setText("Yağlı Tohum:")
        metin8.move(30,400)


        #------inputlar-----#


        self.sut_input = QLineEdit(self)
        self.sut_input.move(110,55)
        self.sut_input.resize(50,20)

        self.suty_input =QLineEdit(self)
        self.suty_input.move(110,105)
        self.suty_input.resize(50,20)

        self.et_input = QLineEdit(self)
        self.et_input.move(110,155)
        self.et_input.resize(50,20)

        self.eyg_input =QLineEdit(self)
        self.eyg_input.move(110,205)
        self.eyg_input.resize(50,20)

        self.sebze_input =QLineEdit(self)
        self.sebze_input.move(110,255)
        self.sebze_input.resize(50,20)

        self.meyve_input =QLineEdit(self)
        self.meyve_input.move(110,305)
        self.meyve_input.resize(50,20)

        self.yag_input =QLineEdit(self)
        self.yag_input.move(110,355)
        self.yag_input.resize(50,20)

        self.yag_tohum_input =QLineEdit(self)
        self.yag_tohum_input.move(110,405)
        self.yag_tohum_input.resize(50,20)


        #-----Hesaplama Butonu----#

        self.hesap_buton = QPushButton("Hesapla",self)
        self.hesap_buton.setToolTip("SONUÇ:")
        self.hesap_buton.move(100,450)


        self.hesap_buton.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        if str(self.sut_input.text()) =="" or str(self.suty_input.text()) =="" or str(self.eyg_input.text()) =="" or str(self.sebze_input.text()) =="" or str(self.meyve_input.text()) =="" or str(self.yag_input.text()) =="" or str(self.yag_tohum_input.text()) =="" or str(self.et_input.text()) == "":
            QMessageBox.warning(self, 'Geçerli Değer Girmediniz!', "Lütfen Değer Girin!",QMessageBox.Ok)

        else:

            sut = float(self.sut_input.text())
            sutyy = float(self.suty_input.text())
            et = float(self.et_input.text())
            eyg = float(self.eyg_input.text())
            sebze = float(self.sebze_input.text())
            meyve = float(self.meyve_input.text())
            yag = float(self.yag_input.text())
            yag_tohumu = float(self.yag_tohum_input.text())

            #--------#
            cho_sut_sutyy = float(9)
            cho_eyg_meyve = float(15)
            cho_sebze = float(6)
            cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv = float(0)

            prt_sut_sutyy_et = float(6)
            prt_eyg_sebze_yagTohumu = float(2)

            yag_sut = float(6)
            yag_sutyy =float(3)
            yag_yag_tohum_et = float(5)

            toplam_gr_cho = float((cho_eyg_meyve*(eyg+meyve))+(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv*(yag+yag_tohumu+et))+(cho_sut_sutyy*(sut+sutyy))+(cho_sebze*sebze))

            toplam_gr_prt = float((prt_eyg_sebze_yagTohumu*(eyg+sebze+yag_tohumu))+(prt_sut_sutyy_et*(sut+sutyy+et))+(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv*(yag+meyve)))

            toplam_gr_yag = float((yag_yag_tohum_et*(yag+yag_tohumu+et))+(yag_sut*sut)+(yag_sutyy*sutyy)+(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv*(eyg+sebze+meyve)))

            enerji_sut = float(sut*(4*(cho_sut_sutyy+prt_sut_sutyy_et)+(yag_sut*9)))
            enerji_sutyy = float(sutyy*(4*(cho_sut_sutyy+prt_sut_sutyy_et)+(yag_sutyy*9)))
            enerji_et = float(et*(4*(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv+prt_sut_sutyy_et)+(yag_yag_tohum_et*9)))
            enerji_eyg = float(eyg*(4*(cho_eyg_meyve+prt_eyg_sebze_yagTohumu)+(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv*9)))
            enerji_sebze = float(sebze*(4*(cho_sebze+prt_eyg_sebze_yagTohumu)+(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv*9)))
            enerji_meyve = float(meyve*(4*(cho_eyg_meyve+cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv)+(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv*9)))
            enerji_yag = float(yag*(4*(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv+cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv)+(yag_yag_tohum_et*9)))
            enerji_tohum = float(yag_tohumu*(4*(cho_yag_thm_et_prt_yag_myv_yag_eyg_sbz_myv+prt_eyg_sebze_yagTohumu)+(yag_yag_tohum_et*9)))

            toplam_enerji = float(enerji_sut+enerji_sutyy+enerji_eyg+enerji_sebze+enerji_meyve+enerji_yag+enerji_tohum+enerji_et)
#-------------------------------------------Yüzde Hesabı--------------------------------------------------#
            cho_yuzde = float((toplam_gr_cho*400)/toplam_enerji)
            prot_yuzde = float((toplam_gr_prt*400)/toplam_enerji)
            yag_yuzde = float((toplam_gr_yag*900)/toplam_enerji)

            QMessageBox.warning(self, 'Sonuçlar', "CHO:"+str(toplam_gr_cho)+"\t%"+str(cho_yuzde)+"\nProtein:"+str(toplam_gr_prt)+"\t%"+str(prot_yuzde)+"\nYağ:"+str(toplam_gr_yag)+"    \t%"+str(yag_yuzde)+"\nEnerji:"+str(toplam_enerji), QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())