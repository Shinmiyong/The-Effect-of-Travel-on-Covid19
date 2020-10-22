import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window=uic.loadUiType('./mainwindow.ui')[0]  #디자인한 ui이름


class month1Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./1month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()

class month2Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./2month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()

class month3Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./3month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()

class month4Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./4month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()


class month5Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./5month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()

class month6Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./6month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()


class month7Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./7month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()


class month8Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("./8month.ui")  ##이곳에 designer에서 저장한 파일명을 입력해줍니다.
        self.ui.show()







class Exam(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   ##ui초기화하는 함수

        #클릭 시 실행되는 화면
        self.btn_1.clicked.connect(
            self.btn1_clicked_process)

        self.btn_2.clicked.connect(
            self.btn2_clicked_process)

        self.btn_3.clicked.connect(
            self.btn3_clicked_process)

        self.btn_4.clicked.connect(
             self.btn4_clicked_process)

        self.btn_5.clicked.connect(
             self.btn5_clicked_process)

        self.btn_6.clicked.connect(
             self.btn6_clicked_process)

        self.btn_7.clicked.connect(
             self.btn7_clicked_process)

        self.btn_8.clicked.connect(
             self.btn8_clicked_process)

    def btn1_clicked_process(self):
        dialog = month1Dialog(self)

    def btn2_clicked_process(self):
        dialog = month2Dialog(self)

    def btn3_clicked_process(self):
        dialog = month3Dialog(self)

    def btn4_clicked_process(self):
        dialog = month4Dialog(self)

    def btn5_clicked_process(self):
        dialog = month5Dialog(self)

    def btn6_clicked_process(self):
        dialog = month6Dialog(self)


    def btn7_clicked_process(self):
        dialog = month7Dialog(self)

    def btn8_clicked_process(self):
        dialog = month8Dialog(self)










app=    QApplication(sys.argv)
mainWIndow = Exam()
mainWIndow.show()
sys.exit(app.exec_())
