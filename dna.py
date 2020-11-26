import csv
from sys import argv

if len(argv) < 3:
    print ("usage error")
    exit()

#this file is a list where each row corresponds to an individual, and each column corresponds to a particular STR.
file = open (argv[1] , "r")
reader = csv.reader(file) 
row1 = next(reader) # only want the first row (the STR names) so I use next() 
row2 = row1[1:] # don't want the first element of the first row so I use [1:]

files = open (argv[2] , "r") #this opens the sequence of DNA strings 
readers = csv.reader(files)
row3 = next(readers)

matched_indexes = []
count = 0
row4 = row2[:]
for i in range(len(row2)): # this compares whether or not the STR name is in the DNA string
    while row2[i] in row3[0]:
        count += 1 
        # if the STR shows up consecutively next to eachother, it loops again adding itself up and increasing the counter  
        row2[i] = row2[i] + row4[i]
    matched_indexes.append(count) # increments it into a list for easier comparison for the next line of code
    count = 0 

readers2 = list(reader)
#need to convert list of list of strings to a list of lists of integers to compare with matched_indexes
for y in readers2:
    y[1:] = [int(x) for x in y[1:]]
for i in readers2: #need to increment through each row ignoring the 'name' so list([1:]) is used
    readers2 = list(i[1:])
    #if matched_indexes matches any of the rows listed in readers2, then it prints out the name of the same row 
    if matched_indexes == readers2:
        readers2 = i[0:1]
        print(', '.join(readers2))
        break
else:
    print("No Match")