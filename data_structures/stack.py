from linked_list import LinkedList

class Stack():
   
   def __init__(self):
      self.stack_list = LinkedList()

   def push(self, value):
      self.stack_list.push_back(value)

   def get_top(self):
      return self.stack_list.tail.value

   def pop(self):
      pop_elem = self.get_top()
      self.stack_list.pop_back()
      return pop_elem

   def print_to_console(self):
      self.stack_list.print_to_console()