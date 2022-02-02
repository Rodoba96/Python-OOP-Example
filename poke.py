# create a Pokemon
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp
        

    def __str__(self):
        return f"{self.name} ({self.primary_type}: {self.hp}/{self.max_hp})"
    
    # feed them to increase health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} is now {self.hp} HP.")
        else:
            print(f"{self.name} is full")

    # make them battle and decide for a winner
    def battle(self, other):
        print(f"\n!!!{self.name} vs {other.name}!!!\n")
        result = self.typewheel(self.primary_type, other.primary_type)

        #depending on the rsult, have some effects
        if result == "lose":
            self.hp -=10
            print(f"{self.name} lost and now has {self.hp} HP.")
        print(f"\n{self.name} fought {other.name} and the result is a {result}\n")
        #call typewheel()

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1:"tie"}
        # mapping between type and result conditions
        game_map = {"water": 0, "fire":1, "grass":2}
        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], #water 0
            [0, -1, 1], #fire 1
            [1, 0, -1], #grass 2
        ]
        # declare a winer
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]
        

# take a look at it
if __name__ == '__main__':
    #print ('\n')
    #print(Pokemon(name="Bulbasaur",primary_type="grass", max_hp=100))
    #print(Pokemon(name="Charmander",primary_type="fire", max_hp=100))
    #print ('\n')

    bulbi = Pokemon(name="Bulbasaur",primary_type="grass", max_hp=100)
    charm = Pokemon(name="Charmander",primary_type="fire", max_hp=100)

    bulbi.battle(charm)




