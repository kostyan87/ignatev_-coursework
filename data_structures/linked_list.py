class Node():

   def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None

class LinkedList():
   
   def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0

   def get_size(self):
      return self.length

   def is_empty(self):
      if self.get_size() == 0: return True
      return False

   def push_front(self, value):
      new_node = Node(value)
      if self.is_empty():
         self.head = new_node
         self.tail = new_node
         self.length = self.length + 1
      else:
         self.head.prev = new_node
         new_node.next = self.head
         self.head = new_node
         self.length = self.length + 1

   def push_back(self, value):
      new_node = Node(value)
      if self.is_empty():
         self.head = new_node
         self.tail = new_node
         self.length = self.length + 1
      else:
         self.tail.next = new_node
         new_node.prev = self.tail
         self.tail = new_node
         self.length = self.length + 1
         new_node.next = None

   def pop_back(self):
      if self.is_empty():
         raise Exception('The list is empty')
      else:
         if self.get_size() == 1:
            self.head = None
            self.tail = None
            self.length -= 1
         else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1

   def print_to_console(self):
      if self.is_empty():
         print('The list is empty')
      else:
         list_elem = self.head
         list_list = []

         for i in range(self.get_size()):
            list_list.append(list_elem.value)
            list_elem = list_elem.next
         
         print(list_list)
