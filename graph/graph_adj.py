    
def parseFile(arg):
    f = open(arg, 'r')

    for line in f.readlines():
        print line

parseFile('connections.txt')