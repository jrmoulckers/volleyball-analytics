class roster:
    MIN_FEMALE = 2
    MIN_PLAYERS = 4
    MAX_PLAYERS = 12

    def __init__(self, players = []):
        self.players = players

    def is_valid(self):
        return True