import fileinput
import operator
import copy
import sys

class Node:
    def __init__(self, state, parent, action, path_cost, is_goal):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.is_goal = is_goal

class SearchSpace:
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

def gcost(crate, state):
	#cost of rising and put down the crate = 0.5, cost of moving the crate between stack = 1 * distance
	value = 0.5 + abs(find_crate(crate, state)[0] - find_crate(crate, problem.initial_state)[0]) + 0.5
	return value

def hcost(state):
	#Heuristic: the number of missplaced creates
	missplaced = 0
	for i, stack in enumerate(state):
		for j, crate in enumerate(stack):
			if find_crate(crate, state) != find_crate(crate, problem.end_state):
				missplaced += 1
	return missplaced

def fcost(crate, state):
	value = gcost(crate, state) + hcost(state)
	return value

def find_crate(crate, state):
    #method to find the crate that should move in a given state
	for i, stack in enumerate(state):
		try:
			j = stack.index(crate)
		except ValueError:
			continue
		return i, j
	return None

def move_crate(state, move_from, move_to):
    #moves the crate on top from one stack to another
    crate = state[move_from][-1]
    del state[move_from][-1]
    state[move_to].append(crate)
    cost = fcost(crate, state)
    return state, cost

def check_end(state):
	#Checks if a state is an end state
	for i, stack in enumerate(state):
		if problem.end_state[i] != ['X']:
			if stack != problem.end_state[i]:
				return False
	return True

def build_solution(node):
	#builds a list with al required steps to reach the end state
	path = []
	total_cost = 0
	while node.parent:
		path.append("(" + str(node.action[0]) + ", " + str(node.action[1]) + "); ")
		total_cost = node.path_cost
		node = node.parent
	return total_cost, path

def a_star_search():
	visited = []
	path = []
	total_cost = 0
	while True:
		if len(frontier) == 0:
			return total_cost, path
		node = frontier.pop()
		if node.is_goal:
			total_cost, path = build_solution(node)
		visited.append(node.state)
		for i, stack in enumerate(node.state):
			for j, new_stack in enumerate(node.state):
				temp_state = copy.deepcopy(node.state)
				if i != j and len(stack) > 0 and len(new_stack) < problem.max_stack:
					new_state, new_state_cost = move_crate(temp_state, i, j)
					child_node = Node(new_state, node, [i, j], new_state_cost, check_end(new_state))
					if child_node.state not in visited and not any(n.state == child_node.state for n in frontier):
						frontier.append(child_node)
						frontier.sort(key = operator.attrgetter('path_cost'), reverse = True)
					else:
						for n in frontier:
							if n.state == child_node.state and n.path_cost > child_node.path_cost:
								frontier.remove(n)
								frontier.append(child_node)
								frontier.sort(key = operator.attrgetter('path_cost'), reverse = True)
	return total_cost, path

#read the problem via stdin
problem = read_problem()
#print(problem.initial_state)
#print(problem.end_state)
#print(problem.max_stack)
#Check if first node is an end state
frontier = [Node(problem.initial_state, None, None, 0, check_end(problem.initial_state))]
#Search
solution_cost, solution = a_star_search()
#Print solution
if len(solution) > 0:
    print(solution_cost)
    print(''.join(elem for elem in solution))
else:
    print("No solution found")
