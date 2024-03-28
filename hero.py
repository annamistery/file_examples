class Hero():
    def __init__ (self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        description = (self.name + ' level is: ' + str(self.level) + ', Race is: ' + self.race + ', Health is ' + str(self.health)).title()   
        print(description)
    def level_up(self):
        self.level += 1
    def move (self):
        print('Hero ' + self.name + ' is starting...')
    def set_health(self, new_health):
        self.health = new_health   
        
class SuperHero(Hero):
    def __init__(self, name, level, race, magiclevel):
        ''' Initiate Super Hero'''     
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100


    def makemagic(self):
        ''' Use magic'''
        self.magic-=10
    def show_hero(self):
        description = (self.name + ' level is: ' + str(self.level) + ', Race is: ' + self.race + ', Health is  ' + str(self.health) +
                    ' Magic ' + str(self.magic)).title()   
        print(description)        