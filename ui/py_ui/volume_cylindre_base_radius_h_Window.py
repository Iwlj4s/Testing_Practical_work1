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
from functions.calculation_functions import cylinder_volume


class Ui_volume_cylindre_base_radius_h_Window(object):
    def setupUi(self, volume_cylindre_base_radius_h_Window):
        if not volume_cylindre_base_radius_h_Window.objectName():
            volume_cylindre_base_radius_h_Window.setObjectName(u"volume_cylindre_base_radius_h_Window")
        volume_cylindre_base_radius_h_Window.setFixedSize(800, 500)

        self.centralwidget = QWidget(volume_cylindre_base_radius_h_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.volume_cylindre_base_radius_h_label = QLabel(self.centralwidget)
        self.volume_cylindre_base_radius_h_label.setObjectName(u"volume_cylindre_base_radius_h_label")
        self.volume_cylindre_base_radius_h_label.setGeometry(QRect(10, 0, 781, 61))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)

        # RESULT FRAME #
        self.volume_cylindre_base_radius_h_label.setFont(font)
        self.volume_cylindre_base_radius_h_label.setWordWrap(True)
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

        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(320, 30, 221, 91))
        self.img.setPixmap(QPixmap(u"./ui/py_ui/img/formula9.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # INPUT FRAME #
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(280, 120, 321, 161))
        self.input_frame = QFormLayout(self.formLayoutWidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setContentsMargins(20, 20, 30, 20)

        self.h_label = QLabel(self.formLayoutWidget)
        self.h_label.setObjectName(u"h_label")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro Medium"])
        font1.setPointSize(20)
        font1.setItalic(True)
        self.h_label.setFont(font1)

        self.input_frame.setWidget(2, QFormLayout.LabelRole, self.h_label)

        # RESULT BUTTON #
        self.volume_cylindre_base_radius_h_result_button = QPushButton(self.formLayoutWidget)
        self.volume_cylindre_base_radius_h_result_button.setObjectName(u"volume_cylindre_base_radius_h_result_button")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.volume_cylindre_base_radius_h_result_button.setFont(font2)

        self.volume_cylindre_base_radius_h_result_button.clicked.connect(self.get_result)

        self.input_frame.setWidget(3, QFormLayout.FieldRole, self.volume_cylindre_base_radius_h_result_button)

        self.R_input = QLineEdit(self.formLayoutWidget)
        self.R_input.setObjectName(u"R_input")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.R_input.setFont(font3)

        self.input_frame.setWidget(0, QFormLayout.FieldRole, self.R_input)

        self.R_label = QLabel(self.formLayoutWidget)
        self.R_label.setObjectName(u"R_label")
        self.R_label.setFont(font1)

        self.input_frame.setWidget(0, QFormLayout.LabelRole, self.R_label)

        self.h_input = QLineEdit(self.formLayoutWidget)
        self.h_input.setObjectName(u"h_input")
        self.h_input.setFont(font3)

        self.input_frame.setWidget(2, QFormLayout.FieldRole, self.h_input)

        volume_cylindre_base_radius_h_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(volume_cylindre_base_radius_h_Window)

        QMetaObject.connectSlotsByName(volume_cylindre_base_radius_h_Window)
    # setupUi

    # Get result
    def get_result(self):
        r_text = self.R_input.text()
        h_text = self.h_input.text()

        enter_digit = user_enter_digit(r_text, h_text)

        print(r_text)
        print(h_text)

        if not enter_digit:
            result = str("Вы вводите некорректные данные, введите цифры")
            self.R_input.setText(result)
            self.h_input.setText(result)
        else:
            result = cylinder_volume(radius=int(r_text), height=int(h_text))
            print(result)
            self.result_text.setText(str(result))

    def retranslateUi(self, volume_cylindre_base_radius_h_Window):
        volume_cylindre_base_radius_h_Window.setWindowTitle(QCoreApplication.translate("volume_cylindre_base_radius_h_Window", u"MainWindow", None))
        self.volume_cylindre_base_radius_h_label.setText(QCoreApplication.translate("volume_cylindre_base_radius_h_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043c\u0430 \u0446\u0438\u043b\u0438\u043d\u0434\u0440\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0440\u0430\u0434\u0438\u0443\u0441 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u0432\u044b\u0441\u043e\u0442\u0430. ", None))
        self.label.setText(QCoreApplication.translate("volume_cylindre_base_radius_h_Window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.result_text.setText("")
        self.img.setText("")
        self.h_label.setText(QCoreApplication.translate("volume_cylindre_base_radius_h_Window", u"h   ", None))
        self.volume_cylindre_base_radius_h_result_button.setText(QCoreApplication.translate("volume_cylindre_base_radius_h_Window", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.R_input.setText("")
        self.R_label.setText(QCoreApplication.translate("volume_cylindre_base_radius_h_Window", u"R   ", None))
        self.h_input.setText("")
    # retranslateUi

