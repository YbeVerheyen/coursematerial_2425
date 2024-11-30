class Unit:
    def __init__(self, health, firepower, armor):
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor
        
        if self.health < 0 or self.firepower < 0 or self.armor < 0:
            raise ValueError("Ingegeven velden moeten boven 0 zijn.")
        
    @property
    def health(self):
        return self.__health
    
    @property
    def firepower(self):
        return self.__firepower
    
    @property
    def armor(self):
        return self.__armor
    
    def shot_by(self, other):
        #damage count
        damage = max(0, other.firepower - self.__armor)
        #min health
        self.__health = max (0, self.__health - damage)