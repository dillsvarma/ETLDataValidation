import sys
columnCount = 0
missing = []

#### Function that Compares two Lists ###
#### Required Ordered list of two files ###
def compare(list1,list2):
    global columnCount
    i = 0
    try:
        while i < len(list2):
            #print(i,len(list2))
            if list1[i] == list2[i]:
                i += 1
                continue
            else:
                missing.append([header[0], cols[0][i],  header[columnCount], list1[i], list2[i]])
                i += 1
    except IndexError:
        print("Index Out of bound Error")
        print(columnCount)
    columnCount += 1

#Main#
def main(self):
    global columnCount
    global header
    global cols
    global cols2
    sourceFile = sys.argv[1]
    targetFile = sys.argv[2]
    with open(sourceFile, 'r') as file:
        file.readline()  # skip the first line
        rows = [[str(x) for x in line.split('\t')] for line in file]
        cols = [list(col) for col in zip(*rows)]

    with open(targetFile, 'r') as file1:
        header = file1.readline().split()  # skip the first line
        #print(header[0])
        rows2 = [[str(x) for x in line1.split('\t')] for line1 in file1]
        print(rows2)
        cols2 = [list(col2) for col2 in zip(*rows2)]

    flag = 0
    for z in range(len(cols)):
        list_x = cols[z]
        list_y = cols2[z]
        compare(list_x, list_y)
    if len(list_x) == len(list_y):
        print("Count Validation: Passed "+str(len(list_x))+":"+str(len(list_y)))
    else:
        print("Count Validation: Failed "+str(len(list_x))+":"+str(len(list_y)))
    if(missing):
        print("Column Validation Failed")
        print(missing)
    else:
        print("Column Validation Passed")

if __name__ == "__main__":main(sys.argv[2:])
