from math import pi, e
from data_structures.linked_list import LinkedList

class Calculator():
   
   def __init__(self, formula_str):
      formula_str = formula_str.lower()
      if self.check(formula_str) == 'CORRECT':
         self._operators = self.get_operators(formula_str)
         self._functions = self.get_functions(formula_str)
         self._constants = self.get_constants(formula_str)
         #self._formula = self.split_into_array(formula_str)
      else:
         self.get_exceptions('exception_str')

   def get_exceptions(self, exception_str):
      pass

   def get_operators(self, formula_str):
      
      operators = LinkedList()

      operators.push_back('(')
      operators.push_back(')')
      operators.push_back('+')
      operators.push_back('-')
      operators.push_back('*')
      operators.push_back('/')
      operators.push_back('^')

      return operators

   def get_functions(self, formula_str):
      
      functions = LinkedList()

      functions.push_back('cos')
      functions.push_back('sin')
      functions.push_back('tg')
      functions.push_back('ctg')
      functions.push_back('ln')
      functions.push_back('log')
      functions.push_back('sqrt')
      functions.push_back('arcsin')

      return functions
   
   def get_constants(self, formula_str):
      
      functions = LinkedList()

      functions.push_back('pi')
      functions.push_back('e')

      return functions

   '''def __str__(self):
      return str(self._formula)'''

   def split_into_array(self, formula_str):
      pass

   def check(self, formula_str):
      '''
      Проверка введенной формулы на корректность. Здесь же выбрасывается исключение с указанием позиции некорректного ввода.
      '''

      if len(formula_str) == 0:
         raise Exception('String is empty')
      if formula_str[0] == '-' or formula_str[0] == '(' or formula_str[0].isdigit() or formula_str[0].isalpha():
         self.check_iter(formula_str)
      else:
         raise Exception('Invalid 1 symbol')

   def check_iter(self, formula_str):
      
      i = 0
      while i < len(formula_str):

         if formula_str[i].isalpha():   
            i = self.check_invalid_symbols(formula_str , i)
            if i > len(formula_str) - 1:
               break

   def check_invalid_symbols(self, formula_str, i):
      """
      Проверка строки на некорректные символы
      """
      if formula_str[i] in self._constants:
         return i
      for j in range(2, 5):
            if formula_str[i: i + j] in self._operators:
               return i + j
      raise Exception('')
      

   def check_brackets(self, parameter_list):
      """
      Проверка на правильную скобочную последовательность
      """
      pass

test_str = Calculator('1 + 4 - 5 + 6 + cos(pi / 4)')

#test_str = Calculator('cosu67+-*/^-6r6urru7ru7676rsi--nmyu^^^^^muyib    tgctyu,i,yoglnr6u6utrlogr6u6rsqrtpiru+-/67r67*****e-----ur////6u6rur')

#test_str = Calculator('cos8894864346845123115487')