"""
创建人：孔健聪
创建时间：2022/08/14
"""
import Main_Interface
import sys
from allUI import Translate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from Common.debugtalk import translate_api


class TranslateWindow(Translate.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Translate.Ui_MainWindow, self).__init__()
        self.setupUi(self)   # 加载UI
        self.plainTextEdit_1.setPlaceholderText('请输入需要翻译的内容')
        self.tips_plainTextEdit.setPlaceholderText('温馨提示：\n\n'
                                                   '使用之前请确认网络环境良好\n\n'
                                                   '本翻译使用的是百度翻译，正所谓冤有头债有主......')
        self.pic_label.setPixmap(QPixmap(r'allUI/images/logo.png'))
        # 将各button进行点击连接（clicker）
        self.translate_Button.clicked.connect(self.translate)     # 翻译
        self.clear_Button.clicked.connect(self.clear)
        self.main_Button.clicked.connect(self.backTo)  # 跳转主页面

    def translate(self):
        index = []
        result = ''
        text_input = self.plainTextEdit_1.toPlainText()
        if len(text_input) > 0:
            # 根据输入的内容，若存在换行符，则切割分为数组存放
            content = str(text_input).split('\n')
            # 根据index长度，进行逐个翻译
            for i in range(len(content)):
                index.append(translate_api(content[i], 'auto'))
            for j in range(len(index)):
                result += index[j] + '\n'
            # 将翻译内容输出到plainText中
            self.plainTextEdit_2.setPlainText(result)
        else:
            self.error_message()

    def clear(self):
        self.plainTextEdit_1.clear()
        self.plainTextEdit_2.clear()

    def error_message(self):
        self.reply = QMessageBox(QMessageBox.Warning, "", "输入内容为空！！！")
        self.reply.show()

    def backTo(self):
        self.hide()
        self.window = Main_Interface.MainWindow()
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    window = TranslateWindow()
    window.show()  # 显示主窗体
    sys.exit(app.exec())

