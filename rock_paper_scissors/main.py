game_dictionary = {"rock": 0,
                   "paper": 1,
                   "scissors": 2}


def get_input(player_name, max_attempts=3):
    while True:
        try:
            options = ",".join(game_dictionary.keys())
            prompt = f"{player_name} please enter your choice [{options}]:"
            choice_string = input(prompt).lower()
            choice_int = game_dictionary[choice_string]
            return choice_int
        except KeyError:
            max_attempts -= 1
            if max_attempts  == 0:
                raise Exception("You stink at typing")
            print("You are bad")


def compete(p1_choice, p2_choice):
    diff = p2_choice - p1_choice
    distance = abs(diff)
    if distance > 1:
        diff = -diff
    return diff
    #
    # if p1_choice == p2_choice:
    #     return 0
    #
    # if abs(p1_choice - p2_choice) == 1: #larger value wins
    #     if p1_choice > p2_choice:
    #         return -50
    #     else:
    #         return 50
    # else: #smaller value wins
    #     if p1_choice < p2_choice:
    #         return -50
    #     else:
    #         return 50


def player_one_always_wins(p1_choice, p2_choice):
    return  -1


def player_two_always_wins(p1_choice, p2_choice):
    return  1



def main():
    p1 = get_input("Player one")
    p2 = get_input("Player two", max_attempts=10)
    compete_variable = compete
    w = compete_variable(p1, p2)
    if w < 0:
        print("Player 1 wins")
    elif w == 0:
        print("It's a tie.")
    else:
        print ("Player 2 wins")
    #
    # compete(1, 2)

main()





