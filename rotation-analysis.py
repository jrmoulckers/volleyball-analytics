import copy
import sys
from typing import MutableSequence

from lineup import lineup
from player import player, gender
from roster import roster
from rotation import rotation
    
def can_sub(sub: player, player: player):
    return sub.rotation_number == player.rotation_number    

def should_sub(sub: player, player: player, is_front: bool):
    return sub.front_rating > player.front_rating if is_front else sub.back_rating >= player.back_rating    

def build_lineup_old(lineup: lineup, unassigned: MutableSequence[player]):
    if(not lineup.is_valid()):
        return -1 # Invalid lineup
    elif not unassigned:
        return assess_rotation(0, rotation(lineup.clone())) # Begin assessing lineup
    
    best_lineup = -1

    # Continue building lineup
    for p in unassigned:
        next_lineup = lineup.clone()
        next_lineup.add_player(p)
        best_lineup = max(best_lineup, build_lineup(next_lineup, [u for u in unassigned if u != p]))
    return best_lineup

def assess_rotation(total_score: int, current_rotation: rotation):
    total_score += current_rotation.get_score()
    if current_rotation.rotation_number == rotation.NUM_ROTATION_ITERATIONS:
        return total_score // rotation.NUM_ROTATION_ITERATIONS # Max rotations reached
    elif not current_rotation.is_valid():
        return -1 # Invalid rotation
    
    assert(current_rotation.rotation_number < rotation.NUM_ROTATION_ITERATIONS)

    next_rotations = current_rotation.advance_rotation()
    best_score = -1
    for r in next_rotations:
        best_score = max(best_score, assess_rotation(total_score, r))
    
    return best_score    



def get_top_lineups_old(roster: roster):
    assert(roster.is_valid)
    return build_lineup_old(lineup([], [], []), roster.players)

def get_rotation_position(court_position: int, rotation_number: int):
    return ((lineup.MAX_LINEUP_SIZE + court_position - rotation_number) % 6) + 1

def is_more_skilled(player1: player, player2: player, rotation_position: int):
    assert(player1 is not None and player2 is not None)
    if rotation_position > 3:
        return player1.front_rating > player2.front_rating
    else:
        return player1.back_rating > player2.front_rating

def get_composite_score(rotations: MutableSequence[MutableSequence[player]]):
    sum = 0
    for r in rotations:
        for pos, p in enumerate(r):
            if pos > 3:
                sum += p.front_rating
            else:
                sum += p.back_rating
        sum //= len(r)
    sum //= len(rotations)
    return sum

def should_add_player(player: player, players: MutableSequence[player], rotations: MutableSequence[MutableSequence[player]] = [[]]):
    current_rotation = rotations[-1]
    rotation_complete = len(current_rotation) == lineup.MAX_LINEUP_SIZE

    num_female = sum(p.gender == gender.FEMALE for p in current_rotation) + (1 if player.gender == gender.FEMALE else 0)
    valid_female = (lineup.MIN_FEMALE if rotation_complete else 0) <= num_female <= lineup.MAX_FEMALE
    num_male = sum(p.gender == gender.MALE for p in current_rotation) + (1 if player.gender == gender.MALE else 0)
    valid_male = (lineup.MIN_MALE if rotation_complete else 0) <= num_male <= lineup.MAX_MALE
    valid_gender = valid_female and valid_male

    rotation_position = get_rotation_position(len(current_rotation) + 1, len(rotations))
    valid_rotation = (player not in current_rotation) and (player.rotation_number in (-1, rotation_position))

    substituted_player = rotations[-2] if len(rotations) >= 2 else None 
    valid_substitution = is_more_skilled(player, substituted_player, rotation_position) if GREEDY_SUBSTITUTION_STRATEGY and substituted_player is not None else True
    return valid_gender and valid_rotation and valid_substitution

def get_top_lineups(players: MutableSequence[player], rotations: MutableSequence[MutableSequence[player]] = [[]]):
    lineup_size = min(len(players), lineup.MAX_LINEUP_SIZE)
    current_rotation = rotations[-1]
    print(len(current_rotation))
    if len(current_rotation) < lineup_size:
        top_lineup = (0, [[]])
        for p in players:
            rotations_copy = copy.deepcopy(rotations)
            if should_add_player(p, players, rotations):
                players_copy = copy.deepcopy(players)
                rotations_copy[-1].append(copy.deepcopy(p))
                current_lineup = get_top_lineups(players_copy, rotations_copy)
                top_lineup = current_lineup if current_lineup[0] > top_lineup[0] else top_lineup
        return top_lineup
    elif len(rotations) == rotation.NUM_ROTATION_ITERATIONS:
        # Return composite score
        return (get_composite_score(rotations), copy.deepcopy(rotations))
    else:
        # Create next rotation
        players_copy = copy.deepcopy(players)
        rotations_copy = copy.deepcopy(rotations)
        rotations_copy.append([])
        return get_top_lineups(players_copy, rotations_copy)
    
GREEDY_SUBSTITUTION_STRATEGY = False
def main():
    players = [
        player('JM', gender.MALE, 85, 40, 95, False, False),
        player('CD', gender.FEMALE, 95, 85, 85, False, False),
        player('CL', gender.FEMALE, 40, 90, 50, False, True),
        player('ES', gender.MALE, 90, 30, 45, False, False),
        player('TB', gender.MALE, 40, 80, 30, False, False),
        player('CH', gender.FEMALE, 30, 80, 60, False, True),
        player('JC', gender.MALE, 45, 30, 70, False, False)
    ]
    print(get_top_lineups(players))

main()