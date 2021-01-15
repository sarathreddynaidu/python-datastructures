class LLNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LL:
    def __init__(self, head=None):
        self.head = head

    def insert_begin(self, value):
        node = LLNode(value, self.head)
        self.head = node

    def insert_end(self, value):
        node = LLNode(value)
        if self.head is None:
            self.head = node
            return
        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break
                else:
                    currentNode = currentNode.nextNode

    def printLL(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-> ", end="")
            currentNode = currentNode.nextNode
        print("None")

ll = LL()
ll.printLL()
ll.insert_begin(10)
ll.printLL()
ll.insert_begin(45)
ll.printLL()
ll.insert_end(55)
ll.printLL()

