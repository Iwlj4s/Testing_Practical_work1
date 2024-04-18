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
from functions.calculation_functions import pounds_to_kg


class Ui_weight_conversion_from_pounds_to_kg_Window(object):
    def setupUi(self, weight_conversion_from_pounds_to_kg_Window):
        if not weight_conversion_from_pounds_to_kg_Window.objectName():
            weight_conversion_from_pounds_to_kg_Window.setObjectName(u"weight_conversion_from_pounds_to_kg_Window")
        weight_conversion_from_pounds_to_kg_Window.setFixedSize(800, 365)

        self.centralwidget = QWidget(weight_conversion_from_pounds_to_kg_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.weight_conversion_from_pounds_to_kg_label = QLabel(self.centralwidget)
        self.weight_conversion_from_pounds_to_kg_label.setObjectName(u"weight_conversion_from_pounds_to_kg_label")
        self.weight_conversion_from_pounds_to_kg_label.setGeometry(QRect(160, 10, 511, 51))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)

        # RESULT FRAME #
        self.weight_conversion_from_pounds_to_kg_label.setFont(font)
        self.weight_conversion_from_pounds_to_kg_label.setWordWrap(True)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(290, 220, 231, 117))

        self.result_frame = QFormLayout(self.formLayoutWidget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setContentsMargins(20, 10, 30, 0)

        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.result_frame.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.result_frame.setWidget(1, QFormLayout.FieldRole, self.label)

        self.result_text = QLineEdit(self.formLayoutWidget_2)
        self.result_text.setObjectName(u"result_text")

        self.result_frame.setWidget(2, QFormLayout.FieldRole, self.result_text)

        # INFO LABEL #
        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(310, 50, 191, 41))
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.info_label.setFont(font1)

        # INPUT FRAME #
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(250, 100, 321, 111))

        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)
        self.U_label = QLabel(self.formLayoutWidget)
        self.U_label.setObjectName(u"U_label")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(20)
        font2.setItalic(True)
        self.U_label.setFont(font2)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.U_label)

        self.pounds_input = QLineEdit(self.formLayoutWidget)
        self.pounds_input.setObjectName(u"pounds_input")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.pounds_input.setFont(font3)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.pounds_input)

        # RESULT BUTTON #
        self.weight_conversion_from_pounds_to_kg_result_button = QPushButton(self.formLayoutWidget)
        self.weight_conversion_from_pounds_to_kg_result_button.setObjectName(u"weight_conversion_from_pounds_to_kg_result_button")
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro Medium"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.weight_conversion_from_pounds_to_kg_result_button.setFont(font4)

        self.weight_conversion_from_pounds_to_kg_result_button.clicked.connect(self.get_result)

        self.input_frame.setWidget(1, QFormLayout.FieldRole, self.weight_conversion_from_pounds_to_kg_result_button)

        weight_conversion_from_pounds_to_kg_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(weight_conversion_from_pounds_to_kg_Window)

        QMetaObject.connectSlotsByName(weight_conversion_from_pounds_to_kg_Window)
    # setupUi

    # Get result
    def get_result(self):
        pounds_text = self.pounds_input.text()

        enter_digit = user_enter_digit(pounds_text)

        print(pounds_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.pounds_input.setText(result)
        else:
            result = pounds_to_kg(pounds=int(pounds_text))
            print(result)
            self.result_text.setText(str(result))

    def retranslateUi(self, weight_conversion_from_pounds_to_kg_Window):
        weight_conversion_from_pounds_to_kg_Window.setWindowTitle(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"MainWindow", None))
        self.weight_conversion_from_pounds_to_kg_label.setText(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0441\u0447\u0435\u0442\u0430 \u0432\u0435\u0441\u0430 \u0444\u0443\u043d\u0442\u043e\u0432 \u0432 \u043a\u0433.", None))
        self.label_2.setText(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"\u041a\u0433", None))
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.info_label.setText(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"1 \u0444\u0443\u043d\u0442 = 405,9 \u0433", None))
        self.U_label.setText(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"\u0424\u0443\u043d\u0442\u044b", None))
        self.pounds_input.setText("")
        self.weight_conversion_from_pounds_to_kg_result_button.setText(QCoreApplication.translate("weight_conversion_from_pounds_to_kg_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
    # retranslateUi

