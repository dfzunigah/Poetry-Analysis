#Poems' Rhythm Pattern Matrix
poemsMatrix =[]
#Number of characters taken into account to make the analysis
parameter = int(input("# of characters to analyze: "))
numberOfPoemsToAnalyse = int(input("How many poems do you want to analyze?: "))

for i in range(numberOfPoemsToAnalyse): 
    filename = input("\nName of the poem: ")
    poem = ""
    lastwords = []

    #Opens a file (e.j: "firstPoem.txt") and turns it into a string
    with open(filename) as ftext:
        for line in ftext.readlines():
            poem = poem + line

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
        test = val[-parameter:]
        j=i+1
        while j<len(lastwords):
            test2 =lastwords[j][-parameter:]
            if test==test2:
            
                if rythm[j]==0 or rythm[i]==0:
                    rythm[i] = i+1
                    rythm[j] = i+1
            j=j+1

    #If there's a rhythm pattern it assigns a 1 (or true) value to its verse
    for ele, val in enumerate (rythm):
        if val!=0:
            rythm[ele]=1

    #Loop through the rhythm pattern vector and sums the true values
    rhythmValue = 0
    for ele, val in enumerate (rythm):
        rhythmValue +=val

    print("Rhythm Value: {}".format(rhythmValue))
    print(rythm)
    print(lastwords)
    print("\nMatrix:\n")
    poemsMatrix.append(rythm)
    for ele in range(len(poemsMatrix)):
        print(poemsMatrix[ele])

