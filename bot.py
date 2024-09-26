from game_play_utils import *
from card_game_setup import *
from game_logic import *
import random
from time import sleep


def bot_game():
    lists = create_lists()
    players = 2
    player_list = []
    points = []
    my_name = input('Player , Δώσε το όνομά σου :')
    while my_name == 'The Bot' or my_name == 'The_Bot':
        print('Αυτό είναι το δικό μου όνομα !')
        my_name = input('Player , Δώσε το όνομά σου :')
    player_list.append(my_name)
    points.append(0)
    player_list.append('The_Bot')
    points.append(0)
    print(player_list)
    print(points)
    lvl = level()
    lines = [[], [], [], [], []]
    if lvl == 1:
        w_list = lists[lvl - 1]  # stands for working_lists
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
                        k = random.randint(0, maxi - 1)
                        lines[y].append(w_list[k])
                        w_list.pop(k)
                        maxi = maxi - 1
    elif lvl == 2:
        w_list = lists[lvl - 1]  # stands for working_lists
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
                        k = random.randint(0, maxi - 1)
                        lines[y].append(w_list[k])
                        w_list.pop(k)
                        maxi = maxi - 1
    elif lvl == 3:
        w_list = lists[lvl - 1]  # stands for working_lists
        maxi = 52
        for y in range(5):
            if y == 0:
                for first in range(14):
                    lines[0].append(first)
            else:
                for i in range(14):
                    if i == 0:
                        lines[y].append(y)
                    else:
                        k = random.randint(0, maxi - 1)
                        lines[y].append(w_list[k])
                        w_list.pop(k)
                        maxi = maxi - 1

    display = display_board(lvl)

    # ---------------------------- Game Start --------------------------------
    finished = False
    print_board(display, lvl)
    total_cards = cards_to_turn(lvl)
    turned = 0
    turn = 0
    played = 0
    print('-----------------------')
    print_board(lines,lvl)
    keep_going = True
    bot = []
    size = get_size(lvl)
    game_con = input('Πατήστε ENTER για να συνεχίσετε')
    print('\n' * 200)  # prints 80 line breaks
    print_board(display, lvl)
    while turned < total_cards and keep_going:
        unpacked = unpack(display)
        if player_list[turn] != 'The_Bot':
            # ------------------- Card 1 ------------------------

            ans = answer(player_list[turn],lvl)
            while display[ans[0]][ans[1]] != 'X':
                print('Card already opened')
                ans = answer(player_list[turn], lvl)
            card1 = lines[ans[0]][ans[1]]
            display[ans[0]][ans[1]] = lines[ans[0]][ans[1]]
            print_board(display, lvl)

            # ------------------- Card 2 ------------------------

            ans2 = answer(player_list[turn], lvl)
            while display[ans2[0]][ans2[1]] != 'X':
                print('Card already opened')
                ans2 = answer(player_list[turn], lvl)
            card2 = lines[ans2[0]][ans2[1]]
            display[ans2[0]][ans2[1]] = lines[ans2[0]][ans2[1]]
            print_board(display, lvl)
        else:
            print('It is the bots turn')
            if len(bot) == 0:
                bot_flag = False
                #-------------------- Bot's Card 1 ----------------------------

                ans = bot_choose(display,lvl)
                card1 = lines[ans[0]][ans[1]]
                display[ans[0]][ans[1]] = lines[ans[0]][ans[1]]
                print('The Bot picked the card:' , ans[0],ans[1])
                print_board(display,lvl)
                sleep(2)

                # -------------------- Bot's Card 2 ----------------------------
                ans2 = bot_choose(display, lvl)
                card2 = lines[ans2[0]][ans2[1]]
                display[ans2[0]][ans2[1]] = lines[ans2[0]][ans2[1]]
                print('The Bot picked the card:', ans2[0], ans2[1])
                print_board(display,lvl)
                sleep(2)
                if not(equal_ad(card1,card2)) or not(equal(card1,card2)):
                    if card1 not in bot:
                        bot.append(card1)
                    if card2 not in bot:
                        bot.append(card2)

            #----------------- If bot knows the answer -------------------------
            elif has_answer(bot) != False:
                hello_kitty = has_answer(bot)
                card1 = hello_kitty[0]
                card2 = hello_kitty[1]
                ans = search(lines, lvl, card1)
                print('The Bot picked the card:', ans[0], ans[1])
                display[ans[0]][ans[1]] = lines[ans[0]][ans[1]]
                print_board(display,lvl)
                sleep(2)
                ans2 = search(lines, lvl, card2)
                print('The Bot picked the card:', ans2[0], ans2[1])
                display[ans2[0]][ans2[1]] = lines[ans2[0]][ans2[1]]
                print_board(display,lvl)
                sleep(2)
                for bot_card in bot:
                    if bot_card == card1 or bot_card == card2:
                        bot.remove(bot_card)
            # ---------------------- If bot doesn't know the answer --------------------------
            else:
                ans = bot_choose(display,lvl)
                card1 = lines[ans[0]][ans[1]]
                print_board(display,lvl)
                if card1 not in bot:
                    bot.append(card1)
                if has_answer(bot) != False:
                    hello_kitty = has_answer(bot)
                    card1 = hello_kitty[0]
                    card2 = hello_kitty[1]
                    ans = search(lines, lvl, card1)
                    display[ans[0]][ans[1]] = lines[ans[0]][ans[1]]
                    print('The Bot picked the card:', ans[0], ans[1])
                    print_board(display,lvl)
                    sleep(2)
                    ans2 = search(lines, lvl, card2)
                    display[ans2[0]][ans2[1]] = lines[ans2[0]][ans2[1]]
                    print('The Bot picked the card:', ans2[0], ans2[1])
                    print_board(display,lvl)
                    sleep(2)
                    for bot_card in bot:
                        if bot_card == card1 or bot_card == card2:
                            bot.remove(bot_card)

                else:
                    ans2 = bot_choose(display, lvl)
                    card2 = lines[ans2[0]][ans2[1]]

                    display[ans[0]][ans[1]] = lines[ans[0]][ans[1]]
                    print('The Bot picked the card:', ans[0], ans[1])
                    print_board(display,lvl)
                    sleep(2)

                    display[ans2[0]][ans2[1]] = lines[ans2[0]][ans2[1]]
                    print('The Bot picked the card:', ans2[0], ans2[1])
                    print_board(display,lvl)
                    sleep(2)




                    if equal_ad(card1,card2) or equal(card1,card2):
                        for bot_card in bot:
                            if bot_card == card1 or bot_card == card2:
                                bot.remove(bot_card)
                    else:
                        if len(bot) >= 5:
                            bot.pop(0)
                            if card2 not in bot:
                                bot.append(card2)


        # --------------------- Starts Checking ----------------------

        if equal(card1,card2) or equal_ad(card1,card2):
            turned += 2
            points[turn] += points_giver(card1)
            points[turn] += points_giver(card2)
            print('Επιτυχές ταίριασμα +!', points_giver(card1)+points_giver(card2),'!',player_list[turn],'έχεις συνολικά', points[turn],'πόντους !')
            if card1[0] == 'J' and card2[0] == 'J':
                print('Ξαναπαίζεις')
                continue
            elif card1[0] == 'K' and card2[0] == 'K':
                turn += 1
                print('Ο επόμενος παίχτης χάνει τη σειρά του !')

        #-------------- Checks for 3rd card -----------------------------------

        elif (card1[0] == 'K' and card2[0] == 'Q') or (card2[0] == 'K' and card1[0] == 'Q'):

            # ----------------- Card 3 -----------------------------------
            if player_list[turn] != 'The_Bot':
                print('Δώσε Τρίτη Κάρτα !')
                ans3 = answer(player_list[turn], lvl)
                while display[ans3[0]][ans3[1]] != 'X':
                    print('Card already opened')
                    ans3 = answer(player_list[turn], lvl)
                card3 = lines[ans3[0]][ans3[1]]
                display[ans3[0]][ans3[1]] = lines[ans3[0]][ans3[1]]
                print_board(display, lvl)
            else:
                flag_3 = False
                if has_answer(bot) != False:
                    hello_kitty = has_answer(bot)
                    card1 = hello_kitty[1]
                    card3 = hello_kitty[0]
                    ans3 = search(lines, lvl, card3)
                    ans = search(lines, lvl, card1)
                    display[ans3[0]][ans3[1]] = lines[ans3[0]][ans3[1]]
                    print('The Bot picked the card:', ans3[0], ans3[1])
                    print_board(display, lvl)
                    sleep(2)

                    for bot_card in bot:
                        if bot_card == card1 or bot_card == card2:
                            bot.remove(bot_card)
                else:
                    ans3 = bot_choose(display, lvl)
                    card3 = lines[ans3[0]][ans3[1]]
                    display[ans3[0]][ans3[1]] = lines[ans3[0]][ans3[1]]
                    print('The Bot picked the card:', ans3[0], ans3[1])
                    print_board(display, lvl)
                    sleep(1)
                    if equal(card1,card3) or equal_ad(card1,card3):
                        for bot_card in bot:
                            if bot_card == card1 or bot_card == card3:
                                bot.remove(bot_card)
                    elif equal(card2,card3) or equal_ad(card2,card3):
                        for bot_card in bot:
                            if bot_card == card2 or bot_card == card3:
                                bot.remove(bot_card)
                    else:
                        bot.append(card3)


            if equal(card1,card3) or equal_ad(card1,card3):
                points[turn] += points_giver(card3)
                points[turn] += points_giver(card1)
                print('Επιτυχές ταίριασμα +!', points_giver(card1)+points_giver(card3),'!',player_list[turn],'έχεις συνολικά', points[turn],'πόντους !')
                if card3[0] == 'K' and card1[0] == 'K':
                    turn += 1
                    display[ans2[0]][ans2[1]] = 'X'
                elif card3[0] == 'Q' and card1[0] == 'Q':
                    display[ans2[0]][ans2[1]] = 'X'
                turned += 2
                print('- Current board -')
                print_board(display, lvl)

            elif equal(card2,card3) or equal_ad(card2,card3):
                points[turn] += points_giver(card3)
                points[turn] += points_giver(card2)
                print('Επιτυχές ταίριασμα +!', points_giver(card3)+ points_giver(card2),'!',player_list[turn],'έχεις συνολικά', points[turn],'πόντους !')
                if card3[0] == 'K' and card2[0] == 'K':
                    turn += 1
                    display[ans[0]][ans[1]] = 'X'
                elif card3[0] == 'Q' and card2[0] == 'Q':
                    display[ans[0]][ans[1]] = 'X'
                turned += 2
                print('- Current board -')
                print_board(display, lvl)
            else:
                display[ans[0]][ans[1]] = 'X'
                display[ans2[0]][ans2[1]] = 'X'
                display[ans3[0]][ans3[1]] = 'X'
                print('Check your board !')
                sleep(2)
                print('Δεν υπήρξε κάποια αντιστοιχία')
                print('- Current board -')
                print_board(display, lvl)
        else:
            print('Check your board ...!')
            sleep(2)
            print('Δεν υπήρξε κάποια αντιστοιχία')
            print('- Current board -')
            display[ans[0]][ans[1]] = 'X'
            display[ans2[0]][ans2[1]] = 'X'
            print_board(display,lvl)

        turn += 1
        if turn >= players:
            turn -= players
        if turned == total_cards:
            break
        elif total_cards-turned <= 4 and not(check_last(display,lines,lvl)):
            keep_going = False



    if keep_going == False:
        print('')
        print(' !!! Το παιχνίδι διακόπηκε καθώς δεν υπάρχουν άλλες διαθέσιμες αντιστοιχίες !!!')
        print('')
        print('Ο πίνακάς σας ήταν -')
        print('')
        print_board(lines,lvl)
        print('')
    maximum_p = max(points)
    one = True
    for i in range(players):
        if points[i] == maximum_p and one == True:
            print('Παίχτη',player_list[i],'έφτασες τους περισσότερους πόντους με βαθμολογία:', maximum_p)
            one = False
        elif points[i] == maximum_p and one == False:
            print('Παίχτη', player_list[i], 'έφτασες και εσύ τους περισσότερους πόντους με βαθμολογία:', maximum_p)












