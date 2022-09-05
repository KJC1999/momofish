"""
创建人：KinChung
创建时间：2022/08/24
"""
import sys
import Main_Interface
import images
from allUI import trendingTopic
from Common.debugtalk import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


weibo_hots = []
zhihu_hots = []
CSDN_hots = []


class myLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()


class get_Weibo_Hots(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global weibo_hots
        weibo_hots = weiBo_trendingTopic()
        self.sinout.emit(1)


class get_Zhihu_Hots(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global zhihu_hots
        zhihu_hots = zhiHu_trendingTopic()
        self.sinout.emit(1)


class get_CSDN_Hots(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global CSDN_hots
        CSDN_hots = CSDN_trendingTopic()
        self.sinout.emit(1)


class TrendingTopicWindow(trendingTopic.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(TrendingTopicWindow, self).__init__()
        self.setupUi(self)  # 加载UI
        self.tabWidget.tabBar().setTabButton(0, QtWidgets.QTabBar.LeftSide, None)   # 锁死tab1，只允许后续tab进行关闭
        # tabWidget加入信号槽，把所有Tab链接；
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        # 信号槽相关
        self.main_Button.clicked.connect(self.backTo)
        # 线程相关
        self.weiboThread = get_Weibo_Hots()
        self.weiboThread.sinout.connect(self.add_Weibo_Label)  # 将showOcr与槽函数相连
        self.weiboThread.start()
        self.zhihuThread = get_Zhihu_Hots()
        self.zhihuThread.sinout.connect(self.add_Zhihu_Label)  # 将showTrans与槽函数相连
        self.zhihuThread.start()
        self.CSDNThread = get_CSDN_Hots()
        self.CSDNThread.sinout.connect(self.add_CSDN_Label)  # 将showTrans与槽函数相连
        self.CSDNThread.start()

    def add_Weibo_Label(self):
        for i in range(len(weibo_hots)):
            this_label = getattr(self, 'labelWeibo_' + str(i+1))
            this_label.setText("<a href=" + weibo_hots[i][0] + ">" + weibo_hots[i][1] + "</a>")
            # this_label.setText(weibo_hots[i][1])
            # 赋予超链接配置
            this_label.setOpenExternalLinks(True)
            # this_label.linkActivated.connect(self.aaa)
            this_label.setWordWrap(True)
            # print(this_label.text())
        # 分配之后清除列表，后续考虑不清除列表（若接口获取失败，保留上次数据输出）
        weibo_hots.clear()

        # 测试下重写后的效果
        # self.labelWeibo_1 = myLabel()
        # self.labelWeibo_1.setText('这是一个文本标签')
        # print(self.labelWeibo_1.text())
        # print('set success')
        # self.labelWeibo_1.linkActivated.connect(self.aaa)
        # self.labelWeibo_1.setWordWrap(True)

    def add_Zhihu_Label(self):
        for i in range(len(zhihu_hots)):
            this_label = getattr(self, 'labelZhihu_' + str(i + 1))
            this_label.setText("<a href=" + zhihu_hots[i][0] + ">" + zhihu_hots[i][1] + "</a>")
            this_label.setOpenExternalLinks(True)
            this_label.setWordWrap(True)
            # print(this_label.text())
        # 分配之后清除列表，后续考虑不清除列表（若接口获取失败，保留上次数据输出）
        zhihu_hots.clear()

    def add_CSDN_Label(self):
        for i in range(len(CSDN_hots)):
            this_label = getattr(self, 'labelCSDN_' + str(i + 1))
            # 将label设置为超链接
            this_label.setText("<a href=" + CSDN_hots[i][0] + ">" + CSDN_hots[i][1] + "</a>")
            this_label.setOpenExternalLinks(True)
            this_label.setWordWrap(True)
        # 分配之后清除列表，后续考虑不清除列表（若接口获取失败，保留上次数据输出）
        CSDN_hots.clear()

    def add_tab(self):
        # tab(标签)新增函数；
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "你好")
        # self.tabWidget.setTabsClosable(True)

    def close_tab(self, index):
        # tab(标签)关闭函数；
        self.tabWidget.removeTab(index)

    def backTo(self):
        self.hide()
        self.window = Main_Interface.MainWindow()
        self.window.show()

    def aaa(self):
        print('kjckjckjc')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    window = TrendingTopicWindow()
    window.show()  # 显示主窗体
    sys.exit(app.exec())
