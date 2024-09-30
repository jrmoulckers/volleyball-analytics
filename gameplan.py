from lineup import lineup
from roster import roster

class gameplan:
    def __init__(self, roster: roster, lineup: lineup):
        self.roster = roster
        self.lineup = lineup