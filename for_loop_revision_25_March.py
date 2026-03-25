a_range = int(input('Enter an integer:'))
b_range = int(input('Enter an integer:'))
c_range = int(input('Enter an integer:'))
for a in range(1,a_range):
   for b in range(1,b_range):
      for c in range(1,c_range):
          a2 = a * a
          b2 = b * b
          c2 = c * c
          if a2 + b2 == c2:
             print('You have entered a Pythagorean Triple',a,b,c)

