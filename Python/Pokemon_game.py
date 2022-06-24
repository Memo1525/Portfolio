#in this project we are going to create a oop pokemon game
class Pokemon:
    def __init__(self,name, primary_tipe, max_hp ):
        self.name = name
        self.primary_type = primary_tipe
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):  #devuelve el objeto en texto investigar __repl__
        return f"{self.name}({self.primary_type}"

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
        else:
            print(f"{self.name} is full.")

    def battle(self, other):
        print(f" Battle: {self.name, other.name}") #esto es inseguro en caso de que pongan algo mas
        #call typewheel()
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f"{self.name} fought {other.name} and the result is a {result}")
        #depending on the results , have effects
        if result == "lose":
            self.hp -=10
            print(f"{self.name}lost and now has {self.hp}")

    @staticmethod
    def typewheel(type1, type2):
        result = {'0': "lose",
                  '1': "win",
                  '-1': "tie"}
        #mapping between types and result conditions
        game_map={"water": 0,
                  "fire" : 1,
                  "grass" : 2}
        #implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], #water
            [0, -1, 1], #fire
            [1, 0, -1], #grass
        ]
        #declare a winner
        game_map["water"]
        wl_result = wl_matrix[game_map[type1]] [game_map[type2]]
        return result[wl_result]



print(Pokemon(name="bulbasur", primary_tipe="grass"))


if __name__ == '__main__':
    b.battle(charm)  #crear los objetos para que funcione
    #this is a condition
    #for run the script directly only
    #avoid printing thigs when you are importing the mocule

