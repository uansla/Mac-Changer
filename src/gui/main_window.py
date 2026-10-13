from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("网卡管理工具 Pro")
        self.resize(800, 500)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        title = QLabel("网卡管理工具 Pro")
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels([
            "网卡名称",
            "MAC地址",
            "状态"
        ])

        layout.addWidget(title)
        layout.addWidget(self.table)

        central.setLayout(layout)
        self.setCentralWidget(central)
