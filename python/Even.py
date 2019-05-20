numbers = [input('Enter a value: ') for i in range(10)]
odds = [y for y in numbers if y % 2 != 0]
if odds:
    print max(odds)
else:
    print "No odd numbers were entered"
