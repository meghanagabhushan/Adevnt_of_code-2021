with open("1/input2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

count = 0
initial = int(lines[0])
for line in lines:
    #print(type(line))
    if int(line)>initial:
        #print(line)
        count = count+1
        #initial = line
    initial = int(line)

print(count)

    
