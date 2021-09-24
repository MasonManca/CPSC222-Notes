#Files
#Files live "on disk"
#3 part file processing template
#step 1: open the file
#Step 2: Process the file(read or write)
#Step 3: close the file

def loadLinesFromFile(filename):
    #filename is a path toa file to open (string)
    #absolute path: start with a drive on windows (C:/)
    # on mac/linux: (/) which is called root
    # Relative path:
    #Example = "data.csv"
    #relative to the pwd, in the same directory
    infile = open(filename, "r") # passing in an r determines how we are opening the file
    lines = infile.readlines()# reads all lines into a list
    infile.close()
    return lines

def cleanLines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructureDataIntoTable(lines):
    data = []
    for line in lines:
        values = line.split(", ")
        #print(values)
        data.append(values)
    return data

def pretty_print(data):
    for row in data:
        for value in row:
            print(value, end=" ")
        print()            
 
def remove_whitespaces(data):
    for row in data: 
        for i in range(len(row)):
            row[i] = row[i].strip()

def convertColumnToNumeric(data, column_index):
    for row in data:
        row[column_index] = int(row[column_index])

lines = loadLinesFromFile("data.csv")
print(lines)

cleanLines(lines)
print("cleaned lines" , lines)

data = restructureDataIntoTable(lines)
print("data: ", data)
#task: write a pretty_print() that prints any 2d list in a grid fashion
# should appear like .csv file

pretty_print(data)

#task 2: Write a remove_whitespaces(data) function and removes the whitespaces
remove_whitespaces(data)
print(data)

#We want to convert column2's data into a numeric type
convertColumnToNumeric(data, column_index)
print("After numeric column2: ", data)