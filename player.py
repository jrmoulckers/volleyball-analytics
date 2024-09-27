from enum import Enum

class gender(Enum):
    MALE = 1
    FEMALE = 2

class player:
    name: str
    gender: gender
    front_rating: int
    back_rating: int
    libero: bool
    setter: bool
    rotation_number: int = -1

    def __init__(self, name, gender, front_rating, back_rating, libero = False, setter = False):
        name = name
        gender = gender
        front_rating = front_rating
        back_rating = back_rating
        libero = libero
        setter = setter