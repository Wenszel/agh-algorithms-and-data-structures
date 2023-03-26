class List:
    def __init__(self, first=None, last=None):
        self.first = first
        if last is None:
            self.last = first
        else:
            self.last = last

    def __repr__(self):
        return f"<List: {self.first}>"

    def insert(self, values):
        if self.first is None:
            self.first = Node(values[0])
            self.last = self.first
        else:
            self.last.next = Node(values[0])
            self.last = self.last.next
        for value in values[1:]:
            self.last.next = Node(value)
            self.last = self.last.next

    def insert_node(self, node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = self.last.next

    def concat(self, linked_list):
        if self.first is None:
            self.first = linked_list.first
            self.last = linked_list.last
        else:
            self.last.next = linked_list.first
            self.last = linked_list.last

    def empty(self):
        return self.first is None

    def get_natural_series(self):
        if self.empty():
            return self
        output = List()
        output.first = self.first
        pointer = self.first
        while pointer.next is not None and pointer.next.val >= pointer.val:
            pointer = pointer.next
        self.first = pointer.next
        pointer.next = None
        return output

    def merge(self, linked_list):
        output = List()
        p1 = self.first
        p2 = linked_list.first
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                output.insert_node(p1)
                p1 = p1.next
            else:
                output.insert_node(p2)
                p2 = p2.next
        while p1 is not None:
            output.insert_node(p1)
            p1 = p1.next
        while p2 is not None:
            output.insert_node(p2)
            p2 = p2.next
        return output

    def sort(self):
        while True:
            l1 = self.get_natural_series()
            l2 = self.get_natural_series()
            if l2.empty():
                self.first = l1.first
                break
            new_list = l1.merge(l2)
            self.concat(new_list)


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"


lista = List()
lista.insert([3, 4, 1, 3, 6, 8, 5, 4])
print(lista)
lista.sort()
print(lista)


