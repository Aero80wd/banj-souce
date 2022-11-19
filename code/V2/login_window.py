import login_window_gui
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
path = 0
def uishow():
    Dialog.show()
    ui.lineEdit_2.setText('')
def close():
    Dialog.close()
def cheak_password():
    global path
    with open('password.txt','r') as pwd:
        pa = pwd.readlines()[0].split(';')

        pc = pa[0][0:-16][::-1]
        pb = pa[1][0:-16][::-1]
        pwrd = [pc,pb]
    uird = [ui.lineEdit.text(),ui.lineEdit_2.text()]
    if pwrd == uird:
        Dialog.close()
        path = 1
    else:
        QMessageBox.critical(ui, 'error', 'login error', QMessageBox.OK)
app = QApplication(sys.argv)


Dialog = QDialog()
ui = login_window_gui.Ui_Dialog()

ui.setupUi(Dialog)
Dialog.setWindowTitle('BANJ-SOUCE V2 (Build SAT 1129) Login')
Dialog.setWindowIcon(QIcon('icon.png'))
ui.pushButton_2.clicked.connect(close)
ui.pushButton.clicked.connect(cheak_password)

Dialog.setHidden(True)






