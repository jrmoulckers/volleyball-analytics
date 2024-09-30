import copy
from enum import Enum

class gender(Enum):
    MALE = 1
    FEMALE = 2        

class player:
    IN_DEPTH_DISPLAY = False

    def __init__(self, name: str, gender: str, front_rating: int, back_rating: int, serve_rating: int, libero: bool = False, setter: bool = False):
        self.name = name
        self.gender = gender
        self.front_rating = front_rating
        self.back_rating = back_rating
        self.serve_rating = serve_rating
        self.libero = libero
        self.setter = setter
        self.rotation_number = -1

    def clone(self):
        return copy.deepcopy(self)
    
    def __eq__(self, other):
        if isinstance(other, player):
            return self.name == other.name
        return NotImplemented

    def __repr__(self):
        gender_string = 'M' if (self.gender == gender.MALE) else 'F'
        return f"{self.name}({gender_string}){self.front_rating}F|{self.back_rating}B" if self.IN_DEPTH_DISPLAY else f'{self.name}'
    
    def __str__(self):
        return f"{self.name}"