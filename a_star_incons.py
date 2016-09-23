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

def input():
    input = fileinput.input()
    i = 0
    for line in input:  # read line by line of stdin
        i += 1
        if i == 1:  # reads first line, which contains maximum stack height
            max_stack = int(line.strip())
        elif i == 2:  # reads second line, which contains the intial state
            # the following block formats the line and creates the initial state data structure
            initial_state = line.strip()
            initial_state = initial_state.replace(" ", "")
            initial_state = initial_state.replace("(", "")
            initial_state = initial_state.replace(")", "")
            initial_state = initial_state.split(';')
            for i, element in enumerate(initial_state):
                initial_state[i] = element.split(",")
                if (initial_state[i] == ['']):
                    initial_state[i].pop()
        elif i == 3:  # reads the third line, which contains the end state
            # the following block formats the line and creates the end state data structure
            end_state = line.strip()
            end_state = end_state.replace(" ", "")
            end_state = end_state.replace("(", "")
            end_state = end_state.replace(")", "")
            end_state = end_state.replace("X", "")
            end_state = end_state.split(';')
            for i, element in enumerate(end_state):
                end_state[i] = element.split(",")
                if (end_state[i] == ['']):
                    end_state[i].pop()
    problem = {'initial_state': initial_state, 'end_state': end_state, 'max_stack': max_stack}
    return problem

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

def gcost(crate, state):
	#cost of rising and put down the crate = 0.5, cost of moving the crate between stack = 1 * distance
	value = 0.5 + abs(find_crate(crate, state)[0] - find_crate(crate, end_state)[0]) + 0.5
	return value

def hcost(state):
	#Heuristic: the number of missplaced creates
	missplaced = 0
	for i, stack in enumerate(state):
		for j, crate in enumerate(stack):
			if find_crate(crate, state) != find_crate(crate, problem['end_state']):
				missplaced += 1
	return missplaced

def fcost(crate, state):
	value = gcost(crate, state) + hcost(state)
	return value

def a_star():
    visited = []
    head = initial_state
    frontier.append(head)
    state = head.state
    state_cost = head.path_cost
    frontier.sort(key = operator.attrgetter('path_cost'), reverse = True)
    visited.append(head)

    while True:
        if len(frontier) == 0:
            return False
        node = frontier.pop()
        if node.is_goal:
            solution = generate_path(node)
            return True
        visited.append(node)
        for j, stack in enumerate(state):
            for k, new_stack in enumerate(state):
                aux_state = copy.deepcopy(state)
                if j != k and node.path_cost > 0:
                    if len(stack) > 0 and len(new_stack) < max_stack:
                        new_state, new_state_cost = move_crate(aux_state, j, k)
                        child_node = Node(new_state, state, [j, k], new_state_cost, check_end(new_state))
                        visited.append(child_node)
                        #print(child_node.state)
                        #print(child_node.path_cost)
                        #print(child_node.action)
                        #print(child_node.is_goal)
                        if child_node not in visited and not any(node.state == child_node.state for n in frontier):
                            frontier.append(child_node)
                            frontier.sort(key = operator.attrgetter('path_cost'), reverse = False)
                        elif child_node not in visited:
                            for node in frontier:
                                if node.state == child_node.state and node.path_cost > child_node.path_cost:
                                    frontier.remove(node)
                                    frontier.append(child_node)
                                    frontier.sort(key = operator.attrgetter('path_cost'), reverse = True)

def generate_path(node):
    actual = node
    steps = []
    if(node != None):
        solution_cost = node.path_cost
    while(actual != None):
        if(actual.parent != None):
            steps.append(actual.action)
        actual = actual.parent
    return steps

def check_end(state):
	#Checks if a state is an end state
	for i, element in enumerate(state):
		if end_state != ['X']:
			if element != end_state[i]:
				return False
	return True

problem = input()
if problem['initial_state'] == problem['end_state']:
    initial_state = Node(problem['initial_state'], None, None, hcost(problem['initial_state']), True)
else:
    initial_state = Node(problem['initial_state'], None, None, hcost(problem['initial_state']), False)
end_state = problem['end_state']
max_stack = problem['max_stack']
head = initial_state
frontier = []
solution = []
solution_cost = 0
a_star()
if len(solution) > 0:
    print(solution_cost)
    print(solution)
else:
    print("No solution found")
