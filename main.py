from calculator import Calculator

if __name__ == "__main__":

   formula = Calculator(input('Enter an algebraic expression:'))
   print('\n')
   print(f'Prefix notation: {formula}')
   print('\n')
   print(f'Result: {formula.calculate()}')