"""
创建人：KinChung
创建时间：2022/08/14
"""
# coding=utf-8
import sys
import os
import images
import Main_Interface
import Common.rewrite
from allUI import Translate
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Common.debugtalk import translate_api, ocr_api

# 定义全局变量result（给线程赋值使用）
variable = {'trans_input': '',      # 翻译文本框内容
            'result_ocr': '',       # ocr提取结果
            'result_trans': '',     # 翻译接口返回结果
            'lang_trans': '',       # 翻译下拉框所选语言
            'lang_ocr': '',         # ocr下拉框所选语言
            'fileName_choose': ''   # ocr图片文件路径
            }


class Trans(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global variable
        index = []
        result = ''     # 字符串定义，保证每次获取的字符串都是全新的
        # 根据输入的内容，若存在换行符，则切割分为数组存放
        content = str(variable['trans_input']).split('\n')
        print(content)
        # 根据index长度，进行逐个翻译
        for i in range(len(content)):
            if content[i] is None:
                pass
            else:
                index.append(translate_api(content[i], variable['lang_trans']))
        for j in range(len(index)):
            if index[j] is None:
                pass
            else:
                result += index[j] + '\n'
                variable['result_trans'] = result
        print(variable['result_trans'])
        self.sinout.emit(1)


# 本地OCR类（暂时停用）
# class OCR(QThread):
#     sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号
#
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         global variable
#         result_list = local_ocr(variable['fileName_choose'], variable['lang_ocr'])
#         for i in range(len(result_list)):
#             variable['result_ocr'] += result_list[i] + '\n'
#         print(variable['result_ocr'])
#         self.sinout.emit(1)


# 百度OCR接口调用--本地文件
# class file_OCR(QThread):
#     sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号
#
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         global variable
#         result = ''
#         result_list = ocr_api('file', variable['fileName_choose'])
#         for i in range(len(result_list)):
#             result += result_list[i]['words'] + '\n'
#             variable['result_ocr'] = result
#         print(variable['result_ocr'])
#         self.sinout.emit(1)


# 百度OCR接口调用--图片文件/粘贴截图
class pic_OCR(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global variable
        result = ''
        result_list = ocr_api('base64', Common.rewrite.Pic_base64)
        for i in range(len(result_list)):
            result += result_list[i]['words'] + '\n'
            variable['result_ocr'] = result
        print(variable['result_ocr'])
        self.sinout.emit(1)


class TranslateWindow(Translate.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Translate.Ui_MainWindow, self).__init__()
        self.setupUi(self)   # 加载UI
        self.plainTextEdit.setPlaceholderText('请输入需要翻译的内容')
        self.tips_textEdit.setPlaceholderText('温馨提示：\n\n'
                                                   '使用之前请确认网络环境良好\n\n'
                                                   '本工具使用的是百度翻译及百度OCR识别，正所谓冤有头债有主......')
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.textEdit_2.setPlaceholderText('支持拖拽图片文件&粘贴图片\n\nTips:尽量避免直接粘贴图片文件')
        # 设置翻译内的Combobox列表
        items_trans = ['中文简体', '中文繁体', '英文', '日文', '韩文']
        self.comboBox_1.addItems(items_trans)
        self.comboBox_1.setCurrentIndex(-1)  # 设置当前下拉框为空
        # 设置OCR内的Combobox列表
        items_ocr = ['中文', '英文', '法语', '德语', '韩文', '日文']
        self.comboBox_ocr.addItems(items_ocr)
        self.comboBox_ocr.setCurrentIndex(0)  # 设置当前下拉框默认选项为中文
        # 将各button进行点击连接（clicker）
        self.upload_Button.clicked.connect(self.upload_Ocr)
        self.translate_Button.clicked.connect(self.useTrans)     # 翻译
        self.clear_Button.clicked.connect(self.clear)
        self.main_Button.clicked.connect(self.backTo)  # 跳转主页面
        # 线程相关
        self.pic_ocrThread = pic_OCR()
        self.pic_ocrThread.sinout.connect(self.showOcr)  # 将showOcr与槽函数相连
        self.transThread = Trans()
        self.transThread.sinout.connect(self.showTrans)  # 将showTrans与槽函数相连

    # """
    # 创建人：KinChung
    # 创建时间：2022/08/23
    # """
    # def useOcr(self):
    #     global variable
    #     language_type = {'中文': 'ch', '英文': 'en',
    #                      '法语': 'fr', '德语': 'german',
    #                      '韩文': 'korean', '日文': 'japan'}
    #     variable['lang_ocr'] = language_type[self.comboBox_ocr.currentText()]
    #     variable['fileName_choose'], filetype = QFileDialog.getOpenFileName(self,
    #                                                             "选取文件",
    #                                                             self.cwd,  # 起始路径
    #                                                             "Picture Files (*.jpg *.png *.jpeg);;"
    #                                                             "All Files (*)")  # 设置文件扩展名过滤,用双分号间隔
    #     if variable['fileName_choose'] == "":
    #         print("\n取消选择")
    #         return
    #     else:
    #         print(variable['fileName_choose'])
    #         self.ocr_textEdit.setText('生成中......')
    #         self.file_ocrThread.start()

    def useTrans(self):
        global variable
        language_type = {'中文简体': 'zh',
                         '中文繁体': 'cht',
                         '英文': 'en',
                         '日文': 'jp',
                         '韩文': 'kor'}
        variable['trans_input'] = self.plainTextEdit.toPlainText().strip('\n')
        print("捕获到输入文本内容为：\n", variable['trans_input'])
        if len(variable['trans_input']) > 0 and len(self.comboBox_1.currentText()) > 0:
            variable['lang_trans'] = language_type[self.comboBox_1.currentText()]
            # 如果检测到文本内字符大于0，则开启线程
            self.transThread.start()
        else:
            self.error_message()

    def showOcr(self):
        if variable['result_ocr'] is None:
            self.ocr_textEdit.setText('返回内容为空，请确认网络环境或文本框内容')
        else:
            self.ocr_textEdit.setText(variable['result_ocr'])

    def showTrans(self):
        self.plainTextEdit_2.clear()    # 先清空输出文本框，再显示结果
        self.plainTextEdit_2.setPlainText(variable['result_trans'])

    def clear(self):
        self.plainTextEdit_2.clear()

    def error_message(self):
        self.reply = QMessageBox(QMessageBox.Warning, "", "输入内容为空！！！")
        self.reply.show()

    def backTo(self):
        self.hide()
        self.window = Main_Interface.MainWindow()
        self.window.show()
        self.window.move(self.pos())

    def upload_Ocr(self):
        self.ocr_textEdit.setText('生成中......')
        self.pic_ocrThread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    window = TranslateWindow()
    window.show()  # 显示主窗体
    sys.exit(app.exec())

