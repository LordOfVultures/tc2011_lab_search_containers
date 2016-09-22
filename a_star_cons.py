import fileinput

expansion_queue = []
visited_queue = []
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

def create_state():
	#missing code
	return state

def expand(state):
	#missing code
	return

def check_end(state):
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
