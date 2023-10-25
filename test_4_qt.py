
import sys
from PySide6.QtWidgets import *

from PySide6.QtCore import Slot, QFile, QRectF, Qt
#%


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        
        self.setWindowTitle('DataFromPlot')
        self.setCentralWidget(widget)
        
        
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+C")

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Example data
        self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
                      "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
                      "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}
        
        self.items = 0
        
        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Right
        self.description = QLineEdit()
        self.description.setClearButtonEnabled(True)
        self.price = QLineEdit()
        self.price.setClearButtonEnabled(True)
 
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
 
        form_layout = QFormLayout()
        form_layout.addRow("Description", self.description)
        form_layout.addRow("Price", self.price)
        self.right = QVBoxLayout()
        self.right.addLayout(form_layout)
        self.right.addWidget(self.add)
        self.right.addStretch()
        self.right.addWidget(self.clear)
       
        # image
        #self.scene = QGraphicsScene()
        #self.rect = self.scene.addRect(QRectF(0, 0, 100, 100))
        #item = scene.itemAt(50, 50, QTransform())
        
        
       
        # QWidget Layout
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.table)
        #self.layout.addWidget(self.scene)
        self.layout.addLayout(self.right)

        # Fill example data
        self.fill_table()
        
        # Signals and Slots
        self.add.clicked.connect(self.add_element)
        self.clear.clicked.connect(self.clear_table)
        
        
        
        
        
    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, QTableWidgetItem(desc))
            self.table.setItem(self.items, 1, QTableWidgetItem(str(price)))
            self.items += 1
    
    @Slot()
    def add_element(self):
        des = self.description.text()
        price = self.price.text()

        self.table.insertRow(self.items)
        self.table.setItem(self.items, 0, QTableWidgetItem(des))
        self.table.setItem(self.items, 1, QTableWidgetItem(price))

        self.description.clear()
        self.price.clear()

        self.items += 1

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, QTableWidgetItem(desc))
            self.table.setItem(self.items, 1, QTableWidgetItem(str(price)))
            self.items += 1

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    window.resize(1000,800)
    window.show()

    #Execute
    sys.exit(app.exec())

    