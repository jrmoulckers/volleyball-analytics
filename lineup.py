from typing import MutableSequence
from player import player

class lineup:
    players: MutableSequence[player]
    bench: MutableSequence[player]
    def __init__(self, players, bench):
        players = players
        bench = bench
        
    def get_composite_score(self):
        return sum(self.get_front_score(), self.get_back_score()) // 2

    def get_front_score(self):
        return sum(s.front_rating for s in self.players) // self.players.count

    def get_back_score(self):
        return sum(s.back_rating for s in self.players) // self.players.count
    
    def is_valid():
        raise NotImplementedError()
    
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
