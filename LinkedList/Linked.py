

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertLinkList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                self.head.next = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traversal(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find_val(self, val):
        node = self.head
        if node.value == val:
            return node.value
        while node is not None:
            if node.value == val:
                return node.value
            node = node.next

    def del_node(self, location):
        if self.head is None:
            return "LinkedList is Empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextNode = tempnode.next
                tempnode.next = nextNode.next






l = Linkedlist()
a = ["A", "B", "C", "D", "E", "F", "G", "I", "J"]

for i in a:
    l.insertLinkList(i, 1)

#print(l.traversal())
print([node.value for node in l])
#print(l.find_val("Z"))
l.del_node(0)
print([node.value for node in l])


