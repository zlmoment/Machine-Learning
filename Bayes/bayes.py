from numpy import *

def load():
    postingList = [['I','love','this','car'],
                   ['this','view','is','amazing'],
                   ['I','feel','great','this','morning'],
                   ['I','am','so','exicted','about','this','concert'],
                   ['He','is','my','best','friend'],
                   ['I','do','not','like','this','car'],
                   ['this','view','is','horrible'],
                   ['I','feel','tired','this','morning'],
                   ['I','am','not','looking','forward','to','the','concert'],
                   ['He','is','my','enemy']]
    classVec = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # union
    return list(vocabSet)

def wordset2vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        #else:
        #    print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def train(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pPstv = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom) 
    p0Vect = log(p0Num / p0Denom) 
    return p0Vect, p1Vect, pPstv

def classify(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
 
def test():
    listOPosts, listClasses = load()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(wordset2vec(myVocabList, postinDoc))
    p0V, p1V, pPstv = train(array(trainMat), array(listClasses))
    testEntry = ['I','feel','happy','this','mornign']
    thisDoc = array(wordset2vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classify(thisDoc, p0V, p1V, pPstv)
    testEntry = ['Larry','is','my','friend']
    thisDoc = array(wordset2vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classify(thisDoc, p0V, p1V, pPstv)
    testEntry = ['I','do','not','like','this','man']
    thisDoc = array(wordset2vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classify(thisDoc, p0V, p1V, pPstv)
    testEntry = ['my','house','is','not','great']
    thisDoc = array(wordset2vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classify(thisDoc, p0V, p1V, pPstv)

