import sys; sys.path.append(r'.\data_structures')
from math import pi, e, cos, sin, tan, atan, log1p, log2, sqrt, asin
from data_structures.stack import Stack
from data_structures.linked_list import LinkedList

class Calculator():
   
   def __init__(self, formula_str):
      formula_str = self.delete_spaces(formula_str.lower())
      self.operators = self.get_operators()
      self.functions = self.get_functions()
      self.constants = self.get_constants()

      self.check_brackets(formula_str)
      self.check_base(formula_str)

      self.formula_list = self.split_into_array(formula_str)
      self.prefix_notation = self.prefix_conversion(self.formula_list)

   def __str__(self):
      return self.prefix_notation

   def split_prefix_notation(self, prefix_notation):
      
      prefix_notation_list = LinkedList()

      i = 0
      while i < len(prefix_notation):

         digit = ''

         while prefix_notation[i] != ' ':
            
            digit = digit + prefix_notation[i]
            i += 1

            if i == len(prefix_notation): break

         prefix_notation_list.push_back(digit)
         i += 1

      return prefix_notation_list

   def calculate(self):

      prefix_notation = self.split_prefix_notation(self.prefix_notation)
      #prefix_notation.print_to_console()
      #print('\n')

      stack = Stack()
      list_elem = prefix_notation.tail

      for _ in range(prefix_notation.get_size(), 0, -1):

         if list_elem.value == 'pi' or list_elem.value == 'e' or list_elem.value[0].isdigit() or list_elem.value == '-pi' or list_elem.value == '-e' or (list_elem.value[0] == '-' and len(list_elem.value) > 1 and not (str(self.functions.search(list_elem.value)).isdigit())):

            if list_elem.value == 'pi':
               stack.push(pi)
            elif list_elem.value == 'e':
               stack.push(e)
            elif list_elem.value == '-pi':
               stack.push(-pi)
            elif list_elem.value == '-e':
               stack.push(-e)
            else:
               stack.push(list_elem.value)

         else:

            if (str(self.functions.search(list_elem.value)).isdigit()):

               digit = stack.get_top()
               stack.pop()
               stack.push(self.function(list_elem.value, float(digit)))

            elif str(self.operators.search(list_elem.value)).isdigit():

               digit_1 = stack.get_top()
               stack.pop()
               digit_2 = stack.get_top()
               stack.pop()

               stack.push(self.operation(float(digit_1) ,list_elem.value, float(digit_2)))

         list_elem = list_elem.prev

      return stack.get_top()

   def operation(self, digit_1, operator, digit_2):

      if operator == '+': return digit_1 + digit_2
      if operator == '/': return digit_1 / digit_2
      if operator == '*': return digit_1 * digit_2
      if operator == '-': return digit_1 - digit_2
      if operator == '^': return digit_1 ** digit_2

   def function(self, function, digit):
      
      if function == 'cos': return cos(digit)
      if function == 'sin': return sin(digit)

      if function == 'tg': 
         if cos(digit) == 0:
            raise Exception('tgError: division by zero') 
         return tan(digit)

      if function == 'ctg':
         if sin(digit) == 0:
            raise Exception('ctgError: division by zero') 
         return cos(digit)/sin(digit)

      if function == 'ln':
         if digit <= 0:
            raise Exception('lnError: sub-logarithmic expression is zero') 
         return log1p(digit)

      if function == 'log':
         if digit <= 0:
            raise Exception('logError: sub-logarithmic expression is zero') 
         return log2(digit)

      if function == 'sqrt':
         if digit < 0:
            raise Exception('sqrtError: negative expression under the sqrt') 
         return sqrt(digit)

      if function == 'asin': return asin(digit)

      if function == '-cos': return -cos(digit)
      if function == '-sin': return -sin(digit)

      if function == '-tg': 
         if cos(digit) == 0:
            raise Exception('tgError: division by zero') 
         return -tan(digit)

      if function == '-ctg':
         if sin(digit) == 0:
            raise Exception('ctgError: division by zero') 
         return -cos(digit)/sin(digit)

      if function == '-ln':
         if digit <= 0:
            raise Exception('lnError: sub-logarithmic expression is zero') 
         return -log1p(digit)

      if function == '-log':
         if digit <= 0:
            raise Exception('logError: sub-logarithmic expression is zero') 
         return -log2(digit)

      if function == '-sqrt':
         if digit < 0:
            raise Exception('sqrtError: negative expression under the sqrt') 
         return -sqrt(digit)

      if function == '-asin': return -asin(digit)

   def prefix_conversion(self, formula_list):
      """
      Преобразование в префиксную форму записи 
      """
      prefix_str = ''
      stack = Stack()
      list_elem = formula_list.tail

      for _ in range(formula_list.get_size(), 0, -1):
         
         if list_elem.value == ')':

            stack.push(list_elem.value)

         elif list_elem.value == 'pi' or list_elem.value == 'e' or list_elem.value[0].isdigit() or list_elem.value == '-pi' or list_elem.value == '-e' or (list_elem.value[0] == '-' and len(list_elem.value) > 1):

            if prefix_str == '':
               prefix_str = list_elem.value + prefix_str
            else:
               prefix_str = list_elem.value + ' ' + prefix_str

         elif list_elem.value == '(':

            while stack.get_top() != ')':

               if prefix_str == '':
                  prefix_str = stack.get_top() + prefix_str
               else:
                  prefix_str = stack.get_top() + ' ' + prefix_str

               stack.pop()
               
            stack.pop()

         elif str(self.operators.search(list_elem.value)).isdigit() or str(self.functions.search(list_elem.value)).isdigit():
            
            if stack.stack_list.is_empty():

               stack.push(list_elem.value)

            elif self.get_priority(list_elem.value) > self.get_priority(stack.get_top()):

               stack.push(list_elem.value)

            else:

               while self.get_priority(stack.get_top()) > self.get_priority(list_elem.value):

                  if prefix_str == '':
                     prefix_str = stack.get_top() + prefix_str
                  else:
                     prefix_str = stack.get_top() + ' ' + prefix_str

                  stack.pop()

                  if stack.stack_list.is_empty(): break
               
               stack.push(list_elem.value)

         list_elem = list_elem.prev

      while not stack.stack_list.is_empty():

         prefix_str = stack.get_top() + ' ' + prefix_str
         stack.pop()

      return prefix_str

   def get_priority (self, operator):
      
      if str(self.functions.search(operator)).isdigit(): return 3

      if operator == '^': return 3
      if operator == '*': return 2
      if operator == '/': return 2
      if operator == '+': return 1
      if operator == '-': return 1
      if operator == '(': return 0
      if operator == ')': return 0

   def split_into_array(self, formula_str):

      formula_array = LinkedList()
      i = 0

      while i < len(formula_str):
         
         shift = True

         if formula_str[i].isdigit():

            digit_str = ''

            while formula_str[i].isdigit() or formula_str[i] == ',' or formula_str[i] == '.':
               digit_str = digit_str + formula_str[i]
               i += 1
               if i > len(formula_str) - 1 : break

            shift = False
            formula_array.push_back(digit_str)

         elif str(self.operators.search(formula_str[i])).isdigit():

            ########################################################
            if formula_str[i] == '-' and (str(self.operators.search(formula_str[i - 1])).isdigit() or i == 0):
               if formula_str[i + 1].isdigit():
                  i += 1
                  digit_str = '-'

                  while formula_str[i].isdigit() or formula_str[i] == ',' or formula_str[i] == '.':
                     digit_str = digit_str + formula_str[i]
                     i += 1
                     if i > len(formula_str) - 1 : break

                  shift = False
                  formula_array.push_back(digit_str)

               elif formula_str[i + 1] == 'e':
                  formula_array.push_back('-e')
                  shift = False
                  i += 2
               
               elif formula_str[i + 1] == 'p':
                  formula_array.push_back('-pi')
                  shift = False
                  i += 3

               elif formula_str[i + 1].isalpha():
                  
                  i += 1
                  for j in range(2, 5):
                     if str(self.functions.search(formula_str[i: i + j])).isdigit():
                        formula_array.push_back('-' + formula_str[i: i + j])
                        break
                     if i + j > len(formula_str) - 1: break
                  
                  shift = False
                  i = i + j
            ########################################################
            else: formula_array.push_back(formula_str[i])

         elif formula_str[i] == 'e':
            
            formula_array.push_back(formula_str[i])

         else:

            for j in range(2, 5):
               if str(self.functions.search(formula_str[i: i + j])).isdigit() or str(self.constants.search(formula_str[i: i + j])).isdigit():
                  formula_array.push_back(formula_str[i: i + j])
                  break
               if i + j > len(formula_str) - 1: break
                  
            shift = False
            i = i + j

         if shift: i = i + 1
      
      return formula_array

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
      functions.push_back('-cos')
      functions.push_back('-sin')
      functions.push_back('-tg')
      functions.push_back('-ctg')
      functions.push_back('-ln')
      functions.push_back('-log')
      functions.push_back('-sqrt')
      functions.push_back('-asin')

      return functions
   
   def get_constants(self):
      
      constants = LinkedList()

      constants.push_back('pi')
      constants.push_back('e')
      constants.push_back('-pi')
      constants.push_back('-e')

      return constants

   def delete_spaces(self, formula_str):
      str_without_spaces = ''

      for i in formula_str:
         if i != ' ':
            if i == ',':
               str_without_spaces = str_without_spaces + '.'
            else:
               str_without_spaces = str_without_spaces + i
      
      return str_without_spaces

   def check_base(self, formula_str):
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

         if formula_str[i] == '0' and formula_str[i + 1].isdigit() and check_fraction == 0:
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