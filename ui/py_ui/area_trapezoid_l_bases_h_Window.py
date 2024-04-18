from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)

from checks.input_check import user_enter_digit
from functions.calculation_functions import trapezoid_area


class Ui_area_trapezoid_l_bases_h_Window(object):
    def setupUi(self, area_trapezoid_l_bases_h_Window):
        if not area_trapezoid_l_bases_h_Window.objectName():
            area_trapezoid_l_bases_h_Window.setObjectName(u"area_trapezoid_l_bases_h_Window")
        area_trapezoid_l_bases_h_Window.resize(813, 498)

        self.centralwidget = QWidget(area_trapezoid_l_bases_h_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.area_trapezoid_l_bases_h_label = QLabel(self.centralwidget)
        self.area_trapezoid_l_bases_h_label.setObjectName(u"area_trapezoid_l_bases_h_label")
        self.area_trapezoid_l_bases_h_label.setGeometry(QRect(10, 0, 781, 61))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)
        self.area_trapezoid_l_bases_h_label.setFont(font)
        self.area_trapezoid_l_bases_h_label.setWordWrap(True)

        # RESULT FRAME #
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 390, 221, 91))

        self.result_frame_2 = QFormLayout(self.formLayoutWidget_2)
        self.result_frame_2.setObjectName(u"result_frame_2")
        self.result_frame_2.setContentsMargins(20, 10, 30, 0)
        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.result_frame_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.result_text_2 = QLineEdit(self.formLayoutWidget_2)
        self.result_text_2.setObjectName(u"result_text_2")

        self.result_frame_2.setWidget(1, QFormLayout.SpanningRole, self.result_text_2)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(330, 40, 221, 91))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula8.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # INPUT FRAME #
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(270, 150, 321, 221))

        self.input_frame_2 = QFormLayout(self.formLayoutWidget)
        self.input_frame_2.setObjectName(u"input_frame_2")
        self.input_frame_2.setContentsMargins(20, 20, 30, 20)

        self.a_input = QLineEdit(self.formLayoutWidget)
        self.a_input.setObjectName(u"a_input")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.a_input.setFont(font1)

        self.input_frame_2.setWidget(0, QFormLayout.FieldRole, self.a_input)

        self.a_label = QLabel(self.formLayoutWidget)
        self.a_label.setObjectName(u"a_label")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(20)
        font2.setItalic(True)
        self.a_label.setFont(font2)

        self.input_frame_2.setWidget(0, QFormLayout.LabelRole, self.a_label)

        self.b_label = QLabel(self.formLayoutWidget)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setFont(font2)

        self.input_frame_2.setWidget(1, QFormLayout.LabelRole, self.b_label)

        self.b_input = QLineEdit(self.formLayoutWidget)
        self.b_input.setObjectName(u"b_input")
        self.b_input.setFont(font1)

        self.input_frame_2.setWidget(1, QFormLayout.FieldRole, self.b_input)

        self.h_label = QLabel(self.formLayoutWidget)
        self.h_label.setObjectName(u"h_label")
        self.h_label.setFont(font2)

        self.input_frame_2.setWidget(2, QFormLayout.LabelRole, self.h_label)

        self.h_input = QLineEdit(self.formLayoutWidget)
        self.h_input.setObjectName(u"h_input")
        self.h_input.setFont(font1)

        self.input_frame_2.setWidget(2, QFormLayout.FieldRole, self.h_input)

        # Result Button #
        self.area_trapezoid_l_bases_h_result_button = QPushButton(self.formLayoutWidget)
        self.area_trapezoid_l_bases_h_result_button.setObjectName(u"area_trapezoid_l_bases_h_result_button")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro Medium"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.area_trapezoid_l_bases_h_result_button.setFont(font3)

        self.area_trapezoid_l_bases_h_result_button.clicked.connect(self.get_result)

        self.input_frame_2.setWidget(3, QFormLayout.FieldRole, self.area_trapezoid_l_bases_h_result_button)

        area_trapezoid_l_bases_h_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(area_trapezoid_l_bases_h_Window)

        QMetaObject.connectSlotsByName(area_trapezoid_l_bases_h_Window)

    # setupUi

    # Get result
    def get_result(self):
        a_text = self.a_input.text()
        b_text = self.b_input.text()
        h_text = self.h_input.text()

        enter_digit = user_enter_digit(a_text, b_text, h_text)

        print(a_text)
        print(b_text)
        print(h_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.a_input.setText(result)
            self.b_input.setText(result)
            self.h_input.setText(result)
        else:
            result = trapezoid_area(base1=int(a_text), base2=int(b_text), height=int(h_text))
            print(result)
            self.result_text_2.setText(str(result))

    def retranslateUi(self, area_trapezoid_l_bases_h_Window):
        area_trapezoid_l_bases_h_Window.setWindowTitle(
            QCoreApplication.translate("area_trapezoid_l_bases_h_Window", u"MainWindow", None))
        self.area_trapezoid_l_bases_h_label.setText(QCoreApplication.translate("area_trapezoid_l_bases_h_Window",
                                                                               u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0434\u043b\u0438\u043d\u044b \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0439 \u0438 \u0432\u044b\u0441\u043e\u0442\u0430.",
                                                                               None))
        self.label_2.setText(QCoreApplication.translate("area_trapezoid_l_bases_h_Window",
                                                        u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442",
                                                        None))
        self.result_text_2.setText("")
        self.img.setText("")
        self.a_input.setText("")
        self.a_label.setText(QCoreApplication.translate("area_trapezoid_l_bases_h_Window", u"a   ", None))
        self.b_label.setText(QCoreApplication.translate("area_trapezoid_l_bases_h_Window", u"b   ", None))
        self.b_input.setText("")
        self.h_label.setText(QCoreApplication.translate("area_trapezoid_l_bases_h_Window", u"h", None))
        self.h_input.setText("")
        self.area_trapezoid_l_bases_h_result_button.setText(
            QCoreApplication.translate("area_trapezoid_l_bases_h_Window",
                                       u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
    # retranslateUi
