import fileinput
import operator
import copy
import sys

possibilities_queue = []
expansion_queue = []
visited_queue = []
end_states_queue = []
paths = []
max_stack = 0
initial_state = []
end_state = []

def find_crate(crate, state):
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

def clean_stacks():
	#Removes empty strings from the stacks
	for i, stack in enumerate(initial_state):
		try:
			stack.remove('')
		except ValueError:
			continue
	for j, stack in enumerate(end_state):
		try:
			stack.remove('')
		except ValueError:
			continue

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

def expand(state, expansion_queue):
	possibilities_queue = []
	for i, stack in enumerate(state):
		for j, new_stack in enumerate(state):
			new_state = copy.deepcopy(state)
			if j != i:
				if len(new_stack) < max_stack and len(stack) > 0:
					new_state, cost = move_crate(new_state, i, j)
					if [new_state, state, check_end(state), cost, i, j] not in visited_queue:
						possibilities_queue.append([new_state, state, check_end(state), cost, i, j])
						visited_queue.append([new_state, state, check_end(state), cost, i, j])
						if check_end(new_state):
							end_states_queue.append([new_state, state, check_end(state), cost, i, j])
	expanded_queue = expansion_queue + possibilities_queue
	expansion_queue = sorted(expanded_queue, key = lambda x: x[3])
	expansion_queue.pop(0)
	print(expansion_queue)
	return

def trace_back(node):
	#saves all the nodes that follow the path to the end state
	if node[1] != None:
		for i, other_node in enumerate(visited_queue):
			if node[1] == other_node[0]:
				paths.append(other_node)
				trace_back(other_node)
	else:
		pass
	return

def find_route():
	#prepares the representation of the path for stdout
	total_cost = 0
	for i, node in enumerate(end_states_queue):
		if node[2]:
			paths.append(node)
			trace_back(node)
	for j, node in enumerate(paths):
		total_cost += node[j][3]
	print(int(total_cost))
	for k, node in enumerate(reversed(paths)):
		if k != len(paths) - 1:
			sys.stdout.write("(" + paths[k][4] + ", " + paths[k][5] + "); ")
		else:
			sys.stdout.write("(" + paths[k][4] + ", " + paths[k][5] + ")")
	return

def start_search():
	for i, stack in enumerate(initial_state):
		for j, new_stack in enumerate(initial_state):
			state = copy.deepcopy(initial_state)
			if j != i:
				if len(new_stack) < max_stack and len(stack) > 0:
					state, cost = move_crate(state, i, j)
					possibilities_queue.append([state, initial_state, check_end(state), cost, i, j])
					visited_queue.append([state, initial_state, check_end(state), cost, i, j])
					if check_end(state):
						end_states_queue.append([state, initial_state, check_end(state), cost, i, j])
	expansion_queue = sorted(possibilities_queue, key = lambda x: x[3])
	while len(expansion_queue) > 0:
		expand(expansion_queue[0][0], expansion_queue)
	if len(end_states_queue) != 0:
		find_route()
	else:
		sys.stdout.write("No solution found")



def check_end(state):
	#Checks if a state is an end state
	for i, element in enumerate(state):
		if end_state != ['X']:
			if element != end_state[i]:
				return False
	return True

input = fileinput.input()
i = 0
for line in input: #read line by line of stdin
	i += 1
	if i == 1: #reads first line, which contains maximum stack height
		max_stack = int(line.strip())
	elif i == 2: #reads second line, which contains the intial state
		#the following block formats the line and creates the initial state data structure
		initial_state = line.strip()
		initial_state = initial_state.replace(" ", "")
		initial_state = initial_state.replace("(", "")
		initial_state = initial_state.replace(")", "")
		initial_state = initial_state.split(';')
		for i, element in enumerate(initial_state):
			initial_state[i] = element.split(",")
	elif i == 3: #reads the third line, which contains the end state
		#the following block formats the line and creates the end state data structure
		end_state = line.strip()
		end_state = end_state.replace(" ", "")
		end_state = end_state.replace("(", "")
		end_state = end_state.replace(")", "")
		end_state = end_state.split(';')
		for i, element in enumerate(end_state):
			end_state[i] = element.split(",")
clean_stacks()
start_search()
sys.stdout.flush()
