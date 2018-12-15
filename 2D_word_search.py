class Node:
    def __init__(self,char):
        self.char = char
        self.child = {}
def add(parent,word):
    for i in word:
        t = 0
        for j in parent.child.keys():
            if j.char == i:
                parent.child[j]+=1
                parent = j
                t = 1
                break
        if not t:
            newchar = Node(i)
            parent.child.update({newchar:1})
            parent = newchar            
def find(parent,word):
    if parent.child is None or not len(parent.child.keys()):
        return False
    for i in word:
        t = 0
        for j in parent.child.keys():
            if j.char == i:
                val = parent.child[j]
                parent = j
                t = 1
                break
        if not t:
            return False
    return True
def search(b,p,i,j,c,checktable):
    global present
    global words
    if i<0 or j<0 or i>=len(b) or j>=len(b[0]):
        return 0 
    if checktable[i][j] == True:
        return 0
    c = c+b[i][j]
    if not find(p,c):
        return 0
    checktable[i][j] = True
    search(b,p,i-1,j,c,checktable)
    search(b,p,i+1,j,c,checktable)
    search(b,p,i,j-1,c,checktable)
    search(b,p,i,j+1,c,checktable)
    checktable[i][j] = False
    if c in words:
        present.append(c)
class Solution:
    def findWords(self, b, w):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        global present
        global words
        words = w
        present = []
        p = Node('*')
        for k in w:
            add(p,k)
        im = len(b)
        jm = len(b[0])
        checktable=[[False for j in range(jm)] for i in range(im)]
        for i in range(len(b)):
            for j in range(len(b[i])):
                search(b,p,i,j,'',checktable)
        return sorted(list(set(present)))

