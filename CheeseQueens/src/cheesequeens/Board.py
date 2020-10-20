'''
Created on 18/10/2020

@author: sergio
'''

from cheesequeens.Box import Box

class Board:
	'''
	classdocs
	'''
	n = 0
	boxes = None
	available_boxes = 0


	def __init__(self, n):
		'''
		Constructor
		'''
		if not isinstance(n, int):
			raise ValueError("N parameter must be integer")
		if n < 1:
			raise ValueError("N parameter must be natural")
		self.n = n
		self.boxes = [[Box(x, y) for x in range(n)] for y in range(n)]
		self.available_boxes = n * n
		
	def display(self):
		print("_" * self.n * 2)
		for bx in self.boxes:
			for by in bx:
				by.display()
			print()
	
	def get_matrix(self):
		a = [[None for x in range(self.n)] for y in range(self.n)]
		for x in range(self.n):
			for y in range(self.n):
				a[x][y] = "*" if self.boxes[x][y].queen else "-"
		return a
			
	def set_box_available(self, x, y, available):
		if x >= 0 and x < self.n and y >= 0 and y < self.n:
			if available and not self.boxes[x][y].available:
				self.boxes[x][y].available = True
				self.available_boxes += 1
				return
			if not available and self.boxes[x][y].available:
				self.boxes[x][y].available = False
				self.available_boxes -= 1
				return
	
	def is_box_available(self, x, y):
		return self.boxes[x][y].available
	
	def get_available_boxes(self):
		return self.available_boxes
	
	def set_queen(self, x, y, queen=True):
		if x >= 0 and x < self.n and y >= 0 and y < self.n:
			self.boxes[x][y].queen = queen
			self.set_box_available(x, y, False)
			
	def is_queen(self, x, y):
		return self.boxes[x][y].queen
	
	def clone(self):
		board = Board(self.n)
		for x in range(self.n):
			for y in range(self.n):
				board.set_queen(x, y, self.is_queen(x, y))
				board.set_box_available(x, y, self.is_box_available(x, y))
		return board
