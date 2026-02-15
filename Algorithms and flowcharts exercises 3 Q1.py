ab = int(input('Enter AB:'))
bc = int(input('Enter BC:'))
cd = int(input('Enter CD:'))
da = int(input('Enter DA:'))
i = int(input('Enter I:'))
if ab == bc:
   if ab == cd:
      if bc == da:
         if i == 90:
                  print('It is a square')	
         else:
            print('It is a rhombus')
      else:
         print('It is an irregular quadrilateral')
   else:
         print('It is an irregular quadrilateral')
else:
   if ab == cd:
      if bc == da:
         if i == 90:
                  print('It is a rectangle')	
         else:
            print('It is a parallelogram')
      else:
         print('It is an irregular quadrilateral')
   else:
         print('It is an irregular quadrilateral')
      
    


            