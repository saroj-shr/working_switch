import RPi.GPIO as GPIO


first_switch = 33
second_switch = 31

class switch(object):
	"""Used to switch light using relay"""
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(first_switch, GPIO.OUT)
		GPIO.setup(second_switch, GPIO.OUT)

	def first_switch(self, value):
		GPIO.output(first_switch,value)

	def second_switch(self, value):
		GPIO.output(second_switch, value)
