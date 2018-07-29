import sys

fin = open('data.txt')
data = fin.read()
fin.close()
fin2 = open('list.xml')
data2 = fin2.read()
fin2.close()
bacteria = []
bacName = sys.argv[1]
def findBacteria(text, name):
    position = 0
    i = 0
    while position<len(text):
        #set position equal to beginning of 'ILLNESS: '
        position = text.index(name) - 9
        bacteria.append(text[position:text.index('ILLNESS', position + 1) - 2])
        print(text[position:text.index('ILLNESS', position + 1) - 2])
        print("<br/>")
        i = text.index('ILLNESS', position + 1)
        #position = text.index('ILLNESS', position + 5)
        try:
            text = text[i:]
            position = text.index(name) - 9
            #position = text.index('"', position)
        except:
            position = len(text)
        
    return bacteria


if(bacName in data2):
    findBacteria(data, bacName)
else:
    print("Please enter an Illness from the list provided.")

#for x in range(0, len(bacteria)):
#    print(bacteria[x])
#fout = open('output.txt', 'w')
#fout.write("\n".join(bacteria))
#fout.close()

        
        
        
