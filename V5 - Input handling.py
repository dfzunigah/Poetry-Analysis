import math

#Computes cosine similarity of vector1 to vector2: (v1 . v2)/{||v1||*||v2||)
def cosine_similarity(vector1,vector2):    
    sumxbyx, sumxbyy, sumybyy = 0, 0, 0
    for i in range(len(vector1)):
        x = vector1[i]; y = vector2[i]
        sumxbyx += x*x
        sumybyy += y*y
        sumxbyy += x*y
    return sumxbyy/math.sqrt(sumxbyx*sumybyy)

#Computes euclidean distance of vector1 and vector2: sqrt(+=(V1-V2)^2)
def euclideanDistance(vector1,vector2): 
    return sum([(x-y)**2 for (x,y) in zip(vector1,vector2)])**(0.5)

#Computes dot product of vector1 and vector2: +=v1*v2
def dotProduct(vector1, vector2):
    return sum(p*q for p,q in zip(vector1, vector2))

#Poems Matrix: It allows to stack poems' vector representation so it'd be easy to compare them
poemsMatrix = []

#User inputs: # of poems user wish to analyze and the # of characters to be used for get the rhythm pattern. Loops used so no exception handling implemented.
numberOfPoemsToAnalyse = ' '
rhythmParameter = ' '

while not numberOfPoemsToAnalyse.strip().isdigit():
     numberOfPoemsToAnalyse = input("How many poems do you wish to analyze: ")
numberOfPoemsToAnalyse = int(numberOfPoemsToAnalyse)

while not rhythmParameter.strip().isdigit():
     rhythmParameter = input("# of characters to be analyzed on the rhythm: ")
rhythmParameter = int(rhythmParameter)

#Loop that allows to do the analysis on multiple poems
for i in range(numberOfPoemsToAnalyse):
    #Input loop to handle non-existing files or user wrong input
    while True:
        filename = input("\nName of the poem: ")
        filename+=".txt"
        try:
            open(filename, 'r').readlines()
        except FileNotFoundError:
            print("Whhoops! No such file! Please enter the name of the file you'd like to use.")
        else:
            break


    poem = ""
    lastwords = []
    rhythmValue = 0

    wordCount = {}
    paragraphCount = 1
    lineCount = 0
    verses = 0
    numberOfHapax = 0
    numberOfBis = 0
    numberOfTris = 0
    numberOfRareWords = 0
    rareWordsRatio = 0
    numberOfTypes = 0
    numberOfTokens = 0
    typeTokenRatio = 0

    
    with open(filename,'r') as ftext:
        for line in ftext.readlines():
            #If there's a double line break it takes it as a paragraph
            if line in ('\n', '\r\n'):
                if lineCount == 0:
                    paragraphCount += 1
                lineCount += 1
            #It separates the every word and counts them individually
            else:
                lineCount = 0
                for word in line.split():
                    wordCount[word] = wordCount.get(word,0) + 1
    
    for i in wordCount:
        #Get the total number of words in the poem by summing all appearances of every word
        numberOfTokens +=wordCount[i]
        #Gets the number of appearances of unique words (Hapax), two (Bis) and three (Tris) appearances words by looping through the words array
        if wordCount[i] == 1:
            numberOfHapax += 1
        elif wordCount[i] == 2:
            numberOfBis += 1
        elif wordCount[i] == 3:
            numberOfTris += 1

    #Loops through the file enumerating each line, at the end it'll have the total number of lines in the file.
    #As it starts at 0, we need to add a +1 so lineCount is right; then we rest the number of paragraphs+1 (The "+1" thing is because paragraphCount also starts at 0)
    with open(filename) as file:        
        for n, line in enumerate(file):
            pass
    verses = n+1
    verses += (1-paragraphCount)

    #Rare words: The sum of 1 (Hapax),2 (Bis) or 3 (Tris) appearances words
    numberOfRareWords = numberOfHapax + numberOfBis + numberOfTris
    #Types: # of words only taken once
    numberOfTypes = len(wordCount)
    #Calculates typeTokenRatio as shown and formats the number to only have 2 decimals
    typeTokenRatio = (numberOfTypes / numberOfTokens) * 100
    typeTokenRatio = float("{0:.2f}".format(typeTokenRatio))
    #Calculates rareWordsRatio as shown and formats the number to only have 2 decimals
    rareWordsRatio = numberOfRareWords/numberOfTypes
    rareWordsRatio = float("{0:.2f}".format(rareWordsRatio))

    
    #Opens a file (e.j: "firstPoem.txt") and turns it into a string
    with open(filename) as ftext:
        for line in ftext.readlines():
            poem += line

    #Pre-processing: Delete all the punctuation
    res = "".join(poem.split("."))
    res = "".join(res.split(","))
    res = "".join(res.split("?"))
    res = "".join(res.split("!"))
    res = "".join(res.split("--"))

    #Split the poem in verses(single line) and takes last word of each verse
    stri=res.split("\n")
    for i, val in enumerate(stri):
        if val!="":
            lastwords.append(val.split(" ")[-1])
    
    #Uses a double loop to compare the last characters [-parameter:] of each verse with each other
    rythm = [0] * len(lastwords)
    for i, val in enumerate(lastwords):
        test = val[-rhythmParameter:]
        j = i+1
        while j<len(lastwords):
            test2 = lastwords[j][-rhythmParameter:]
            if test == test2:
                if rythm[j] == 0 or rythm[i] == 0:
                    rythm[i] = i+1
                    rythm[j] = i+1
            j+=1

    #If there's a rhythm pattern it assigns a 1 (or true) value to its verse
    for ele, val in enumerate (rythm):
        if val!= 0:
            rythm[ele] = 1

    #Loop through the rhythm pattern vector and sums the true values
    for ele, val in enumerate (rythm):
        rhythmValue += val
    
    #Creates vector representation of the poem as a 7 position array with the structure: [rhythmValue, rareWordsRatio, typeTokenRatio, numberOfTypes, numberOfTokens, verses, paragraphCount]
    poemVectorRepresentation = [rhythmValue, rareWordsRatio, typeTokenRatio, numberOfTypes, numberOfTokens, verses, paragraphCount]

    #Appends to the matrix the vector of the poem analyzed
    poemsMatrix.append(poemVectorRepresentation)
    
    #Prints matrix of all poems analyzed
    for x in range(len(poemsMatrix)):
        print("{}: {}".format(x+1,poemsMatrix[x]))

    #If there's at least 2 elements, ask if the user'd like to compare two(2) poems    
    if len(poemsMatrix)>=2:
        answer = input("\nDo you want to compare two poems?(Y/N)")
        if(answer == "Y" or answer == "y" or answer == "YES"):
            compareA = 0
            compareB = 0
            #Uses loops to prevent user from entering wrong values
            while 1 > compareA or len(poemsMatrix) < compareA:
                try:
                    compareA = int(input("# of the first poem (1 - {}): ".format(len(poemsMatrix))))
                except ValueError:
                    print ("**Please enter an integer**")

            while 1 > compareB or len(poemsMatrix) < compareB:
                try:
                    compareB = int(input("# of the second poem (1 - {}): ".format(len(poemsMatrix))))
                except ValueError:
                    print ("**Please enter an integer**")

            #It shows: Cosine similarity, euclidean distance and dot product
            print("\nCosine similarity: {}".format(cosine_similarity(poemsMatrix[compareA-1], poemsMatrix[compareB-1])))
            print("Euclidean distance: {}".format(euclideanDistance(poemsMatrix[compareA-1], poemsMatrix[compareB-1])))
            print("Dot product: {}".format(dotProduct(poemsMatrix[compareA-1], poemsMatrix[compareB-1])))
