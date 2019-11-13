class Player:

    def __init__(self, name, hp, mp, speed):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.speed = speed

    def __repr__(self):
        return "{}(\"{}\", {}, {}, {})".format(self.__class__.__name__, self.name, self.hp, self.mp, self.speed)

    def __str__(self):
        return "It's a Player {} with {} hp, {} mana, {} speed".format(self.name, self.hp, self.mp, self.speed)
    

player = Player("Test", 1, 1, 2)
repr(player)
str(player)

