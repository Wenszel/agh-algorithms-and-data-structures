class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"<Node val:{self.value} next:{self.next}>"


def insert(head: Node, value:int) -> Node:
    pointer = head
    while pointer.next is not None and value > pointer.value:
        pointer = pointer.next
    new_node = Node(value)
    if pointer.next is None:
        new_node.next = None
    pointer.next = new_node
    return head


def remove_max(head: Node) -> Node:
    pointer: Node = head
    max_value_node_shadow: Node = head
    while pointer.next is not None:
        if pointer.next.value > max_value_node_shadow.next.value:
            max_value_node_shadow = pointer
        pointer = pointer.next
    max_value_node_shadow.next = max_value_node_shadow.next.next

    return head


lista = Node(1)
lista = insert(lista, 2)
lista = insert(lista, 5)
lista = insert(lista, 4)
print(lista)
lista = remove_max(lista)
print(lista)