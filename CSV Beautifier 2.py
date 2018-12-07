#Functions-------------------------------------------------------------------------------------------------------------------------
def contents(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            result.append(line)
    return result

def addNumberFromI (i ,n, List):
    while (i < len(List)):
        List[i] += n
        i += 1


def FindMaxLength(Matris, lineLimit):
    MaxList = []
    for List in Matris:
        Max = 0
        index = 0
        for i in range(len(List)):
            if (len(List[i]) > Max):
                Max = len(List[i])
                index = i
            if (len(List[i]) > lineLimit):
                addNumberFromI(i+1 , len(List[i]) // lineLimit , divideLineIndexes)
        MaxList.append(Max)
    return MaxList


def MakeLine(List):
    string = "+-----"
    for element in List:
        string += '-' * element
    else:
        string += '+'
    return string


def justify(string, number):
    return string + (' ' * (number - len(string)))


def processTheContents():
    for i in range(len(contentList)):
        index = 0
        TmpString = ""
        quotationExist = False
        for item in contentList[i]:
            if (item == '"' and not quotationExist):
                quotationExist = True
            elif (item == '"' and quotationExist):
                quotationExist = False
            if (item == "," and quotationExist == False):
                matrisBasedList[index].append(TmpString)
                index += 1
                TmpString = ""
            elif (item != '\n' and item != '"'):
                TmpString += item
        else:
            matrisBasedList[index].append(TmpString)


def printTheTable(matrisBasedList, MaxLengthList, dividerLine):
    index = 0
    for i in range(len(matrisBasedList[0])):
        if (index < len(divideLineIndexes) and i == divideLineIndexes[index]):
            print(dividerLine)
            index += 1
        print('|', end='')
        for j in range(len(matrisBasedList)):
            print(justify(matrisBasedList[j][i], MaxLengthList[j]), end='')
            print('|', end="")
        print()
    print(dividerLine)


def makeNewLine(stringToAdd, i, j):
    for k in range(len(matrisBasedList)):
        matrisBasedList[k] = matrisBasedList[k][:j+1] + [""] + matrisBasedList[k][j+1:]
    matrisBasedList[i][j+1] = stringToAdd


def addLinesIfNecessary(matrisBasedList , lineLimit):
    i = 0
    while (i < len(matrisBasedList[0])):
        j = 0
        while(j < len(matrisBasedList)):
            while (len(matrisBasedList[j][i]) > lineLimit):
                Tmp = matrisBasedList[j][i][lineLimit:]
                matrisBasedList[j][i] = matrisBasedList[j][i][:lineLimit]
                makeNewLine(Tmp, j, i)
                MaxLengthList[j] = lineLimit
            j += 1
        i += 1


#Main Program----------------------------------------------------------------------------------------------------------------------
contentList = contents(input("Please Enter The Directory of Your CSV File : "))
allLineLimit = int(input("Please Enter Your Maximum Length of Each Table Content : "))
matrisBasedList = [[] for _ in range(6)]
processTheContents()
divideLineIndexes = [i for i in range(len(matrisBasedList[0]))]
MaxLengthList = FindMaxLength(matrisBasedList, allLineLimit)
addLinesIfNecessary(matrisBasedList,allLineLimit)
dividerLine = MakeLine(MaxLengthList)
printTheTable(matrisBasedList, MaxLengthList, dividerLine)