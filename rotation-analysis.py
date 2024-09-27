import sys
from typing import MutableSequence

from lineup import lineup
from player import player, gender
from rotation import rotation

lineup_size = 6
min_female = 2
min_male = 1
max_female = lineup_size - min_male
max_male = 3
num_rotation_iterations = 6
    
def can_sub(sub: player, player: player):
    return sub.rotation_number == player.rotation_number    

def should_sub(sub: player, player: player, is_front: bool):
    return sub.front_rating > player.front_rating if is_front else sub.back_rating >= player.back_rating    

def build_lineup(lineup: lineup, unassigned):
    if(not lineup.is_valid()):
        return -1 # Invalid lineup
    elif len(unassigned) == 0:
        raise NotImplementedError # Begin assessing lineup
    
    # Continue building lineup
    
    raise NotImplementedError

def assess_lineup(total_score, rotation: rotation):
    rotation_score = NotImplemented
    if rotation.rotation_number == num_rotation_iterations:
        return (total_score + rotation_score) // num_rotation_iterations # Max rotations reached
    elif not rotation.is_valid():
        return -1 # Invalid rotation
    assert(rotation.rotation_number < num_rotation_iterations)

    total_score += rotation.get_score()
    rotation.advance_rotation()
    assess_lineup(total_score, rotation)

def get_top_lineups(players: MutableSequence[player]):
    assert(sum(p.setter for p in players) <= 2)
    assert(sum(p.libero for p in players) <= 1)
    assert(min_male <= sum(p.gender == gender.MALE for p in players) <= max_male)
    assert(min_female <= sum(p.gender == gender.FEMALE for p in players) <= max_female)
            
    raise NotImplementedError()

def main():
    players = [
        player('JM', gender.MALE, 80, 40, False, False),
        player('CD', gender.FEMALE, 95, 85, False, False),
        player('CL', gender.FEMALE, 40, 90, False, True),
        player('ES', gender.MALE, 85, 30, False, False),
        player('TB', gender.MALE, 40, 75, False, False),
        player('CH', gender.FEMALE, 30, 80, False, True),
        player('JC', gender.MALE, 45, 30, False, False)
    ]
    get_top_lineups(players)

main()