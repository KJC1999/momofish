from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QImageReader, QTextDocumentFragment
from Common.debugtalk import compare_big

Pic_base64 = ''


class TextEdit(QTextEdit):
    """
    创建人：KinChung
    创建时间：2022/10/18
    目的：重写QTextEdit
    """
    def __init__(self):
        super(TextEdit, self).__init__()

    def canInsertFromMimeData(self, source: QtCore.QMimeData) -> bool:
        return source.hasImage() or source.hasUrls() or \
               super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source: QtCore.QMimeData) -> None:
        if source.hasImage():
            self.insert_image(source.imageData())
        elif source.hasUrls():
            for url in source.urls():
                file_info = QFileInfo(url.toLocalFile())
                ext = file_info.suffix().lower()
                if ext in QImageReader.supportedImageFormats():
                    self.insert_image(QImage(file_info.filePath()), ext)
                else:
                    self.insert_file(url)
        else:
            super(TextEdit, self).insertFromMimeData(source)

    def insert_image(self, image: QImage, fmt: str = "png"):
        """插入图片"""
        global Pic_base64
        data = QByteArray()
        buffer = QBuffer(data)
        image.save(buffer, fmt)
        # 记录图片的长和宽
        pic_width = image.width()
        pic_height = image.height()
        # 记录文本框的长和宽
        edit_width = self.width()
        edit_height = self.height()
        base64_data = str(data.toBase64())[2:-1]
        Pic_base64 = base64_data    # 全局变量记录插入的变量base64
        # 比较图片与当前文本框的长度，再进行等比例缩放图片
        if pic_width > edit_width and pic_height > edit_height:
            if compare_big(pic_width/edit_width, pic_height/edit_height) is False:
                cal_width = edit_width
                cal_height = int(pic_height * edit_width / pic_width)
            else:
                cal_width = int(pic_width * edit_height / pic_height)
                cal_height = edit_height
        elif pic_width > edit_width or pic_height > edit_height:
            if pic_width > edit_width:
                cal_width = edit_width
                cal_height = int(pic_height * edit_width / pic_width)
            else:
                cal_width = int(pic_width * edit_height / pic_height)
                cal_height = edit_height
        elif pic_width < edit_width and pic_height < edit_height:
            cal_width = pic_width
            cal_height = pic_height
        data = f'<img src="data:image/{fmt};base64,{base64_data}" width="{cal_width}" height="{cal_height}"/>'
        fragment = QTextDocumentFragment.fromHtml(data)
        self.textCursor().insertFragment(fragment)

    def insert_file(self, url: QUrl):
        """插入文件"""
        file = None
        # noinspection PyBroadException
        try:
            file = QFile(url.toLocalFile())
            if not file.open(QIODevice.ReadOnly or QIODevice.Text):
                return
            file_data = file.readAll()
            # noinspection PyBroadException
            try:
                self.textCursor().insertHtml(str(file_data, encoding="utf8"))
            except Exception:
                self.textCursor().insertHtml(str(file_data))
        except Exception:
            if file:
                file.close()

