from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)


class Ui_distance_conversion_from_miles_to_km_WIndow(object):
    def setupUi(self, distance_conversion_from_miles_to_km_WIndow):
        if not distance_conversion_from_miles_to_km_WIndow.objectName():
            distance_conversion_from_miles_to_km_WIndow.setObjectName(u"distance_conversion_from_miles_to_km_WIndow")
        distance_conversion_from_miles_to_km_WIndow.resize(712, 322)
        self.centralwidget = QWidget(distance_conversion_from_miles_to_km_WIndow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(240, 50, 231, 41))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(14)
        self.info_label.setFont(font)
        self.distance_conversion_from_miles_to_km_label = QLabel(self.centralwidget)
        self.distance_conversion_from_miles_to_km_label.setObjectName(u"distance_conversion_from_miles_to_km_label")
        self.distance_conversion_from_miles_to_km_label.setGeometry(QRect(10, 0, 711, 51))
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(16)
        self.distance_conversion_from_miles_to_km_label.setFont(font1)
        self.distance_conversion_from_miles_to_km_label.setWordWrap(True)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(170, 100, 351, 112))
        self.input_frame_2 = QFormLayout(self.formLayoutWidget)
        self.input_frame_2.setObjectName(u"input_frame_2")
        self.input_frame_2.setContentsMargins(20, 20, 30, 20)
        self.Versta = QLabel(self.formLayoutWidget)
        self.Versta.setObjectName(u"Versta")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(20)
        font2.setItalic(True)
        self.Versta.setFont(font2)

        self.input_frame_2.setWidget(0, QFormLayout.LabelRole, self.Versta)

        self.pounds_input_2 = QLineEdit(self.formLayoutWidget)
        self.pounds_input_2.setObjectName(u"pounds_input_2")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.pounds_input_2.setFont(font3)

        self.input_frame_2.setWidget(0, QFormLayout.FieldRole, self.pounds_input_2)

        self.distance_conversion_from_miles_to_km_result_button_ = QPushButton(self.formLayoutWidget)
        self.distance_conversion_from_miles_to_km_result_button_.setObjectName(u"distance_conversion_from_miles_to_km_result_button_")
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro Medium"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.distance_conversion_from_miles_to_km_result_button_.setFont(font4)

        self.input_frame_2.setWidget(1, QFormLayout.FieldRole, self.distance_conversion_from_miles_to_km_result_button_)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(220, 230, 231, 81))
        self.result_frame_2 = QFormLayout(self.formLayoutWidget_2)
        self.result_frame_2.setObjectName(u"result_frame_2")
        self.result_frame_2.setContentsMargins(20, 10, 30, 0)
        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.result_frame_2.setWidget(0, QFormLayout.FieldRole, self.label_4)

        self.result_text_2 = QLineEdit(self.formLayoutWidget_2)
        self.result_text_2.setObjectName(u"result_text_2")
        self.result_text_2.setFont(font)

        self.result_frame_2.setWidget(1, QFormLayout.FieldRole, self.result_text_2)

        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.result_frame_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        distance_conversion_from_miles_to_km_WIndow.setCentralWidget(self.centralwidget)

        self.retranslateUi(distance_conversion_from_miles_to_km_WIndow)

        QMetaObject.connectSlotsByName(distance_conversion_from_miles_to_km_WIndow)
    # setupUi

    def retranslateUi(self, distance_conversion_from_miles_to_km_WIndow):
        distance_conversion_from_miles_to_km_WIndow.setWindowTitle(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"MainWindow", None))
        self.info_label.setText(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"1 \u0432\u0435\u0440\u0441\u0442\u0430 = 1066,8 \u043c", None))
        self.distance_conversion_from_miles_to_km_label.setText(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0441\u0447\u0435\u0442\u0430 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0438\u0437 \u0432\u0435\u0440\u0441\u0442 \u0432 \u043a\u0438\u043b\u043e\u043c\u0435\u0442\u0440\u044b. ", None))
        self.Versta.setText(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"\u0412\u0435\u0440\u0441\u0442\u0430  ", None))
        self.pounds_input_2.setText("")
        self.distance_conversion_from_miles_to_km_result_button_.setText(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text_2.setText("")
        self.label_3.setText(QCoreApplication.translate("distance_conversion_from_miles_to_km_WIndow", u"\u041a\u043c  ", None))
    # retranslateUi

