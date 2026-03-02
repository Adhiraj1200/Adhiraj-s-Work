negitive = int(input('How many negitives did you get:'))
if negitive == 1:
    for x in range(10):
        print('prompt')
elif negitive == 2:
    for x in range(50):
        print('reminder')
elif negitive == 3:
    for x in range(100):
        print('warning')
else:
    for x in range(500):
        print('removal')