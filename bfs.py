import fileinput
import copy

initial_state = []
end_state = []
visited = []
forExploring = []
max_stack = []
cost = 0


class Node():
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


# function that reads input
def readingInput():
    # input = fileinput.input()
    archi = open('Test1.txt', 'r')
    global end_state
    global initial_state
    global max_stack
    i = 0
    # for line in input:  # read line by line of stdin
    for line in archi.readlines():
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
            for i, element in enumerate(end_state):
                end_state[i] = element.split(",")
                if (end_state[i] == ['']):
                    end_state[i].pop()
            print(end_state)

    archi.close()


def bfs():
    global initial_state
    global end_state
    global visited
    global forExploring
    initial_state = Node(initial_state, None, None, 0)
    forExploring.append(initial_state)
    visited.append(initial_state.state)
    current_node = Node(None, None, None, 0)
    i = 0
    while (forExploring and current_node.state != end_state):  # if not empty
        current_node = forExploring.pop(0)  # getting first element of the list
        # print ("Current",current_node.state)
        creatingNode(current_node)

        if (current_node.state == end_state):  # if exito
            print_path(current_node)

        if (not forExploring and current_node.state != end_state):  # if empty
            print("No solution found")
        #if (i == 2):
        #    break
        #i = i + 1


# method for comparing the nodes with the end node
def comparingNode(endNode, currentNode):
    if (currentNode.state):  # if not empty
        for element in range(len(endNode)):
            if (currentNode.state[element]):  # if not empty:
                if (not endNode[element]):  # if it is empty
                    currentNode.state[element] = []  # convert the listo to blank
        return cmp(endNode, currentNode)  # return the comparison


def creatingNode(currentNode):
    leaves_nodes = []  # variable that has the results of the nodes

    for element in range(len(currentNode.state)):
        for listNode in range(len(currentNode.state)):
            list_Nodes = copy.deepcopy(currentNode.state)  # copying the state
            if (list_Nodes[element] and element != listNode and len(list_Nodes[listNode]) < max_stack):  # if not empty

                list_Nodes[element].pop(0)  # remove the element from the list
                #if (element != listNode and len(list_Nodes[listNode]) < max_stack):  # not moving to the same place and the lenght is less or equal to stack
                list_Nodes[listNode].append(currentNode.state[element][0])  # adding the new element to the assigned space
                if(not(visited.count(list_Nodes))):
                    newCost = 1 + abs(element - listNode) + cost
                    newNode = Node(list_Nodes, currentNode, [element, listNode], newCost)
                    print ("--------Final", newNode.state)
                    forExploring.append(newNode)  # adding new nodes to forExploring
                    visited.append(list_Nodes)  # adding new nodes to visited
                #leaves_nodes.append(newNode)  # Saving Result

    #comparingLists(visited, leaves_nodes)


# method for comparing lists and adding to visited and for exploring
def comparingLists(listVisited, listNewNodes):
    global visited
    global forExploring

    for nodeVisited in range(0, len(listVisited)):
        for nodeNew in range(0, len(listNewNodes)):

            if (cmp(listVisited[nodeVisited].state, listNewNodes[nodeNew].state) != 0):  # if the nodes are not in the visited list
                print ("ListaC", listNewNodes[nodeNew].state)
                forExploring.append(listNewNodes[nodeNew])  # adding new nodes to forExploring
                visited.append(listNewNodes[nodeNew])  # adding new nodes to visited

    print("FINAL ITERACION")


def print_path(node):
    actual = node
    steps = []
    if (node != None):
        print(node.path_cost)
    while (actual != None):
        if (actual.parent != None):
            steps.append(actual.action)
        actual = actual.parent
    print(steps)


readingInput()
bfs()
