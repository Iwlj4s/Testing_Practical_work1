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
from functions.calculation_functions import triangle_area_sides_angle


class Ui_area_triangle_l_two_sides_size_angle_beetween_sides_Window(object):
    def setupUi(self, area_triangle_l_two_sides_size_angle_beetween_sides_Window):
        if not area_triangle_l_two_sides_size_angle_beetween_sides_Window.objectName():
            area_triangle_l_two_sides_size_angle_beetween_sides_Window.setObjectName(u"area_triangle_l_two_sides_size_angle_beetween_sides_Window")
        area_triangle_l_two_sides_size_angle_beetween_sides_Window.setFixedSize(831, 470)

        self.centralwidget = QWidget(area_triangle_l_two_sides_size_angle_beetween_sides_Window)
        self.centralwidget.setObjectName(u"centralwidget")

        self.area_triangle_l_two_sides_size_angle_beetween_sides_label = QLabel(self.centralwidget)
        self.area_triangle_l_two_sides_size_angle_beetween_sides_label.setObjectName(u"area_triangle_l_two_sides_size_angle_beetween_sides_label")
        self.area_triangle_l_two_sides_size_angle_beetween_sides_label.setGeometry(QRect(10, 0, 791, 81))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(12)
        self.area_triangle_l_two_sides_size_angle_beetween_sides_label.setFont(font)

        # INPUT FRAME #
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(240, 170, 321, 198))

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
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.b_input.setFont(font2)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.b_input)

        self.a_input = QLineEdit(self.formLayoutWidget)
        self.a_input.setObjectName(u"a_input")
        self.a_input.setFont(font2)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.a_input)

        self.a_label = QLabel(self.formLayoutWidget)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.a_label)

        # RESULT BUTTON #
        self.area_triangle_l_two_sides_size_angle_beetween_sides_result_button = QPushButton(self.formLayoutWidget)
        self.area_triangle_l_two_sides_size_angle_beetween_sides_result_button.setObjectName(u"area_triangle_l_two_sides_size_angle_beetween_sides_result_button")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro Medium"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.area_triangle_l_two_sides_size_angle_beetween_sides_result_button.setFont(font3)
        self.area_triangle_l_two_sides_size_angle_beetween_sides_result_button.clicked.connect(self.get_result)

        self.input_frame.setWidget(4, QFormLayout.FieldRole, self.area_triangle_l_two_sides_size_angle_beetween_sides_result_button)

        self.angle_label = QLabel(self.formLayoutWidget)
        self.angle_label.setObjectName(u"angle_label")
        self.angle_label.setFont(font1)

        self.input_frame.setWidget(3, QFormLayout.LabelRole, self.angle_label)

        self.angle_input = QLineEdit(self.formLayoutWidget)
        self.angle_input.setObjectName(u"angle_input")
        self.angle_input.setFont(font2)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.angle_input)

        # RESULT FRAME #
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 370, 221, 91))

        self.result_frame = QFormLayout(self.formLayoutWidget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setContentsMargins(20, 10, 30, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro"])
        font4.setPointSize(16)
        self.label.setFont(font4)

        self.result_frame.setWidget(0, QFormLayout.LabelRole, self.label)

        self.result_text = QLineEdit(self.formLayoutWidget_2)
        self.result_text.setObjectName(u"result_text")

        self.result_frame.setWidget(1, QFormLayout.SpanningRole, self.result_text)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(270, 60, 271, 101))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula2.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        area_triangle_l_two_sides_size_angle_beetween_sides_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(area_triangle_l_two_sides_size_angle_beetween_sides_Window)

        QMetaObject.connectSlotsByName(area_triangle_l_two_sides_size_angle_beetween_sides_Window)

    # setupUi

    # Get result
    def get_result(self):
        a_text = self.a_input.text()
        b_text = self.b_input.text()
        angle_text = self.angle_input.text()

        enter_digit = user_enter_digit(a_text, b_text, angle_text)

        print(a_text)
        print(b_text)
        print(angle_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.a_input.setText(result)
            self.b_input.setText(result)
            self.angle_input.setText(result)
        else:
            result = triangle_area_sides_angle(side1=int(a_text), side2=int(b_text), angle=int(angle_text))
            print(result)
            self.result_text.setText(str(result))


    def retranslateUi(self, area_triangle_l_two_sides_size_angle_beetween_sides_Window):
        area_triangle_l_two_sides_size_angle_beetween_sides_Window.setWindowTitle(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"MainWindow", None))
        self.area_triangle_l_two_sides_size_angle_beetween_sides_label.setText(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0434\u043b\u0438\u043d\u044b \u0434\u0432\u0443\u0445 \u0435\u0433\u043e \u0441\u0442\u043e\u0440\u043e\u043d \u0438 \u0432\u0435\u043b\u0438\u0447\u0438\u043d\u0430 \u0443\u0433\u043b\u0430 \u043c\u0435\u0436\u0434\u0443 \u044d\u0442\u0438\u043c\u0438 \u0441\u0442\u043e\u0440\u043e\u043d\u0430\u043c\u0438.", None))
        self.b_label.setText(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"b", None))
        self.b_input.setText("")
        self.a_input.setText("")
        self.a_label.setText(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"a   ", None))
        self.area_triangle_l_two_sides_size_angle_beetween_sides_result_button.setText(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.angle_label.setText(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"angle   ", None))
        self.angle_input.setText("")
        self.label.setText(QCoreApplication.translate("area_triangle_l_two_sides_size_angle_beetween_sides_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.img.setText("")
    # retranslateUi

