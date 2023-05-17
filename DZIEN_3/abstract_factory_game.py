#Frog game
class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.action()
        msg = f'Żaba {self} spotyka {obstacle} i {act}'
        print(msg)

class Bug:
    def __str__(self):
        return 'robaka'

    def action(self):
        return 'zjada go'


class FrogWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t---------- Frog World --------------'

    def make_character(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        return Bug()


# Warlock game
class Warlock:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'Czarnoksiężnik {self} walczy ze {obstacle} i {act}'
        print(msg)


class Ork:
    def __str__(self):
        return 'złym orkiem'

    def action(self):
        return 'masakruje go i wysyła do zaświatów'


class WarlockWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t---------- Warlock World --------------'

    def make_character(self):
        return Warlock(self.player_name)

    def make_obstacle(self):
        return Ork()
