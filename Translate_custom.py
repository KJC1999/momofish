"""
创建人：孔健聪
创建时间：2022/08/20
"""
import sys
import Main_Interface
from allUI import Translate_custom
from PyQt5.QtWidgets import *
from Common.debugtalk import translate_api_custom, translate_custom, translate_api


class CustomWindow(Translate_custom.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Translate_custom.Ui_MainWindow, self).__init__()
        self.setupUi(self)   # 加载UI
        # 设置Combobox内列表
        items = ['中文简体', '中文繁体', '英文', '日文', '韩文']
        self.Lang_comboBox.addItems(items)
        self.Lang_comboBox.setCurrentIndex(-1)  # 设置当前下拉框为空
        # 将各button进行点击连接（clicker）
        self.translate_Button_2.clicked.connect(self.translate_custom)  # 定制化翻译
        self.translate_Button.clicked.connect(self.translate)     # 翻译
        self.clear_Button_2.clicked.connect(self.clear2)
        self.clear_Button.clicked.connect(self.clear1)
        self.main_Button.clicked.connect(self.backTo)  # 跳转主页面

    def translate_custom(self):
        # 获取上方左侧定制化窗口内文本（获取到的为str）
        input = self.plainTextEdit_3.toPlainText().replace('\n', '').replace(' ', '')
        language = self.City_comboBox.currentText()
        if len(input) > 0 and len(language) > 0:
            # 将翻译内容输出到plainText中
            self.plainTextEdit_4.setPlainText(translate_custom(input, language))
        else:
            self.error_message()

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

    def error_message(self):
        self.reply = QMessageBox(QMessageBox.Warning, "", "输入内容或选项为空！！！")
        self.reply.show()

    def backTo(self):
        self.hide()
        self.window = Main_Interface.MainWindow()
        self.window.show()

    def clear1(self):
        self.plainTextEdit_1.clear()
        self.plainTextEdit_2.clear()

    def clear2(self):
        self.plainTextEdit_3.clear()
        self.plainTextEdit_4.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    window = CustomWindow()
    window.show()  # 显示主窗体
    sys.exit(app.exec())
