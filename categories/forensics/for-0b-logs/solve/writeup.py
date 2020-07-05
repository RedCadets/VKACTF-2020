file = open('system.log','r')
for line in file:
    index = line.find('good')
    if index == -1:
        print(line)
file.close()