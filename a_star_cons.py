import fileinput
import operator
import copy
import sys

class Node():
    def __init__(self, state, parent, action, path_cost, is_goal):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.is_goal = is_goal

class SearchSpace():
	def __init__(self, initial_state, end_state, max_stack):
		self.initial_state = initial_state
		self.end_state = end_state
		self.max_stack = max_stack

def read_problem():
	input = fileinput.input()
	line_number = 1
	for line in input:
		if line_number == 1:
			max_stack = int(line)
		elif line_number == 2:
			initial_state = line.strip().replace(" ", "").replace("(", "").replace(")", "").split(";")
			for i, element in enumerate(initial_state):
				initial_state[i] = element.split(",")
				if (initial_state[i] == ['']):
				    initial_state[i].pop()
		elif line_number == 3:
			end_state = line.strip().replace(" ", "").replace("(", "").replace(")", "").split(";")
			for i, element in enumerate(end_state):
				end_state[i] = element.split(",")
				if (end_state[i] == ['']):
					end_state[i].pop()
		line_number += 1
	problem = SearchSpace(initial_state, end_state, max_stack)
	return problem

def check_end(state):
	#Checks if a state is an end state
	for i, element in enumerate(state):
		if element != ['X']:
			if element != problem.end_state[i]:
				return False
	return True

def a_star_search():
	return

#read the problem via stdin
problem = read_problem()
#print(problem.initial_state)
#print(problem.end_state)
#print(problem.max_stack)
#Check if first node is an end state
frontier = [Node(problem.initial_state, None, None, 0, check_end(problem.initial_state))]
solution = []
solution_cost = 0
#Start SearchSpace
a_star_search()
#Print solution
if len(solution) > 0:
    print(solution_cost)
    print(solution)
else:
    print("No solution found")
