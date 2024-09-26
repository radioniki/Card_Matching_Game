def create_lists():
    # dhmiourgei tis listes opou analoga to epipedo tha mperdeutei auth pou prepei gia na ginei to backboard
    easy_mode = []
    # dhmiourgei thn lista gia to eukolo epipedo
    for i in range(10, 14):
        for y in range(4):
            if y == 0:
                # vazei ola ta fulla pou einai spathi
                if i == 11:
                    easy_mode.append('J'+'\u2663')
                elif i == 12:
                    easy_mode.append('Q'+'\u2663')
                elif i == 13:
                    easy_mode.append('K'+'\u2663')
                else:
                    easy_mode.append('10'+'\u2663')
            if y == 1:
                # vazei ola ta fulla pou einai mpastouni
                if i == 11:
                    easy_mode.append('J'+'\u2660')
                elif i == 12:
                    easy_mode.append('Q'+'\u2660')
                elif i == 13:
                    easy_mode.append('K'+'\u2660')
                else:
                    easy_mode.append('10'+'\u2660')
            if y == 2:
                # vazei ola ta fulla pou einai karo
                if i == 11:
                    easy_mode.append('J'+'\u2666')
                elif i == 12:
                    easy_mode.append('Q'+'\u2666')
                elif i == 13:
                    easy_mode.append('K'+'\u2666')
                else:
                    easy_mode.append('10'+'\u2666')
            if y == 3:
                # vazei ola ta fulla pou einai koupa
                if i == 11:
                    easy_mode.append('J'+'\u2665')
                elif i == 12:
                    easy_mode.append('Q'+'\u2665')
                elif i == 13:
                    easy_mode.append('K'+'\u2665')
                else:
                    easy_mode.append('10'+'\u2665')

    medium_mode = []
    # dhmiourgei thn lista gia to metrio epipedo
    for i in range(1, 11):
        for y in range(4):
            if y == 0:
                # vazei ola ta fulla pou einai spathi
                medium_mode.append(str(i)+'\u2663')
            elif y == 1:
                # vazei ola ta fulla pou einai mpastouni
                medium_mode.append(str(i)+'\u2660')
            elif y == 2:
                # vazei ola ta fulla pou einai karo
                medium_mode.append(str(i)+'\u2666')
            else:
                # vazei ola ta fulla pou einai koupa
                medium_mode.append(str(i)+'\u2665')

    # dhmiourgei thn lista gia to duskolo epipedo, pou einai h enwsh twn 2 prohgoumenwn
    hard_mode = medium_mode + list(set(easy_mode) - set(medium_mode))

    # epistrefei lista pou periexei oles tis listes
    list_of_lists = [easy_mode, medium_mode, hard_mode]
    return list_of_lists


def get_players():
    # epistrefei aritho paiktwn ean kai efoson einai apodekti timi
    players = "Λάθος"
    while players.isdigit() == False or int(players) <= 1:
        # elegxei an einai arithmos auto pou dothike alliws ksanazhtaei
        players = input("Δώσε αριθμό παικτών:")
        players.strip()
        if players.isdigit() == False:
            print("Λάθος Δεδομένο \nΠροσπαθήστε ξανά !")
        elif int(players) <= 1:
            print("Λάθος Δεδομένο \nΠροσπαθήστε ξανά !")
        else:
            # epistrefei ton arithmo twn paiktwn
            return int(players)


def points_giver(ep):
    # upologizei tous pontous pou pairnei o paikths apo thn karta
    if "A" in ep:
        # enas pontos gia otan einai A
        points = 1
    elif ("J" in ep) or ("Q" in ep) or ("K" in ep):
        # 10 pontoi an einai figoura
        points = 10
    else:
        # antistixoi pontoi gia kathe fullo
        for i in range(2, 11):
            if str(i) in ep:
                points = i
    # epistefei tous pontous
    return points
