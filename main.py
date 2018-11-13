import sys
from PyQt5.QtWidgets import ( QWidget, QToolTip,
    QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QGridLayout, QDesktopWidget)
from PyQt5.QtGui import QFont , QPainter, QBrush, QColor
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
        self.setGeometry(100, 100, 100, 50)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

        self.setGeometry(QDesktopWidget().screenGeometry().width() - 68 - self.width() + QDesktopWidget().screenGeometry().x(),
                         QDesktopWidget().screenGeometry().height() - 40 - self.height() +QDesktopWidget().screenGeometry().y(),
                         self.width(), self.height())

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        animation = QPropertyAnimation(self)
        animation.setTargetObject(self)
        #animation.setPropertyName("popupOpacity")
        self.setWindowOpacity(10)


        popup_message = QLabel()
        popup_message.setText('It`s time to have a break!')
        popup_message.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        popup_message.setStyleSheet("color : white;"
                                    "margin-top: 6px;"
                                    "margin-bottom: 6px;"
                                    "margin-left: 10px;"
                                    "margin-right: 10px;")


        layout = QGridLayout(self)
        layout.addWidget(popup_message)

        painter = QPainter(self)
#        painter.setRenderHint(self)

        roundRect = QRect()
        roundRect.setX(self.rect().x() +5)
        roundRect.setY(self.rect().y() +5)
        roundRect.setWidth(self.rect().width() - 10)
        roundRect.setHeight(self.rect().height() - 10)
        painter.setBrush(QBrush(QColor(0, 0, 0, 180)))
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(roundRect,10,10)


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