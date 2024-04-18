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
from functions.calculation_functions import resistance_parallel


class Ui_resistance_parallel_Window(object):
    def setupUi(self, resistance_parallel_Window):
        if not resistance_parallel_Window.objectName():
            resistance_parallel_Window.setObjectName(u"resistance_parallel_Window")
        resistance_parallel_Window.setFixedSize(814, 469)

        # INPUT FRAME #
        self.centralwidget = QWidget(resistance_parallel_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(270, 180, 321, 171))

        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)

        self.r2_label = QLabel(self.formLayoutWidget)
        self.r2_label.setObjectName(u"r2_label")
        font = QFont()
        font.setFamilies([u"Source Code Pro Medium"])
        font.setPointSize(20)
        font.setItalic(True)
        self.r2_label.setFont(font)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.r2_label)

        self.r2_input = QLineEdit(self.formLayoutWidget)
        self.r2_input.setObjectName(u"r2_input")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.r2_input.setFont(font1)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.r2_input)

        self.r1_input = QLineEdit(self.formLayoutWidget)
        self.r1_input.setObjectName(u"r1_input")
        self.r1_input.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.r1_input)

        self.r1_label = QLabel(self.formLayoutWidget)
        self.r1_label.setObjectName(u"r1_label")
        self.r1_label.setFont(font)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.r1_label)

        # RESULT BUTTON #
        self.resistance_parallel_result_button = QPushButton(self.formLayoutWidget)
        self.resistance_parallel_result_button.setObjectName(u"resistance_parallel_result_button")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.resistance_parallel_result_button.setFont(font2)

        self.resistance_parallel_result_button.clicked.connect(self.get_result)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.resistance_parallel_result_button)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 370, 221, 91))
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

        self.result_frame.setWidget(1, QFormLayout.SpanningRole, self.result_text)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(330, 80, 231, 91))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula3.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resistance_parallel_label = QLabel(self.centralwidget)
        self.resistance_parallel_label.setObjectName(u"resistance_parallel_label")
        self.resistance_parallel_label.setGeometry(QRect(20, 10, 781, 61))
        self.resistance_parallel_label.setFont(font3)
        self.resistance_parallel_label.setWordWrap(True)
        resistance_parallel_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(resistance_parallel_Window)

        QMetaObject.connectSlotsByName(resistance_parallel_Window)
    # setupUi

    # Get result
    def get_result(self):
        r1_text = self.r1_input.text()
        r2_text = self.r2_input.text()

        enter_digit = user_enter_digit(r1_text, r2_text)

        print(r1_text)
        print(r2_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.r1_input.setText(result)
            self.r2_input.setText(result)
        else:
            result = resistance_parallel(r1=int(r1_text), r2=int(r2_text))
            print(result)
            self.result_text.setText(str(result))

    def retranslateUi(self, resistance_parallel_Window):
        resistance_parallel_Window.setWindowTitle(QCoreApplication.translate("resistance_parallel_Window", u"MainWindow", None))
        self.r2_label.setText(QCoreApplication.translate("resistance_parallel_Window", u"r2   ", None))
        self.r2_input.setText("")
        self.r1_input.setText("")
        self.r1_label.setText(QCoreApplication.translate("resistance_parallel_Window", u"r1   ", None))
        self.resistance_parallel_result_button.setText(QCoreApplication.translate("resistance_parallel_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("resistance_parallel_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.img.setText("")
        self.resistance_parallel_label.setText(QCoreApplication.translate("resistance_parallel_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u044f \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0446\u0435\u043f\u0438, \u0441\u043e\u0441\u0442\u043e\u044f\u0449\u0435\u0439 \u0438\u0437 \u0434\u0432\u0443\u0445 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u044c\u043d\u043e \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0439.", None))
    # retranslateUi

