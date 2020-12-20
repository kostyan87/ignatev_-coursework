from math import pi, e
from data_structures.linked_list import LinkedList

class Calculator():
   
   def __init__(self, formula_str):
      formula_str = self.delete_spaces(formula_str.lower())
      self.operators = self.get_operators()
      self.functions = self.get_functions()
      self.constants = self.get_constants()
      if self.check(formula_str) == 'CORRECT':
         pass#self._formula = self.split_into_array(formula_str)
      else:
         self.get_exceptions('exception_str')

   def get_exceptions(self, exception_str):
      pass

   def get_operators(self):
      
      operators = LinkedList()

      operators.push_back('(')
      operators.push_back(')')
      operators.push_back('+')
      operators.push_back('-')
      operators.push_back('*')
      operators.push_back('/')
      operators.push_back('^')

      return operators

   def get_functions(self):
      
      functions = LinkedList()

      functions.push_back('cos')
      functions.push_back('sin')
      functions.push_back('tg')
      functions.push_back('ctg')
      functions.push_back('ln')
      functions.push_back('log')
      functions.push_back('sqrt')
      functions.push_back('asin')

      return functions
   
   def get_constants(self):
      
      constants = LinkedList()

      constants.push_back('pi')
      constants.push_back('e')

      return constants

   '''def __str__(self):
      return str(self._formula)'''

   def split_into_array(self, formula_str):
      pass

   def delete_spaces(self, formula_str):
      str_without_spaces = ''

      for i in formula_str:
         if i != ' ':
            str_without_spaces = str_without_spaces + i
      
      return str_without_spaces

   def check(self, formula_str):
      '''
      Проверка введенной формулы на корректность. Здесь же выбрасывается исключение с указанием позиции некорректного ввода.
      '''

      if len(formula_str) == 0:
         raise Exception('String is empty')
      if formula_str[0] == '-' or formula_str[0] == '(' or formula_str[0].isdigit() or formula_str[0].isalpha():
         self.check_brackets(formula_str)
         self.check_symbols(formula_str)
         self.check_operators(formula_str)
      else:
         raise Exception('Invalid symbol at 0 positions')

   def check_symbols(self, formula_str):
      
      i = 0
      while i < len(formula_str):

         check_shift = True
         # Проверка на отстутствие некорректного символа на i-ой позиции
         if formula_str[i].isalpha():   
            i = self.check_invalid_alphas(formula_str, i)
            if i > len(formula_str) - 1:
               break
            check_shift = False
         elif not formula_str[i].isdigit() and not str(self.operators.search(formula_str[i])).isdigit():
            raise Exception(f'Invalid symbol at {i} positions')
         
         if check_shift:
            i += 1


   def check_invalid_alphas(self, formula_str, i):
      """
      Проверка символа(среза) на корректность
      """
      if str(self.constants.search(formula_str[i])).isdigit():
         return i + 1
      for j in range(2, 5):
         if str(self.constants.search(formula_str[i: i + j])).isdigit() or str(self.functions.search(formula_str[i: i + j])).isdigit():
            return i + j
      raise Exception(f'Invalid symbol at {i} positions') 

   def check_operators(self, formula_str):
      # Проверка на отстутствие двух подряд операторов
   '''elif str(self.operators.search(formula_str[i])).isdigit() and self.operators.search(formula_str[i]) > 1:
      i = i + 1
      while formula_str[i] == ' ':
         i += 1
      if i > len(formula_str) - 1:
         break
      if str(self.operators.search(formula_str[i])).isdigit() and self.operators.search(formula_str[i]) > and self.operators.search(formula_str[i]) != 3:
         raise Exception(f'Two operators in a row for {i}-{i + 1} positions')'''

   def check_brackets(self, formula_str):
      """
      Проверка на правильную скобочную последовательность
      """
      pass

test_str = Calculator('1 + 4 - 5 + 6 + cos(pi / 4)')

#test_str = Calculator('cosu67+-*/^-6r6urru7ru7676rsi--nmyu^^^^^muyib    tgctyu,i,yoglnr6u6utrlogr6u6rsqrtpiru+-/67r67*****e-----ur////6u6rur')

#test_str = Calculator('cos8894864346845123115487')