# Open input file
file = open("flowers.dat", "r")
# Write while loop here
    # Print flower name using the following format
    # print(var + " grows in the " + var2)
keepGoing = True
list = []
first = []
second = []
while keepGoing:
    out = file.readline()
    if out != '':
        list.append(out)
    else:
        for x in range(26):
            if x % 2 == 0:
                first.append(list[x])
                second.append(list[x+1])
        for x in range(13):
            firstSplit = first[x]
            firstSplit = firstSplit.split("\n")
            print(firstSplit[0] + " grows in the " + second[x])
        keepGoing = False
        
