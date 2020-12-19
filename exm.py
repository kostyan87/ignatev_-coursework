def split_into_array(self, formula_str):

   split_array = []
   i = 0
   while i < len(formula_str):
      if formula_str[i].isalpha():
         for j in range(2, 5):
            if formula_str[i: i + j] in self._operators:
               split_array.append(formula_str[i: i + j])
               i = i + j
            if i > len(formula_str) - 1:
               break
            if formula_str[i] in self._operators:
               split_array.append(formula_str[i])
      elif formula_str[i] in self._operators:
         split_array.append(formula_str[i])
      elif formula_str[i].isdigit():
         digit = ''
         while formula_str[i].isdigit():
            digit = digit + formula_str[i]
            i += 1
            if i > len(formula_str) - 1:
               break
         split_array.append(digit)
         i -= 1
      else:
         if formula_str[i] != '' or not formula_str[i].isdigit():
            raise Exception('Incorrect characters in the formula')
      i += 1
   return split_array