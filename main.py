from PyQt5.QtWidgets import QApplication
from ui.app import MainWindow


def main() -> None:
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec_()


if __name__ == "__main__":
    main()
