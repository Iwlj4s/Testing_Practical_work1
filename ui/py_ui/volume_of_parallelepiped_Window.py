from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)


class Ui_volume_of_parallelepiped_Window(object):
    def setupUi(self, volume_of_parallelepiped_Window):
        if not volume_of_parallelepiped_Window.objectName():
            volume_of_parallelepiped_Window.setObjectName(u"volume_of_parallelepiped_Window")
        volume_of_parallelepiped_Window.resize(800, 486)
        self.centralwidget = QWidget(volume_of_parallelepiped_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 390, 221, 91))
        self.result_frame = QFormLayout(self.formLayoutWidget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setContentsMargins(20, 10, 30, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.result_frame.setWidget(0, QFormLayout.LabelRole, self.label)

        self.result_text = QLineEdit(self.formLayoutWidget_2)
        self.result_text.setObjectName(u"result_text")

        self.result_frame.setWidget(1, QFormLayout.SpanningRole, self.result_text)

        self.volume_of_parallelepiped_abel = QLabel(self.centralwidget)
        self.volume_of_parallelepiped_abel.setObjectName(u"volume_of_parallelepiped_abel")
        self.volume_of_parallelepiped_abel.setGeometry(QRect(10, 0, 781, 61))
        self.volume_of_parallelepiped_abel.setFont(font)
        self.volume_of_parallelepiped_abel.setWordWrap(True)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(280, 120, 321, 221))
        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)
        self.a_input = QLineEdit(self.formLayoutWidget)
        self.a_input.setObjectName(u"a_input")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.a_input.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.a_input)

        self.a_label = QLabel(self.formLayoutWidget)
        self.a_label.setObjectName(u"a_label")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(20)
        font2.setItalic(True)
        self.a_label.setFont(font2)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.a_label)

        self.b_label = QLabel(self.formLayoutWidget)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setFont(font2)

        self.input_frame.setWidget(1, QFormLayout.LabelRole, self.b_label)

        self.b_input = QLineEdit(self.formLayoutWidget)
        self.b_input.setObjectName(u"b_input")
        self.b_input.setFont(font1)

        self.input_frame.setWidget(1, QFormLayout.FieldRole, self.b_input)

        self.c_label = QLabel(self.formLayoutWidget)
        self.c_label.setObjectName(u"c_label")
        self.c_label.setFont(font2)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.c_label)

        self.c_input = QLineEdit(self.formLayoutWidget)
        self.c_input.setObjectName(u"c_input")
        self.c_input.setFont(font1)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.c_input)

        self.volume_of_parallelepiped_result_button = QPushButton(self.formLayoutWidget)
        self.volume_of_parallelepiped_result_button.setObjectName(u"volume_of_parallelepiped_result_button")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro Medium"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.volume_of_parallelepiped_result_button.setFont(font3)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.volume_of_parallelepiped_result_button)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(330, 40, 221, 91))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula11.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        volume_of_parallelepiped_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(volume_of_parallelepiped_Window)

        QMetaObject.connectSlotsByName(volume_of_parallelepiped_Window)
    # setupUi

    def retranslateUi(self, volume_of_parallelepiped_Window):
        volume_of_parallelepiped_Window.setWindowTitle(QCoreApplication.translate("volume_of_parallelepiped_Window", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("volume_of_parallelepiped_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.volume_of_parallelepiped_abel.setText(QCoreApplication.translate("volume_of_parallelepiped_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043c\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u0435\u043f\u0438\u043f\u0435\u0434\u0430 \u043f\u043e \u0442\u0440\u0435\u043c \u0435\u0433\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\u043c", None))
        self.a_input.setText("")
        self.a_label.setText(QCoreApplication.translate("volume_of_parallelepiped_Window", u"a   ", None))
        self.b_label.setText(QCoreApplication.translate("volume_of_parallelepiped_Window", u"b   ", None))
        self.b_input.setText("")
        self.c_label.setText(QCoreApplication.translate("volume_of_parallelepiped_Window", u"c", None))
        self.c_input.setText("")
        self.volume_of_parallelepiped_result_button.setText(QCoreApplication.translate("volume_of_parallelepiped_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.img.setText("")
    # retranslateUi

