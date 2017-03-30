filename = input()

wordcount={}
paragraphcount = 1
linecount = 0
verses = 0
with open(filename, 'r') as ftext:


    for line in ftext.readlines():
        if line in ('\n', '\r\n'):
            if linecount == 0:
                paragraphcount = paragraphcount + 1
            linecount = linecount + 1
        else:
            linecount = 0
            #frequent words
            for word in line.split():
                wordcount[word] = wordcount.get(word,0) + 1
    
print (wordcount)
print (paragraphcount)

with open(filename) as f:
        for i, l in enumerate(f):
            pass    
verses = i+1
verses = verses +1 - paragraphcount

print(verses)
