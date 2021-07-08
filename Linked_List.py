class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data," ---> ",end ='')
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after(self,data,x):
        new_node = Node(data)
        n = self.head
        while n.ref is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Element is Not Present in the Linked list ")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        new_node = Node(data)
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n = n.ref
        if n is None:
            print("Element is Not Present in the Linked List")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is Empty ")
        else:
            self.head = self.head.ref
    def delete_end(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("Linked List is Empty")
        n = self.head
        while n.ref.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n is None:
            print("Element is Not Present in the Linked List ")
        else:
            n.ref = n.ref.ref


ll = LinkedList()

ll.add_begin(100)
ll.add_end(500)
ll.add_after(200,100)
ll.add_before(300,500)
ll.delete_end()
ll.delete_begin()
ll.delete_by_value(200)

ll.print_ll()










