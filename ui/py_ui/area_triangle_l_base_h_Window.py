from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)

from functions.calculation_functions import triangle_area_base_height
from checks.input_check import user_enter_digit


class Ui_area_triangle_l_base_h_Window(object):
    def setupUi(self, area_triangle_l_base_h_Window):
        if not area_triangle_l_base_h_Window.objectName():
            area_triangle_l_base_h_Window.setObjectName(u"area_triangle_l_base_h_Window")
        area_triangle_l_base_h_Window.setFixedSize(817, 460)
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(14)
        area_triangle_l_base_h_Window.setFont(font)
        self.centralwidget = QWidget(area_triangle_l_base_h_Window)
        self.centralwidget.setObjectName(u"centralwidget")

        self.area_triangle_l_base_h_label = QLabel(self.centralwidget)
        self.area_triangle_l_base_h_label.setObjectName(u"area_triangle_l_base_h_label")
        self.area_triangle_l_base_h_label.setGeometry(QRect(20, 0, 791, 81))
        self.area_triangle_l_base_h_label.setFont(font)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(330, 60, 151, 71))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/1.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(250, 140, 321, 171))

        # INPUT FRAME #
        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)

        self.b_label = QLabel(self.formLayoutWidget)
        self.b_label.setObjectName(u"b_label")

        font1 = QFont()
        font1.setFamilies([u"Source Code Pro Medium"])
        font1.setPointSize(20)
        font1.setItalic(True)
        self.b_label.setFont(font1)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.b_label)

        self.b_input = QLineEdit(self.formLayoutWidget)
        self.b_input.setObjectName(u"b_input")
        self.b_input.setFont(font)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.b_input)

        self.a_input = QLineEdit(self.formLayoutWidget)
        self.a_input.setObjectName(u"a_input")
        self.a_input.setFont(font)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.a_input)

        self.a_label = QLabel(self.formLayoutWidget)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.a_label)

        # RESULT BUTTON #
        self.pushButtonarea_triangle_l_base_h_result_button = QPushButton(self.formLayoutWidget)
        self.pushButtonarea_triangle_l_base_h_result_button.setObjectName(
            u"pushButtonarea_triangle_l_base_h_result_button")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.pushButtonarea_triangle_l_base_h_result_button.setFont(font2)

        self.pushButtonarea_triangle_l_base_h_result_button.clicked.connect(self.get_result)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.pushButtonarea_triangle_l_base_h_result_button)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 370, 321, 141))

        # RESULT FRAME #
        self.result_frame = QFormLayout(self.formLayoutWidget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setContentsMargins(20, 10, 30, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(16)
        self.label.setFont(font3)

        self.result_frame.setWidget(0, QFormLayout.LabelRole, self.label)

        self.result_text = QLineEdit(self.formLayoutWidget_2)
        self.result_text.setObjectName(u"result_text")

        self.result_frame.setWidget(1, QFormLayout.LabelRole, self.result_text)

        area_triangle_l_base_h_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(area_triangle_l_base_h_Window)

        QMetaObject.connectSlotsByName(area_triangle_l_base_h_Window)

    # setupUi

    # Get result
    def get_result(self):
        a_text = self.a_input.text()

        b_text = self.b_input.text()

        enter_digit = user_enter_digit(a_text, b_text)

        print(a_text)
        print(b_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.a_input.setText(result)
            self.b_input.setText(result)
        else:
            result = triangle_area_base_height(base=int(a_text), height=int(b_text))
            print(result)
            self.result_text.setText(str(result))

    def retranslateUi(self, area_triangle_l_base_h_Window):
        area_triangle_l_base_h_Window.setWindowTitle(
            QCoreApplication.translate("area_triangle_l_base_h_Window", u"MainWindow", None))
        self.area_triangle_l_base_h_label.setText(QCoreApplication.translate("area_triangle_l_base_h_Window",
                                                                             u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430 \u0434\u043b\u0438\u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u0432\u044b\u0441\u043e\u0442\u0430.",
                                                                             None))
        self.img.setText("")
        self.b_label.setText(QCoreApplication.translate("area_triangle_l_base_h_Window", u"b", None))
        self.b_input.setText("")
        self.a_input.setText("")
        self.a_label.setText(QCoreApplication.translate("area_triangle_l_base_h_Window", u"a   ", None))
        self.pushButtonarea_triangle_l_base_h_result_button.setText(
            QCoreApplication.translate("area_triangle_l_base_h_Window",
                                       u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("area_triangle_l_base_h_Window",
                                                      u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
    # retranslateUi
