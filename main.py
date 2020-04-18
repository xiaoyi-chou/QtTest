# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

# All pictures
all_pic = []
for file in os.listdir():
    if file.endswith('.png') | file.endswith('.jpg'):
        all_pic.append(file)
print(all_pic)

# Keep records
f = 'Output.txt'
if os.stat(f).st_size == 0:
    text_file = open(f, 'a+')
    text_file.write('file_name,categories,start_x,start_y,end_x,end_y' + '\n')
    text_file.close()
        
n = 0

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        #self.setGeometry(30,30,600,400)
        #self.image = QPixmap('CatHeart.png')
        #self.setPixmap(QPixmap('CatHeart.png'))
        """
        ly = QVBoxLayout()
        ly_bt = QHBoxLayout()
        
        btn_prev = QPushButton('Previous')
        btn_next = QPushButton('Next')
        ly.addWidget(btn1)
        #self.label = QLabel(self)
        """
        
        self.begin = QPoint()
        self.end = QPoint()
        self.show()

    def paintEvent(self, event):
        """
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40))   
        # Set QBrush, then called by QRect to draw rectangular
        qp.setBrush(br)   
        qp.drawRect(QRect(self.begin, self.end)) 
        """
        """
        painter = QPainter(self)
        img = QPixmap('CatHeart.png')
        painter.drawPixmap(self.rect(), img)
        painter.setPen(QPen(Qt.red, 5))
        painter.drawRect(40, 40, 400, 200)
        """
        painter = QPainter(self)
        #img = QPixmap('CatHeart.png')
        img = QPixmap(all_pic[n])
        painter.setBrush(QBrush(QColor(100, 10, 10, 40)))
        painter.drawPixmap(self.rect(), img)
        painter.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()
        #print(str(self.begin)[19:])
        #print(str(self.end)[19:])
        global st
        st = str(self.begin)[19:]
        
        #return str(self.begin)[19:]

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        #print(str(self.end)[19:])
        #MainWindow.lb_xy1.setText(str(begin))
        #MainWindow.updatePos(self)#, self.begin, self.end)
        global ed
        ed = str(self.end)[19:]
        
        #self.label.setText(str(self.end)[19:])
        #print(self.label.text())

    def mouseReleaseEvent(self, event):
        #self.begin = event.pos()
        self.end = event.pos()
        self.update()
        #print(str(self.begin)[19:])
        #print(str(self.end)[19:])
        global ed
        ed = str(self.end)[19:]
        
        
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        self.setGeometry(100,100,600,900)
        
        # QStackedWidget is exactly how tabbed views in applications work. 
        # Only one view ('tab') is visible at any one time. 
        # You can control which widget to show at any time by using .setCurrentIndex() 
        # or .setCurrentWidget() to set the item by either the index (in order the 
        # widgets were added) or by the widget itself.
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.image_layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.image_layout)
        
        btn1 = QPushButton('Heart')
        btn2 = QPushButton('Cat')
        btn3 = QPushButton('TV')
        btn4 = QPushButton('Save')
        self.lb_cate = QLabel(self)
        self.lb_xy1 = QLabel(self)
        self.lb_xy2 = QLabel(self)
        
        
        btn_prev = QPushButton('Previous')
        btn_next = QPushButton('Next')
        
        button_layout.addWidget(btn_prev)
        button_layout.addWidget(btn_next)
        
        button_layout.addWidget(btn1)  
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)       
        button_layout.addWidget(btn4)
        button_layout.addWidget(self.lb_cate)
        button_layout.addWidget(self.lb_xy1)
        button_layout.addWidget(self.lb_xy2)
        
        #img = QLabel(self)
        #img.setPixmap(QPixmap('CatHeart.png'))
        
        #image_layout.addWidget(img)
        self.mw = MyWidget()
        self.image_layout.addWidget(self.mw)
        
        #MyWidget.mousePressEvent.connect(updatePos(str(MyWidget.begin)))
        
        """
        for n, color in enumerate(['red','green','blue','yellow']):
            btn = QPushButton( str(color) )
            btn.pressed.connect( lambda n = n: layout.setCurrentIndex(n) )
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))
        """
        
        btn1.clicked.connect(self.on_click1)
        btn2.clicked.connect(self.on_click2)
        btn3.clicked.connect(self.on_click3)
        btn4.clicked.connect(self.on_clickSave)
        
        btn_prev.clicked.connect(self.prevPic)
        btn_next.clicked.connect(self.nextPic)
        
        #self.lb_xy1.setText(str(MyWidget.begin))
        
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    
    def on_clickSave(self):
        self.lb_xy1.setText(st)
        self.lb_xy2.setText(ed)
        
        #coordinate = st + ed
        coordinate =all_pic[n] + "," + self.lb_cate.text() + "," + (st[1:-1] + ',' + ed[1:-1]).replace(' ', '')
        text_file = open('Output.txt', 'a+')  # use 'a' to append  # use 'w' to recreate
        text_file.write(coordinate + '\n')
        text_file.close()
        
        # The dimension of coordinates can exceed the image size.
        # Should get image size and set min and max height and width.
    
    def on_click1(self):
        #sending_button = self.sender()
        self.lb_cate.setText('Heart')
    
    def on_click2(self):
        #sending_button = self.sender()
        self.lb_cate.setText('Cat')
    
    def on_click3(self):
        #sending_button = self.sender()
        self.lb_cate.setText('TV')
    
    """
    def mousePressEvent(self, event):
        self.lb_xy1.setText(st)
        
    def mouseMoveEvent(self, event):
        self.lb_xy2.setText(ed)
    
    def mouseReleaseEvent(self, event):
        self.lb_xy2.setText(ed)
        
    """
    
    def prevPic(self):
        global n
        n = max(n - 1, 0)
        self.image_layout.removeWidget(self.mw)
        self.image_layout.addWidget(self.mw)
    
    def nextPic(self):
        global n
        n = min(n + 1, len(all_pic)-1)
        self.image_layout.removeWidget(self.mw)
        self.image_layout.addWidget(self.mw)
        
        

app = QApplication(sys.argv)  # able to pass command line into application
#app = QApplication([])  # if no command line

window = MainWindow()
window.show()  # MUST SHOW!

app.exec_()  # exec is defauld in Python