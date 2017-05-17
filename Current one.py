import math

#Author: Daniel F. Zuñiga H. @ National University of Colombia
#Script's Name: develop.py
#Version: V6.0.0 - Functional programming and fully operating
#Bogotá, Colombia [16 may 2017] @ 11:49 p.m

#A computational method to represent poems in parallel corpora
#The research has been based on Francis Webb corpus: 67 english-based poems and their spanish translation are used as main test subject.

#Improvements:
#      Mayor improvements in speed and resource management have to be made.

#Implements a dictionary (Key : Value) as a easy way to modificate the corpus to be studied
#The reason to use a dictionary is to facilitate the iteration through poems and their translation
dict = {# Book I
        "One's Self I Sing": "Yo Canto Para Mí Mismo",
        "To Foreign Lands": "A Las Naciones Extranjeras",
        "Eidolons": "Imágenes",
        "Beginning My Studies": "Al Comenzar Mis Estudios",
        "To the States": "A Los Estados",
        "Still Though the One I Sing": "El Himno Que Todavía Canto",
        "Shut Not Your Doors": "No Me Cierren Sus Puertas",
        "Poets to Come": "Poetas Futuros",
        "To You": "Para Ti",
        "Thou Reader": "Tú, Lector",
        # Book II
        "Starting from Paumanok": "Venido De Paumanok",
        # Book III
        "Song of Myself": "Canto A Mí Mismo",
        # Book IV
        "To the Garden the World": "Hacía El Jardín Del Mundo",
        "From Pent-Up Aching Rivers": "Desde Los Ríos Acorralados Y Dolientes",
        "A Woman Waits for Me": "Una Mujer Me Espera",
        "Spontaneous Me": "Espontáneo Soy",
        "One Hour to Madness and Joy": "Una Hora De Locura Y De Placer",
        "O Hymen! O Hymenee!": "¡Oh Himen!¡Oh, Himeneo!",
        "I Am He That Aches with Love": "Yo Soy Aquel",
        "Native Moments": "Nativos Instantes",
        "Once I Pass'd Through a Populous City": "Tiempo Ha Que Atravesé Una Populosa Ciudad",
        "Facing West from California's Shores": "Cara Al Oeste",
        "As Adam Early in the Morning": "Como Adán",
        # Book V
        "In Paths Untrodden": "En Las Sendas No Holladas",
        "Scented Herbage of My Breast": "Fragante Herbaje De Mi Pecho",
        "Whoever You Are Holding Me Now in Hand": "Cualesquiera Que Seáis Los Que Ahora",
        "For You, O Democracy": "Para Ti, ¡Oh Democracia!",
        "These I Singing in Spring": "Canción A La Primavera",
        "Not Heaving from My Ribb'd Breast Only": "Ni Agitando Sólo Mi Oprimido Pecho",
        "Of the Terrible Doubt of Appearances": "Con La Terrible Duda De Las Apariencias",
        "The Base of All Metaphysics": "La Base De Todas Las Metafísicas",
        "Recorders Ages Hence": "Archiveros Del Futuro",
        "When I Heard at the Close of the day": "Cuando Supe Al Cabo Del Día",
        "Are You the New Person Drawn Toward Me": "Eres La Nueva Persona Atraída Por Mí",
        "Roots and Leaves Themselves Alone": "Raíces Y Hojas Solamente",
        "Not Heat Flames Up and Consumes": "El Ardor De Las Llamas No Se Eleva Ni Se Consume",
        "Trickle Drops": "¡Escurríos, Gotas!",
        "City of Orgies": "Ciudad De Orgías",
        "Behold This Swarthy Face": "Contemplad Este Curtido Rostro",
        "I Saw in Louisiana a Live-Oak Growing": "He Visto En Louisiana Crecer Un Roble",
        "To a Stranger": "A Un Extranjero",
        "This Moment Yearning and Thoughtful": "En Este Momento...",
        "I Hear It Was Charged Against Me": "Sé Que Se Me Ha Acusado",
        "The Prairie-Grass Dividing": "Separando Las Hierbas De La Pradera",
        "When I Persue the Conquer'd Fame": "Cuando Repaso La Fama Conquistada",
        "We Two Boys Together Clinging": "Nosotros, Dos Muchachos, Abrazándonos",
        "A Promise to California": "Una Promesa A California",
        "Here the Frailest Leaves of Me": "Aquí, Las Fragilísimas Hojas Mías",
        "No Labor-Saving Machine": "Nada De Máquina Para Economizar Trabajo",
        "A Glimpse": "A tráves Del Intersticio",
        "A Leaf for Hand in Hand": "Una Hoja",
        "Earth, My Likeness": "Tierra, Mi Semejante",
        "I Dream'd in a Dream": "He Soñado En Un Sueño",
        "What Think You I Take My Pen in Hand": "Para Qué Creéis Que Tomo Mi Pluma",
        "To the East and to the West": "Hacia el Este Y Hacia El Oeste",
        "Sometimes with One I Love": "Algunas Veces, Con Uno Que Amo",
        "To a Western Boy": "A Un Muchacho Del Oeste",
        "Fast Anchor'd Eternal O Love!": "Eterno Amarrado Al Ancla, ¡Oh, Amor!",
        "Among the Multitude": "Entre La Multitud",
        "O You Whom I Often and Silently Come": "¡Oh Tú, Al Que A Menudo Y Silencioso Acudo!",
        "That Shadow My Likeness": "Esta Sombra, A Mí Semejante",
        "Full of Life Now": "Lleno De Vida, Ahora",
        # Book VI
        "Salut au Monde!": "Salut au Monde 1",
        # Book XX
        "Europe[The 72d and 73d Years of These States]": "Europa[El 72º y 73º años de estos Estados]",
        "Gods": "Dioses",
        # Book XXII
        "When Lilacs Last in the Dooryard Bloom'd": "Cuando Las Últimas Lilas Estaban En Flor",
        "O Captain! My Captain!": "Oh, Capitán, Mi Capitán"}


#Computes cosine distance of vector1 (v1) to vector2 (v2): 1 - (v1 . v2)/(||v1||*||v2||)
#Note: Remember that theorically "sqrt(sumxbyx*sumybyy)" is equal to "sqrt(sumxbyx)*sqrt(sumybyy)"
#      and computationally difference is about 2x10^-16
def cosine_distance(vector1,vector2):

    """Returns: Number [between 0 - 1]
       Parameters: vector1 [list] and vector2 [list]
    """

    sumxbyx, sumxbyy, sumybyy = 0, 0, 0
    for i in range(len(vector1)):
        x = vector1[i]; y = vector2[i]
        sumxbyx += x*x
        sumybyy += y*y
        sumxbyy += x*y
    return 1-(sumxbyy/math.sqrt(sumxbyx*sumybyy))


#Computes euclidean distance of vector1(V1) and vector2(V2): sqrt(+=(V1-V2)^2)
def euclideanDistance(vector1,vector2):

    """Returns: Number [between 0 - 1]
       Parameters: vector1 [list] and vector2 [list]
    """
    
    return sum([(x-y)**2 for (x,y) in zip(vector1,vector2)])**(0.5)


#Computes dot product distance of vector1(v1) and vector2(v2): 1 - ( +=v1*v2 )
def dotProductDistance(vector1, vector2):

    """Returns: Number [between 0 - 1]
       Parameters: vector1 [list] and vector2 [list]
    """
    
    return 1-sum(p*q for p,q in zip(vector1, vector2))


#Computes the normalization of a vector: each component * 1/||V||
def normalizeVector(vector):

    """Returns: List
       Parameters: vector [list]
    """
    
    returning = vector
    aid = 0
    for j in range(len(vector)):
        aid+= (vector[j]**2)
    aid = aid**0.5
    for i in range(len(vector)):
        returning[i]=float(vector[i])/aid
    return returning


#Count the number of paragraphs by counting the number of double linebreaks
def paragraphCount(poemName):

    """Returns: Number
       Parameters: poemName [String]
    """
    
    lineCount = 0
    paragraphCount = 1
    with open (poemName + ".txt", 'r') as ftext:
        for line in ftext.readlines():
            #If there's a double linebreak, it takes it as a paragraph
            if line in ('\n', '\r\n'):
                if lineCount == 0:
                    paragraphCount += 1
    return paragraphCount


#Counts the number of verses
def versesCount(poemName):

    """Returns: Number
       Parameters: poemName [String]
    """
    
    #Loops through the file enumerating each line, at the end it'll have the total number of lines in the file.
    #As it starts at 0, we need to add a +1 so lineCount is right; then we substract the number of paragraphs
    with open(poemName + ".txt") as file:        
        for n, line in enumerate(file):
            pass
    verses = n+1
    verses += (1-paragraphCount(poemName))

    return verses


#Calculates the rhyme of a single poem: The percentage of the poem that has rhyme
def rhymeCalculus(poemName, R_LengthParameter):

    """Returns: Number [between 0 - 1]
       Parameters: poemName [String], R_LengthParameter [Integer] 
    """
    
    #Helper variables to calculate rhyme metrics
    poem = ""
    lastwords = []
    rhymeValue = 0
    
    #Opens the poem's file and turns it into a string, this way it's easier to handle poems
    with open(poemName + ".txt") as ftext:
        for line in ftext.readlines():
            poem += line

    #Pre-processing: Delete all the punctuation
    res = "".join(poem.split("."))
    res = "".join(res.split(","))
    res = "".join(res.split("?"))
    res = "".join(res.split("!"))
    res = "".join(res.split("--"))
    res = "".join(res.split(")"))
    res = "".join(res.split("("))
    res = "".join(res.split(";"))

    #Split the poem into verses(single line) and takes last number of characters (specified by "R_LengthParameter") of each verse
    #Then they're added to a list (lastwords)
    stri=res.split("\n")
    for i, val in enumerate(stri):
        if val!="":
            lastwords.append(val[-R_LengthParameter:])
    
    #Uses a double loop to compare the last characters [-R_LengthParameter:] of each verse with each other
    #Creates a rhyme vector full of 0's and as it loops through the lastwords list, it matches the verses where there's rhyme
    rythm = [0] * len(lastwords)
    for i, val in enumerate(lastwords):
        test = val
        j = i+1
        while j<len(lastwords):
            test2 = lastwords[j]
            if test == test2:
                if rythm[j] == 0 or rythm[i] == 0:
                    rythm[i] = i+1
                    rythm[j] = i+1
            j+=1

    #If there's a rhyme pattern it assigns a 1 (or true) value to its verse.
    #This way, instead of visualizing the rhyme pattern of the poem, it's possible to get poem's rhyme as a binary representation 
    for ele, val in enumerate (rythm):
        if val!= 0:
            rythm[ele] = 1

    #Calculates the relative rhyme value of a poem
    #Loop through the rhythm pattern vector and sums the true values (the ones identified as 1)
    #then normalizes it by dividing by the number of verses (previously calculated), the result is a porcentage of rhythm through the poem
    for ele, val in enumerate (rythm):
        rhymeValue += val
    rhymeValue /= versesCount(poemName)
    
    return rhymeValue


#Returns the vector of a poem. It receives the name of the poem (poemName) and the rhyme parameter previously defined (R_LengthParameter)
def poemVector(poemName, R_LengthParameter):

    """Returns: List [with 7 positions]
       Parameters: poemName [String], R_LengthParameter [Integer] 
    """

    #Helper variables to calculate syntax metrics
    wordCount = {}
    paragraphs = 1
    lineCount = 0
    numberOfHapax = 0
    numberOfBis = 0
    numberOfTris = 0
    numberOfRareWords = 0
    rareWordsRatio = 0
    numberOfTypes = 0
    numberOfTokens = 0
    typeTokenRatio = 0

    #Syntax Metrics Calculus
    
    with open (poemName + ".txt", 'r') as ftext:
        for line in ftext.readlines():
            #If there's a double linebreak, it takes it as a paragraph
            if line in ('\n', '\r\n'):
                if lineCount == 0:
                    paragraphs += 1
                lineCount += 1
            #It separates every word and counts them individually
            #wordCount is a dictionary with the form [word : # of appearances]
            else:
                lineCount = 0
                for word in line.split():
                    wordCount[word] = wordCount.get(word,0) + 1
                    
    for i in wordCount:
        #Get the total number of words in the poem by adding all appearances of every word
        numberOfTokens +=wordCount[i]
        #Gets the number of appearances of unique words (Hapax), two (Bis) and three (Tris) appearances words by looping through the words array
        if wordCount[i] == 1:
            numberOfHapax += 1
        elif wordCount[i] == 2:
            numberOfBis += 1
        elif wordCount[i] == 3:
            numberOfTris += 1

    #Rare words: The adding of 1 (Hapax),2 (Bis) or 3 (Tris) appearances words
    numberOfRareWords = numberOfHapax + numberOfBis + numberOfTris
    #Types: # of words only taken once
    numberOfTypes = len(wordCount)
    #Calculates typeTokenRatio as shown and formats the number to only have 2 decimals
    typeTokenRatio = (numberOfTypes / numberOfTokens) * 100
    typeTokenRatio = float("{0:.2f}".format(typeTokenRatio))
    #Calculates rareWordsRatio as shown and formats the number to only have 2 decimals
    rareWordsRatio = numberOfRareWords/numberOfTypes
    rareWordsRatio = float("{0:.2f}".format(rareWordsRatio))

    #Creates vector representation of the poem as a 7 position array
    #It follows the next structure: [rhymeValue, rareWordsRatio, typeTokenRatio, numberOfTypes, numberOfTokens, verses, paragraphCount]
    poemVectorRepresentation = [rhymeCalculus(poemName,R_LengthParameter), rareWordsRatio, typeTokenRatio, numberOfTypes,numberOfTokens, versesCount(poemName),paragraphCount(poemName)]
    
    return poemVectorRepresentation


#Calculates the rhyme average of a full corpus. It receives the R_LengthParameter (number) and a key as string (corpus)
#Keys:
#     original -> Calculates rhyme average of original poems
#     translated -> Calculates rhyme average of translated poems
def rhymeCorpusAverage(R_LengthParameter, corpus):

    """Returns: Number [from 0 to 1]
       Parameters: R_LengthParameter [Integer], corpus [String]

       corpus = "original", "translated"
    """
    
    rhymeAverage = 0
    #According to the key calculates rhyme for each poem then adds it
    #and it's divided by the number of poems analyzed
    #(that's equal to the length of the dictionary)
    if corpus == "original":
        for key, value in dict.items():
            rhymeAverage += rhymeCalculus(key,R_LengthParameter)
        rhymeAverage /= len(dict)
        return rhymeAverage
    elif corpus == "translated":
        for key, value in dict.items():
            rhymeAverage += rhymeCalculus(value,R_LengthParameter)
        rhymeAverage /= len(dict)
        return rhymeAverage


#Plots Rhyme Average of a corpus Vs R_Length Parameter
#It receives the maximum R_Length Parameter it'll plot, that's it'll plot from 1 to that parameter
def plotRLengthVsRhymeAverage(Max_RLength):

    """Returns: None. Shows a plot.
       Parameters: Max_RLength [Integer]
    """
    
    #Plots two(2) curves: One for original poems and one for translated poems
    originalRhymeAverage = []
    translatedRhymeAverage = []

    #Automatically creates an array with the values of the RLengthParameter
    #These will be used as scale for the X-axis
    plotXAxis = list(range(1, Max_RLength+1))
    
    for rhymeParameter in range(1,Max_RLength+1):
        originalRhymeAverage.append(rhymeCorpusAverage(rhymeParameter,"original"))
        translatedRhymeAverage.append(rhymeCorpusAverage(rhymeParameter,"translated"))

    #Plotting settings
    import matplotlib.pyplot as plt
    plt.title('R-Length Parameter VS Rhyme Average in Corpus')
    plt.ylabel('Rhyme Average in Corpus')
    plt.xlabel('R-Length Parameter')
    plt.plot(plotXAxis,originalRhymeAverage,'-o', label="Original poems")
    plt.plot(plotXAxis,translatedRhymeAverage,'-o', label="Translated poems")
    plt.legend(loc='upper right')
    plt.show()


#Calculates each poem rhyme and sets them in a list
#It uses key words:
#                  "original" -> Gets the rhyme of each original poem
#                  "translated" -> Gets the rhyme of each translated poem
def eachPoemRhymeInCorpus(R_LengthParameter, corpus):

    """Returns: List [its length is = to dictionary length]
       Parameters: R_LengthParameter [Integer], corpus [String]

       corpus = "original", "translated"
    """
    
    # The idea is to use this function twice, so we get two lists
    #One with rhyme of original poems and one with rhyme of translated poems
    originalRhymes = []
    translatedRhymes = []
    if corpus == "original":
        for key, value in dict.items():
            originalRhymes.append(rhymeCalculus(key,R_LengthParameter))
        return originalRhymes
    elif corpus == "translated":
        for key, value in dict.items():
            translatedRhymes.append(rhymeCalculus(value,R_LengthParameter))
        return translatedRhymes


#Plots rhyme of original poems and one with rhyme of translated poems
#Each point represents translated poem rhyme (X-axis) vs original poem rhyme (Y-axis)
#If a point is plotted over or near the blue line, it means that translation conserved rhyme
def plotEachPoemRhymeInCorpus(RLengthParameter):

    """Returns: None. Shows a plot.
       Parameters: R_LengthParameter [Integer]
    """
    
    #Gets two lists with poems rhyme for each corpus
    traductionRhymes = eachPoemRhymeInCorpus(RLengthParameter,"translated")
    originalRhymes = eachPoemRhymeInCorpus(RLengthParameter,"original")

    #Calculates a +/- 20% of minimun and maximun values so plot seems centered
    #Applied to both X and Y axis
    lowerXPlotLimit = min(traductionRhymes) - (min(traductionRhymes)*20)/100
    upperXPlotLimit = max(traductionRhymes) + (max(traductionRhymes)*20)/100

    lowerYPlotLimit = min(originalRhymes) - (min(originalRhymes)*20)/100
    upperYPlotLimit = max(originalRhymes) + (max(originalRhymes)*20)/100

    #Plotting Settings
    #X-axis -> Translated poems rhyme
    #Y-axis -> Original poems rhyme
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    plt.title('Rhyme Comparison among poems. R-Length Parameter: {}'.format(RLengthParameter))
    plt.ylabel('Original Rhyme')
    plt.xlabel('Translated Rhyme') 
    plt.plot(traductionRhymes,originalRhymes,'ro')
    plt.plot([0,1], [0, 1])
    plt.axis([0,1,0,1])
    #plt.axis([lowerXPlotLimit, upperXPlotLimit, lowerYPlotLimit, upperYPlotLimit])

    #Label each point
    n = [0] * len(originalRhymes)
    for p in range(len(originalRhymes)):
        n[p]=p

    for i, txt in enumerate(n):
        ax.annotate(txt+1, (traductionRhymes[i],originalRhymes[i]))
    
    plt.show()


#Calculates poem matrix, it uses keys to know which matrix to calculate.
#Keys:
#     "original" -> Only calculates poem vector representation of original poems
#     "translated" -> Only calculates poem vector representation of translated poems
#     "originalNormalized" -> Only calculates poem normalized vector representation of original poems
#     "translatedNormalized" -> Only calculates poem normalized vector representation of translated poems
#     "corpus" -> Calculates poem vector representation of all poems. Original poems are placed
#                 from position [0] to position [half-1] and translated poems are placed from
#                 position [half] to position [lastElement]
#     "corpusNormalized" ->  Calculates poem normalized vector representation of all poems.
#                            Original poems are placed from position [0] to position [half-1]
#                            and translated poems are placed from position [half] to position [lastElement]
def poemsMatrix(whichOne, RLengthParameter):

    """Returns: List [length = dictionary length or 2*dictionary length]
       Parameters: whichOne [String], R_LengthParameter [Integer]

       whichOne = "original", "translated", "originalNormalized", "translatedNormalized", "corpus", "corpusNormalized"
    """
    
    poemsMatrix = []
    if whichOne == "original":
        for key, value in dict.items():
            poemsMatrix.append(poemVector(key,RLengthParameter))
        return poemsMatrix
    if whichOne == "translated":
        for key, value in dict.items():
            poemsMatrix.append(poemVector(value,RLengthParameter))
        return poemsMatrix
    if whichOne == "originalNormalized":
        for key, value in dict.items():
            poemsMatrix.append(normalizeVector(poemVector(key,RLengthParameter)))
        return poemsMatrix
    if whichOne == "translatedNormalized":
        for key, value in dict.items():
            poemsMatrix.append(normalizeVector(poemVector(value,RLengthParameter)))
        return poemsMatrix
    #In the case of corpus ones, first half represent original poems
    #and the second one represents translated poems
    if whichOne == "corpus":
        for key, value in dict.items():
            poemsMatrix.append(poemVector(key,RLengthParameter))
        for key, value in dict.items():
            poemsMatrix.append(poemVector(value,RLengthParameter))
        return poemsMatrix
    if whichOne == "corpusNormalized":
        for key, value in dict.items():
            poemsMatrix.append(normalizeVector(poemVector(key,RLengthParameter)))
        for key, value in dict.items():
            poemsMatrix.append(normalizeVector(poemVector(value,RLengthParameter)))
        return poemsMatrix


#Uses an independent list to place poems' name, so it'll be easy to refer to each poem
#Uses keys to get the correct poems' name:
#   original -> Gets only the original poems' name
#   translated -> Gets only the translated poems' name
#   corpus -> Gets all poems' name
def createPoemsNameVector(whichOne):

    """Returns: List [length = dictionary length or 2*dictionary length]
       Parameters: whichOne [String]

       whichOne = "original", "translated", "corpus"
    """
    
    poemsNameVector = []
    if whichOne == "original":
        for key, value in dict.items():
            poemsNameVector.append(key)
        return poemsNameVector
    if whichOne == "translated":
        for key, value in dict.items():
            poemsNameVector.append(value)
        return poemsNameVector
    #In the case of "corpus", first half represent original poems
    #and the second one represents translated poems
    if whichOne == "corpus":
        for key, value in dict.items():
            poemsNameVector.append(key)
        for key, value in dict.items():
            poemsNameVector.append(value)
        return poemsNameVector


#According to the key "whichOne" print the correspondent matrix
#Printing it's not formatted because this function is helpful to verificate/test results
def printMatrix(whichOne, RLengthParameter):

    """Returns: None. Prints data.
       Parameters: whichOne [String], RLengthParameter [Integer]

       whichOne = "original", "translated", "originalNormalized", "translatedNormalized", "corpus", "corpusNormalized"
    """
    
    #In each case:
    #1. Gets the poems name in a list
    #2. Gets the poems list
    #3. Prints a title
    #4. In each line prints "title" : "poem vector"
    if whichOne == "original" or whichOne == "translated" or whichOne == "corpus":
        poemsName = createPoemsNameVector(whichOne)
        poems = poemsMatrix(whichOne,RLengthParameter)
        print ("\nMatrix: {}\n".format(whichOne))
        for x in range(len(poems)):
            print("{}: {}".format(poemsName[x],poems[x]))
    if whichOne == "originalNormalized":
        poemsName = createPoemsNameVector("original")
        poems = poemsMatrix(whichOne,RLengthParameter)
        print ("\nMatrix: {}\n".format(whichOne))
        for x in range(len(poems)):
            print("{}: {}".format(poemsName[x],poems[x]))
    if whichOne == "translatedNormalized":
        poemsName = createPoemsNameVector("translated")
        poems = poemsMatrix(whichOne,RLengthParameter)
        print ("\nMatrix: {}\n".format(whichOne))
        for x in range(len(poems)):
            print("{}: {}".format(poemsName[x],poems[x]))
    if whichOne == "corpusNormalized":
        poemsName = createPoemsNameVector("corpus")
        poems = poemsMatrix(whichOne,RLengthParameter)
        print ("\nMatrix: {}\n".format(whichOne))
        for x in range(len(poems)):
            print("{}: {}".format(poemsName[x],poems[x]))


#Calculates the comparison matrix
#Position[1] = [cosine_distance1 , euclidean_distance1 , dot_distance1].
#For example if we have a dictionary like:
# "A" : "a"
# "B" : "b"
#Then this function will return a list (lenght = 2 = number of poems with translation)
#with each component having a list of 3 components (cosine, euclidean, dot)
def getComparisonMatrix(RLengthParameter):

    """Returns: List [Each position has a list of 3 components, its length is = to dictionary length]
       Parameters: RLengthParameter [Integer]
    """
    
    comparisonMatrix = []

    #Uses the full corpus matrix normalized and the full corpus names
    #This is: It analyze all poems
    poems = poemsMatrix("corpusNormalized",RLengthParameter)
    poemsName = createPoemsNameVector("corpus")

    #Uses "comparableParameter" to identify a poem and its traduction
    #poem @ position [1] <-> Translated poem @ position [1+comparableParameter]
    comparableParameter = len(dict)
    for x in range(comparableParameter):
        cosine = cosine_distance(poems[x], poems[x+comparableParameter])
        euclidean = euclideanDistance(poems[x], poems[x+comparableParameter])
        dot = dotProductDistance(poems[x], poems[x+comparableParameter])
        oneComparison = [cosine, euclidean, dot]
        comparisonMatrix.append(oneComparison)
    return comparisonMatrix


#Prints in a visually organized way the values of the comparison matrix obtained above
#This method was created for testing
def printValuesOfComparisonMatrix(RLengthParameter):

    """Returns: None. Prints data.
       Parameters: RLengthParameter [Integer]
    """
    
    matrix = getComparisonMatrix(RLengthParameter)
    print("Values of comparisons: Cosine distance, euclidean distance and dot distance\n")
    for x in range(len(matrix)):
        print(matrix[x])
    print()


#Prints in a formatted way the comparison matrix
#In this case each component of the matrix is taken as a formatted string
#with the poem's name, and string-like values of cosine, euclidean and dot distances
def printComparisonMatrix(RLengthParameter):

    """Returns: None. Prints data.
       Parameters: RLengthParameter [Integer]
    """
    
    comparisonMatrix = []
    #Uses the full corpus matrix normalized and the full corpus names
    #This is: It analyze all poems
    poems = poemsMatrix("corpusNormalized",RLengthParameter)
    poemsName = createPoemsNameVector("corpus")
    comparableParameter = len(dict)
    #Gets the length of the longest poem name; this is for printing format
    formatting = len(max(poemsName,key=len))

    #Calculates three(3) distances, format them as a string and then appends them to a list
    for x in range(comparableParameter):
        cosine = cosine_distance(poems[x], poems[x+comparableParameter])
        euclidean = euclideanDistance(poems[x], poems[x+comparableParameter])
        dot = dotProductDistance(poems[x], poems[x+comparableParameter])
        
        comparison = "" + poemsName[x]
        comparison = "{:<{}}|| ".format(comparison,formatting)
        comparison += "{:<23}|| {:<21}|| {:<20}".format(cosine, euclidean, dot)
        comparisonMatrix.append(comparison)
    #Formats comparison matrix printing
    print("Three Method Comparison Table for a RLength Parameter of: {}".format(RLengthParameter))
    print("\n{:<{}}{:<25}{:<28}{}".format("Name",formatting+4,"Cosine distance","Euclidean distance","Dot product"))
    numberFormatting = 73 + formatting 
    print("_"*numberFormatting)
    for x in range(len(comparisonMatrix)):
        print(comparisonMatrix[x])
    print()


#Demo - These are all the utilities the script can do
def getEverythingDone(RLengthParameter):
    printValuesOfComparisonMatrix(RLengthParameter)
    printComparisonMatrix(RLengthParameter)
    printMatrix("original",RLengthParameter)
    printMatrix("translated",RLengthParameter)
    printMatrix("corpus",RLengthParameter)
    printMatrix("originalNormalized",RLengthParameter)
    printMatrix("translatedNormalized",RLengthParameter)
    printMatrix("corpusNormalized",RLengthParameter)
    plotEachPoemRhymeInCorpus(RLengthParameter)
    plotRLengthVsRhymeAverage(10)

#Ask the user the # of characters to be analyzed as rhyme.
#Uses a "Baka-yoke" loop preventing wrong user input
RLengthParameter = ' '
while not RLengthParameter.strip().isdigit():
     RLengthParameter = input("# of characters to be analyzed on the rhyme: ")
RLengthParameter = int(RLengthParameter)

#Pacience -> Script isn't built to do things the fastest way.
#Use help(functionName) for a brief introduction to each function

#Uncomment next line if you want to test all script utilities
#getEverythingDone(RLengthParameter)
printComparisonMatrix(RLengthParameter)
plotEachPoemRhymeInCorpus(RLengthParameter)
plotRLengthVsRhymeAverage(10)

