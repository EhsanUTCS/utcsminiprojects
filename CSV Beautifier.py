#Functions-------------------------------------------------------------------------------------------------------------------------
def contents(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            result.append(line)
    return result


def FindMaxLength(Matris):
    MaxList = []
    for List in Matris:
        Max = 0
        for i in range(len(List)):
            if (len(List[i]) > Max):
                Max = len(List[i])
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
        for item in contentList[i]:
            if (item == ","):
                matrisBasedList[index].append(TmpString)
                index += 1
                TmpString = ""
            elif (item != '\n'):
                TmpString += item
        else:
            matrisBasedList[index].append(TmpString)


def printTheTable(matrisBasedList, MaxLengthList, dividerLine):
    print(dividerLine)
    for i in range(len(matrisBasedList[0])):
        print('|', end='')
        for j in range(len(matrisBasedList)):
            print(justify(matrisBasedList[j][i], MaxLengthList[j]), end='')
            print('|', end="")
        print()
        print(dividerLine)


#Main Program----------------------------------------------------------------------------------------------------------------------
contentList = contents(input())
matrisBasedList = [[] for _ in range(6)]
processTheContents()
MaxLengthList = FindMaxLength(matrisBasedList)
dividerLine = MakeLine(MaxLengthList)
printTheTable(matrisBasedList, MaxLengthList, dividerLine)