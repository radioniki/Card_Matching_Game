import random
from card_game_setup import *
from game_logic import *
from src.game_logic import equal

lists = create_lists()

def backboard(lists,lvl):
    '''Kataskevazei ena pinaka pou krataei tis times tou paixnidiou
     a -> Deikths Duskolias
     lists -> Lista pou periexei tis listes gia th kathe periptwsh

     >>> len(lines) == 5
     True
    '''
    lines = [[], [], [], [], []]
    if lvl == 1:
        w_list = lists[lvl - 1] # stands for working_lists
        maxi = 16
        for y in range(5):
            if y == 0:
                for first in range(5):
                    lines[0].append(first)
            else:
                for i in range(5):
                    if i == 0:
                        lines[y].append(y)
                    else:
                        k = random.randint(0,maxi-1)
                        lines[y].append(w_list[k])
                        w_list.pop(k)
                        maxi = maxi - 1
    elif lvl == 2:
        w_list = lists[lvl - 1] # stands for working_lists
        maxi = 40
        for y in range(5):
            if y == 0:
                for first in range(11):
                    lines[0].append(first)
            else:
                for i in range(11):
                    if i == 0:
                        lines[y].append(y)
                    else:
                        k = random.randint(0, maxi-1)
                        lines[y].append(w_list[k])
                        w_list.pop(k)
                        maxi = maxi - 1
    elif lvl == 3:
        w_list = lists[lvl - 1] # stands for working_lists
        maxi = 52
        for y in range(5):
            if y == 0:
                for first in range(13):
                    lines[0].append(first)
            else:
                for i in range(13):
                    if i == 0:
                        lines[y].append(y)
                    else:
                        k = random.randint(0,maxi-1)
                        lines[y].append(w_list[k])
                        w_list.pop(k)
                        maxi = maxi - 1
    return lines



def get_size(level):
    """ Epistrefei twn aritmo twn sthlwn tou sugkekrimenou paixnidiou
    >>> get_size(1) == 4
    True
    >>> get_size(3)
    13

    """
    if level == 1:
        return 4
    elif level == 2:
        return 10
    else:
        return 13


def print_board(board,level):
    '''Emfanizei thn ekastote katastash tou pinaka'''
    n = level_cards(level)
    for line in range(5):
        for i in range(n+1):
            if i < n:
                if line == 0 and i !=0 and i < 10:
                    print(board[line][i],end='   ')
                elif line == 0 and i != 0:
                    print(board[line][i], end='  ')
                elif line != 0 and i != 0 and len(str(board[line][i])) == 1:
                    print(board[line][i], end='   ')
                elif line != 0 and i != 0 and len(str(board[line][i])) < 3:
                    print(board[line][i],end='  ')
                elif line != 0 and i != 0 and len(str(board[line][i])) == 3:
                    print(board[line][i],end=' ')
                else:
                    print(board[line][i], end=' ')
            else:
                print(board[line][i])





def answer(name,levely):
    """Epistrefei Pinaka me tis suntetagmenes pou dialegei o paixths"""
    total = []
    size = 0
    if levely == 1:
        size = 4
    elif levely == 2:
        size = 10
    elif levely == 3:                       #size = μέγεθος του πίνακα
        size = 13
    for i in range(1,5):
        for y in range(1,size + 1):
            total.append([i, y])
    sunt = []                               #sunt = lista me thn epilogh tou paixth (arxika kenh)
    while sunt not in total:
        checked = False
        print(name,end=': ')
        k = input('Δώσε γραμμή και στήλη κάρτας :')
        k.strip()                              #vgazw ta kena spaces aristera kai dejia
        sunt = k.split(' ')
        try:
            sunt[0] = int(sunt[0])
            sunt[1] = int(sunt[1])
        except:
            print('Λάθος Δεδομένο , παρακαλώ προσπαθήστε ξανά !')       #data check
            checked = True
        if sunt not in total  and checked == False:
            print('Δεδομένα εκτός ορίων')
            print('Παρακαλώ προσπαθήστε ξανά!')
    return sunt


def cards_to_turn(level):
    '''Epistrefei to poses kartes uparxoun se kathe epipedo
    >>>cards_to_turn(1)
    16
    >>>cards_to_turn(2)
    40
    >>>cards_to_turn(3) == 52
    True
    '''
    if level == 1:
        cards = 16
    elif level == 2:
        cards = 40
    else:
        cards = 52
    return cards


def check_last(display,back_board,lvl):
    '''Elengxei an uparxoun peraitero dunates antistoixies ston pinaka'''
    n = get_size(lvl)
    i = 0



    #   Gia kathe stoixeio sto display pou den exei anoixtei kai ara exei value 'X' to sugrinei me ola ta upoloipa
    #  pou den exoun anoixtei gia na dei an uparxei dunath antistoixia

    while i < 5:
        j = 0
        while j < n + 1:
            if display[i][j] == 'X':
                key = back_board[i][j]
                i2 = 0
                while i2 < 5:
                    j2 = 0
                    while j2 < n + 1:
                        if display[i2][j2] == 'X':
                            key2 = back_board[i2][j2]
                            if key != key2:
                                if equal(key,key2) or equal_ad(key,key2):
                                    return True
                        j2 += 1
                    i2 += 1
            j += 1
        i += 1
    return False


def bot_choose(display,lvl):
    '''Function pou dialegei tuxaia mia kleisth karta gia na anoijei to botaki'''
    n = get_size(lvl)
    k1 = random.randint(1,4)
    k2 = random.randint(1,n)
    while display[k1][k2] != 'X':
        k1 = random.randint(1, 4)
        k2 = random.randint(1, n)
    return [k1,k2]




def unpack(board):
    '''Kanei unpack to board to opoio periexei ws stoixeia tou kai alles listes'''
    unpacked_list = []
    for i in board:
        for j in i:
            unpacked_list.append(j)
    return unpacked_list


def has_answer(bot):
    '''Epistrefei tis kartes i,j an uparxei antistoixia , alliws epistrefei False

    >>>has_answer([])
    False
    >>>has_answer(['10♦','Q♦'])
    ['10♦','Q♦']
    '''
    if len(bot) == 0:
        return False
    for i in bot:
        for j in bot:
            if i != j and equal_ad(i,j):
                return [i,j]
    return False


def search(board,lvl,card):
    '''Kanei anazhthsh thn karta (card) ston pinaka board
    board -> Pinakas opou ginetai h anazhthsh
    lvl -> epipedo duskolias
    card -> karta pros anazhthsh
    '''
    n = get_size(lvl)
    for i in range(1,5):
        j = 0
        while j < n +1:
            if board[i][j] == card:
                return [i,j]
            j += 1
