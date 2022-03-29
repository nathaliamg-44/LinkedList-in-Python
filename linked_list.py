class Node:
  def __init__(self, val, next=None):
    self.value = val
    self.next = next


class LinkedList:
    """This is a linked list implementation"""
    size = 0
    def __init__(self):
        self.head = None
        

    def push_front(self, val):
        """Add a new element to the front of the linked list. O(1)"""
        # None
        # (value: a, next: None)
        # (value: b, next:(value: a, next: None))
        node = Node(val)
        if (self.size==0):
          self.head=node
          self.size+=1
        else:
          node.next=self.head
          self.head=node
          self.size+=1

    def get_element(self, index):
        """Returns the value of the element at the provided index. O(n)"""
        if (index >= self.size):
          raise IndexError
        i = 0
        node = self.head
        while i < index:
          i += 1
          node = node.next
        return node.value

    def count(self):
        """Returns the number of elements in the list. O(1)"""
        return self.size

    def pop_front(self):
        """Removes the val from the front of the list and returns the value
        of that val. O(1)"""
        # node= head       head.next:None , return head.value
        node = self.head
        self.head=node.next
        node.next=None
        self.size-=1
        return node.value

    def insert_after(self, index, val):
        """Inserts an val in the list after the provided index. O(n)"""
        #crear un nodo con un valor, darle como nodo siguiente el apuntador del nodo         anterior  y luego apuntar ese nodo al nuevo que inserte.
        i = 0
        if(index>=self.size):
          raise IndexError
        node = self.head
        while i < index:
          i += 1
          node = node.next
        node1 = Node(val, node.next)
        node.next = node1
        self.size+=1
      
    def remove_element(self, index):
        """Removes element at the provided index. Returns the removed
        element. O(n)"""
        i = 0
        node = self.head
        while i < index-1:
          i += 1
          node = node.next
        apuntador=node.next
        node.next=apuntador.next
        apuntador.next= None
        self.size-=1
        return apuntador.value

      

    def reverse(self):
        node = self.head
        nodeb= self.head.next
        nodec = nodeb.next
        while nodeb.next!=None:
          nodeb.next = node
          self.head = nodeb
          node=nodeb
          nodeb = nodec
          if (nodec!=None):  
            nodec=nodec.next
        nodeb.next = node
        self.head = nodeb
        """Reverses the direction of the linked list. O(n)"""