import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QApplication

from ui.py_ui.start_window import Ui_MainWindow


def load_stylesheet(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    app = QApplication(sys.argv)

    style_path = 'style/style.css'
    style = load_stylesheet(style_path)
    app.setStyleSheet(style)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()


if __name__ == "__main__":
    main()
