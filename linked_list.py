class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

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





a = Node(3)
b = Node(1)
c = Node(4)

l = LinkedList()
l.add_right(a)
print(l)
l.add_right(b)
print(l)
l.add_right(c)
print(l)
l.add_left(Node(6))
print(l)
