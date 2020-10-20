'''
Created on 18/10/2020

@author: Sergio Marsilli
@facebook: Sergio.Marsilli.23
@twitter: Sergio_Marsilli
'''

from time import time
from cheesequeens.Board import Board
from cheesequeens.StackNode import StackNode

def rotate_matrix(m):
	return [[m[j][i] for j in range(len(m))] for i in range(len(m)-1,-1,-1)]

def invert_matrix(m):
	om = [[None for x in range(len(m))] for y in range(len(m))]
	for r in range(len(m)):
		for c in range(len(m)):
			om[r][len(m)-c-1] = m[r][c]
	return om

def compare_matrix(m1,m2):
	for i in range(len(m1)):
		for j in range(len(m1)):
			if m1[i][j] != m2[i][j]:
				return False
	return True

def verify_matrix(s,m):
	for o in s:
		if compare_matrix(o, m): return False
		t = rotate_matrix(m)
		if compare_matrix(o, t): return False
		t = rotate_matrix(t)
		if compare_matrix(o, t): return False
		t = rotate_matrix(t)
		if compare_matrix(o, t): return False
		t = invert_matrix(m)
		if compare_matrix(o, t): return False
		t = rotate_matrix(t)
		if compare_matrix(o, t): return False
		t = rotate_matrix(t)
		if compare_matrix(o, t): return False
		t = rotate_matrix(t)
		if compare_matrix(o, t): return False
	return True
		

if __name__ == '__main__':
	n = int(input("Give me the number of queens\n"))
	t1 = int(round(time()*1000))
	#n = 9
	x = y = sx = sy = 0
	q = ns = 0
	board = Board(n)
	board_stack = []
	solutions = []
	
	while x < n:
		while y < n:
			if board.get_available_boxes() > 0:
				if n-q > board.get_available_boxes():
					x = y = n
					break
				elif board.is_box_available(x, y):
					node = StackNode(board.clone(), x, y)
					board_stack.append(node)
					board.set_queen(x, y)
					q += 1
					for i in range(n):
						board.set_box_available(x, i, False)
						board.set_box_available(i, y, False)
						board.set_box_available(x-i, y-i, False)
						board.set_box_available(x-i, y+i, False)
						board.set_box_available(x+i, y-i, False)
						board.set_box_available(x+i, y+i, False)
					x = sx
					y = sy
					break
			elif q == n:
				ns += 1
				if verify_matrix(solutions, board.get_matrix()):
					solutions.append(board.get_matrix())
				x = y = n
				break
				
			if board.get_available_boxes() == 0:
				x = y = n
				break
			else:
				y += 1
			
		else:
			x += 1
		
		if x == n and y == n and len(board_stack) > 0:
			q -= 1
			node = board_stack.pop()
			if len(board_stack) == 0:
				sx = node.x + int((node.y+1)/n)
				sy = (node.y+1) % n
			else:
				sx = node.x
				sy = node.y+1
			x = sx
			y = sy
			board = node.board
		elif y == n:
			y = 0
		
		
	t2 = int(round(time()*1000))
	if len(solutions) == 0:
		print("There aren't solutions :'(")
	else:
		for i in range(len(solutions)):
			print("Solution", i+1)
			print("==="*n)
			for x in solutions[i]:
				for y in x:
					print(y," ", end="")
				print("\n")
				
	print("END")
	print("Time ", t2-t1, " ms")
