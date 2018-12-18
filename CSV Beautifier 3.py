#Modules---------------------------------------------------------------------------------------------------------------------------
import curses
from curses import wrapper
#Functions-------------------------------------------------------------------------------------------------------------------------
def contents(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            result.append(line)
    return result


def add_number_from_i(i, n, List):
    if (n == 0):
        return
    while (i < len(List)):
        List[i] += n
        i += 1


def make_the_matris(content_list):
    result = []
    for string in content_list:
        Tmp = ''
        quotation_exist = False
        tmp_list = []
        for char in string:
            if (char == '"' and not quotation_exist):
                quotation_exist = True
            elif (char == '"' and quotation_exist):
                quotation_exist = False
            if (char == ',' and not quotation_exist):
                tmp_list.append(Tmp)
                Tmp = ''
            elif (char != '\n' and char != '"'):
                Tmp += char
        else:
            tmp_list.append(Tmp)
        result.append(tmp_list)
    return result


def make_new_line(matris, i, column_count):
    tmp = ['' for _ in range(column_count)]
    matris.insert(i+1, tmp)


def make_max_length_list(matris):
    result = []
    for i in range(len(matris[0])):
        Max = 0
        for j in range(len(matris)):
            if (len(matris[j][i]) > Max):
                Max = len(matris[j][i])
        result.append(Max)
    return result


def make_divider_line(max_length_list):
    string = "+-----"
    for element in max_length_list:
        string += '-' * element
    else:
        string += '+'
    return string


def justify(string, number):
    return string + (' ' * (number - len(string)))


def add_line_if_necessary(matris, i, max_width, divider_line_index_list, max_length_list):
    j = 0
    icopy = i
    while (j < len(matris[0])):
        add_number_from_i(i, len(matris[i][j]) //
                          max_width, divider_line_index_list)
        while (len(matris[i][j]) > max_width):
            tmp = matris[i][j][max_width:]
            matris[i][j] = matris[i][j][:max_width]
            max_length_list[j] = max_width
            if (i+1 < len(matris) and matris[i+1][j] == ''):
                matris[i+1][j] = tmp
                i += 1
            else:
                make_new_line(matris, i, len(matris[0]))
                matris[i+1][j] = tmp
                i += 1
        i = icopy
        j += 1


def print_the_table(stdscr, matris, max_length_list, divider_line, divider_line_index_list):
    stdscr.addstr(divider_line + '\n')  # print(divider_line)
    index = 0
    for i in range(len(matris)):
        stdscr.addstr('|')  # print("|", end='')
        for j in range(len(matris[0])):
            # print(justify(matris[i][j], max_length_list[j]), end='')
            stdscr.addstr(justify(matris[i][j], max_length_list[j]))
            stdscr.addstr('|')  # print("|", end='')
        stdscr.addstr('\n')
        if (index < len(divider_line_index_list) and i == divider_line_index_list[index]):
            stdscr.addstr(divider_line + '\n')  # print(divider_line)
            index += 1


def make_dotted_matris(given_matris, index, max_width):
    for i in range(len(given_matris)):
        for j in range(len(given_matris[0])):
            if (i != index and len(given_matris[i][j]) > max_width):
                given_matris[i][j] = given_matris[i][j][:max_width-3] + '...'


def main(stdscr):
    stdscr.clear()
    currentPoint = 1
    matris = make_the_matris(content_list)
    max_length_list = make_max_length_list(matris)
    while (True):
        stdscr.clear()
        matris = make_the_matris(content_list)
        copy_of_matris = matris.copy()
        divider_line_index_list = [i for i in range(len(matris))]
        make_dotted_matris(copy_of_matris, currentPoint, max_width)
        add_line_if_necessary(copy_of_matris, currentPoint,
                              max_width, divider_line_index_list, max_length_list)
        divider_line = make_divider_line(max_length_list)
        print_the_table(stdscr, copy_of_matris, max_length_list,
                        divider_line, divider_line_index_list)
        c = stdscr.getch()
        if (c == curses.KEY_UP):
            currentPoint -= 1
        if (c == curses.KEY_DOWN):
            currentPoint += 1
        if (currentPoint == len(matris)):
            currentPoint = 0
        elif (currentPoint == -1):
            currentPoint = len(matris) - 1


#Main Program----------------------------------------------------------------------------------------------------------------------
content_list = contents(input("Please Enter The Directory of Your CSV File : "))
max_width = int(input("Please Enter Your Maximum Width : "))
wrapper(main)