## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end =' ')
    while (current.link != None): # 핵심
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre
    # Case 1 : (하필이면) 머리 앞에 삽입
    if head.data == findData : # 다현,화사
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case 2 : 찾는 애가 중간에 있을 때 # 사나,솔라
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(Node)
            return
    # Case3 찾는 애가 없을 때,마지막에 추가 # 재남,문별
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(Node)
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    # Case 1 (하필) 머리를 삭제할 떄
    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return
    # Case 2 중간 노드를 삭제할 때
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del (current)
            return
        #
def findNode(findData) :
    global memory, head, current, pre
    current = head
    if (current.data == findData) :
        return current # 노드를 리턴
    while current.link != None :
        current = current.link
        if (current.data == findData) :
            return current
    return Node()

## 변수
memory = [] # 노드 보관할 메모리 (파이썬에선 없어도 됨)
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] #5백,5천 상관 없음

## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] : # 정연~ 끝까지
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사') # 다현을 찾아 그 앞에 화사를 삽입해
# insertNode('사나', '솔라')
# insertNode('재남', '문별')
#deleteNode('다현')
# deleteNode('쯔위')
# deleteNode('재남')

retNode = findNode('사나')
print(retNode.data, '의 뮤비가 나옵니다. 쿵짝')








