from random import randint
from re import match


class Player_vs_ai(object):

    def __init__(self):

        self.regex_5 = r'([1-6])\1{4}'

        self.regex_4 = r'([1-6])\1{3}[1-6]|[1-6]([1-6])\2{3}'

        self.regex_fh = r'([1-6])\1{2}([1-6])\2{1}|([1-6])\3{1}([1-6])\4{2}'

        self.regex_2_6 = r'23456'

        self.regex_1_5 = r'12345'

        self.regex_3 = (r'([1-6])\1{2}[1-6][1-6]|[1-6][1-6]([1-6])\2{2}|'
                        r'[1-6]([1-6])\3{2}[1-6]')

        self.regex_p_p = r'([1-6])\1([1-6])\2[1-6]|[1-6]([1-6])\3([1-6])\4'

        self.regex_p = (r'([1-6])\1[1-6][1-6][1-6]|[1-6]([1-6])\2[1-6][1-6]|'
                        r'[1-6][1-6]([1-6])\3[1-6]|[1-6][1-6][1-6]([1-6])\4')

    def roll_dice(self, die_values_list, values_in_hand):

        current_hand = [["+-----+", "+-----+", "+-----+", "+-----+",
                         "+-----+"],
                        [],
                        [],
                        [],
                        ["+-----+", "+-----+", "+-----+", "+-----+",
                         "+-----+"]]

        for i in die_values_list:

            values_in_hand.append(i)

            if i == 1:
                current_hand[1].append("|     |")
                current_hand[2].append("|  o  |")
                current_hand[3].append("|     |")

            elif i == 2:
                current_hand[1].append("| o   |")
                current_hand[2].append("|     |")
                current_hand[3].append("|   o |")

            elif i == 3:
                current_hand[1].append("| o   |")
                current_hand[2].append("|  o  |")
                current_hand[3].append("|   o |")

            elif i == 4:
                current_hand[1].append("| o o |")
                current_hand[2].append("|     |")
                current_hand[3].append("| o o |")

            elif i == 5:
                current_hand[1].append("| o o |")
                current_hand[2].append("|  o  |")
                current_hand[3].append("| o o |")

            elif i == 6:
                current_hand[1].append("| o o |")
                current_hand[2].append("| o o |")
                current_hand[3].append("| o o |")

            else:
                print("No roll has occured")

        print(" ".join(current_hand[0]), " ".join(current_hand[1]),
              " ".join(current_hand[2]), " ".join(current_hand[3]),
              " ".join(current_hand[4]), sep='\n')

    def second_roll_choice(self):

        player_conserved_dice = []

        player_second_re_roll_request = input("Would you like to re-roll"
                                              " any dice? (yes, "
                                              "no or all): ").lower()

        while player_second_re_roll_request not in('yes', 'no', 'all'):
            print("", "Invalid input, try again", "", sep='\n')
            player_second_re_roll_request = input("Would you like to re-roll"
                                                  " any dice? (yes, "
                                                  "no or all): ").lower()
            print("")

        if player_second_re_roll_request == 'yes':
            player_which_dice = input("Which numbers would"
                                      " you like to keep? ""(Enter integers "
                                      "with no spaces of puncuation in "
                                      "between): ")
            print("")

        elif player_second_re_roll_request == 'no':
            pvai.roll_dice(player_first_re_roll, player_final_hand)

        elif player_second_re_roll_request == 'all':
            pvai.roll_dice([randint(1, 6) for x in range(5)],
                           player_final_hand)
        else:
            print("Invalid input, try again")
            print("")

        while player_second_re_roll_request == 'yes' and \
                match(r'^[1-6]{1,5}$', player_which_dice) is None:
            print("Please roll at least one of 5 dice 6-sided dice,"
                  " cheater. ")
            player_which_dice = input("Which numbers would"
                                      " you like to keep? ""(Enter integers "
                                      "with no spaces of puncuation in "
                                      "between): ")
            print("")

        if player_second_re_roll_request == 'yes':

            player_conserved_dice = [int(i) for i in player_which_dice]

        if player_second_re_roll_request == 'yes':
            for i in set(player_conserved_dice):
                while player_first_re_roll.count(i) <\
                 player_conserved_dice.count(i):
                    print("Ha ha ha you can not fool me, great master of"
                          " dice! Don't enter numbers which aren't in your"
                          " hand cheater.")
                    print("")

                    player_conserved_dice = []

                    player_which_dice = input("Which numbers would"
                                              " you like to keep? "
                                              "(Enter integers "
                                              "with no spaces of puncuation in "
                                              "between): ")
                    print("")

                    player_conserved_dice = [int(i) for i in player_which_dice]

        if player_second_re_roll_request == 'yes' and\
           len(player_conserved_dice) == 5:
            pvai.roll_dice(player_conserved_dice, player_final_hand)

        if player_second_re_roll_request == 'yes' and\
           len(player_conserved_dice) != 5:
            pvai.roll_dice(player_conserved_dice + [randint(1, 6) for x in
                           range(5 - len(player_conserved_dice))],
                           player_final_hand)
        # print(player_conserved_dice, "player 2nd roll")

    def second_roll_ai_choice(self):

        ai_conserved_dice = []

        if match(pvai.regex_5, "".join([str(x)
                 for x in ai_first_re_roll])):

            if match(pvai.regex_5, "".join([str(x)
                     for x in player_first_re_roll])) and\
                    sum(player_first_re_roll) > sum(ai_first_re_roll):
                pvai.roll_dice([randint(1, 6) for x in range(5)],
                               ai_final_hand)

            elif match(pvai.regex_5, "".join([str(x)
                       for x in player_first_re_roll]))\
                    is None or sum(player_first_re_roll) ==\
                    sum(ai_first_re_roll):
                        pvai.roll_dice(ai_first_re_roll, ai_final_hand)

        elif match(pvai.regex_4, "".join([str(x)
                   for x in sorted(ai_first_re_roll)])):

            if match(pvai.regex_4 or
                     pvai.regex_5,
                     "".join([str(x) for x in sorted(player_first_re_roll)]))\
                     and sum(player_first_re_roll) > sum(ai_first_re_roll):
                    pvai.roll_dice([randint(1, 6) for x in range(5)],
                                   ai_final_hand)

            else:
                ai_conserved_dice.extend([i in i for i in ai_first_re_roll if
                                         ai_first_re_roll.count(i) == 4])

                pvai.roll_dice(ai_conserved_dice + [randint(1, 6) for x
                                                    in range(5 -
                                                    len(ai_conserved_dice))],
                               ai_final_hand)

        elif match(pvai.regex_fh, "".join([str(x)
                   for x in sorted(ai_first_re_roll)])):

            if match(pvai.regex_4 or pvai.regex_5 or
                     pvai.regex_fh,
                     "".join([str(x) for x in sorted(player_first_re_roll)])):

                if (set([i for i in ai_first_re_roll if
                    ai_first_re_roll.count(i) == 3]).pop() >
                    set([i for i in ai_first_re_roll if
                        ai_first_re_roll.count(i) == 2]).pop()):
                    ai_conserved_dice.extend([i for i in ai_first_re_roll if
                                              ai_first_re_roll.count(i) == 3])

                elif (set([i for i in ai_first_re_roll if
                      ai_first_re_roll.count(i) == 2]).pop() >
                      set([i for i in ai_first_re_roll if
                           ai_first_re_roll.count(i) == 3]).pop()):
                            ai_conserved_dice.extend([i for i in
                                                      ai_first_re_roll if
                                                      ai_first_re_roll.
                                                      count(i) == 2])

                pvai.roll_dice(ai_conserved_dice + [randint(1, 6) for x
                               in range(5 - len(ai_conserved_dice))],
                               ai_final_hand)

            else:
                pvai.roll_dice(ai_first_re_roll, ai_final_hand)

        elif match(pvai.regex_2_6, "".join([str(x) for x in
                   sorted(ai_first_re_roll)])):

            if match(pvai.regex_5 or pvai.regex_4 or
                     pvai.regex_fh or pvai.regex_2_6,
                     "".join([str(x) for x in sorted(player_first_re_roll)])):
                        ai_conserved_dice.append(max(ai_first_re_roll))

                        pvai.roll_dice(ai_conserved_dice +
                                       [randint(1, 6) for x in range(5 -
                                        len(ai_conserved_dice))],
                                       ai_final_hand)

            else:
                pvai.roll_dice(ai_first_re_roll, ai_final_hand)

        elif match(pvai.regex_1_5, "".join([str(x) for x in
                   sorted(ai_first_re_roll)])):

            if match(pvai.regex_5 or pvai.regex_4 or
                     pvai.regex_fh or pvai.regex_2_6
                     or pvai.regex_1_5,
                     "".join([str(x) for x in sorted(player_first_re_roll)])):
                        ai_conserved_dice.append(max(ai_first_re_roll))

                        pvai.roll_dice(ai_conserved_dice +
                                       [randint(1, 6) for x in
                                        range(5 -
                                        len(ai_conserved_dice))],
                                       ai_final_hand)

            else:
                pvai.roll_dice(ai_first_re_roll, ai_final_hand)

        elif match(pvai.regex_3, "".join([str(x) for x in
                                         sorted(ai_first_re_roll)])):

            if match(pvai.regex_5 or pvai.regex_4 or
                     pvai.regex_fh,
                     "".join([str(x) for x in sorted(player_first_re_roll)])):

                if (set([i for i in ai_first_re_roll if
                        ai_first_re_roll.count(i) == 3]).pop() <
                    max(set([i for i in player_first_re_roll if
                            player_first_re_roll.count(i) in(5, 4, 3, 2)]))):
                    ai_conserved_dice.append(max(ai_first_re_roll))

                pvai.roll_dice(ai_conserved_dice +
                               [randint(1, 6) for x
                                in range(5 -
                                len(ai_conserved_dice))],
                               ai_final_hand)

            else:
                ai_conserved_dice.extend([i for i in ai_first_re_roll if
                                          ai_first_re_roll.count(i) == 3])

                pvai.roll_dice(ai_conserved_dice +
                               [randint(1, 6) for x in
                                range(5 - len(ai_conserved_dice))],
                               ai_final_hand)

        elif match(pvai.regex_p_p, "".join([str(x) for x in
                   sorted(ai_first_re_roll)])):

            if match(pvai.regex_5 or pvai.regex_4 or
                     pvai.regex_fh or pvai.regex_3,
                     "".join([str(x) for x in sorted(player_first_re_roll)])):

                if (set([i for i in ai_first_re_roll if
                    max(ai_first_re_roll.count(i) == 2)]).pop() <
                    set([i for i in ai_first_re_roll if
                        ai_first_re_roll.count(i) in(5, 4, 3, 2)]).pop()):
                    ai_conserved_dice.append(max(ai_first_re_roll))

                    pvai.roll_dice(ai_conserved_dice +
                                   [randint(1, 6) for x
                                    in range(5
                                    - len(ai_conserved_dice))],
                                   ai_final_hand)
            else:
                ai_conserved_dice.extend([i for i in ai_first_re_roll if
                                         max(ai_first_re_roll.count(i)
                                             == 2)])

                pvai.roll_dice(ai_conserved_dice +
                               [randint(1, 6) for x in
                                range(5 - len(ai_conserved_dice))],
                               ai_final_hand)

        elif match(pvai.regex_p,
                   "".join([str(x) for x in sorted(ai_first_re_roll)])):

                if match(pvai.regex_5 or pvai.regex_4 or
                         pvai.regex_fh or pvai.regex_3 or
                         pvai.regex_p_p,
                         "".join([str(x) for x in
                                 sorted(player_first_re_roll)])):

                    if (set([i for i in ai_first_re_roll if
                            ai_first_re_roll.count(i) == 2]).pop() <
                        max(set([i for i in player_first_re_roll if
                                player_first_re_roll.count(i)
                                in(5, 4, 3, 2)]))):
                        ai_conserved_dice.append(max(ai_first_re_roll))

                        pvai.roll_dice(ai_conserved_dice +
                                       [randint(1, 6) for x
                                        in range(5 -
                                        len(ai_conserved_dice))],
                                       ai_final_hand)

                else:
                    ai_conserved_dice.extend([i for i in ai_first_re_roll if
                                              ai_first_re_roll.count(i) == 2])

                    pvai.roll_dice(ai_conserved_dice +
                                   [randint(1, 6) for x in
                                    range(5 - len(ai_conserved_dice))],
                                   ai_final_hand)

        else:

            if match(pvai.regex_5 or pvai.regex_4 or
                     pvai.regex_fh or pvai.regex_2_6 or
                     pvai.regex_1_5,
                     "".join([str(x) for x in sorted(player_first_re_roll)])):

                ai_conserved_dice.append(max(ai_first_re_roll))

                pvai.roll_dice(ai_conserved_dice +
                               [randint(1, 6) for x in
                                range(5 - len(ai_conserved_dice))],
                               ai_final_hand)

            else:

                ai_conserved_dice.extend([i for i in
                                         ai_first_re_roll if i != 1])

                pvai.roll_dice(ai_conserved_dice +
                               [randint(1, 6) for x in
                                range(5 - len(ai_conserved_dice))],
                               ai_final_hand)

        # print(ai_conserved_dice, "ai 2nd roll")


class Score(Player_vs_ai):

    def __init__(self):

        self.player_score = 0
        self.ai_score = 0

    def score_comparison(self, player_hand, ai_hand):

        if match(pvai.regex_5, "".join([str(x)
                 for x in sorted(player_hand)])):
            rs.player_score += 8

        elif match(pvai.regex_4, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 7

        elif match(pvai.regex_fh, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 6

        elif match(pvai.regex_2_6, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 5

        elif match(pvai.regex_1_5, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 4

        elif match(pvai.regex_3, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 3

        elif match(pvai.regex_p_p, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 2

        elif match(pvai.regex_p, "".join([str(x)
                   for x in sorted(player_hand)])):
            rs.player_score += 1

        else:
            rs.player_score == 0

        if match(pvai.regex_5, "".join([str(x)
                 for x in sorted(ai_hand)])):
            rs.ai_score += 8

        elif match(pvai.regex_4, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 7

        elif match(pvai.regex_fh, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 6

        elif match(pvai.regex_2_6, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 5

        elif match(pvai.regex_1_5, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 4

        elif match(pvai.regex_3, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 3

        elif match(pvai.regex_p_p, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 2

        elif match(pvai.regex_p, "".join([str(x)
                   for x in sorted(ai_hand)])):
            rs.ai_score += 1

        else:
            rs.ai_score == 0


class Betting(Score):

    def __init__(self):

        self.player_gold = 1000

        self.ai_gold = 1000

        self.winners_gold = 0

    def player_vs_ai_bet(self):

        player_bet = int(input((f"You have {bet.player_gold} gold and your"
                                f" oppenent has {bet.ai_gold}"
                                " gold how much would you like to bet?: ")))

        while match(r'^[0-9]{1,4}$', str(player_bet)) is None:
            print("Invalid input, try again")
            player_bet = int(input((f"You have {bet.player_gold} gold and your"
                                    f" oppenent has {bet.ai_gold}"
                                    " gold how much would you like to bet?: ")))

        bet.winners_gold += (player_bet * 2)
        bet.player_gold -= player_bet
        bet.ai_gold -= player_bet

    def ai_raise(self):

        if ((rs.ai_score - rs.player_score == 1) or
            (rs.ai_score == rs.player_score and
             sum(ai_first_re_roll) > sum(player_first_re_roll))):

            bet.winners_gold += round(bet.ai_gold * 1/8)
            bet.ai_gold -= round(bet.ai_gold * 1/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 1/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 1/8)))

            bet.winners_gold += round(bet.ai_gold * 1/8)
            bet.player_gold -= round(bet.ai_gold * 1/8)

        elif rs.ai_score - rs.player_score == 2:
            bet.winners_gold += round(bet.ai_gold * 2/8)
            bet.ai_gold -= round(bet.ai_gold * 2/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 2/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 2/8)))

            bet.winners_gold += round(bet.ai_gold * 2/8)
            bet.player_gold -= round(bet.ai_gold * 2/8)

        elif rs.ai_score - rs.player_score == 3:
            bet.winners_gold += round(bet.ai_gold * 3/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 3/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 3/8)))

            bet.winners_gold += round(bet.ai_gold * 3/8)
            bet.player_gold -= round(bet.ai_gold * 3/8)

        elif rs.ai_score - rs.player_score == 4:
            bet.winners_gold += round(bet.ai_gold * 4/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 4/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 4/8)))

            bet.winners_gold += round(bet.ai_gold * 4/8)
            bet.player_gold -= round(bet.ai_gold * 4/8)

        elif rs.ai_score - rs.player_score == 5:
            bet.winners_gold += round(bet.ai_gold * 5/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 5/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 5/8)))

            bet.winners_gold += round(bet.ai_gold * 5/8)
            bet.player_gold -= round(bet.ai_gold * 5/8)

        elif rs.ai_score - rs.player_score == 6:
            bet.winners_gold += round(bet.ai_gold * 6/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 6/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 6/8)))

            bet.winners_gold += round(bet.ai_gold * 6/8)
            bet.player_gold -= round(bet.ai_gold * 6/8)

        elif rs.ai_score - rs.player_score == 7:
            bet.winners_gold += round(bet.ai_gold * 7/8)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold * 7/8)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold * 7/8)))

            bet.winners_gold += round(bet.ai_gold * 7/8)
            bet.player_gold -= round(bet.ai_gold * 7/8)

        elif rs.ai_score - rs.player_score == 8:
            bet.winners_gold += round(bet.ai_gold)

            ai_raise = input("Your opponent has raised {} gold. To continue you"
                             " have to"
                             " match this. Enter y to match: "
                             .format(round(bet.ai_gold)))

            while ai_raise.lower() != 'y':
                print("Enter y to continue")
                ai_raise = input("Your opponent has raised {} gold. To continue"
                                 " you have to"
                                 " match this. Enter y to match: "
                                 .format(round(bet.ai_gold)))

            bet.winners_gold += round(bet.ai_gold)
            bet.player_gold -= round(bet.ai_gold)

        else:
            pass


class Gamer_over(Betting):

    def who_wins(self):

        if rs.player_score > rs.ai_score:

            bet.player_gold += bet.winners_gold
            print(f"Congratulations, you win! You now have {bet.player_gold}"
                  " gold.")

        elif rs.ai_score > rs.player_score:

            bet.ai_gold += bet.winners_gold
            print(f"You lose! You now have {bet.player_gold} gold.")

        elif (rs.ai_score == rs.player_score and
              sum(player_final_hand) > sum(ai_final_hand)):

            bet.player_gold += bet.winners_gold
            print(f"Congratulations, you win! You now have {bet.player_gold}"
                  " gold.")

        elif (rs.ai_score == rs.player_score and
              sum(player_final_hand) < sum(ai_final_hand)):

            bet.ai_gold += bet.winners_gold
            print(f"You lose! You now have {bet.player_gold} gold.")
        else:

            bet.player_gold = 1000

            bet.ai_gold = 1000

            bet.winners_gold = 0

            print(f"It's a draw. You now have {bet.player_gold} gold.")


# roll_dice applies numerical value to the dice ASCII image
# roll_dice iniates the first role for player and/or ai
# second_roll_choice allows the player to re roll
# second_roll_ai_choice allows the player to re roll

# calling classes

rs = Score()

pvai = Player_vs_ai()

bet = Betting()

go = Gamer_over()

# Introductory message outlining the rules of the game

print("", "Welcome to Dice Poker!", "",
      "The goal of the game is to roll the strongest", "",
      "Ranking of Hands (lowest to highest):",
      "", "- Nothing — five mismatched dice forming no sequence longer"
      " than four.",
      "- Pair — two dice showing the same value.",
      "- Two Pairs — two pairs of dice, each showing the same value.",
      "- Three-of-a-Kind — three dice showing the same value.",
      "- Five High Straight — dice showing values from 1 through 5, "
      "inclusive.",
      "- Six High Straight — dice showing values from 2 through 6, inclusive.",
      "- Full House — Pair of one value and Three-of-a-Kind of another.",
      "- Four-of-a-Kind — four dice showing the same value.",
      "- Five-of-a-Kind — all five dice showing the same value.",
      "", "You are allowed 5 dice per roll and the higher your numbers"
      " the stronger your hand!",
      "", "Good luck and enjoy your game. :)",
      sep='\n')

# Round 1

# Players turn

print("", "Your 1st hand:", "", sep='\n')
print("Your Gold:", bet.player_gold, "gold")
print("")

# inital bet

bet.player_vs_ai_bet()
print("")
print("Your Gold:", bet.player_gold, "gold")

# rolling

player_first_re_roll = []
print("")
player_first_roll = pvai.roll_dice([randint(1, 6) for x in range(5)],
                                   player_first_re_roll)

# AI's turn
print("", "Your Opponent's 1st hand:", "", sep='\n')
print("Opponent's Gold:", bet.ai_gold, "gold")
print("")

# rolling

ai_first_re_roll = []

ai_first_roll = pvai.roll_dice([randint(1, 6) for x in range(5)],
                               ai_first_re_roll)

# round 1 score calculated

rs.score_comparison(player_first_re_roll, ai_first_re_roll)

# Round 2

# Players turn
print("", "Your 2nd hand:", "", sep='\n')
print("Your Gold:", bet.player_gold, "gold")
print("")

# betting/ai raise

bet.player_vs_ai_bet()
print("")
print("Your Gold:", bet.player_gold, "gold")
print("")
bet.ai_raise()

# rolling

player_final_hand = []


pvai.second_roll_choice()
# print(player_final_hand, "player final")
# AI's turn

print("", "Your Opponent's 2nd hand:", "", sep='\n')
print("Your Opponent's:", bet.ai_gold, "gold")
print("")

# rolling

ai_final_hand = []

pvai.second_roll_ai_choice()
# print(ai_final_hand, "ai final")
# final score calculated

rs.player_score = 0
rs.ai_score = 0

rs.score_comparison(player_final_hand, ai_final_hand)

# the following function decides who is the winner

print("")
go.who_wins()
print("")
# print('player - ', rs.player_score, ' ai - ', rs.ai_score)
