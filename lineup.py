import copy
from typing import MutableSequence
from player import gender, player
from roster import roster
 
class lineup:
    MIN_LINEUP_SIZE = 3
    MAX_LINEUP_SIZE = 6
    MIN_FEMALE = roster.MIN_FEMALE
    MIN_MALE = 1
    MAX_FEMALE = MAX_LINEUP_SIZE - MIN_MALE
    MAX_MALE = 3

    def __init__(self, players: MutableSequence[player], bench: MutableSequence[player], unassigned: MutableSequence[player]):
        self.players = players
        self.bench = bench
        self.unassigned = unassigned
        
    def get_composite_score(self):
        return (self.get_front_score() + self.get_back_score()) // 2

    def get_front_score(self):
        return sum(s.front_rating for s in self.players) // len(self.players)

    def get_back_score(self):
        return sum(s.back_rating for s in self.players) // len(self.players)
    
    def add_player(self, player: player):
        if(len(self.players) < self.MAX_LINEUP_SIZE):
            self.players.append(player)
        else:
            self.bench.append(player)
        
    def is_valid(self):
        lineup_complete = not self.unassigned
        valid_size = self.MIN_LINEUP_SIZE <= len(self.players) <= self.MAX_LINEUP_SIZE
        num_female = sum([p.gender == gender.FEMALE for p in self.players])
        num_male = sum([p.gender == gender.MALE for p in self.players])
        valid_female = (self.MIN_FEMALE if lineup_complete else 0) <= num_female <= self.MAX_FEMALE
        valid_male = (self.MIN_MALE if lineup_complete else 0) <= num_male <= self.MAX_MALE

        valid = (valid_size or lineup_complete) and valid_male and valid_female

        if not valid:
            print("VALIDATIONS")
            print(self.players)
            print(valid_size)
            print("Male", valid_male, num_male)
            print("Female", valid_female, num_female)
            print("___________")
        return valid
        
    def __str__(self):
        return """
                Rotation: 1        
            Front:   | Back: 
        |^^^^^^^^^^^^^^^^^^^^^^^^^|
        |                         |
        |                         |
        |                         |
        |_________________________|
        |                         |
        |                         |
        |                         |
        |_________________________|
        Bench:
        """
    
    def clone(self):
        return copy.deepcopy(self)
