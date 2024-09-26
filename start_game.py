from game_play_utils import *
from card_game_setup import *
from game_logic import *
import random
from time import sleep
from basic_game import *
from bot import *
from advanced_game import *


print('Καλωσήλθατε στο Matching Game')
k = input('Πατήστε 1 για απλό παιχνίδι\nΠατήστε 2 για advanced παιχνίδι :')
while k != '1' and k != '2':
    print('Λάθος δεδομένα')
    k = input('Πατήστε 1 για απλό παιχνίδι\nΠατήστε 2 για advanced παιχνίδι :')
if k == '1':
    game()
else:
    j = input('Πατήστε 1 για να παίξετε με τον υπολογιστή\nΠατήστε 2 για να παίξετε με φίλους :')
    while j != '1' and j != '2':
        print('Λάθος δεδομένα')
        j = input('Πατήστε 1 για να παίξετε με τον υπολογιστή\nΠατήστε 2 για να παίξετε με φίλους :')
    if j == '1':
        bot_game()
    else:
        advanced_game()