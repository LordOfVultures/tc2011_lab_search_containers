import fileinput
import operator

expansion_queue = []
possibilities_queue = []
visited_queue = []
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

def expand(state):
	#missing code
	return

def start_search():
	for i, stack in enumerate(initial_state):
		for j, new_stack in enumerate(initial_state):
			if j != i:
				if len(new_stack) < max_stack:
					state, cost = move_crate(initial_state, i, j)
					possibilities_queue.append([state, cost, i, j])
	expansion_queue = sorted(possibilities_queue, key=operator.itemgetter(1))

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
		print (max_stack)
	elif i == 2: #reads second line, which contains the intial state
		#the following block formats the line and creates the initial state data structure
		initial_state = line.strip()
		initial_state = initial_state.replace(" ", "")
		initial_state = initial_state.replace("(", "")
		initial_state = initial_state.replace(")", "")
		initial_state = initial_state.split(';')
		for i, element in enumerate(initial_state):
			initial_state[i] = element.split(",")
		print(initial_state)
	elif i == 3: #reads the third line, which contains the end state
		#the following block formats the line and creates the end state data structure
		end_state = line.strip()
		end_state = end_state.replace(" ", "")
		end_state = end_state.replace("(", "")
		end_state = end_state.replace(")", "")
		end_state = end_state.split(';')
		for i, element in enumerate(end_state):
			end_state[i] = element.split(",")
		print(end_state)
new_state = move_crate(initial_state, 0, 1)
start_search()
print(expansion_queue)
