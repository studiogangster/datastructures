
import math
class Node():


    isRoot = False
    value = None
    leftNode = None
    rightNode = None

    sizeOfElements = 0
    depth = 0


    def __init__(self , value, isRoot=False):
        self.isRoot = isRoot
        self.value = value


    def __insertToLeft(self, value , depth):
        if self.leftNode == None:
            self.leftNode = Node( value )
        else:
            depth = self.leftNode.insert(value , depth)

        return depth
        


    def __insertToRight(self, value , depth):
        if self.rightNode == None:
            self.rightNode = Node( value )
        else:
            depth = self.rightNode.insert(value, depth)

        return depth
        
        

    def insert(self , value , depth = 0):
        depth += 1
        if self.value > value:
            depth = self.__insertToLeft(value, depth)
        else:
            depth = self.__insertToRight(value, depth)
        self.sizeOfElements += 1
        return depth

    def Insert(self, value):
        depth = self.insert( value )
        if self.depth < depth:
            self.depth = depth

        return depth

    def search(self, value):

        nodeFound = False

        if self.value == value:
            nodeFound = True

        elif self.value > value:
            if not self.leftNode == None:
                nodeFound = self.leftNode.search(value)
        else:
            if not self.rightNode == None:
                nodeFound = self.rightNode.search(value)

        return nodeFound



    def dfs(self):
        element = self.value
        print("traverseTo", element)

        if not self.leftNode == None:
            self.leftNode.dfs()
        
        if not self.rightNode == None:
            self.rightNode.dfs()


    def bfs(self , stack = None):


        
        print()

        if stack == None:
            print(  self.value, end=" " )
            stack = list()

            if not self.leftNode == None:
                stack.append(self.leftNode )
            if not self.rightNode == None:
                stack.append(self.rightNode)


            if len(stack) < 1:
                return
            else:
                self.bfs( stack )
        else:
            nStack = list()
            for elem in stack:
                print(  elem.value , end=" " )
                if not elem.leftNode == None:
                    nStack.append(elem.leftNode )
                if not elem.rightNode == None:
                    nStack.append(elem.rightNode)
            
            if len(nStack) < 1:
                return
            else:
                self.bfs( nStack )

        stack = list()
        stack.append(  self )

        

        pass

    def printTree(self):
        pass






elements = [ 2,3,1,33,12,54,4,2,3,123,32 ]

rootNode = Node(  elements.pop(0) , True )

for element in elements:
    depth = rootNode.Insert( element )
    print("Inserted", element, "at depth", depth, "Tree Height", rootNode.depth)


rootNode.bfs()
print()
rootNode.dfs()

# vagueelements = [3,2,3123,2,12,312,312,312,31,23,123,123,123,12,312,1,3321312,2,2,2,12,2]

# for element in elements:
#     result = rootNode.search( element )
#     print( "Found " + str(element) if result else "Not found" )

# for element in vagueelements:
#     result = rootNode.search( element )
#     print( "Found: " + str(element) if result else "Not found: " + str(element))
