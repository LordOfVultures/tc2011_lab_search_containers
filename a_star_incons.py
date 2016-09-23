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
	for i, stack in enumerate(state):
		try:
			j = stack.index(crate)
		except ValueError:
			continue
		return i, j
	return None

def gcost(crate, state):
	#cost of rising and put down the crate = 0.5, cost of moving the crate between stack = 1 * distance
	value = 0.5 + abs(find_crate(crate, state)[0] - find_crate(crate, end_state)[0]) + 0.5
	return value

def hcost(state):
	#Heuristic: the number of missplaced creates
	missplaced = 0
	for i, stack in enumerate(state):
		for j, crate in enumerate(stack):
			if find_crate(crate, state) != find_crate(crate, end_state):
				missplaced += 1
	return missplaced

def fcost(crate, state):
	value = gcost(crate, state) + hcost(state)
	return value

def a_star_rec(head, visited):
    node = head
    nodestate = node.state
    stateLen = len(nodestate)
    cost = node.path_cost
    if(nodestate == end_state):
        return node
    else:
        for i in range(0, stateLen):
            for j in range(0, stateLen):
                if (i != j and (len(nodestate[j])) > 0 and (len(nodestate[i])) < max_stack):
                    nstate = copy.deepcopy(nodestate)
                    nstate[i].append(nstate[j].pop())
                    if (not(visited.count(nstate))):
                        actions = [i, j]
                        ncost = fcost(nstate[j][len(nstate[j]) - 1], nstate)
                        if nstate is not problem['end_state']:
                            nNode = Node(nstate, node, actions, ncost, False)
                        else:
                            nNode = Node(nstate, node, actions, ncost, True)
                        visited.append(nstate)
                        aux = a_star_rec(nNode, visited)
                        if(aux != None):
                            return aux
    return None

def a_star():
    visited = []
    aux = a_star_rec(head, visited)
    if(aux != None):
        return aux
    else:
        return None

def print_path(node):
    actual = node
    steps = []
    if(node != None):
        print(node.path_cost)
    while(actual != None):
        if(actual.parent != None):
            steps.append(actual.action)
        actual = actual.parent
    print(steps)

problem = input()
if problem['initial_state'] == problem['end_state']:
    initial_state = Node(problem['initial_state'], None, None, 0, True)
else:
    initial_state = Node(problem['initial_state'], None, None, 0, False)
end_state = problem['end_state']
max_stack = problem['max_stack']
head = initial_state
frontier = []
aux = a_star()
if aux is not None:
    print_path(aux)
else:
    print("No solution found")
