import sys

from operations import solution
from operations import trigerrcheck
from operations import logsolve

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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

ap = QApplication([])
win =  QWidget()

win.setStyleSheet(open('styles/parwindowstyling.css').read())
win.setWindowTitle("Calculator")
win.setWindowIcon(QtGui.QIcon('assets/icon.png'))
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
quad = QPushButton("Quadratic")

#coloring
one.setStyleSheet(open("styles/styling.css").read())
two.setStyleSheet(open("styles/styling.css").read())
three.setStyleSheet(open("styles/styling.css").read())
four.setStyleSheet(open("styles/styling.css").read())
five.setStyleSheet(open("styles/styling.css").read())
six.setStyleSheet(open("styles/styling.css").read())
seven.setStyleSheet(open("styles/styling.css").read())
eight.setStyleSheet(open("styles/styling.css").read())
nine.setStyleSheet(open("styles/styling.css").read())
zero.setStyleSheet(open("styles/styling.css").read())
dot.setStyleSheet(open("styles/styling.css").read())
plus.setStyleSheet(open("styles/altstyling.css").read())
minus.setStyleSheet(open("styles/altstyling.css").read())
multiply.setStyleSheet(open("styles/altstyling.css").read())
divide.setStyleSheet(open("styles/altstyling.css").read())
equal.setStyleSheet(open("styles/altstyling.css").read())
power.setStyleSheet(open("styles/altstyling.css").read())
clear.setStyleSheet(open('styles/parwindowstyling.css').read())
trig.setStyleSheet(open('styles/parwindowstyling.css').read())
line.setStyleSheet(open("styles/styling.css").read())
log.setStyleSheet(open('styles/parwindowstyling.css').read())
quad.setStyleSheet(open('styles/parwindowstyling.css').read())

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
#row 8
lay.addWidget(quad,9,1,1,4)



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
        
    def b(self, numbr):
        x = str(numbr)
        y = self.line.text()
        y += x
        self.line.setText(y)
    
    def beq(self, op):
        x = trigerrcheck(self.line.text(),op,self.is_inverse,self.mode)
        self.line.setText(str(x))

    def makeui(self):

        self.setWindowTitle("Trigonometry")
        self.setWindowIcon(QtGui.QIcon('assets/trigicon.png'))
        self.is_inverse = False
        '''True is degrees mode,
         False is Radians'''
        self.mode = True
        self.setStyleSheet(open('styles/parwindowstyling.css').read())
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
        self.sin.setStyleSheet(open("styles/altstyling.css").read())
        self.cos.setStyleSheet(open("styles/altstyling.css").read())
        self.tan.setStyleSheet(open("styles/altstyling.css").read())
        self.csc.setStyleSheet(open("styles/altstyling.css").read())
        self.sec.setStyleSheet(open("styles/altstyling.css").read())
        self.cot.setStyleSheet(open("styles/altstyling.css").read())
        self.invert.setStyleSheet(open("styles/altstyling.css").read())
        self.switchlabel.setStyleSheet(open("styles/altstyling.css").read())

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


        self.one.clicked.connect(lambda: self.b(1))
        self.two.clicked.connect(lambda: self.b(2))
        self.three.clicked.connect(lambda: self.b(3))
        self.four.clicked.connect(lambda: self.b(4))
        self.five.clicked.connect(lambda: self.b(5))
        self.six.clicked.connect(lambda: self.b(6))
        self.seven.clicked.connect(lambda: self.b(7))
        self.eight.clicked.connect(lambda: self.b(8))
        self.nine.clicked.connect(lambda: self.b(9))
        self.zero.clicked.connect(lambda: self.b(0))
        self.dot.clicked.connect(lambda: self.b("."))
        self.pi.clicked.connect(lambda: self.b("π"))

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

    #functions
    def switch(self):
        if self.inpbase == True:
            self.inpORbase.setText("base")
            self.inpORbase.setStyleSheet(open("styles/styling.css").read())
            self.inpbase = False

        elif self.inpbase == False:
            self.inpORbase.setText("input")
            self.inpORbase.setStyleSheet(open("styles/altstyling.css").read())
            self.inpbase = True

    def c(self, num):
        numb = str(num)
        if self.inpbase == True:
            x = self.inp.text()
            x += numb
            self.inp.setText(x)
        elif self.inpbase == False:
            x = self.base.text()
            x += numb
            self.base.setText(x)

    def out(self):
        i = self.inp.text()
        b = self.base.text()
        to_set = logsolve(i,b)
        self.output.setText(str(to_set))

        
    def makeui(self):

        self.inpbase = True
        ''' True is input
            False is base'''

        self.setWindowTitle("Logarithms")
        self.setStyleSheet(open('styles/parwindowstyling.css').read())
        self.setWindowIcon(QtGui.QIcon("assets/logicon.png"))
        self.l = QGridLayout()
        self.setLayout(self.l)

        #input fields
        self.inplabel = QLabel("Input:")
        self.inp = QLineEdit()
        self.baselabel = QLabel("Base:")
        self.base = QLineEdit()
        self.outputlabel = QLabel("Output:")
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

        #equal
        self.equal = QPushButton("=")
        self.equal.setStyleSheet(open("styles/altstyling.css").read())

        #switch
        self.inpORbase = QPushButton("input")
        self.inpORbase.setStyleSheet(open("styles/altstyling.css").read())

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
        self.l.addWidget(self.equal,8,1,1,2)
        self.l.addWidget(self.inpORbase,8,3)

        #connections
        self.inpORbase.clicked.connect(lambda: self.switch())
        self.equal.clicked.connect(lambda: self.out())
        self.e.clicked.connect(lambda: self.c("e"))
######################## logwin end

class quadwin(QWidget):
    def __init__(self):
        super().__init__()
        self.makeui()

    def operation(self):
        print("yeet")
        pass
        
    def clr(self):
        self.abox.setText("")
        self.bbox.setText("")
        self.cbox.setText("")
    
    def setbox(self,mode):
        if mode == "a":
            self.mode = self.abox
        elif mode == "b":
            self.mode = self.bbox
        else:
            self.mode = self.cbox

    def d(self,numbr):
        x = str(numbr)
        y = self.mode.text()
        y += x
        self.mode.setText(y)

    def makeui(self):
        
        self.setWindowTitle("Quadratics")
        self.l = QGridLayout()
        self.setLayout(self.l)
        self.setStyleSheet(open('styles/parwindowstyling.css').read())

        #fields
        self.toplabel = QLabel("a𝑥²+b𝑥+c")
        self.guidelabel = QLabel("Enter value for:")
        self.alabel = QPushButton("    a :")
        self.abox = QLineEdit()
        self.blabel = QPushButton("    b :")
        self.bbox = QLineEdit()
        self.clabel = QPushButton("    c :")
        self.cbox = QLineEdit()
        self.equal = QPushButton("=")
        self.output = QLabel("")
        self.clear = QPushButton("CLR")
        self.equal.setStyleSheet(open("styles/altstyling.css").read())
        self.clear.setStyleSheet(open("styles/altstyling.css").read())
        self.alabel.setStyleSheet(open("styles/styling.css").read())
        self.blabel.setStyleSheet(open("styles/styling.css").read())
        self.clabel.setStyleSheet(open("styles/styling.css").read())

        #defaut config
        self.mode = self.alabel
        
        #nuumbers
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

        #layout
        self.l.addWidget(self.toplabel,1,1,1,3)
        self.l.addWidget(self.guidelabel,2,1,1,3)
        self.l.addWidget(self.alabel,3,1)
        self.l.addWidget(self.abox,3,2,1,2)
        self.l.addWidget(self.blabel,4,1)
        self.l.addWidget(self.bbox,4,2,1,2)
        self.l.addWidget(self.clabel,5,1)
        self.l.addWidget(self.cbox,5,2,1,2)
        self.l.addWidget(self.equal,6,1,1,3)
        self.l.addWidget(self.one,8,1)
        self.l.addWidget(self.two,8,2)
        self.l.addWidget(self.three,8,3)
        self.l.addWidget(self.four,9,1)
        self.l.addWidget(self.five,9,2)
        self.l.addWidget(self.six,9,3)
        self.l.addWidget(self.seven,10,1)
        self.l.addWidget(self.eight,10,2)
        self.l.addWidget(self.nine,10,3)
        self.l.addWidget(self.dot,11,1)
        self.l.addWidget(self.zero,11,2)
        self.l.addWidget(self.clear,11,3)

        self.clear.clicked.connect(self.clr)
        self.equal.clicked.connect(lambda: self.operation())
        self.alabel.clicked.connect(lambda: self.setbox("a"))
        self.blabel.clicked.connect(lambda: self.setbox("b"))
        self.clabel.clicked.connect(lambda: self.setbox("c"))
        self.one.clicked.connect(lambda: self.d(1))
        self.two.clicked.connect(lambda: self.d(2))
        self.three.clicked.connect(lambda: self.d(3))
        self.four.clicked.connect(lambda: self.d(4))
        self.five.clicked.connect(lambda: self.d(5))
        self.six.clicked.connect(lambda: self.d(6))
        self.seven.clicked.connect(lambda: self.d(7))
        self.eight.clicked.connect(lambda: self.d(8))
        self.nine.clicked.connect(lambda: self.d(9))
        self.zero.clicked.connect(lambda: self.d(0))
        self.dot.clicked.connect(lambda: self.d("."))
#functions

def a(n):
    x = str(n)
    y = line.text()
    y += x
    line.setText(y)

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

def qu():
    global speedwagon
    speedwagon = quadwin()
    speedwagon.show()

#connections

one.clicked.connect(lambda: a(1))
two.clicked.connect(lambda: a(2))
three.clicked.connect(lambda: a(3))
four.clicked.connect(lambda: a(4))
five.clicked.connect(lambda: a(5))
six.clicked.connect(lambda: a(6))
seven.clicked.connect(lambda: a(7))
eight.clicked.connect(lambda: a(8))
nine.clicked.connect(lambda: a(9))
zero.clicked.connect(lambda: a(0))
dot.clicked.connect(lambda: a("."))
plus.clicked.connect(lambda: a("+"))
minus.clicked.connect(lambda: a("-"))
multiply.clicked.connect(lambda: a("x"))
divide.clicked.connect(lambda: a("÷"))
power.clicked.connect(lambda: a("^"))
equal.clicked.connect(eq)
clear.clicked.connect(clr)
line.returnPressed.connect(eq)
trig.clicked.connect(tr)
log.clicked.connect(lo)
quad.clicked.connect(qu)

win.show()
sys.exit(ap.exec_())