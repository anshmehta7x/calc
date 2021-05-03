import sys
from operations import solution
from operations import trigerrcheck

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QSlider
from PyQt5 import QtGui


from PyQt5.Qt import Qt

ap = QApplication([])
win =  QWidget()

win.setStyleSheet(open('parwindowstyling.css').read())
win.setWindowTitle("Calculator")
win.setWindowIcon(QtGui.QIcon('icon.png'))
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
trig = QPushButton("Trig")
log = QPushButton("Log")

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
trig.setStyleSheet(open('parwindowstyling.css').read())
line.setStyleSheet(open('styling.css').read())
log.setStyleSheet(open('parwindowstyling.css').read())


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
#row 7
lay.addWidget(trig,8,1,1,2)
lay.addWidget(log,8,3,1,2)



#trig window
class trigwin(QWidget):

    def __init__(self):
        super().__init__()
        self.makeui()
    
    def inv(self):
        if self.invert.isChecked() == True:
            self.is_inverse = True
            self.sin.setText("sin⁻¹")
            self.cos.setText("cos⁻¹")
            self.tan.setText("tan⁻¹")
            self.csc.setText("csc⁻¹")
            self.sec.setText("sec⁻¹")
            self.cot.setText("cot⁻¹")
        else:
            self.is_inverse = False
            self.sin.setText("sin")
            self.cos.setText("cos")
            self.tan.setText("tan")
            self.csc.setText("csc")
            self.sec.setText("sec")
            self.cot.setText("cot")
    
    def angle_mode(self):
        if self.degrad.value() == 2:
            self.mode = False
            self.switchlabel.setText("Rad")
        elif self.degrad.value() == 1:
            self.mode = True
            self.switchlabel.setText("Deg")


    def b1(self):
        x = self.line.text()
        x += "1"
        self.line.setText(x)
    
    def b2(self):
        x = self.line.text()
        x += "2"
        self.line.setText(x)
    
    def b3(self):
        x = self.line.text()
        x += "3"
        self.line.setText(x)

    def b4(self):
        x = self.line.text()
        x += "4"
        self.line.setText(x)

    def b5(self):
        x = self.line.text()
        x += "5"
        self.line.setText(x)
    
    def b6(self):
        x = self.line.text()
        x += "6"
        self.line.setText(x)

    def b7(self):
        x = self.line.text()
        x += "7"
        self.line.setText(x)
    
    def b8(self):
        x = self.line.text()
        x += "8"
        self.line.setText(x)

    def b9(self):
        x = self.line.text()
        x += "9"
        self.line.setText(x)
    
    def b0(self):
        x = self.line.text()
        x += "0"
        self.line.setText(x)

    def bdot(self):
        x = self.line.text()
        x += "."
        self.line.setText(x)
    
    def bpi(self):
        x = self.line.text()
        x += "π"
        self.line.setText(x)
    
    def beq(self, op):
        x = trigerrcheck(self.line.text(),op,self.is_inverse,self.mode)
        self.line.setText(str(x))

    def makeui(self):

        self.setWindowTitle("Trigonometry")
        self.setWindowIcon(QtGui.QIcon('trigicon.png'))
        self.is_inverse = False
        '''True is degrees mode,
         False is Radians'''
        self.mode = True
        self.setStyleSheet(open('parwindowstyling.css').read())
        self.l = QGridLayout()
        self.one = QPushButton("1")
        self.two = QPushButton("2")
        self.three = QPushButton("3")
        self.four = QPushButton("4")
        self.five = QPushButton("5")
        self.six = QPushButton("6")
        self.seven = QPushButton("7")
        self.eight = QPushButton("8")
        self.nine = QPushButton("9")
        self.zero = QPushButton("0")
        self.dot = QPushButton(".")
        self.pi = QPushButton("π")
        self.line = QLineEdit()
        self.sin = QPushButton("sin")
        self.cos = QPushButton("cos")
        self.tan = QPushButton("tan")
        self.csc = QPushButton("csc")
        self.sec = QPushButton("sec")
        self.cot = QPushButton("cot")
        self.invert = QCheckBox("Invert")
        self.degrad = QSlider(Qt.Horizontal)
        self.switchlabel = QLabel("Deg")
        #slider for degrees/radians
        self.degrad.setMaximum(2)
        self.degrad.setMinimum(1)
        self.degrad.setValue(1)


        #colors
        self.sin.setStyleSheet(open('altstyling.css').read())
        self.cos.setStyleSheet(open('altstyling.css').read())
        self.tan.setStyleSheet(open('altstyling.css').read())
        self.csc.setStyleSheet(open('altstyling.css').read())
        self.sec.setStyleSheet(open('altstyling.css').read())
        self.cot.setStyleSheet(open('altstyling.css').read())
        self.invert.setStyleSheet(open('altstyling.css').read())
        self.switchlabel.setStyleSheet(open('altstyling.css').read())

        self.switchlabel.setAlignment(Qt.AlignCenter)


        self.l.addWidget(self.line,1,1,1,3)
        self.l.addWidget(self.one,2,1)
        self.l.addWidget(self.two,2,2)
        self.l.addWidget(self.three,2,3)
        self.l.addWidget(self.four,3,1)
        self.l.addWidget(self.five,3,2)
        self.l.addWidget(self.six,3,3)
        self.l.addWidget(self.seven,4,1)
        self.l.addWidget(self.eight,4,2)
        self.l.addWidget(self.nine,4,3)
        self.l.addWidget(self.dot,5,1)
        self.l.addWidget(self.zero,5,2)
        self.l.addWidget(self.pi,5,3)
        self.l.addWidget(self.sin,6,1)
        self.l.addWidget(self.cos,6,2)
        self.l.addWidget(self.tan,6,3)
        self.l.addWidget(self.csc,7,1)
        self.l.addWidget(self.sec,7,2)
        self.l.addWidget(self.cot,7,3)
        self.l.addWidget(self.invert,8,1)
        self.l.addWidget(self.switchlabel,8,3)
        self.l.addWidget(self.degrad,8,2)
        
        #connections

        self.invert.toggled.connect(self.inv)
        self.degrad.valueChanged.connect(self.angle_mode)


        self.one.clicked.connect(self.b1)
        self.two.clicked.connect(self.b2)
        self.three.clicked.connect(self.b3)
        self.four.clicked.connect(self.b4)
        self.five.clicked.connect(self.b5)
        self.six.clicked.connect(self.b6)
        self.seven.clicked.connect(self.b7)
        self.eight.clicked.connect(self.b8)
        self.nine.clicked.connect(self.b9)
        self.zero.clicked.connect(self.b0)
        self.dot.clicked.connect(self.bdot)
        self.pi.clicked.connect(self.bpi)

        self.sin.clicked.connect(lambda: self.beq("sin"))
        self.cos.clicked.connect(lambda: self.beq("cos"))
        self.tan.clicked.connect(lambda: self.beq("tan"))
        self.csc.clicked.connect(lambda: self.beq("csc"))
        self.sec.clicked.connect(lambda: self.beq("sec"))
        self.cot.clicked.connect(lambda: self.beq("cot"))

        #set layout
        self.setLayout(self.l)

#log window
class logwin(QWidget):

    def __init__(self):
        super().__init__()
        self.makeui()
    
    def makeui(self):
        self.setWindowTitle("Logarithms")
        self.setStyleSheet(open('parwindowstyling.css').read())
        self.l = QGridLayout()
        self.setLayout(self.l)

        #input fields
        self.inplabel = QLabel("Input:")
        self.inp = QLineEdit()
        self.baselabel = QLabel("Base:")
        self.base = QLineEdit()
        self.outputlabel = QLabel("Output")
        self.output = QLabel()

        #numbers
        self.one = QPushButton("1")
        self.two = QPushButton("2")
        self.three = QPushButton("3")
        self.four = QPushButton("4")
        self.five = QPushButton("5")
        self.six = QPushButton("6")
        self.seven = QPushButton("7")
        self.eight = QPushButton("8")
        self.nine = QPushButton("9")
        self.zero = QPushButton("0")
        self.dot = QPushButton(".")
        self.e = QPushButton("e")

        #layout
        self.l.addWidget(self.inplabel,1,1)
        self.l.addWidget(self.inp,1,2,1,2)
        self.l.addWidget(self.baselabel,2,1)
        self.l.addWidget(self.base,2,2,1,2)
        self.l.addWidget(self.outputlabel,3,1)
        self.l.addWidget(self.output,3,2,1,2)
        self.l.addWidget(self.one,4,1)
        self.l.addWidget(self.two,4,2)
        self.l.addWidget(self.three,4,3)
        self.l.addWidget(self.four,5,1)
        self.l.addWidget(self.five,5,2)
        self.l.addWidget(self.six,5,3)
        self.l.addWidget(self.seven,6,1)
        self.l.addWidget(self.eight,6,2)
        self.l.addWidget(self.nine,6,3)
        self.l.addWidget(self.dot,7,1)
        self.l.addWidget(self.zero,7,2)
        self.l.addWidget(self.e,7,3)

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

def tr():   
    global polnareff
    polnareff = trigwin()
    polnareff.show()

def lo():
    global kakyoin
    kakyoin = logwin()
    kakyoin.show()

    
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
line.returnPressed.connect(eq)
trig.clicked.connect(tr)
log.clicked.connect(lo)

win.show()
sys.exit(ap.exec_())

