"""
创建人：KinChung
创建时间：2022/08/11
"""
import sys
import Translate
import Calculator
import Translate_custom
import Trending_topic
import images
from allUI import Main_Interface
from Common.debugtalk import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QDateTime


class MainWindow(Main_Interface.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)   # 加载UI
        # 设置Combobox内列表
        items = ['香洲', '蓬江', '端州', '宝安']
        self.City_comboBox.addItems(items)
        self.City_comboBox.setCurrentIndex(-1)  # 设置当前下拉框为空
        # 将button绑定触发事件
        self.pushButton_1.clicked.connect(self.go_translate)
        self.pushButton_2.clicked.connect(self.go_calculator)
        self.pushButton_3.clicked.connect(self.go_Hots)
        self.pushButton_10.clicked.connect(self.go_translate_custom)
        # 捕获下拉索引的改变，绑定触发事件
        self.City_comboBox.currentIndexChanged.connect(self.selection_change)

        self.Timer = QTimer()  # 自定义QTimer类
        self.Timer.start(500)  # 每0.5s运行一次
        self.Timer.timeout.connect(self.update_time)  # 与updateTime函数连接

        self.Timer2 = QTimer()  # 自定义QTimer类
        self.Timer2.start(3600000)  # 每1小时更新一次
        self.Timer2.timeout.connect(self.selection_change)  # 与updateTime函数连接

    def update_time(self):
        time = QDateTime.currentDateTime()  # 获取现在的时间
        timePlay = time.toString('hh:mm:ss')  # 设置显示时间的格式
        datePlay = time.toString('yyyy-MM-dd')  # 设置显示日期的格式
        weekPlay = time.toString('dddd')    # 设置周几
        self.label_time.setText(timePlay)
        self.label_date.setText(datePlay)
        self.plainTextEdit.setPlainText("各位打工人%s好！\n"
                                                 "今日摸鱼宣言： 偶尔摸鱼有害健康,常常摸鱼收获满满。\n\n"
                                                 "%s" % (momofish_week(weekPlay), momofish_declaration()))

    def selection_change(self):
        global local_city
        local_city = self.City_comboBox.currentText()   # currentText()：返回选中选项的文本
        wea = get_weather(local_city)
        self.update_weather(wea)

    def update_weather(self, wea):
        """ 更新天气显示 """
        self.label_day_wea.setText('白天')
        self.label_day_wea_pic.setPixmap(QPixmap(self.get_images('day_' + wea['day_wea'])))
        self.label_day_tem.setText('%s %s℃' % (wea['day_wea'], wea['day_tem']))

        self.label_night_wea.setText('夜间')
        self.label_night_wea_pic.setPixmap(QPixmap(self.get_images('night_' + wea['night_wea'])))
        self.label_night_tem.setText('%s %s℃' % (wea['night_wea'], wea['night_tem']))

    def get_images(self, wea_str):
        imags = {"day_小雨": ':/allUI/images/day_light_rain.png', "night_小雨": ':/allUI/images/night_light_rain.png',
                 "day_中雨": ':/allUI/images/day_moderate_rain.png', "night_中雨": ':/allUI/images/night_moderate_rain.png',
                 "day_大雨": ':/allUI/images/day_heavy_rain.png', "night_大雨": ':/allUI/images/night_heavy_rain.png',
                 "day_暴雨": ':/allUI/images/day_rainstorm.png', "night_暴雨": ':/allUI/images/night_rainstorm.png',
                 "day_暴雨到大暴雨": ':/allUI/images/day_rainstorm2downpour.png',
                 "night_暴雨到大暴雨": ':/allUI/images/night_rainstorm2downpour.png',
                 "day_阵雨": ':/allUI/images/day_shower.png', "night_阵雨": ':/allUI/images/night_shower.png',
                 "day_多云": ':/allUI/images/day_cloudy.png', "night_多云": ':/allUI/images/night_cloudy.png',
                 "day_晴": ':/allUI/images/day_sunny.png', "night_晴": ':/allUI/images/night_sunny.png',
                 "day_雷阵雨": ':/allUI/images/day_Thunder_shower.png', "night_雷阵雨": ':/allUI/images/night_Thunder_shower.png'
                 }
        return imags[wea_str]

    def go_translate(self):
        self.hide()
        self.T_win = Translate.TranslateWindow()    # 实例化另外一个窗口
        self.T_win.show()   # 显示新窗口

    def go_calculator(self):
        self.hide()
        self.C_win = Calculator.CalculatorWindow()  # 实例化另外一个窗口
        self.C_win.show()  # 显示新窗口

    def go_translate_custom(self):
        self.hide()
        self.H_win = Translate_custom.CustomWindow()  # 实例化另外一个窗口
        self.H_win.show()  # 显示新窗口

    def go_Hots(self):
        self.hide()
        self.H_win = Trending_topic.TrendingTopicWindow()  # 实例化另外一个窗口
        self.H_win.show()  # 显示新窗口

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    window = MainWindow()
    window.show()  # 显示主窗体
    sys.exit(app.exec())
