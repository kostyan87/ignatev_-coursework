from linked_list import LinkedList

class Queue():
   
   def __init__(self):
      self.queue_list = LinkedList()

   def push(self, value):
      self.queue_list.push_front(value)

   def get_top(self):
      return self.queue_list.tail.value

   def pop(self):
      pop_elem = self.get_top()
      self.queue_list.pop_back()
      return pop_elem

   def print_to_console(self):
      self.queue_list.print_to_console()