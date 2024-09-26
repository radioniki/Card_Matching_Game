from game_play_utils import *


# Η συνάρτηση level() επιστρέφει το επίπεδο δυσκολίας που επιλέγει ο χρήστης
def level():
    # εμφανίζονται στην οθόνη οι επιλογές για το επίπεδο δυσκολίας και ο χρήστης επιλέγει
    apant = input("Δώστε μου επίπεδο δυσκολίας \nΕύκολο : 1 \nΜέτριο : 2 \nΔύσκολο : 3 \nΔιαλέξτε : ")
    # Σε περίπτωση που ο χρήστης δεν εισάγει σώστα τις προαπαιτούμενες τιμές 1, 2, 3, εμφανίζεται αντίστοιχο μήνυμα λάθους και ζητείται απο τον χρήστη να εισάγει ξανά απάντηση
    while apant != "1" and apant != "2" and apant != "3":
        apant = input('Λάθος Δεδομένο \nΠροσπαθήστε ξανά: ')
    return int(apant)


# Η συνάρτηση level_cards(apant) δέχεται το επίπεδο δυσκολίας(apant) και επίστρέφει τον αριθμό των στηλών του πίνακα 4,10,13 ανάλογα με το επίπεδο δυσκολίας
def level_cards(apant):
    if int(apant) == 1:
        size = 4
    elif int(apant) == 2:
        size = 10
    elif int(apant) == 3:
        size = 13
    return size


# η συνάρτηση display_board(level_chosen) δημιουργεί πίνακα το μέγεθος του οποίου εξαρτάται από το επίπεδο που διαλέγει ο χρήστης (level_chosen) και εισάγει σε κάθε θέση της λίστας την τιμή χ
def display_board(level_chosen):
    resizable = level_cards(level_chosen)
    display = [[], [], [], [], []]
    for y in range(1, 5):
        display[y].append(y)
    for i in range(1, 5):
        for y in range(resizable):
            display[i].append("X")
    for k in range(resizable + 1):
        display[0].append(k)
    return display


# Η συνάρτηση equal(a,b) δέχεται δυο κάρτες a,b απο τον πίνακα και ελέγχει  εάν η αξία των φύλλων ανεξαρτήτως του συμβόλου τους είναι ίδια
def equal(a, b):
    # εάν το len των string των καρτών ισούται με τρία τότε δεν πρέπει στη σύγκριση να συμπεριληφθεί το σύμβολο οπότε το παραλείπουμε απο τη σύγκριση
    if len(str(a)) == 3 and len(str(b)) == 3:
        a = a[:2]
        b = b[:2]

    # εάν το len των string των καρτών ισούται με δύο τότε δεν πρέπει στη σύγκριση να συμπεριληφθεί το σύμβολο οπότε το παραλείπουμε απο τη σύγκριση
    elif len(str(a)) == 2 and len(str(b)) == 2:
        a = a[:1]
        b = b[:1]
    # εάν το len των string των καρτών διαφέρει τότε παίρνουμε περιπτώσεις και αντίστοιχα παραλείπουμε από τη σύγκριση το σύμβολο των καρτών
    elif len(str(a)) == 2 and len(str(b)) == 3:
        a = a[:1]
        b = b[:2]
    else:
        a = a[:2]
        b = b[:1]
    # εάν ισούται η αξία των καρτών η συνάρτηση επιστρέφει True αλλιώς επιστρέφει False
    if a == b:
        return True
    else:
        return False


# Η συνάρτηση δέχεται δύο κάρτες και ελέγχει εάν το σύμβολο τους είναι ίδιο και επίστρέφει True αλλιώς επιστρέφει False
def equal_ad(card1, card2):
    card_1 = card1[-1]
    card_2 = card2[-1]
    if card_1 == card_2:
        return True
    else:
        return False


def level():
    apant = input("Δώστε μου επίπεδο δυσκολίας \nΕύκολο : 1 \nΜέτριο : 2 \nΔύσκολο : 3 \nΔιαλέξτε : ")
    while apant!="1" and apant!="2" and apant!="3":
         apant = input('Λάθος Δεδομένο \nΠροσπαθήστε ξανά: ')
    return int(apant)

def level_cards(apant):
    if int(apant) == 1:
        size = 4
    elif int(apant) == 2:
        size = 10
    elif int(apant) == 3:
        size = 13
    return size



def display_board(level_chosen):
    resizable = level_cards(level_chosen)
    display = [[], [], [], [],[]]
    for y in range(1,5):
        display[y].append(y)
    for i in range(1,5):
        for y in range(resizable):
               display[i].append("X")
    for k in range(resizable+1):
        display[0].append(k)
    return display

def equal(a,b):
    if len(str(a)) == 3 and len(str(b)) == 3:
        a = a[:2]
        b = b[:2]
    elif len(str(a)) == 2 and len(str(b)) == 2:
        a = a[:1]
        b = b[:1]
    elif len(str(a)) == 2 and len(str(b)) == 3:
        a = a[:1]
        b = b[:2]
    else:
        a = a[:2]
        b = b[:1]
    if a == b:
        return True
    else:
        return False



def equal_ad(card1,card2):
    card_1 = card1[-1]
    card_2 = card2[-1]
    if card_1 == card_2:
        return True
    else:
        return False