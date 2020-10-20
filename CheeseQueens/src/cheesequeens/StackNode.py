'''
Created on 19/10/2020

@author: sergio
'''

class StackNode:
	'''
	classdocs
	'''
	board = None
	x = 0
	y = 0


	def __init__(self, board, x, y):
		'''
		Constructor
		'''
		self.board = board
		self.x = x
		self.y = y
