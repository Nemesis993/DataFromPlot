# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:50:10 2023

@author: Baumann
"""

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QHBoxLayout, \
    QPushButton, QVBoxLayout, QApplication, \
    QMainWindow, QWidget, QLabel, QFileDialog, \
        QLineEdit, QInputDialog
from PySide6.QtGui import QPalette, QColor, QPixmap, QPainter


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        
class ImageWidget(QWidget):

    def __init__(self, fileName=None):
        super().__init__()
        self.pic = QLabel(self)
        self.setFixedSize(800,600)
        if not fileName:
            self.pic.setPixmap(QPixmap("images/test_image_0.png").scaled(QSize(1, 1), Qt.KeepAspectRatio)) #scaled(pic.size()))
        else:
            self.pic.setPixmap(QPixmap(fileName).scaled(QSize(800,600), Qt.KeepAspectRatio))
        self.pic.setScaledContents(True)
        self.mouse_pressed_l = False
        self.mouse_location_l = (0,0)
            
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("left")
            print(event.pos().x(), event.pos().y())
            self.mouse_pressed_l = True     
            self.mouse_location_l = ()
        elif event.button() == Qt.MouseButton.RightButton:
            print("right")

    #def open_file(self, fileName):
     #   self.pic.setPixmap(QPixmap(fileName).scaled(QSize(800,600), Qt.KeepAspectRatio))
        #self.show()

        
        
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.state = 'init'
        
        self.setWindowTitle('DataFromPlot')
        #self.resize(800,500)
        
        self.Axis = {'x':(0.0, 0.0), 'y':(0.0, 0.0)}
        
        layout_main = QVBoxLayout()
        layout_htop = QHBoxLayout()
        layout_h1 = QHBoxLayout()
        layout_vl = QVBoxLayout()
        self.layout_vm = QVBoxLayout()
        layout_vr = QVBoxLayout()

        layout_h1.setContentsMargins(0,0,0,0)
        layout_h1.setSpacing(20)
        
        # left side  ------------------------------------------------
        self.button_new_axis = QPushButton("New Axis")
        self.button_new_axis.setCheckable(True)
        self.button_new_axis.clicked.connect(self.new_axis)
        layout_vl.addWidget(self.button_new_axis)
        layout_vl.addWidget(Color('red'))
        layout_vl.addWidget(Color('yellow'))
        layout_vl.addWidget(Color('purple'))

        layout_h1.addLayout(layout_vl, 1)

        # main widget  ------------------------------------------------
        #layout1.addWidget(Color('green'), 4)
        self.main_widget = ImageWidget()
        self.layout_vm.addWidget(self.main_widget)#, 4)
        #self.pic = QLabel(self)
        #layout_vm.addWidget(self.pic, 4)
        #self.pic.setPixmap(QPixmap("images/test_image_0.png").scaled(QSize(1, 1), Qt.KeepAspectRatio)) #scaled(pic.size()))
        #self.pic.setScaledContents(True)
        self.layout_vm.addWidget(Color('green'))#, 4)
        layout_h1.addLayout(self.layout_vm, 4)
        #pic.show()

        # right side  ------------------------------------------------
        button = QPushButton("New Data")
        button.clicked.connect(self.new_data)
        #button.setCheckable(True)
        layout_vr.addWidget(button)
        
        button = QPushButton("Delete Data-Point")
        button.clicked.connect(self.delete_datapoint)
        #button.setCheckable(True)
        layout_vr.addWidget(button)
        
        button = QPushButton("Show Data")
        button.clicked.connect(self.show_data)
        layout_vr.addWidget(button)
        layout_vr.addWidget(Color('red'))
        layout_vr.addWidget(Color('purple'))
        
        layout_h1.addLayout(layout_vr, 1)
        
        
        # top toolbar ------------------------------------------------
        button = QPushButton("Open Image")
        button.clicked.connect(self.open_file)
        layout_htop.addWidget(button)
        
        button = QPushButton("Tools")
        button.clicked.connect(self.the_button_was_clicked)
        layout_htop.addWidget(button)
        
        layout_htop.addWidget(Color('purple'))
        layout_main.addLayout(layout_htop)
        layout_main.addLayout(layout_h1)


        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        print("Clicked!")
    
    def new_axis(self):
        self.main_widget.mouse_pressed_l = False
        text, ok = QInputDialog.getText(self, "New Axis Name",\
                                "Name:", QLineEdit.Normal)
        if ok and text:
            #location = Qt.MouseButton.LeftButton()
            location = (100, 100)
            self.draw_something(location)
            
    def draw_something(self, location):
        canvas = self.main_widget.pic.pixmap()
        painter = QPainter(canvas)
        painter.drawEllipse(location, 10, 10)
        painter.end()
        self.main_widget.pic.setPixmap(canvas)
    
    def show_data(self):
        pass
    
    def new_data(self):
        pass
    
    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Image", "home/Documents/PythonProjects/DataFromPlot/images/")
        print(fileName[0])
        #self.main_widget.close()
        new_main = ImageWidget(fileName[0])
        self.layout_vm.replaceWidget(self.main_widget, new_main)
        self.main_widget.close()
        self.main_widget = new_main
    
    def delete_datapoint(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    #window.resize(800,500)
    window.show()
    
    app.exec()
    #sys.exit(app.exec_())