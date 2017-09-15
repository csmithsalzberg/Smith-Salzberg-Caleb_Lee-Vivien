#initialize dictionary and read in csv file
dict={}
file = open('occupations.csv','r')
ugly = file.read()
lines = ugly.split("\n")

#delete unnecessary lines from csv file
del lines[0]
del lines[len(lines)-1]
del lines[len(lines)-1]

#adding each line to dictionary
for line in lines:
    if line[0]=="\"":
        dict[line[0:(line.index("\"",1)+1)]] = line[(line.index("\"",1)+2):]
    else:
        dict[line.split(",")[0]]=line.split(",")[1]

print(dict)
