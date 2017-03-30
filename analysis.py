print("BASICS:\n")
print("\nHAPAX: # words only appear once\nBIS: # words only appear twice\nTRIS: # words only appear three times")
print("Rare Words = HAPAX + BIS + TRIS")
print("Rare Words Vector: [HAPAX, BIS, TRIS, Rare Words Ratio]")
print("Tokens: # of words in a text\nTypes: Tokens take only once")
print("Poem Vector Representation: [[Rare Word List], # types, # tokens, Vocabulary Richness, # verses, #stanzas]\n")

poemsMatrix =[]
numberOfPoemsToAnalyse = int(input("How many poems do you want to analyze?: "))

for i in range(numberOfPoemsToAnalyse):
    filename = input("\nName of the file (including .txt): ")

    wordcount={}
    paragraphcount = 1
    linecount = 0
    verses = 0
    numberOfHapax=0
    numberOfBis=0
    numberOfTris=0
    numberOfRareWords =0
    numberOfTypes=0
    numberOfTokens=0
    typeTokenRatio=0

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
    
#print (wordcount)
    print ("Number of paragraphs: {}".format(paragraphcount))

    for ele in wordcount:
        numberOfTokens = numberOfTokens + wordcount[ele] 

    for ele in wordcount:
        if wordcount[ele] == 1:
            numberOfHapax = numberOfHapax+1
        elif wordcount[ele] == 2:
            numberOfBis = numberOfBis+1
        elif wordcount[ele] == 3:
            numberOfTris = numberOfTris+1

    with open(filename) as f:
        for i, l in enumerate(f):
            pass    

    verses = i+1
    verses = verses +1 - paragraphcount
    numberOfRareWords = numberOfHapax + numberOfBis + numberOfTris
    numberOfTypes = len(wordcount)
    typeTokenRatio=(numberOfTypes/numberOfTokens)*100
    typeTokenRatio=float("{0:.2f}".format(typeTokenRatio))
    rareWordsList = [numberOfHapax, numberOfBis, numberOfTris, float("{0:.2f}".format(numberOfRareWords/numberOfTypes))]
    poemVectorRepresentation = [rareWordsList,numberOfTypes,numberOfTokens,typeTokenRatio,verses,paragraphcount]
    poemsMatrix.append(poemVectorRepresentation)

    print ("Number of Verses: {}".format(verses))
    print ("Number of Hapax: {}".format(numberOfHapax))
    print ("Number of Bis: {}".format(numberOfBis))
    print ("Number of Tris: {}".format(numberOfTris))
    print ("Number of Rare Words: {}".format(numberOfRareWords))
    print ("Rare Word Vector: {}".format(rareWordsList))
    print ("Number of Types: {}".format(numberOfTypes))
    print ("Number of Tokens: {}".format(numberOfTokens))
    print ("Type/Token Ratio (VR): {}%".format(typeTokenRatio))
    print ("Poem Vector Representation: {}".format(poemVectorRepresentation))
    print ("\nMatrix:\n")
    for ele in range(len(poemsMatrix)):
        print(poemsMatrix[ele])

input("\n>>Press enter to exit<<")
