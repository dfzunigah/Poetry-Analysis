import math

#Daniel F. Zuñiga H. @ National University of Colombia
#fuctional.py
#V5.6.2 - Data visualization
#Bogotá, Colombia [11 may 2017] @ 4:25 a.m

#A computational method to represent poems in parallel corpora
#The research has been based on Francis Webb corpus. 67 english-based poems and their spanish translation are used as main test subject.

#Note: (Improvements) Algorithm is not yet finished but it's functional.
#      Mayor improvements in speed and resource management have to be made.
#      Next step is to structure a more efficient way (Functional based or object oriented) to develop the process

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

#Computes cosine distance of vector1 (v1) to vector2 (v2): (v1 . v2)/{||v1||*||v2||)
#Note: Remember that theorically "sqrt(sumxbyx*sumybyy)" is equal to "sqrt(sumxbyx)*sqrt(sumybyy)"
#      and computationally difference is about 2x10^-16
def cosine_distance(vector1,vector2):    
    sumxbyx, sumxbyy, sumybyy = 0, 0, 0
    for i in range(len(vector1)):
        x = vector1[i]; y = vector2[i]
        sumxbyx += x*x
        sumybyy += y*y
        sumxbyy += x*y
    return 1-(sumxbyy/math.sqrt(sumxbyx*sumybyy))

#Computes euclidean distance of vector1(V1) and vector2(V2): sqrt(+=(V1-V2)^2)
def euclideanDistance(vector1,vector2): 
    return sum([(x-y)**2 for (x,y) in zip(vector1,vector2)])**(0.5)

#Computes dot product distance of vector1(v1) and vector2(v2): +=v1*v2
def dotProductDistance(vector1, vector2):
    return 1-sum(p*q for p,q in zip(vector1, vector2))

#Normalizes a vector: each component * 1/||V||
def normalizeVector(vector):
    aid = 0
    for j in range(len(vector)):
        aid+= (vector[j]**2)
    aid = aid**0.5
    for i in range(len(vector)):
        vector[i]=float(vector[i])/aid
    return vector

#Ask the user the # of characters to be analyzed as rhyme.
#Uses a "Baka-yoke" loop preventing wrong user input
rhymeParameter = ' '
while not rhymeParameter.strip().isdigit():
     rhymeParameter = input("# of characters to be analyzed on the rhyme: ")
rhymeParameter = int(rhymeParameter)

#Returns the vector of a poem. It receives the name of the poem (poemName) and the rhyme parameter previously defined (rhymeParameter)
def poemVector(poemName, rhymeParameter):
    
    #Helper variables to calculate rhyme metrics
    poem = ""
    lastwords = []
    rhymeValue = 0

    #Helper variables to calculate syntax metrics
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

    #Syntax Metrics Calculus
    
    with open (poemName + ".txt", 'r') as ftext:
        for line in ftext.readlines():
            #If there's a double linebreak, it takes it as a paragraph
            if line in ('\n', '\r\n'):
                if lineCount == 0:
                    paragraphCount += 1
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

    #Loops through the file enumerating each line, at the end it'll have the total number of lines in the file.
    #As it starts at 0, we need to add a +1 so lineCount is right; then we substract the number of paragraphs
    with open(poemName + ".txt") as file:        
        for n, line in enumerate(file):
            pass
    verses = n+1
    verses += (1-paragraphCount)

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

    #Rhyme Metrics Calculus
    
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

    #Split the poem in verses(single line) and takes last number of characters (specified by "rhymeParameter") of each verse
    #Then they're added to a list
    stri=res.split("\n")
    for i, val in enumerate(stri):
        if val!="":
            lastwords.append(val[-rhymeParameter:])
    
    #Uses a double loop to compare the last characters [-rhymeParameter:] of each verse with each other
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
    rhymeValue /= verses

    #Creates vector representation of the poem as a 7 position array
    #It follows the next structure: [rhymeValue, rareWordsRatio, typeTokenRatio, numberOfTypes, numberOfTokens, verses, paragraphCount]
    #Then normalize the vector using the function previously defined
    poemVectorRepresentation = [rhymeValue, rareWordsRatio, typeTokenRatio, numberOfTypes, numberOfTokens, verses, paragraphCount]
    #poemVectorRepresentation = normalizeVector(poemVectorRepresentation)
    
    return poemVectorRepresentation

#General Analysis Variables

#Poems Matrix: It allows to stack poems' vector representation so it'd be easy to compare them
poemsMatrix = []
#Comparison Matrix: Allows to see the three comparing methods for a series of comparisons
comparisonMatrix = []
#Poems' name stacked. As it's an secuencial algorithm poem in poemsNameVector = [1] is the name corresponding to the poem in poemsMatrix = [1]
poemsNameVector = []
#Used to know how many poems there are in the corpus
comparableParameter = 0

#Loops through corpus dictionary adding each poem to the poems matrix (poemsMatrix) and their name to the poems name vector (poemsNameVector)
#We uses a two independent loops, so original poems are placed from bottom [position 0] to half corpus/matrix [position comparableParameter] and
#translated poems are placed from half corpus/matrix [position comparableParameter] to top [positon last-item]
for key, value in dict.items():
    poemsMatrix.append(poemVector(key,rhymeParameter))
    poemsNameVector.append(key)
comparableParameter = len(poemsMatrix)
for key, value in dict.items():
    poemsMatrix.append(poemVector(value,rhymeParameter))
    poemsNameVector.append(value)

#Data Visualisation Analysis

#Prints matrix of all poems analyzed with an specific rhyme parameter
#This method was defined for checking the proper functioning of the algorithm
def printPoemsMatrix():
    
    for x in range(len(poemsMatrix)):
        print("{}: {}".format(poemsNameVector[x],poemsMatrix[x]))

#Plots corpus rhyme using 2-tuples as (translated poem rhyme, original poem rhyme)
#If rhyme is perfect for the whole corpus it's expected to represent a diagonal line
def plotCorpusRhyme():
    
    for x in range(len(poemsMatrix)):
        rhymes = [item[0] for item in poemsMatrix]
    originalRhymes = rhymes[:comparableParameter]
    traductionRhymes = rhymes[comparableParameter:]

    #Calculates a +/- 20% of minimun and maximun values so plot seems centered
    #Applied to both X and Y axis
    lowerXPlotLimit = min(traductionRhymes) - (min(traductionRhymes)*20)/100
    upperXPlotLimit = max(traductionRhymes) + (max(traductionRhymes)*20)/100

    lowerYPlotLimit = min(originalRhymes) - (min(originalRhymes)*20)/100
    upperYPlotLimit = max(originalRhymes) + (max(originalRhymes)*20)/100

    #Assigns labels, plots a reference line, plots 2-tuples as red circles ('ro') then centers the plot
    #X-axis -> Translated poems rhyme
    #Y-axis -> Original poems rhyme
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    plt.title('Rhyme Comparison among poems')
    plt.ylabel('Original Rhyme')
    plt.xlabel('Translated Rhyme') 
    plt.plot(traductionRhymes,originalRhymes,'ro')
    plt.plot([0,1.2], [0, 1.2])
    plt.axis([lowerXPlotLimit, upperXPlotLimit, lowerYPlotLimit, upperYPlotLimit])

    n = [0] * len(originalRhymes)
    for p in range(len(originalRhymes)):
        n[p]=p

    for i, txt in enumerate(n):
        ax.annotate(txt+1, (traductionRhymes[i],originalRhymes[i]))
    
    plt.show()

#Demo
plotCorpusRhyme()



        
