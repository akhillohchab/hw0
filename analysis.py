import csv

f = open('iowa-liquor-sample.csv')

allLines = csv.reader(f)
pattern = 'single malt scotch'
count = 0
for row in allLines:
        for item in row:
                if pattern in item.lower():
                        count+=1
#                        print item
print count
