class Hero(object):
    def __init__(self, hero_name):
        self.name = hero_name
        self.health = 100
        self.condition = None

    def test(self):
        print(str(self.name))

    # I want to call this function at certain points - finish a labour - or when the player requests it from a menu before making a choice
    def check_status(self):
        print(f"{self.name} has {str(self.health)} health.")
        # I want to update this so that it is syntactically correct
        print(f"{self.name} has the {str(self.condition)} condition.")