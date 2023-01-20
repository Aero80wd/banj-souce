import login_window_gui
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qt_material import apply_stylesheet
from tkinter import Tk,simpledialog,messagebox
root = Tk()
root.withdraw()
QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

path = 0
def uishow():
    Dialog.show()
    ui.lineEdit_2.setText('')
    ui.lineEdit.setText('user')

def close():
    Dialog.close()

def cheak_password():
    global path
    with open('password.txt', 'r') as pwd:
        pa = str(pwd.readlines()).strip('\'[]')

    if pa == ui.lineEdit_2.text():
        Dialog.close()
        path = 1
    else:
        print(-1)
        print('\'' + pa + '\'')
        print(type(pa))
        return
app = QApplication(sys.argv)


Dialog = QDialog()
ui = login_window_gui.Ui_Dialog()

ui.setupUi(Dialog)

Dialog.setWindowTitle('BANJ-SOUCE V3.3 (Theme upgrade) Login')
Dialog.setWindowIcon(QIcon('icon.png'))
Dialog.setFixedSize(Dialog.width(), Dialog.height())
Dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
ui.pushButton_2.clicked.connect(close)
ui.pushButton.clicked.connect(cheak_password)

Dialog.setHidden(True)






