from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)


class Ui_surface_area_cylinder_base_r_h_Window(object):
    def setupUi(self, surface_area_cylinder_base_r_h_Window):
        if not surface_area_cylinder_base_r_h_Window.objectName():
            surface_area_cylinder_base_r_h_Window.setObjectName(u"surface_area_cylinder_base_r_h_Window")
        surface_area_cylinder_base_r_h_Window.resize(800, 492)
        self.centralwidget = QWidget(surface_area_cylinder_base_r_h_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.surface_area_cylinder_base_r_h_label = QLabel(self.centralwidget)
        self.surface_area_cylinder_base_r_h_label.setObjectName(u"surface_area_cylinder_base_r_h_label")
        self.surface_area_cylinder_base_r_h_label.setGeometry(QRect(10, 0, 781, 61))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)
        self.surface_area_cylinder_base_r_h_label.setFont(font)
        self.surface_area_cylinder_base_r_h_label.setWordWrap(True)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(270, 160, 361, 251))
        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)
        self.Smain_input = QLineEdit(self.formLayoutWidget)
        self.Smain_input.setObjectName(u"Smain_input")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.Smain_input.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.Smain_input)

        self.Smain_label = QLabel(self.formLayoutWidget)
        self.Smain_label.setObjectName(u"Smain_label")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(20)
        font2.setItalic(True)
        self.Smain_label.setFont(font2)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.Smain_label)

        self.Sbp_label = QLabel(self.formLayoutWidget)
        self.Sbp_label.setObjectName(u"Sbp_label")
        self.Sbp_label.setFont(font2)

        self.input_frame.setWidget(1, QFormLayout.LabelRole, self.Sbp_label)

        self.Sbp_input = QLineEdit(self.formLayoutWidget)
        self.Sbp_input.setObjectName(u"Sbp_input")
        self.Sbp_input.setFont(font1)

        self.input_frame.setWidget(1, QFormLayout.FieldRole, self.Sbp_input)

        self.R_label = QLabel(self.formLayoutWidget)
        self.R_label.setObjectName(u"R_label")
        self.R_label.setFont(font2)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.R_label)

        self.R_input = QLineEdit(self.formLayoutWidget)
        self.R_input.setObjectName(u"R_input")
        self.R_input.setFont(font1)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.R_input)

        self.h_label = QLabel(self.formLayoutWidget)
        self.h_label.setObjectName(u"h_label")
        self.h_label.setFont(font2)

        self.input_frame.setWidget(3, QFormLayout.LabelRole, self.h_label)

        self.h_input = QLineEdit(self.formLayoutWidget)
        self.h_input.setObjectName(u"h_input")
        self.h_input.setFont(font1)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.h_input)

        self.surface_area_cylinder_base_r_h_result_button = QPushButton(self.formLayoutWidget)
        self.surface_area_cylinder_base_r_h_result_button.setObjectName(u"surface_area_cylinder_base_r_h_result_button")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro Medium"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.surface_area_cylinder_base_r_h_result_button.setFont(font3)

        self.input_frame.setWidget(4, QFormLayout.FieldRole, self.surface_area_cylinder_base_r_h_result_button)

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(160, 60, 561, 101))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula10.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 390, 221, 91))
        self.result_frame = QFormLayout(self.formLayoutWidget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setContentsMargins(20, 10, 30, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.result_frame.setWidget(0, QFormLayout.LabelRole, self.label)

        self.result_text = QLineEdit(self.formLayoutWidget_2)
        self.result_text.setObjectName(u"result_text")

        self.result_frame.setWidget(1, QFormLayout.SpanningRole, self.result_text)

        surface_area_cylinder_base_r_h_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(surface_area_cylinder_base_r_h_Window)

        QMetaObject.connectSlotsByName(surface_area_cylinder_base_r_h_Window)
    # setupUi

    def retranslateUi(self, surface_area_cylinder_base_r_h_Window):
        surface_area_cylinder_base_r_h_Window.setWindowTitle(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"MainWindow", None))
        self.surface_area_cylinder_base_r_h_label.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438 \u0446\u0438\u043b\u0438\u043d\u0434\u0440\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0440\u0430\u0434\u0438\u0443\u0441 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u0432\u044b\u0441\u043e\u0442\u0430. ", None))
        self.Smain_input.setText("")
        self.Smain_label.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"S\u043e\u0441\u043d.   ", None))
        self.Sbp_label.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"S\u0431\u043f.   ", None))
        self.Sbp_input.setText("")
        self.R_label.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"R   ", None))
        self.R_input.setText("")
        self.h_label.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"h   ", None))
        self.h_input.setText("")
        self.surface_area_cylinder_base_r_h_result_button.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.img.setText("")
        self.label.setText(QCoreApplication.translate("surface_area_cylinder_base_r_h_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
    # retranslateUi

