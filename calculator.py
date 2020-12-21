from math import pi, e
from data_structures.linked_list import LinkedList

class Calculator():
   
   def __init__(self, formula_str):
      formula_str = self.delete_spaces(formula_str.lower())
      self.operators = self.get_operators()
      self.functions = self.get_functions()
      self.constants = self.get_constants()
      self.check_brackets(formula_str)
      self.check_iter(formula_str)
      #self._formula = self.split_into_array(formula_str)

   def get_operators(self):
      
      operators = LinkedList()

      operators.push_back('(')
      operators.push_back(')')
      operators.push_back('+')
      operators.push_back('-')
      operators.push_back('*')
      operators.push_back('/')
      operators.push_back('^')
      operators.push_back('.')
      operators.push_back(',')

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

   def check_iter(self, formula_str):
      '''
      Проверка введенной формулы на корректность. Здесь же выбрасывается исключение с указанием позиции некорректного ввода.'''

      if len(formula_str) == 0:
         raise Exception('String is empty')
      if formula_str[0] == '-' or formula_str[0] == '(' or formula_str[0].isdigit() or formula_str[0].isalpha():
         
         i = 0
         while i < len(formula_str):

            shift = True
            if formula_str[i].isdigit():

               i = self.check_digit(formula_str, i)
               shift = False
               
               '''Проверка, что далее следует оператор. Учесть, что оператора может и не быть.'''

            elif str(self.operators.search(formula_str[i])).isdigit():
               
               if formula_str[i] == '/' and formula_str[i + 1] == '0':
                  raise Exception(f'OperatorError: division by zero')

               if i != len(formula_str) - 1:
                  if str(self.operators.search(formula_str[i + 1])).isdigit():
                     if self.operators.search(formula_str[i + 1]) != 0 and self.operators.search(formula_str[i + 1]) != 3 and self.operators.search(formula_str[i]) != 1:
                        raise Exception(f'OperatorError: second operator {formula_str[i + 1]} at {i + 1} positions')
                     if self.operators.search(formula_str[i + 1]) == 0 and self.operators.search(formula_str[i]) == 1:
                        raise Exception(f'OperatorError: second operator {formula_str[i + 1]} at {i + 1} positions')
                     if (formula_str[i + 1] == ',' or formula_str[i + 1] == '.')  and self.operators.search(formula_str[i]) == 1:
                        raise Exception(f'OperatorError: invalid operator {formula_str[i + 1]} at {i + 1} positions')
                  elif formula_str[i + 1].isdigit() and self.operators.search(formula_str[i]) == 1:
                     raise Exception(f'OperatorError: digit {formula_str[i + 1]} after {formula_str[i]} at {i + 1} positions')

               '''Проверка, что далее следует число(константа) или функция'''

            elif (formula_str[i] == 'p' and formula_str[i + 1] == 'i') or formula_str[i] == 'e':
               
               i = self.check_const(formula_str, i)
               shift = False

            elif formula_str[i].isalpha():

               i = self.check_func(formula_str, i)
               shift = False
               '''Проверка, что далее идут скобки, а за ними'''

            if shift: i += 1

      else:
         raise Exception('Invalid symbol at 0 positions')

   def check_func(self, formula_str, i):

      current_i = i
      for j in range(2, 5):
         if str(self.functions.search(formula_str[i: i + j])).isdigit():
            i = i + j
         if i > len(formula_str) - 1:
            raise Exception(f'FuncError: missing () after the function name at {i} positions')
      
      if i == current_i:
         raise Exception(f'invalid symbol {formula_str[i]} at {i} positions')

      if formula_str[i] != '(': 
         raise Exception(f'FuncError: missing () after the function name at {i} positions')
      elif i < len(formula_str):
         if formula_str[i + 1] == ')':
            raise Exception(f'FuncError: the brackets are empty {i + 1} positions')
      else:

         while formula_str[i] != ')':
            i += 1

         if i < len(formula_str):
            if formula_str[i + 1] == '(':
               raise Exception(f'FuncError: there is ( after function at {i + 1} positions')
            elif formula_str[i + 1] == '.':
               raise Exception(f'FuncError: there is . after function at {i + 1} positions')
            elif formula_str[i + 1] == ',':
               raise Exception(f'FuncError: there is , after function at {i + 1} positions')
            elif not str(self.operators.search(formula_str[i + 1])).isdigit():
               raise Exception(f'FuncError: there is no operator at {i + 1} positions')

      return i + 1

   def check_const(self, formula_str, i):
      
      if formula_str[i : i + 2] == 'pi':

         if i != 0:
            if formula_str[i - 1] == ')':
               raise Exception(f'ConstError: there is ) before pi at {i - 1} positions')
            elif formula_str[i - 1] == ',':
               raise Exception(f'ConstError: there is , before pi at {i - 1} positions')
            elif formula_str[i - 1] == '.':
               raise Exception(f'ConstError: there is . before pi at {i - 1} positions')
            elif not str(self.operators.search(formula_str[i - 1])).isdigit():
               raise Exception(f'ConstError: there is no operator at {i - 1} positions')

         if i < len(formula_str) - 2:
            if formula_str[i + 2] == '(':
               raise Exception(f'ConstError: there is ( after pi at {i + 2} positions')
            elif formula_str[i + 2] == ',':
               raise Exception(f'ConstError: there is , after pi at {i + 2} positions')
            elif formula_str[i + 2] == '.':
               raise Exception(f'ConstError: there is . after pi at {i + 2} positions')
            elif not str(self.operators.search(formula_str[i + 2])).isdigit():
               raise Exception(f'ConstError: there is no operator at {i + 2} positions')

         return i + 2

      else:

         if i != 0:
            if formula_str[i - 1] == ')':
               raise Exception(f'ConstError: there is ) before e at {i - 1} positions')
            elif formula_str[i - 1] == ',':
               raise Exception(f'ConstError: there is , before e at {i - 1} positions')
            elif formula_str[i - 1] == '.':
               raise Exception(f'ConstError: there is . before e at {i - 1} positions')
            elif not str(self.operators.search(formula_str[i - 1])).isdigit():
               raise Exception(f'ConstError: there is no operator at {i - 1} positions')

         if i < len(formula_str) - 1:
            if formula_str[i + 1] == '(':
               raise Exception(f'ConstError: there is ( after e at {i + 1} positions')
            elif formula_str[i + 1] == ',':
               raise Exception(f'ConstError: there is , after e at {i + 1} positions')
            elif formula_str[i + 1] == '.':
               raise Exception(f'ConstError: there is . after e at {i + 1} positions')
            elif not str(self.operators.search(formula_str[i + 1])).isdigit():
               raise Exception(f'ConstError: there is no operator at {i + 1} positions')

         return i + 1

   def check_digit(self, formula_str, i):
      
      check_fraction = 0
      while formula_str[i].isdigit() or formula_str[i] == ',' or formula_str[i] == '.':

         if formula_str[i] == '0' and formula_str[i + 1].isdigit():
            raise Exception(f'DigitError: invalid zero at {i} positions')

         if formula_str[i] == ',' or formula_str[i] == '.':
            if formula_str[i + 1].isdigit():
               check_fraction += 1
            else:
               raise Exception(f'DigitError: invalid {formula_str[i]} at {i} positions')
            
         if check_fraction > 1:
            raise Exception(f'DigitError: second fraction {formula_str[i]} at {i} positions')

         i += 1
         if i >= len(formula_str): break
         
      if i <= len(formula_str) - 1:
         if not str(self.operators.search(formula_str[i])).isdigit():
            raise Exception(f'DigitError: there is no operator at {i} positions')
         if self.operators.search(formula_str[i]) == 0:
            raise Exception(f'DigitError: there is ( after digit at {i} positions')

      return i

   def check_brackets(self, formula_str):
      """   
      Проверка на правильную скобочную последовательность
      """
      open_brackets = 0
      close_brackets = 0

      for i in formula_str:

         if i == '(':
            open_brackets += 1
         if i == ')':
            close_brackets += 1
         if (open_brackets - close_brackets) < 0:
            raise Exception('BracketsError: more brackets on the right than on the left')
      
      if (open_brackets - close_brackets) == 0: pass
      else: raise Exception('BracketsError: more brackets on the left than on the right')

# first tests

#test = Calculator('14+8+58+1+2')
#test = Calculator('(14+8)-58/1*2')
#test = Calculator('14+(8+(58+1)+2)')
#test = Calculator('14^(8^58)+(1)+2h')
#test = Calculator('4(14+8)-58/1*2')
#test = Calculator('14g+(8+(58+1)+2)')
#test = Calculator('14^(8^58)+(1)+2#')
#test = Calculator('     ')
#test = Calculator('(14+8)+5ymym8+1+2')
print('((14+8)+4,1*(2,8-e05888*pi)-58+-pi+(pi/0+2*9))'[18])
test = Calculator('pi/(8)*2*asin(cos(45)*cos(pi/78+9*pi/e-48*cos(48-159*sin(ln(tg(78)*e))))+cos(3*pi)*sin(pi) - ln(e))*e+cos(56)*256')