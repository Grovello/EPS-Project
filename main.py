import sys
from PyQt5.QtWidgets import ( QWidget, QToolTip,
    QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Settings')

        saveButton = QPushButton('Save', self)
        quitButton = QPushButton('Quit', self)
        popupButton = QPushButton('Popup', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(popupButton)
        hbox.addWidget(saveButton)
        hbox.addWidget(quitButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        quitButton.clicked.connect(QApplication.instance().quit)
        self.show()


class PopUp(QWidget):

    def __init__(self):
        super().__init__()
        self.PopupUI()

    def PopupUI(self):
        self.setGeometry(150, 150, 150, 150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = MainWindow()
    pupupW = PopUp()

    sys.exit(app.exec_())


    # def closeEvent(self, ):
    #     reply = QMessageBox.question(self, 'Message',
    #                                  "Are you sure to quit?", QMessageBox.Yes |
    #                                  QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()