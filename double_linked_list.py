class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.nodes = []
        self.size = 0

    def __str__(self):
        s = ''
        for i in range(self.size):
            s += f'{self.nodes[i].value} -> '
        return s

    def add_right(self, node):
        if len(self.nodes) != 0:
            self.nodes[-1].next = node

        self.nodes.append(node)
        self.size += 1

    def add_left(self, node):

        self.nodes.append(node)
        self.size += 1

        if self.size != 0:
            for i in range(1, self.size):
                temp = self.nodes[-i]
                self.nodes[-i] = self.nodes[-i-1]
                self.nodes[-i-1] = temp

            self.nodes[0].next = self.nodes[1]

    def pop_right(self):
        if self.size == 0:
            print('Already Empty')

        else:
            self.nodes.pop()
            self.nodes[-1].next = None
            self.size -= 1

    def pop_left(self):
        if self.size == 0:
            print('Already Empty')

        else:
            for i in range(self.size - 1):
                temp = self.nodes[i]
                self.nodes[i] = self.nodes[i+1]
                self.nodes[i+1] = temp

            self.nodes.pop()
            self.size -= 1


a = Node(3)
b = Node(1)
c = Node(4)

l = DoubleLinkedList()
l.add_right(a)
print(l)
l.add_right(b)
print(l)
l.add_right(c)
print(l)
l.add_left(Node(6))
print(l)
l.pop_right()
print(l)
l.pop_left()
print(l)