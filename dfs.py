import fileinput
import copy

class Node():
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

def input():
    input = fileinput.input()
    i = 0
    for line in input:  # read line by line of stdin
        i += 1
        if i == 1:  # reads first line, which contains maximum stack height
            max_stack = int(line.strip())
            print (max_stack)
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
            print(initial_state)
        elif i == 3:  # reads the third line, which contains the end state
            # the following block formats the line and creates the end state data structure
            end_state = line.strip()
            end_state = end_state.replace(" ", "")
            end_state = end_state.replace("(", "")
            end_state = end_state.replace(")", "")
            end_state = end_state.replace("X", "")
            end_state = end_state.split(';')
            print (end_state)
            for i, element in enumerate(end_state):
                end_state[i] = element.split(",")
                if (end_state[i] == ['']):
                    end_state[i].pop()
            print(end_state)
            break
    problem = {'initial_state': initial_state, 'end_state': end_state, 'max_stack': max_stack}
    return problem

def dfsrecursive(head, visited):
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
                        ncost = 1 + abs(i - j) + cost
                        nNode = Node(nstate, node, actions, ncost)
                        visited.append(nstate)
                        aux = dfsrecursive(nNode, visited)
                        if(aux != None):
                            return aux
    return None

def dfs():
    visited = []
    aux = dfsrecursive(head, visited)
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

"""problem = input()
initial_state = Node(problem['initial_state'], None, None, 0)
end_state = problem['end_state']
max_stack = problem['max_stack']"""
initial_state = Node([['A'], ['B'], ['C'], [], [], []], None, None, 0)
end_state = [[], [], [], ['A'], ['B'], ['C']]
max_stack = 3
head = initial_state
frontier = []
aux = dfs()
if (aux != None):
    print("Answer")
    print_path(aux)
else:
    print ("No solution found")
