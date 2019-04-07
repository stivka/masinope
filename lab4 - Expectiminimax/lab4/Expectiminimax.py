"""

You can choose from three AI-s:
* dummy_ai - Simple AI that plays by game theory
* minimax_ai - More advanced AI that uses expectiminimax for better endgame
* human_ai - If you want to play against other person

Run the pig_game() method with AI function as argument.

"""
import random

PLAYER_ONE = 1
PLAYER_TWO = -1

ROLL = 0
PASS = 1


def human_ai(turn, pot, player_two_points, player_one_points):
    if pot > 0:
        s = input("Do you want to keep rolling (Y/n)? ")
        return PASS if len(s) > 0 and s[0].lower() == "n" else ROLL
    else:
        return ROLL


def dummy_ai(turn, pot, player_two_points, player_one_points):
    return ROLL if pot < 21 else PASS


def minimax_ai(turn, pot, player_two_points, player_one_points):
    # Returns the move with highest minimax estimate.
    depth = 10
    
    opponent_points = player_one_points if turn == PLAYER_TWO else player_two_points

    ai_points = player_two_points if turn == PLAYER_TWO else player_one_points

    pass_state = exp_minimax(-turn, 0, 0, ai_points + pot, opponent_points, depth, turn)

    roll_state = exp_minimax(turn, 1, pot, ai_points, opponent_points, depth, turn)
    
    return ROLL if roll_state > pass_state or pass_state == roll_state and pot < 21 else PASS


def exp_minimax(turn, chance, pot, ai_points, opponent_points, depth, player):
    depth = depth - 1
    """
    What follows is 4 cases. In the order that if possible, only 1. case, if possible
    only second case..
    """
    # Case 1a: Somebody won
    if ai_points >= 100:
        return 1
    elif opponent_points >= 100:
        return -1
    # Case 1b: 0 depth remains
    elif depth < 1:
        return 0

    # Case 2: Chance node
    if chance:
        success = exp_minimax(turn, 0, pot + 4, ai_points, opponent_points, depth, player)
        failure = exp_minimax(-turn, 0, 0, ai_points, opponent_points, depth, player)
        return success if success > failure else failure
    # Case 3: AI's turn (return min value)
    elif turn == player:
        roll_state = exp_minimax(turn, 1, pot, ai_points, opponent_points, depth, player)
        pass_state = exp_minimax(-turn, 0, 0, ai_points + pot, opponent_points, depth, player)
        return roll_state if roll_state > pass_state else pass_state
    # Case 4: Opponent's turn (return min value)
    else:
        roll_state = exp_minimax(turn, 1, pot, ai_points, opponent_points, depth, player)
        pass_state = exp_minimax(-turn, 0, 0, ai_points, opponent_points + pot, depth, player)
        return roll_state if roll_state < pass_state else pass_state


def pig_game(ai_function, opponent_function = human_ai):
    player_one_points = player_two_points = rolled = 0
    turn = PLAYER_TWO

    while player_one_points < 100 and player_two_points < 100:
        print("Player one points", player_one_points, "player two points", player_two_points, "holding", rolled)
        if turn == PLAYER_ONE:
            decision = ai_function(turn, rolled, player_two_points, player_one_points)
        else:
            decision = opponent_function(turn, rolled, player_two_points, player_one_points)

        if decision == PASS:
            rolled = 0
            turn = -turn
        else:
            dieroll = random.randint(1, 6)
            if dieroll == 1:
                if turn == PLAYER_ONE:
                    player_one_points -= rolled
                else:
                    player_two_points -= rolled
                rolled = 0
                turn = -turn
            else:
                rolled += dieroll
                if turn == PLAYER_ONE:
                    player_one_points += dieroll
                else:
                    player_two_points += dieroll

    if player_one_points >= 100:
        return 1
    elif player_two_points >= 100:
        return 0


""" Start game from here 
Assign the numbers of games to be played,
players put against each other (dummy_ai, minimax_ai, human_ai)
"""
ai = dummy = 0
numOfGames = 100

for i in range(numOfGames):
    if pig_game(dummy_ai, minimax_ai):
        dummy += 1
    else:
        ai += 1

print('Minimax: ', ai)
print('Dummy: ', dummy)
