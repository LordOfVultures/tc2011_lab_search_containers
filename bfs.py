import fileinput
import copy

initial_state = []
end_state = []
visited = []
forExploring=[]
max_stack = []


#function that reads input
def readingInput(): 
    #input = fileinput.input()
    archi=open('Test1.txt','r')
    global end_state
    global initial_state
    global max_stack
    i = 0
    #for line in input:  # read line by line of stdin
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
    forExploring.append(initial_state)
    visited.append(initial_state)
    current_node =[]
    while(forExploring and comparingNode( end_state,current_node ) != 0 ):#if not empty
        current_node=forExploring.pop(0)#getting first element of the list
        print ("Current",current_node)
        creatingNode(current_node)        
        
#method for comparing the nodes with the end node
def comparingNode(endNode,currentNode ):
    if(currentNode):#if not empty
        for element in range(len(endNode)):
            if (currentNode[element]): #if not empty:
                if (not endNode[element] ): #if it is empty
                    currentNode[element] = [] #convert the listo to blank
        return cmp(endNode , currentNode) #return the comparison
    
            

def creatingNode(state):
    leaves_nodes=[] #variable that has the results of the nodes
    
    for element in range(len(state)): 
        #print ("Elemento:",state[element]) 
        for listNode in range(len(state)):
            list_Nodes=copy.deepcopy(state) #copying the state
            if (list_Nodes[element]): #if not empty
                
                if (list_Nodes[element]): #in case the spot is not empty
                   
                    list_Nodes[element].pop(0)#remove the element from the list                       
                
                
                if (element != listNode ):  #not moving to the same place
                                                        
                    list_Nodes[listNode].append(state[element][0]) #adding the new element to the assigned space
                    leaves_nodes.append(list_Nodes) #Saving Result
                    
    comparingLists(visited,leaves_nodes)
#method for comparing lists and adding to visited and for exploring    
def comparingLists(listVisited , listNewNodes):
        global visited
        for nodeVisited in range(len(listVisited)):
            for nodeNew in range(len(listNewNodes)):
                if (cmp(listVisited[nodeVisited], listNewNodes[nodeNew]) != 0): #if the nodes are not in the visited list
                    forExploring.append(listNewNodes[nodeNew]) #adding new nodes to forExploring
                    visited.append(listNewNodes[nodeNew]) #adding new nodes to visited
        
                        
readingInput()
bfs()