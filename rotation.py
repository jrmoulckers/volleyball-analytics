import copy
from lineup import lineup

class rotation:
    NUM_ROTATION_ITERATIONS = 6

    def __init__(self, players):
        self.lineup = lineup
        self.rotation_number = 0

    def __str__(self):
        return str(self.lineup)
    
    def clone(self):
        return copy.deepcopy(self)
    
    def is_valid(self):
        return self.lineup.is_valid()
    
    def advance_rotation(self):
        self.rotation_number += 1
        return [self.clone()]
    
    def get_score(self):
        return self.lineup.get_composite_score()