
from PyQt5 import QtWidgets
from calculator import Ui_MainWindow  # import file
import sys


class mywindow(QtWidgets.QMainWindow):
	# first number
	firstNum = None
	# numbers after first
	useristypingsecondnumber = False

	def __init__(self):

		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

        #connect buttons
		self.ui.pushButton_0.clicked.connect(self.digit_pressed)
		self.ui.pushButton_1.clicked.connect(self.digit_pressed)
		self.ui.pushButton_2.clicked.connect(self.digit_pressed)
		self.ui.pushButton_3.clicked.connect(self.digit_pressed)
		self.ui.pushButton_4.clicked.connect(self.digit_pressed)
		self.ui.pushButton_5.clicked.connect(self.digit_pressed)
		self.ui.pushButton_6.clicked.connect(self.digit_pressed)
		self.ui.pushButton_7.clicked.connect(self.digit_pressed)
		self.ui.pushButton_8.clicked.connect(self.digit_pressed)
		self.ui.pushButton_9.clicked.connect(self.digit_pressed)	
		self.ui.pushButton_tochka.clicked.connect(self.tochka)
		self.ui.pushButton_plusorminus.clicked.connect(self.unary_operation_pressed)
		self.ui.pushButton_procent.clicked.connect(self.unary_operation_pressed)
		self.ui.pushButton_plus.clicked.connect(self.plusandminusanddelitandumnojit)
		self.ui.pushButton_minus.clicked.connect(self.plusandminusanddelitandumnojit)
		self.ui.pushButton_multiply.clicked.connect(self.plusandminusanddelitandumnojit)
		self.ui.pushButton_delit.clicked.connect(self.plusandminusanddelitandumnojit)

		self.ui.pushButton_equal.clicked.connect(self.equals_pressed)
		self.ui.pushButton_clear.clicked.connect(self.clear_pressed)
		# checking "press on button"
		self.ui.pushButton_plus.setCheckable(True)
		self.ui.pushButton_minus.setCheckable(True)
		self.ui.pushButton_delit.setCheckable(True)
		self.ui.pushButton_multiply.setCheckable(True)
    #write numbers
	def digit_pressed(self):
		button = self.sender()

		if ((self.ui.pushButton_plus.isChecked() or
			self.ui.pushButton_minus.isChecked() or
			self.ui.pushButton_delit.isChecked() or
			self.ui.pushButton_multiply.isChecked() 
			) and (not self.useristypingsecondnumber)):
			newlabel = format(float(button.text()) , '.15g')
			self.useristypingsecondnumber = True
		else:
			if (('.' in self.ui.label.text()) and (button.text() == "0")):
				newlabel = format(self.ui.label.text() + button.text(),'.15')
			else:
				newlabel = format(float(self.ui.label.text() + button.text()), '.15g')


		

		self.ui.label.setText(newlabel)
    #write "."
	def tochka(self):
		self.ui.label.setText(self.ui.label.text() + ".")
    #operation +|- and %
	def unary_operation_pressed(self):
		button = self.sender()

		labelNumber = float(self.ui.label.text())

		if button.text() == "+/-":
			labelNumber = labelNumber * -1
		else: #button text == "%'
			labelNumber = labelNumber * 0.01

		newlabel = format(labelNumber, '.15g')
		self.ui.label.setText(newlabel)
    #operation +,-,\,*
	def plusandminusanddelitandumnojit(self):
		button = self.sender()
    	

		self.ui.firstNum = float(self.ui.label.text())

		button.setCheckable(True)
	# check equal
	def equals_pressed(self):

		secondNum = float(self.ui.label.text())

		if self.ui.pushButton_plus.isChecked():
			labelNumber = self.ui.firstNum + secondNum
			newlabel = format(labelNumber, '.15g')
			self.ui.label.setText(newlabel)
			self.ui.pushButton_plus.setChecked(False)

		elif self.ui.pushButton_minus.isChecked():
			labelNumber = self.ui.firstNum - secondNum
			newlabel = format(labelNumber, '.15g')
			self.ui.label.setText(newlabel)
			self.ui.pushButton_minus.setChecked(False)

		elif self.ui.pushButton_delit.isChecked():
			labelNumber = self.ui.firstNum / secondNum
			newlabel = format(labelNumber, '.15g')
			self.ui.label.setText(newlabel)
			self.ui.pushButton_delit.setChecked(False)

		elif self.ui.pushButton_multiply.isChecked():
			labelNumber = self.ui.firstNum * secondNum
			newlabel = format(labelNumber, '.15g')
			self.ui.label.setText(newlabel)
			self.ui.pushButton_multiply.setChecked(False)

		self.useristypingsecondnumber = False
	# button clear
	def clear_pressed(self):
		self.ui.pushButton_plus.setChecked(False)
		self.ui.pushButton_minus.setChecked(False)
		self.ui.pushButton_delit.setChecked(False)
		self.ui.pushButton_multiply.setChecked(False)

		self.useristypingsecondnumber = False
		self.ui.label.setText("0")
# app
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())