import sys
import Main_Interface
from allUI import Calculator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CalculatorWindow(Calculator.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Calculator.Ui_MainWindow, self).__init__()
        self.setupUi(self)  # 加载UI
        # 信号与槽设置
        self.btn0.clicked.connect(self.btn0_clicked)
        self.btn00.clicked.connect(self.btn00_clicked)
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)
        self.btn3.clicked.connect(self.btn3_clicked)
        self.btn4.clicked.connect(self.btn4_clicked)
        self.btn5.clicked.connect(self.btn5_clicked)
        self.btn6.clicked.connect(self.btn6_clicked)
        self.btn7.clicked.connect(self.btn7_clicked)
        self.btn8.clicked.connect(self.btn8_clicked)
        self.btn9.clicked.connect(self.btn9_clicked)
        self.btnClear.clicked.connect(self.btnClear_clicked)
        self.btnBack.clicked.connect(self.btnBack_clicked)   # 回退按钮
        self.btnPlus.clicked.connect(self.btnPlus_clicked)
        self.btnSub.clicked.connect(self.btnSub_clicked)
        self.btnMul.clicked.connect(self.btnMul_clicked)
        self.btnDiv.clicked.connect(self.btnDiv_clicked)
        self.btnEqual.clicked.connect(self.btnEqual_clicked)
        self.btnReset.clicked.connect(self.btnReset_clicker)
        self.btn_doc.clicked.connect(self.btnDoc_clicked)
        self.main_Button.clicked.connect(self.backTo)  # 跳转主页面

    def btnClear_clicked(self):
        self.lineEdit.clear()

    def btn1_clicked(self):
        self.lineEdit.insert("1")

    def btn2_clicked(self):
        self.lineEdit.insert("2")

    def btn3_clicked(self):
        self.lineEdit.insert("3")

    def btn4_clicked(self):
        self.lineEdit.insert("4")

    def btn5_clicked(self):
        self.lineEdit.insert("5")

    def btn6_clicked(self):
        self.lineEdit.insert("6")

    def btn7_clicked(self):
        self.lineEdit.insert("7")

    def btn8_clicked(self):
        self.lineEdit.insert("8")

    def btn9_clicked(self):
        self.lineEdit.insert("9")

    def btn0_clicked(self):
        self.lineEdit.insert("0")

    def btn00_clicked(self):
        self.lineEdit.insert("00")

    def btnPlus_clicked(self):
        text = self.lineEdit.text()
        if len(text) < 3:
            if len(text) == 0:
                self.error_message()
            else:
                self.lineEdit.insert(' + ')
        else:
            # 判断前方是否有符号，只要存在符号，则先去符号，再重新插入符号
            if text[-2] in ['+', '-', '*', '/']:
                for i in range(3):
                    text = text[:-1]
                self.lineEdit.clear()
                self.lineEdit.insert(text + ' + ')
            else:
                self.lineEdit.insert(' + ')

    def btnSub_clicked(self):
        text = self.lineEdit.text()
        if len(text) < 3:
            if len(text) == 0:
                self.error_message()
            else:
                self.lineEdit.insert(' - ')
        else:
            # 判断前方是否有符号，只要存在符号，则先去符号，再重新插入符号
            if text[-2] in ['+', '-', '*', '/']:
                for i in range(3):
                    text = text[:-1]
                self.lineEdit.clear()
                self.lineEdit.insert(text + ' - ')
            else:
                self.lineEdit.insert(' - ')

    def btnMul_clicked(self):
        text = self.lineEdit.text()
        if len(text) < 3:
            if len(text) == 0:
                self.error_message()
            else:
                self.lineEdit.insert(' * ')
        else:
            # 判断前方是否有符号，只要存在符号，则先去符号，再重新插入符号
            if text[-2] in ['+', '-', '*', '/']:
                for i in range(3):
                    text = text[:-1]
                self.lineEdit.clear()
                self.lineEdit.insert(text + ' * ')
            else:
                self.lineEdit.insert(' * ')

    def btnDiv_clicked(self):
        text = self.lineEdit.text()
        if len(text) < 3:
            if len(text) == 0:
                self.error_message()
            else:
                self.lineEdit.insert(' / ')
        else:
            # 判断前方是否有符号，只要存在符号，则先去符号，再重新插入符号
            if text[-2] in ['+', '-', '*', '/']:
                for i in range(3):
                    text = text[:-1]
                self.lineEdit.clear()
                self.lineEdit.insert(text + ' / ')
            else:
                self.lineEdit.insert(' / ')

    def btnDoc_clicked(self):
        text = self.lineEdit.text()
        if len(text) == 0:
            self.error_message()
        elif text[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.lineEdit.insert(".")
        else:
            self.error_message()

    def btnEqual_clicked(self):
        text = self.lineEdit.text()
        if len(text) == 0:
            return 0
        else:
            try:
                result = (eval(text))
                self.lineEdit.clear()
                self.lineEdit.insert(str(result))
                self.plainTextEdit.insertPlainText(text + ' = ' + str(result) + '\n')
            except Exception as e:
                print(e)
                self.error_message()

    def error_message(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()  # 获取主界面 初始坐标
        self.reply = QMessageBox(QMessageBox.Warning, "", "输入内容有误！！！")
        x = size.x()+int(size.width()/4)+35
        y = size.y()+int(size.height()/4)+27
        self.reply.move(x, y)  # 子界面移动到 居中
        self.reply.show()

    def btnBack_clicked(self):
        self.lineEdit.backspace()

    def btnReset_clicker(self):
        self.plainTextEdit.clear()

    def backTo(self):
        self.hide()
        self.window = Main_Interface.MainWindow()
        self.window.show()
        self.window.move(self.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CalculatorWindow()

    win.show()
    sys.exit(app.exec_())


