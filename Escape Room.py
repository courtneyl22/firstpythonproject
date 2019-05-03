# name: Courtney Luc
# Text adventure based game
import time


def displayIntro():
    print("You wake up in a small, foreign room and realize you're in a psych ward...")
    time.sleep(1)
    print("You feel something heavy on your ankle...")
    time.sleep(1)
    print("You realize you're chained to the bed, but the chain is long enough to move a bit...")
    time.sleep(2)
    print()


def choosePath():
    answer = ""
    while answer != "1" and answer != "2":  # input validation
        answer = input("Which path will you choose? (1 or 2): ")

    return answer


answer = input('Would you like to play? 1(yes)')


if answer == '1':
    displayIntro()
    answer = input('What do you do next? 1(look around) 2(go to door)')

    if answer == '1':
        answer = input("You don't see much; there's one wall with a painting, and one wall has a window by the bed."
                       " 1(look through window) 2(try to break window)")
        choosePath()

        if answer == "1":
            answer = input("You take a close look, there's something shiny in the bushes. It's a key!"
                           " But it looks far. 1(look around) 2(open window)")
            choosePath()

            if answer == "1":
                answer = input("You scan the room again. In the corner, you see a crowbar in a glass case. Odd. "
                               "The case says open for emergencies only. 1(break case) 2(solve riddle)")
                choosePath()

                if answer == "2":  # riddle number 1
                    answer = input('What part of London is in France?').lower().strip()

                    if answer == 'the letter n':  # riddle solver: 1
                        answer = input('''You now have access to the crowbar. 1(pry open window) 2(reach for key)''')
                        choosePath()

                        if answer == '2':
                            answer = input('The crowbar was long enough and you finally got the key!'
                                           ' 1(try it on the window) 2(try it on the chain)')
                            choosePath()

                            if answer == '2':
                                answer = input("It's a perfect fit! 1(go to door) 2(check walls)")
                                choosePath()

                                if answer == '1':
                                    print("it's locked, you need to find the key. Try again")
                                else:
                                    print("You see the painting again. You notice it's crooked. "
                                          "You take it off the wall and you see a safe that requires a code.")
                                    answer = input("Password hint: Toshimitsu Takagi")
                                choosePath()

                                if answer == '2004':
                                    print("You found the final key! You go to the door, "
                                          "unlock it and you're now free! Congratulations!!")
                                    while answer != '2004':
                                        answer = input("Try again")
                            else:
                                print("Why? There's no lock on the window. Try again")

                        else:  # finite decision
                            print('Without knowing, you tipped off the silent alarm. '
                                  'The nurses come in, chain you to the bed and sedates you.')
                            time.sleep(1)
                            print('GAME OVER')

                    while answer != 'the letter n':
                        answer = input("Try again")

                else:  # finite decision
                    print()
                    print("You not only injure yourself, you sound the alarm, the nurse comes in, sedates you.")
                    time.sleep(1)
                    print("GAME OVER")

        while answer == 'open window':
            answer = input("It's jammed, but it's open enough to grab the key. (go back)")
            while answer == "go back":
                answer = input("You take a close look, there's something shiny in the bushes. It's a key!"
                               " 1(But it looks far. look around) 2(open window)")

        else:  # finite decision
            print()
            print("You injure yourself, the nurse hears you and sedates you.")
            time.sleep(1)
            print("GAME OVER")

        choosePath()
    else:
        answer = input("You're chained, you can't go that far. What now? 1(drag bed)")
    if answer == '1':  # input validation
        print("You make a lot of noise and didn't get far. "
              "A nurse comes in, assumes you're mad and sedates you.")
        time.sleep(1)
        print("GAME OVER")
while answer != "1":
    choosePath()