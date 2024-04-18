from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)

from ui.py_ui.area_triangle_l_base_h_Window import Ui_area_triangle_l_base_h_Window
from ui.py_ui.area_triangle_l_two_sides_size_angle_beetween_sides_Window import \
    Ui_area_triangle_l_two_sides_size_angle_beetween_sides_Window
from ui.py_ui.resistance_parallel_Window import Ui_resistance_parallel_Window
from ui.py_ui.resistance_series_connected_Window import Ui_resistance_series_connected_Window
from ui.py_ui.current_strength_electronic_circuit_Window import Ui_current_strength_electronic_circuit_Window
from ui.py_ui.weight_conversion_from_pounds_to_kg_Window import Ui_weight_conversion_from_pounds_to_kg_Window
from ui.py_ui.coast_car_round_trip_Window import Ui_coast_car_round_trip_Window
from ui.py_ui.area_trapezoid_l_bases_h_Window import Ui_area_trapezoid_l_bases_h_Window
from ui.py_ui.volume_cylindre_base_radius_h_Window import Ui_volume_cylindre_base_radius_h_Window
from ui.py_ui.surface_area_cylinder_base_r_h_Window import Ui_surface_area_cylinder_base_r_h_Window
from ui.py_ui.volume_of_parallelepiped_Window import Ui_volume_of_parallelepiped_Window
from ui.py_ui.distance_conversion_from_miles_to_km_WIndow import Ui_distance_conversion_from_miles_to_km_WIndow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1085, 855)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1071, 841))

        self.main_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(100, 10, 100, 10)

        # 1. Вычисление площади треугольника, если известна длина основания и высота #
        self.area_triangle_l_base_h = QPushButton(self.verticalLayoutWidget)
        self.area_triangle_l_base_h.setObjectName(u"area_triangle_l_base_h")
        self.area_triangle_l_base_h.setMinimumSize(QSize(445, 0))

        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(9)
        self.area_triangle_l_base_h.setFont(font)

        self.area_triangle_l_base_h.clicked.connect(self.open_area_triangle_l_base_h_window)

        self.main_layout.addWidget(self.area_triangle_l_base_h)

        # 2. Вычисление площади треугольника, если известны длины двух его сторон и величина угла между этими
        # сторонами #
        self.area_triangle_l_two_sides_size_angle_beetween_sides = QPushButton(self.verticalLayoutWidget)
        self.area_triangle_l_two_sides_size_angle_beetween_sides.setObjectName(
            u"area_triangle_l_two_sides_size_angle_beetween_sides")
        self.area_triangle_l_two_sides_size_angle_beetween_sides.setFont(font)

        self.area_triangle_l_two_sides_size_angle_beetween_sides.clicked.connect(
            self.open_area_triangle_l_two_sides_size_angle_beetween_sides_window)

        self.main_layout.addWidget(self.area_triangle_l_two_sides_size_angle_beetween_sides)

        # 3. Вычисление сопротивления электрической цепи, состоящей из двух параллельно соединенных сопротивлений. #
        self.resistance_parallel = QPushButton(self.verticalLayoutWidget)
        self.resistance_parallel.setObjectName(u"resistance_parallel")
        self.resistance_parallel.setFont(font)

        self.resistance_parallel.clicked.connect(self.open_resistance_parallel_Window)

        self.main_layout.addWidget(self.resistance_parallel)

        # 4. Вычисление сопротивления электрической цепи, состоящей из двух последовательно соединенных сопротивлений #
        self.resistance_series_connected = QPushButton(self.verticalLayoutWidget)
        self.resistance_series_connected.setObjectName(u"resistance_series_connected")
        self.resistance_series_connected.setFont(font)

        self.resistance_series_connected.clicked.connect(self.open_resistance_series_connected_Window)

        self.main_layout.addWidget(self.resistance_series_connected)

        # 5. Вычисление силы тока в электрической цепи. #
        self.current_strength_electronic_circuit = QPushButton(self.verticalLayoutWidget)
        self.current_strength_electronic_circuit.setObjectName(u"current_strength_electronic_circuit")
        self.current_strength_electronic_circuit.setFont(font)

        self.current_strength_electronic_circuit.clicked.connect(self.open_current_strength_electronic_circuit_Window)

        self.main_layout.addWidget(self.current_strength_electronic_circuit)

        # 6. Вычисление пересчета веса фунтов в кг. 1 фунт = 405,9 г #
        self.weight_conversion_from_pounds_to_kg = QPushButton(self.verticalLayoutWidget)
        self.weight_conversion_from_pounds_to_kg.setObjectName(u"weight_conversion_from_pounds_to_kg")
        self.weight_conversion_from_pounds_to_kg.setFont(font)

        self.weight_conversion_from_pounds_to_kg.clicked.connect(self.open_weight_conversion_from_pounds_to_kg_Window)

        self.main_layout.addWidget(self.weight_conversion_from_pounds_to_kg)

        # 7. Вычисление стоимости поездки на автомобиле на дачу (туда и обратно).#
        self.coast_car_round_trip = QPushButton(self.verticalLayoutWidget)
        self.coast_car_round_trip.setObjectName(u"coast_car_round_trip")
        self.coast_car_round_trip.setFont(font)

        self.coast_car_round_trip.clicked.connect(self.open_coast_car_round_trip_Window)

        self.main_layout.addWidget(self.coast_car_round_trip)

        # 8. Вычисление площади трапеции, если известны длины оснований и высота #
        self.area_trapezoid_l_bases_h = QPushButton(self.verticalLayoutWidget)
        self.area_trapezoid_l_bases_h.setObjectName(u"area_trapezoid_l_bases_h")
        self.area_trapezoid_l_bases_h.setFont(font)

        self.area_trapezoid_l_bases_h.clicked.connect(self.open_area_trapezoid_l_bases_h_Window)

        self.main_layout.addWidget(self.area_trapezoid_l_bases_h)

        # 9. Вычисление объема цилиндра, если известны радиус основания и высота #
        self.volume_cylindre_base_radius_h = QPushButton(self.verticalLayoutWidget)
        self.volume_cylindre_base_radius_h.setObjectName(u"volume_cylindre_base_radius_h")
        self.volume_cylindre_base_radius_h.setFont(font)

        self.volume_cylindre_base_radius_h.clicked.connect(self.open_volume_cylindre_base_radius_h_Window)

        self.main_layout.addWidget(self.volume_cylindre_base_radius_h)

        # 10. Вычисление площади поверхности цилиндра, если известны радиус основания и высота #
        self.surface_area_cylinder_base_r_h = QPushButton(self.verticalLayoutWidget)
        self.surface_area_cylinder_base_r_h.setObjectName(u"surface_area_cylinder_base_r_h")
        self.surface_area_cylinder_base_r_h.setFont(font)

        self.surface_area_cylinder_base_r_h.clicked.connect(self.open_surface_area_cylinder_base_r_h_Window)

        self.main_layout.addWidget(self.surface_area_cylinder_base_r_h)

        # 11. Вычисление объема параллелепипеда по трем его измерениям #
        self.volume_of_parallelepiped = QPushButton(self.verticalLayoutWidget)
        self.volume_of_parallelepiped.setObjectName(u"volume_of_parallelepiped")
        self.volume_of_parallelepiped.setFont(font)

        self.volume_of_parallelepiped.clicked.connect(self.open_volume_of_parallelepiped_Window)

        self.main_layout.addWidget(self.volume_of_parallelepiped)

        # 12. Вычисление пересчета расстояния из верст в километры. 1 верста = 1066,8 м. #
        self.distance_conversion_from_miles_to_km = QPushButton(self.verticalLayoutWidget)
        self.distance_conversion_from_miles_to_km.setObjectName(u"distance_conversion_from_miles_to_km")
        self.distance_conversion_from_miles_to_km.setFont(font)

        self.distance_conversion_from_miles_to_km.clicked.connect(self.open_distance_conversion_from_miles_to_km_WIndow)

        self.main_layout.addWidget(self.distance_conversion_from_miles_to_km)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # 1. Open area_triangle_l_base_h Window
    def open_area_triangle_l_base_h_window(self):
        self.area_triangle_l_base_h_Window = QtWidgets.QMainWindow()
        self.ui = Ui_area_triangle_l_base_h_Window()
        self.ui.setupUi(self.area_triangle_l_base_h_Window)
        self.area_triangle_l_base_h_Window.show()

    # 2. Open area_triangle_l_two_sides_size_angle_beetween_sides Window
    def open_area_triangle_l_two_sides_size_angle_beetween_sides_window(self):
        self.area_triangle_l_two_sides_size_angle_beetween_sides_Window = QtWidgets.QMainWindow()
        self.ui = Ui_area_triangle_l_two_sides_size_angle_beetween_sides_Window()
        self.ui.setupUi(self.area_triangle_l_two_sides_size_angle_beetween_sides_Window)
        self.area_triangle_l_two_sides_size_angle_beetween_sides_Window.show()

    # 3. Open resistance_parallel_Window
    def open_resistance_parallel_Window(self):
        self.resistance_parallel_Window = QtWidgets.QMainWindow()
        self.ui = Ui_resistance_parallel_Window()
        self.ui.setupUi(self.resistance_parallel_Window)
        self.resistance_parallel_Window.show()

    # 4. Open resistance_series_connected_Window
    def open_resistance_series_connected_Window(self):
        self.resistance_series_connected_Window = QtWidgets.QMainWindow()
        self.ui = Ui_resistance_series_connected_Window()
        self.ui.setupUi(self.resistance_series_connected_Window)
        self.resistance_series_connected_Window.show()

    # 5. Open current_strength_electronic_circuit_Window
    def open_current_strength_electronic_circuit_Window(self):
        self.current_strength_electronic_circuit_Window = QtWidgets.QMainWindow()
        self.ui = Ui_current_strength_electronic_circuit_Window()
        self.ui.setupUi(self.current_strength_electronic_circuit_Window)
        self.current_strength_electronic_circuit_Window.show()

    # 6. Open weight_conversion_from_pounds_to_kg_Window
    def open_weight_conversion_from_pounds_to_kg_Window(self):
        self.weight_conversion_from_pounds_to_kg_Window = QtWidgets.QMainWindow()
        self.ui = Ui_weight_conversion_from_pounds_to_kg_Window()
        self.ui.setupUi(self.weight_conversion_from_pounds_to_kg_Window)
        self.weight_conversion_from_pounds_to_kg_Window.show()

    # 7. Open coast_car_round_trip_Window
    def open_coast_car_round_trip_Window(self):
        self.coast_car_round_trip_Window = QtWidgets.QMainWindow()
        self.ui = Ui_coast_car_round_trip_Window()
        self.ui.setupUi(self.coast_car_round_trip_Window)
        self.coast_car_round_trip_Window.show()

    # 8. Open area_trapezoid_l_bases_h_Window
    def open_area_trapezoid_l_bases_h_Window(self):
        self.area_trapezoid_l_bases_h_Window = QtWidgets.QMainWindow()
        self.ui = Ui_area_trapezoid_l_bases_h_Window()
        self.ui.setupUi(self.area_trapezoid_l_bases_h_Window)
        self.area_trapezoid_l_bases_h_Window.show()

    # 9. Open volume_cylindre_base_radius_h_Window
    def open_volume_cylindre_base_radius_h_Window(self):
        self.volume_cylindre_base_radius_h_Window = QtWidgets.QMainWindow()
        self.ui = Ui_volume_cylindre_base_radius_h_Window()
        self.ui.setupUi(self.volume_cylindre_base_radius_h_Window)
        self.volume_cylindre_base_radius_h_Window.show()

    # 10. Open surface_area_cylinder_base_r_h_Window
    def open_surface_area_cylinder_base_r_h_Window(self):
        self.surface_area_cylinder_base_r_h_Window = QtWidgets.QMainWindow()
        self.ui = Ui_surface_area_cylinder_base_r_h_Window()
        self.ui.setupUi(self.surface_area_cylinder_base_r_h_Window)
        self.surface_area_cylinder_base_r_h_Window.show()

    # 11. Open volume_of_parallelepiped_Window
    def open_volume_of_parallelepiped_Window(self):
        self.volume_of_parallelepiped_Window = QtWidgets.QMainWindow()
        self.ui = Ui_volume_of_parallelepiped_Window()
        self.ui.setupUi(self.volume_of_parallelepiped_Window)
        self.volume_of_parallelepiped_Window.show()

    # 12. Open distance_conversion_from_miles_to_km_WIndow
    def open_distance_conversion_from_miles_to_km_WIndow(self):
        self.distance_conversion_from_miles_to_km_WIndow = QtWidgets.QMainWindow()
        self.ui = Ui_distance_conversion_from_miles_to_km_WIndow()
        self.ui.setupUi(self.distance_conversion_from_miles_to_km_WIndow)
        self.distance_conversion_from_miles_to_km_WIndow.show()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.area_triangle_l_base_h.setText(QCoreApplication.translate("MainWindow",
                                                                       u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430 \u0434\u043b\u0438\u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u0432\u044b\u0441\u043e\u0442\u0430.",
                                                                       None))
        self.area_triangle_l_two_sides_size_angle_beetween_sides.setText(QCoreApplication.translate("MainWindow",
                                                                                                    u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0434\u043b\u0438\u043d\u044b \u0434\u0432\u0443\u0445 \u0435\u0433\u043e \u0441\u0442\u043e\u0440\u043e\u043d \u0438 \n"
                                                                                                    "\u0432\u0435\u043b\u0438\u0447\u0438\u043d\u0430 \u0443\u0433\u043b\u0430 \u043c\u0435\u0436\u0434\u0443 \u044d\u0442\u0438\u043c\u0438 \u0441\u0442\u043e\u0440\u043e\u043d\u0430\u043c\u0438.",
                                                                                                    None))
        self.resistance_parallel.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u044f \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0446\u0435\u043f\u0438, \u0441\u043e\u0441\u0442\u043e\u044f\u0449\u0435\u0439 \u0438\u0437 \u0434\u0432\u0443\u0445 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u044c\u043d\u043e \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0439.",
                                                                    None))
        self.resistance_series_connected.setText(QCoreApplication.translate("MainWindow",
                                                                            u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u044f \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0446\u0435\u043f\u0438, \u0441\u043e\u0441\u0442\u043e\u044f\u0449\u0435\u0439 \u0438\u0437 \u0434\u0432\u0443\u0445 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0439.",
                                                                            None))
        self.current_strength_electronic_circuit.setText(QCoreApplication.translate("MainWindow",
                                                                                    u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u0438\u043b\u044b \u0442\u043e\u043a\u0430 \u0432 \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0446\u0435\u043f\u0438.",
                                                                                    None))
        self.weight_conversion_from_pounds_to_kg.setText(QCoreApplication.translate("MainWindow",
                                                                                    u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0441\u0447\u0435\u0442\u0430 \u0432\u0435\u0441\u0430 \u0444\u0443\u043d\u0442\u043e\u0432 \u0432 \u043a\u0433",
                                                                                    None))
        self.coast_car_round_trip.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u043f\u043e\u0435\u0437\u0434\u043a\u0438 \u043d\u0430 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0435 \u043d\u0430 \u0434\u0430\u0447\u0443 (\u0442\u0443\u0434\u0430 \u0438 \u043e\u0431\u0440\u0430\u0442\u043d\u043e)",
                                                                     None))
        self.area_trapezoid_l_bases_h.setText(QCoreApplication.translate("MainWindow",
                                                                         u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0434\u043b\u0438\u043d\u044b \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0439 \u0438 \u0432\u044b\u0441\u043e\u0442\u0430.",
                                                                         None))
        self.volume_cylindre_base_radius_h.setText(QCoreApplication.translate("MainWindow",
                                                                              u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043c\u0430 \u0446\u0438\u043b\u0438\u043d\u0434\u0440\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0440\u0430\u0434\u0438\u0443\u0441 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u0432\u044b\u0441\u043e\u0442\u0430.",
                                                                              None))
        self.surface_area_cylinder_base_r_h.setText(QCoreApplication.translate("MainWindow",
                                                                               u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438 \u0446\u0438\u043b\u0438\u043d\u0434\u0440\u0430, \u0435\u0441\u043b\u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u0440\u0430\u0434\u0438\u0443\u0441 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0438\n"
                                                                               "\u0432\u044b\u0441\u043e\u0442\u0430. ",
                                                                               None))
        self.volume_of_parallelepiped.setText(QCoreApplication.translate("MainWindow",
                                                                         u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043c\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u0435\u043f\u0438\u043f\u0435\u0434\u0430 \u043f\u043e \u0442\u0440\u0435\u043c \u0435\u0433\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\u043c",
                                                                         None))
        self.distance_conversion_from_miles_to_km.setText(QCoreApplication.translate("MainWindow",
                                                                                     u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0441\u0447\u0435\u0442\u0430 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0438\u0437 \u0432\u0435\u0440\u0441\u0442 \u0432 \u043a\u0438\u043b\u043e\u043c\u0435\u0442\u0440\u044b.",
                                                                                     None))
    # retranslateUi
