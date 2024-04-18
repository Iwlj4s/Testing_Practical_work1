from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)


class Ui_coast_car_round_trip_Window(object):
    def setupUi(self, coast_car_round_trip_Window):
        if not coast_car_round_trip_Window.objectName():
            coast_car_round_trip_Window.setObjectName(u"coast_car_round_trip_Window")
        coast_car_round_trip_Window.resize(870, 517)
        self.centralwidget = QWidget(coast_car_round_trip_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.coast_car_round_trip_label = QLabel(self.centralwidget)
        self.coast_car_round_trip_label.setObjectName(u"coast_car_round_trip_label")
        self.coast_car_round_trip_label.setGeometry(QRect(60, 10, 711, 71))
        font = QFont()
        font.setFamilies([u"Source Code Pro Black"])
        font.setPointSize(16)
        font.setBold(True)
        self.coast_car_round_trip_label.setFont(font)
        self.coast_car_round_trip_label.setWordWrap(True)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 410, 261, 91))
        self.result_frame = QFormLayout(self.formLayoutWidget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setContentsMargins(20, 10, 30, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.result_frame.setWidget(0, QFormLayout.LabelRole, self.label)

        self.result_text = QLineEdit(self.formLayoutWidget_2)
        self.result_text.setObjectName(u"result_text")

        self.result_frame.setWidget(1, QFormLayout.SpanningRole, self.result_text)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(20, 80, 841, 61))
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Black"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.img.setFont(font2)
        self.img.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.img.setWordWrap(False)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(200, 140, 431, 201))
        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)
        self.Gas_km_input = QLineEdit(self.formLayoutWidget)
        self.Gas_km_input.setObjectName(u"Gas_km_input")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.Gas_km_input.setFont(font3)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.Gas_km_input)

        self.Gas100km_label = QLabel(self.formLayoutWidget)
        self.Gas100km_label.setObjectName(u"Gas100km_label")
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro Medium"])
        font4.setPointSize(20)
        font4.setItalic(True)
        self.Gas100km_label.setFont(font4)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.Gas100km_label)

        self.Distance_input = QLineEdit(self.formLayoutWidget)
        self.Distance_input.setObjectName(u"Distance_input")
        self.Distance_input.setFont(font3)

        self.input_frame.setWidget(1, QFormLayout.FieldRole, self.Distance_input)

        self.Distance_label = QLabel(self.formLayoutWidget)
        self.Distance_label.setObjectName(u"Distance_label")
        self.Distance_label.setFont(font4)

        self.input_frame.setWidget(1, QFormLayout.LabelRole, self.Distance_label)

        self.gas_price_input = QLineEdit(self.formLayoutWidget)
        self.gas_price_input.setObjectName(u"gas_price_input")
        self.gas_price_input.setFont(font3)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.gas_price_input)

        self.gas_price_label = QLabel(self.formLayoutWidget)
        self.gas_price_label.setObjectName(u"gas_price_label")
        self.gas_price_label.setFont(font4)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.gas_price_label)

        self.coast_car_round_trip_result_button = QPushButton(self.formLayoutWidget)
        self.coast_car_round_trip_result_button.setObjectName(u"coast_car_round_trip_result_button")
        font5 = QFont()
        font5.setFamilies([u"Source Code Pro Medium"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.coast_car_round_trip_result_button.setFont(font5)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.coast_car_round_trip_result_button)

        coast_car_round_trip_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(coast_car_round_trip_Window)

        QMetaObject.connectSlotsByName(coast_car_round_trip_Window)
    # setupUi

    def retranslateUi(self, coast_car_round_trip_Window):
        coast_car_round_trip_Window.setWindowTitle(QCoreApplication.translate("coast_car_round_trip_Window", u"MainWindow", None))
        self.coast_car_round_trip_label.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u043f\u043e\u0435\u0437\u0434\u043a\u0438 \u043d\u0430 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0435 \u043d\u0430 \u0434\u0430\u0447\u0443 (\u0442\u0443\u0434\u0430 \u0438 \u043e\u0431\u0440\u0430\u0442\u043d\u043e).", None))
        self.label.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.img.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"2(\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u0435 \u0431\u0435\u043d\u0437\u0438\u043d\u0430 \u043d\u0430 100 \u043a\u043c. \u043f\u0443\u0442\u0438 / 100 \u00d7 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0434\u043e \u0434\u0430\u0447\u0438 \u00d7 \u0446\u0435\u043d\u0430 \u043e\u0434\u043d\u043e\u0433\u043e \u043b\u0438\u0442\u0440\u0430 \u0431\u0435\u043d\u0437\u0438\u043d\u0430)", None))
        self.Gas_km_input.setText("")
        self.Gas100km_label.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"Gas100km", None))
        self.Distance_input.setText("")
        self.Distance_label.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"Distance", None))
        self.gas_price_input.setText("")
        self.gas_price_label.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"Price1Lgas", None))
        self.coast_car_round_trip_result_button.setText(QCoreApplication.translate("coast_car_round_trip_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
    # retranslateUi

