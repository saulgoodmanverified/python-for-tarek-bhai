import csv

# slicing
a = ['b', 4 , 'f']
# a[ start, end, step]
# the value end is upto but not included
# print(a[1:3:])

header = ['name', 'age', 'country', 'gender']

eric = ['eric', 24, 'US', 'male']
jane = ['Jane', 34, 'US', 'female']

# print(eric + jane)
with open('demo.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # writing headers

    writer.writerow(header)

    writer.writerow(jane) 

    writer.writerow(eric)
    