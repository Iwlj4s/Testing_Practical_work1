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
from functions.calculation_functions import current_voltage_resistance


class Ui_current_strength_electronic_circuit_Window(object):
    def setupUi(self, current_strength_electronic_circuit_Window):
        if not current_strength_electronic_circuit_Window.objectName():
            current_strength_electronic_circuit_Window.setObjectName(u"current_strength_electronic_circuit_Window")
        current_strength_electronic_circuit_Window.setFixedSize(800, 484)

        self.centralwidget = QWidget(current_strength_electronic_circuit_Window)
        self.centralwidget.setObjectName(u"centralwidget")

        # RESULT FRAME #
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

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(320, 50, 221, 91))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula5.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # INPUT FRAME #
        self.current_strength_electronic_circuit_label = QLabel(self.centralwidget)
        self.current_strength_electronic_circuit_label.setObjectName(u"current_strength_electronic_circuit_label")
        self.current_strength_electronic_circuit_label.setGeometry(QRect(140, 0, 551, 61))
        self.current_strength_electronic_circuit_label.setFont(font)
        self.current_strength_electronic_circuit_label.setWordWrap(True)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(270, 210, 321, 161))

        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)

        self.R_label = QLabel(self.formLayoutWidget)
        self.R_label.setObjectName(u"R_label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro Medium"])
        font1.setPointSize(20)
        font1.setItalic(True)
        self.R_label.setFont(font1)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.R_label)

        # RESULT BUTTON #
        self.current_strength_electronic_circuit_result_button = QPushButton(self.formLayoutWidget)
        self.current_strength_electronic_circuit_result_button.setObjectName(u"current_strength_electronic_circuit_result_button")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.current_strength_electronic_circuit_result_button.setFont(font2)

        self.current_strength_electronic_circuit_result_button.clicked.connect(self.get_result)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.current_strength_electronic_circuit_result_button)

        self.U_input = QLineEdit(self.formLayoutWidget)
        self.U_input.setObjectName(u"U_input")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.U_input.setFont(font3)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.U_input)

        self.U_label = QLabel(self.formLayoutWidget)
        self.U_label.setObjectName(u"U_label")
        self.U_label.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.U_label)

        self.R_input = QLineEdit(self.formLayoutWidget)
        self.R_input.setObjectName(u"R_input")
        self.R_input.setFont(font3)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.R_input)

        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(260, 150, 381, 41))
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro"])
        font4.setPointSize(14)
        self.info_label.setFont(font4)
        current_strength_electronic_circuit_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(current_strength_electronic_circuit_Window)

        QMetaObject.connectSlotsByName(current_strength_electronic_circuit_Window)
    # setupUi

    # Get result
    def get_result(self):
        u_text = self.U_input.text()
        r_text = self.R_input.text()

        enter_digit = user_enter_digit(u_text, r_text)

        print(u_text)
        print(r_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.U_input.setText(result)
            self.R_input.setText(result)
        else:
            result = current_voltage_resistance(voltage=int(u_text), resistance=int(r_text))
            print(result)
            self.result_text.setText(str(result))

    def retranslateUi(self, current_strength_electronic_circuit_Window):
        current_strength_electronic_circuit_Window.setWindowTitle(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.img.setText("")
        self.current_strength_electronic_circuit_label.setText(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u0438\u043b\u044b \u0442\u043e\u043a\u0430 \u0432 \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0446\u0435\u043f\u0438.", None))
        self.R_label.setText(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"R   ", None))
        self.current_strength_electronic_circuit_result_button.setText(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.U_input.setText("")
        self.U_label.setText(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"U   ", None))
        self.R_input.setText("")
        self.info_label.setText(QCoreApplication.translate("current_strength_electronic_circuit_Window", u"U \u2013 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 | R - \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

