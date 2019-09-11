import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

memberDict = dict()
firstLine = True
with open('home_ownership_data.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if(firstLine):
            firstLine = False
            continue

        # map id to ownership type
        memberDict[row[0]] = row[1]

ownerAverage = dict()
ownerAverage['RENT'] = 0.0
ownerAverage['OWN'] = 0.0
ownerAverage['MORTGAGE'] = 0.0
rentCount = 0
ownCount = 0
motCount = 0

firstLine = True

with open('loan_data.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if(firstLine):
            firstLine = False
            continue
        
        if(memberDict[row[0]] == 'RENT'):
            rentCount+=1
        if(memberDict[row[0]] == 'OWN'):
            ownCount+=1
        if(memberDict[row[0]] == 'MORTGAGE'):
            motCount+=1
        ownerAverage[memberDict[row[0]]] += float(row[1])

ownerAverage['RENT'] /= rentCount
ownerAverage['OWN'] /= ownCount
ownerAverage['MORTGAGE'] /= motCount

# plot bar graph
objects = ownerAverage.keys()
y_pos = np.arange(len(ownerAverage))
plt.bar(y_pos, ownerAverage.values(), align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('$ average')
plt.title('OwnerShip types')

plt.savefig('plot.png')