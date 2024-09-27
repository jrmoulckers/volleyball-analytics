from lineup import lineup

class rotation:
    def __init__(self, lineup: lineup):
        self.lineup = lineup
        self.rotation_number = 0

    def __str__(self):
        return str(self.lineup)
    
    def is_valid():
        raise NotImplementedError()
    
    def advance_rotation(self):
        self.rotation_number += 1
        raise NotImplementedError
    
    def get_score(self):
        return self.lineup.get_composite_score()