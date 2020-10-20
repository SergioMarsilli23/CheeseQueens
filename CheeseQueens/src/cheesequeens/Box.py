'''
Created on 18/10/2020

@author: sergio
'''

class Box:
	'''
	classdocs
	'''
	x = 0
	y = 0
	available = True
	queen = False


	def __init__(self, x, y, available=True):
		'''
		Constructor
		'''
		self.x = x
		self.y = y
		self.available = available
		
	def display(self):
		print("0" if self.available else "x" if self.queen else "*" , end = " ")
