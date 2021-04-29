import sys
from operations import *

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

ap = QApplication([])
win =  QWidget()

win.setStyleSheet(open('parwindowstyling.css').read())
win.setWindowTitle("Calculator")

lay = QGridLayout()
win.setLayout(lay)
#win.setGeometry(150,150,400,600)


#buttons
line = QLineEdit()
one = QPushButton("1")
two = QPushButton("2")
three = QPushButton("3")
four = QPushButton("4")
five = QPushButton("5")
six = QPushButton("6")
seven = QPushButton("7")
eight = QPushButton("8")
nine = QPushButton("9")
zero = QPushButton("0")
dot = QPushButton(".")
plus = QPushButton("+")
minus = QPushButton("-")
multiply = QPushButton("x")
divide = QPushButton("÷")
equal = QPushButton("=")
power = QPushButton("^")
clear = QPushButton("CLR")

#coloring
one.setStyleSheet(open('styling.css').read())
two.setStyleSheet(open('styling.css').read())
three.setStyleSheet(open('styling.css').read())
four.setStyleSheet(open('styling.css').read())
five.setStyleSheet(open('styling.css').read())
six.setStyleSheet(open('styling.css').read())
seven.setStyleSheet(open('styling.css').read())
eight.setStyleSheet(open('styling.css').read())
nine.setStyleSheet(open('styling.css').read())
zero.setStyleSheet(open('styling.css').read())
dot.setStyleSheet(open('styling.css').read())
plus.setStyleSheet(open('altstyling.css').read())
minus.setStyleSheet(open('altstyling.css').read())
multiply.setStyleSheet(open('altstyling.css').read())
divide.setStyleSheet(open('altstyling.css').read())
equal.setStyleSheet(open('altstyling.css').read())
power.setStyleSheet(open('altstyling.css').read())
clear.setStyleSheet(open('parwindowstyling.css').read())

#row 1
lay.addWidget(line,1,1,2,4)
#row 2
lay.addWidget(one,3,1)
lay.addWidget(two,3,2)
lay.addWidget(three,3,3)
lay.addWidget(plus,3,4)
#row 3
lay.addWidget(four,4,1)
lay.addWidget(five,4,2)
lay.addWidget(six,4,3)
lay.addWidget(minus,4,4)
#row 4
lay.addWidget(seven,5,1)
lay.addWidget(eight,5,2)
lay.addWidget(nine,5,3)
lay.addWidget(multiply,5,4)
#row 5
lay.addWidget(power,6,1)
lay.addWidget(dot,6,2)
lay.addWidget(zero,6,3)
lay.addWidget(divide,6,4)
#row 6
lay.addWidget(equal,7,1,1,3)
lay.addWidget(clear,7,4)

#functions

def a1():
    x = line.text()
    x += "1"
    line.setText(x)
    

def a2():
    x = line.text()
    x += "2"
    line.setText(x)
    

def a3():
    x = line.text()
    x += "3"
    line.setText(x)

def a4():
    x = line.text()
    x += "4"
    line.setText(x)

def a5():
    x = line.text()
    x += "5"
    line.setText(x)

def a6():
    x = line.text()
    x += "6"
    line.setText(x)

def a7():
    x = line.text()
    x += "7"
    line.setText(x)

def a8():
    x = line.text()
    x += "8"
    line.setText(x)

def a9():
    x = line.text()
    x += "9"
    line.setText(x)

def a0():
    x = line.text()
    x += "0"
    line.setText(x)

def aplus():
    x = line.text()
    x += "+"
    line.setText(x)

def aminus():
    x = line.text()
    x += "-"
    line.setText(x)

def amult():
    x = line.text()
    x += "x"
    line.setText(x)

def adiv():
    x = line.text()
    x += "÷"
    line.setText(x)

def adot():
    x = line.text()
    x += "."
    line.setText(x)

def apower():
    x = line.text()
    x += "^"
    line.setText(x)

def clr():
    line.setText("")

def eq():
    x = line.text()
    s = solution(x)
    line.setText(str(s))
    

#connections
one.clicked.connect(a1)
two.clicked.connect(a2)
three.clicked.connect(a3)
four.clicked.connect(a4)
five.clicked.connect(a5)
six.clicked.connect(a6)
seven.clicked.connect(a7)
eight.clicked.connect(a8)
nine.clicked.connect(a9)
zero.clicked.connect(a0)
dot.clicked.connect(adot)
plus.clicked.connect(aplus)
minus.clicked.connect(aminus)
multiply.clicked.connect(amult)
divide.clicked.connect(adiv)
power.clicked.connect(apower)
equal.clicked.connect(eq)
clear.clicked.connect(clr)

win.show()
sys.exit(ap.exec_())

