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
from PyQt5.QtWebEngineWidgets import *


weibo_hots = []
zhihu_hots = []
CSDN_hots = []


class get_Weibo_Hots(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global weibo_hots
        result = weiBo_trendingTopic()
        # 判断当前获取的热搜list是否为空，为空则使用缓存内的list
        if len(result) > 0:
            weibo_hots.clear()
            weibo_hots = result
            print('获取微博热搜成功.....')
        elif len(result) == 0:
            print('检测到微博热搜返回为空，沿用旧list')
            pass
        self.sinout.emit(1)


class get_Zhihu_Hots(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global zhihu_hots
        result = zhiHu_trendingTopic()
        if len(result) > 0:
            zhihu_hots.clear()
            zhihu_hots = result
            print('获取知乎热搜成功.....')
        elif len(result) == 0:
            print('检测到知乎热搜返回为空，沿用旧list')
            pass
        self.sinout.emit(1)


class get_CSDN_Hots(QThread):
    sinout = pyqtSignal(int)  # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):
        global CSDN_hots
        result = CSDN_trendingTopic()
        if len(result) > 0:
            CSDN_hots.clear()
            CSDN_hots = result
            print('获取CSDN热搜成功.....')
        elif len(result) == 0:
            print('检测到CSDN热搜返回为空，沿用旧list')
            pass
        CSDN_hots = CSDN_trendingTopic()
        self.sinout.emit(1)


class HtmlView(QWebEngineView):
    """
    创建人：KinChung
    创建时间：2022/09/09
    内嵌浏览器模板
    """
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.tab = self.parent()

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = HtmlView(self.tab)
            ix = self.tab.addTab(webView, "New Tab")
            self.tab.setCurrentIndex(ix)
            return webView
        return QWebEngineView.createWindow(self, windowType)


class TrendingTopicWindow(trendingTopic.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(TrendingTopicWindow, self).__init__()
        self.setupUi(self)  # 加载UI
        self.tabWidget.tabBar().setTabButton(0, QtWidgets.QTabBar.LeftSide, None)   # 锁死tab1，只允许后续tab进行关闭
        # tabWidget加入信号槽，把所有Tab链接；
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
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
        # 信号槽相关
        self.main_Button.clicked.connect(self.backTo)
        self.pushButton.clicked.connect(self.weiboThread.start)
        self.pushButton_2.clicked.connect(self.zhihuThread.start)
        self.pushButton_3.clicked.connect(self.CSDNThread.start)

    def add_Weibo_Label(self):
        for i in range(len(weibo_hots)):
            this_label = getattr(self, 'labelWeibo_' + str(i+1))
            this_label.setText("<a style='text-decoration: none' href=\"" + weibo_hots[i][0] + "\">" + weibo_hots[i][1] + "</a>")
            this_label.clicked.connect(self.goWeb)
            this_label.setWordWrap(True)
            # print(this_label.text())

    def add_Zhihu_Label(self):
        for i in range(len(zhihu_hots)):
            this_label = getattr(self, 'labelZhihu_' + str(i + 1))
            this_label.setText("<a style='text-decoration: none' href=" + zhihu_hots[i][0] + ">" + zhihu_hots[i][1] + "</a>")
            this_label.clicked.connect(self.goWeb)
            this_label.setWordWrap(True)
            # print(this_label.text())

    def add_CSDN_Label(self):
        for i in range(len(CSDN_hots)):
            this_label = getattr(self, 'labelCSDN_' + str(i + 1))
            this_label.setText("<a style='text-decoration: none' href=" + CSDN_hots[i][0] + ">" + CSDN_hots[i][1] + "</a>")
            # this_label.setText(CSDN_hots[i][1])
            this_label.clicked.connect(self.goWeb)
            this_label.setWordWrap(True)

    def add_tab(self, url):
        appoint_url = QUrl(url)     # 设置跳转后指向的url
        view = HtmlView(self)
        view.load(appoint_url)  # 加载url
        self.tabWidget.addTab(view, "🔥")

    def close_tab(self, index):
        # tab(标签)关闭函数；
        self.tabWidget.removeTab(index)

    def backTo(self):
        self.hide()
        self.window = Main_Interface.MainWindow()
        self.window.show()
        self.window.move(self.pos())

    def goWeb(self, *arg, **kwargs):
        objectName = self.sender().objectName()
        label = objectName.split('_')
        if label[0] == 'labelWeibo':
            print('检测到所选热搜为微博......')
            i = int(label[1])
            label.append(weibo_hots[i-1][0])
            self.add_tab(label[2])
        elif label[0] == 'labelZhihu':
            print('检测到所选热搜为知乎......')
            i = int(label[1])
            label.append(zhihu_hots[i-1][0])
            self.add_tab(label[2])
        elif label[0] == 'labelCSDN':
            print('检测到所选热搜为CSDN......')
            i = int(label[1])
            label.append(CSDN_hots[i-1][0])
            self.add_tab(label[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    window = TrendingTopicWindow()
    window.show()  # 显示主窗体
    sys.exit(app.exec())
