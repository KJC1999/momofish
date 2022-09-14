from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


# class myLabel(QLabel):
#     clicked = pyqtSignal()
#     def mouseReleaseEvent(self, QMouseEvent):
#         if QMouseEvent.button() == Qt.LeftButton:
#             self.clicked.emit()
#
#
# class Wind(QDialog):
#     clicked = pyqtSignal()
#
#     def __init__(self):
#         super().__init__()
#         self.label = myLabel()
#         self.label.setText('这是一个文本标签')
#         # self.label.pyqtSignal()
#         vb = QVBoxLayout()
#         vb.addWidget(self.label)
#         self.setLayout(vb)
#
#         self.label.clicked.connect(self.showData)
#
#     def showData(self):
#         print('ok')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = Wind()
#     win.show()
#     sys.exit(app.exec_())

from PyQt5.QtWebEngineWidgets import *
import PyQt5.QtWebEngineWidgets
print(PyQt5.QtWebEngineWidgets.path)

