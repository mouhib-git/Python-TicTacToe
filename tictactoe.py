

line1 = "1-2-3"
line2 = "4-5-6"
line3 = "7-8-9"
test1 = test2 = test3 = True


def win(ch1, ch2, ch3, sbl):
    if ch1[2] == ch2[2] == ch3[3] == sbl:
        return True
    elif ch1[4] == ch2[4] == ch3[4] == sbl:
        return True
    elif ch1[0] == ch2[0] == ch3[0] == sbl:
        return True
    elif ch1[4] == ch2[2] == ch3[0] == sbl:
        return True
    elif ch3[4] == ch3[2] == ch3[0] == sbl:
        return True
    elif ch2[4] == ch2[2] == ch2[0] == sbl:
        return True
    elif ch1[4] == ch1[2] == ch1[0] == sbl:
        return True
    elif ch1[0] == ch2[2] == ch3[4] == sbl:
        return True
    else:
        return False


def testexistance(x, ch1, ch2, ch3):
    if (ch1.find(x) == -1) and (ch2.find(x) == -1) and (ch3.find(x) == -1):
        return True
    else:
        return False


while test1 and test2 and test3:

    print(line1)
    print(line2)
    print(line3)

    choice1 = 0
    while choice1 not in range(1, 9) and testexistance(str(choice1), line1, line2, line3):
        choice1 = input("PLAYER 1, select a number !")

    # line 1 editing
    if choice1 == '1':
        line1 = line1.replace('1', 'X')

    elif choice1 == '2':
        line1 = line1.replace('2', 'X')

    elif choice1 == '3':
        line1 = line1.replace('3', 'X')

    # line2
    elif choice1 == '4':
        line2 = line2.replace('4', 'X')

    elif choice1 == '5':
        line2 = line2.replace('5', 'X')

    elif choice1 == '6':
        line2 = line2.replace('6', 'X')

    # line3
    elif choice1 == '7':
        line3 = line3.replace('7', 'X')

    elif choice1 == '8':
        line3 = line3.replace('8', 'X')

    elif choice1 == '9':
        line3 = line3.replace('9', 'X')

    choice2 = 0
    if not win(line1, line2, line3, 'X'):
        print(line1)
        print(line2)
        print(line3)
        while choice2 not in range(1, 9) and testexistance(str(choice2), line1, line2, line3):
            choice2 = input("PLAYER 2, select a number !  ")

        # line 1 editing
        if choice2 == '1':
            line1 = line1.replace('1', 'O')

        elif choice2 == '2':
            line1 = line1.replace('2', 'O')

        elif choice2 == '3':
            line1 = line1.replace('3', 'O')

        # line2
        elif choice2 == '4':
            line2 = line2.replace('4', 'O')

        elif choice2 == '5':
            line2 = line2.replace('5', 'O')

        elif choice2 == '6':
            line2 = line2.replace('6', 'O')

        # line3
        elif choice2 == '7':
            line3 = line3.replace('7', 'O')

        elif choice2 == '8':
            line3 = line3.replace('8', 'O')

        elif choice2 == '9':
            line3 = line3.replace('9', 'O')

        if win(line1, line2, line3, 'X') or win(line1, line2, line3, 'O'):
            test1 = test2 = test3 = False

        if win(line1, line2, line3, 'X'):
            print('PLAYER 1, Congrats ,you re the Winner! ')

        elif win(line1, line2, line3, 'O'):
            print('PLAYER 2, Congrats ,you re the Winner! ')
