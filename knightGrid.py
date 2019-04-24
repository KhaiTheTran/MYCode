# -*- coding: cp1252 -*-
# Khai The Tran
# trank6@uw.edu
# Computer Science
# UW Seattle
# 11/27/2017

"""ExtraHop Programming Problem

Problem: Please write a function in Python that takes an 8x8 grid of letters and
a list of words and returns the longest word from the list (ignoring case) that
can be produced from the grid using the following procedure:

Start at any position in the grid, and use the letter at that position as the
first letter in the candidate word.
Move to a position in the grid that would be a valid move for a knight in a
game of chess, and add the letter at that position to the candidate word.
Repeat step 2 any number of times.

For example, if the list of words is ["algol", "fortran", "simula"] and the grid
is:

  1 2 3 4 5 6 7 8
1 Q W E R T N U I
2 O P A A D F G H
3 T K L Z X C V B
4 N M R W F R T Y
5 U I O P A S D F
6 G H J O L Z X C
7 V B N M Q W E R
8 T Y U I O P A S

...then the longest word from the list that can be produced using the rules is
“fortran”, by starting at the ‘F’ at position (5, 4), and moving to (4, 6), then
(3, 4), (1, 3), back to (3, 4) and then (4, 2) and finally (6,1). Again, note
that the match is case-insensitive, and that grid positions can be reused.

Create a list of words found in Shakespeare’s early comedy, Love’s Labour’s
Lost (text available at http://shakespeare.mit.edu/lll/full.html). Make sure to
remove punctuation and ignore case when generating the word list. What is the
output of your function using this word list on the grid below?

        E X T R A H O P
        N E T W O R K S
        Q I H A C I Q T
        L F U N U R X B
        B W D I L A T V
        O S S Y N A C K
        Q W O P M T C P
        K I P A C K E T
"""
import re, string
#
#
#
def readData(filename):
#read file (processing)
    fileoutput = open(filename, 'r')
    data = ''
    data = fileoutput.read()
    return(data)
# put data to a array
#
#
def dataListArray(listdata):
#input
    data= []
#procesing
    data = readData(listdata).strip().split()
    return data
# looking for the longest word
#
#
def dataArray(listdataArray):
#input
    regex = re.compile('[^a-z]')
    dataOut = ''
    dataOut1 = ''
#procesing
    for i in listdataArray:
        i=i.lower()
        dataOut = regex.sub('',i)
        if len(dataOut) > len(dataOut1):
            dataOut1 = dataOut
        
    return (dataOut1)
    
# the Knight looks for the way to go
#
#
def findKnightWay(theWord,wordArray, iA):
    marchResult = []
    row = 0
    colum = 0
    iA= iA+1
# set up colum and row
    if (iA%8)== 0 and iA >= 8:
        row = iA/8
        colum = 8 
    elif (iA%8) >= 0 and iA < 8:
        row = 1
        colum = iA%8
    elif (iA%8)> 0 and iA >8:
        row = (iA/8)+1
        colum = iA%8
# looking for possible steps of Knight
    if colum <= 6 and theWord.upper() ==(wordArray[iA+9]).upper() and row <8:
        marchResult.append(str(row+1)+' '+str(colum+2))
        
    if colum >= 3 and theWord.upper() == (wordArray[iA+5]).upper() and row <8:
        marchResult.append(str(row+1)+' '+str(colum-2))
        
    if colum != 8 and theWord.upper() == (wordArray[iA+16]).upper() and row <7:
        marchResult.append(str(row+2)+' '+str(colum+1))
        
    if colum != 1 and theWord.upper() == (wordArray[iA+14]).upper() and row <7:
        marchResult.append(str(row+2)+' '+str(colum-1))
        
    if colum <= 6 and theWord.upper() == (wordArray[iA-7]).upper() and row > 1:
        marchResult.append(str(row-1)+' '+str(colum+2))
        
    if colum >= 3 and theWord.upper() == (wordArray[iA-11]).upper() and row > 1:
        marchResult.append(str(row-1)+' '+str(colum-2))
        
    if colum != 8 and theWord.upper() == (wordArray[iA-16]).upper() and row > 2:
        marchResult.append(str(row-2)+' '+str(colum+1))
        
    if colum != 1 and theWord.upper() == (wordArray[iA-18]).upper() and row > 2:
        marchResult.append(str(row-2)+' '+str(colum-1))

    return marchResult

# find position of char in grid
def countStep(nextIndex):
    a = int(nextIndex[0])
    b = int(nextIndex[2])
    return ((a-1)*8+b-1)
def findRowCol(iA):
    row = 0
    colum = 0
    iA= iA+1
# set up colum and row
    if (iA%8)== 0 and iA >= 8:
        row = iA/8
        colum = 8 
    elif (iA%8) >= 0 and iA < 8:
        row = 1
        colum = iA%8
    elif (iA%8)> 0 and iA >8:
        row = (iA/8)+1
        colum = iA%8
    return (str(row)+' '+str(colum))
#count the steps and position of Knight
def stepofKnight(theWord,wordArray):
    listKnightStep = []
    KnightStep = []
    numArray =0
    count = 2
    finishWord = True
    nextIndex=''
    for j in wordArray:
        if j.upper() == theWord[0].upper():
                listKnightStep = findKnightWay(theWord[1],wordArray,numArray)
                if len(listKnightStep) != 0:
                    print("Starting at the '"+theWord[0].upper()+ "' at position:")
                    print(int(findRowCol(numArray)[0]),int(findRowCol(numArray)[2]))
                    #KnightStep.append(findRowCol(numArray))
                    nextIndex = str(listKnightStep[0])
                    print('And moving to:'+wordArray[countStep(nextIndex)])
                    print(int((listKnightStep[0])[0]), int((listKnightStep[0])[2]))
                    #KnightStep.append(listKnightStep)
                    
                    # Knight step
                    while finishWord:
                        listKnightStep = findKnightWay(theWord[count],wordArray,countStep(nextIndex))
                       # KnightStep.append(listKnightStep)
                        print('And then: '+str(theWord[count]).upper())
                        print(int((listKnightStep[len(listKnightStep)-1])[0]), int((listKnightStep[len(listKnightStep)-1])[2]))
 
                        if len(listKnightStep) > 1:
                            nextIndex = str(listKnightStep[len(listKnightStep)-1])
                        elif len(listKnightStep) > 0:
                            nextIndex = str(listKnightStep[0])
                        count = count +1
                        if len(theWord)== count:
                            finishWord = False                                                     
        if len(KnightStep)+1 == len(theWord):
            break
        numArray = numArray +1
    #return (KnightStep)
    
def main():
    listdata ='Loves_Labours_Lost.txt'
    listKnight ='knightWay.txt'
    print('Hello, This is the ExtraHop Programming Problem!')
    theWord = dataArray(dataListArray(listdata))
    print('The longest word is: '+theWord.upper())
    print('The Grid: \n'+readData(listKnight))
    wordArray = []
    wordArray = dataListArray(listKnight)
    #Show Knight steps
    
    stepofKnight(theWord,wordArray)

main()
    


