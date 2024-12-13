from collections import defaultdict

class Node:
    def __init__(self, primaryKey, parent, on : bool, authority, leftChild = None, rightChild = None):
        self.primaryKey = primaryKey
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.on = on
        self.authority = authority
        self.numAlarm = 2
        self.authorityDict = defaultdict(int)
        self.authorityDict[self.authority] = 1 


    def changeAuthority(self, newAuthority):
        prevAuthority = self.authority
        self.authority = newAuthority

    def changeParent(self, newParent):
        self.parent = newParent

    def setChild(self, newChild):
        assert self.leftChild == None or self.rightChild == None

        if self.leftChild == None:
            self.leftChild = newChild
        
        else:
            self.rightChild = newChild


        node = newChild
        authority = newChild.authority
        while node.primaryKey != 0:
            if authority <= 0:
                break
            parentNode = node.parent

            authority -= 1
            
            parentNode.authorityDict[authority] += 1
            parentNode.numAlarm += 1
            node = parentNode

    def changeLight(self):
        if self.on == True:
            self.on = False
            return
        
        self.on = True
        return


def solution():
    N, Q = map(int, input().split())

    for _ in range(Q):
        command = list(map(int, input().split()))

        if command[0] == 100:
            treeNodeList = process100(N, command)

        elif command[0] == 200:
            treeNodeList = process200(command, treeNodeList)

        elif command[0] == 300:
            process300()

        elif command[0] == 400:
            process400()

        elif command[0] == 500:
            process500()

        print(treeNodeList)

def process100(N, command):
    treeNodeList = [0] * (N + 1)
    mainNode = Node(0, None, True, 0, None, None)
    treeNodeList[0] = mainNode

    for i in range(N):
        primaryKey = i + 1
        parentKey = command[i + 1]
        authority = command[N + i + 1]

        parentNode = treeNodeList[parentKey]
        assert type(parentNode) == Node

        node = Node(primaryKey, parentNode, True, authority, None, None)

        parentNode.setChild(node)
        treeNodeList[primaryKey] = node

    return treeNodeList



def process200(command, treeNodeList):
    nodeUniqueNum = command[1]

    node = treeNodeList[nodeUniqueNum]

    if node.on == True:
        treeNodeList = turnOff(node, treeNodeList)
        node.on = False

    else:
        treeNodeList = turnOn(node, treeNodeList)
        node.on = True


    return treeNodeList

def process300():
    pass

def process400():
    pass

def process500():
    pass

def turnOn(node : Node, treeNodeList):
    nodeAuthorityDict = node.authorityDict

    while node.primaryKey != 0:
        parentNode = node.parent
        appliedAuthorityDict, numOnAlarm = addDictFromAnotherDict(parentNode.authorityDict,
                                                               nodeAuthorityDict)

        parentNode.authorityDict = appliedAuthorityDict
        parentNode.numAlarm += numOnAlarm

        treeNodeList[parentNode.primaryKey] = parentNode

        node = node.parent

    return treeNodeList
    

def turnOff(node : Node, treeNodeList):
    nodeAuthorityDict = node.authorityDict


    while node.primaryKey != 0:
        parentNode = node.parent
        appliedAuthorityDict, numOffAlarm = subtractDictFromAnotherDict(parentNode.authorityDict,
                                                               nodeAuthorityDict)

        parentNode.authorityDict = appliedAuthorityDict
        parentNode.numAlarm -= numOffAlarm

        treeNodeList[parentNode.primaryKey] = parentNode

        node = node.parent

    return treeNodeList

def subtractDictFromAnotherDict(dict1, dict2):
    numOffAlarm = 0
    for key in dict2.keys():
        if key <= 0:
            continue
        dict1[key - 1] -= dict2[key]
        numOffAlarm += dict2[key]

    return dict1, numOffAlarm

def addDictFromAnotherDict(dict1, dict2):
    numOnAlarm = 0
    for key in dict2.keys():
        if key <= 0:
            continue
        dict1[key - 1] += dict2[key]
        numOnAlarm += dict2[key]

    return dict1, numOnAlarm

solution()