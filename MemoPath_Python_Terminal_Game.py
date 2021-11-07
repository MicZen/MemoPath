import random

class Player:
    
    def __init__(self, name):
        self.name = name

class Field:
    cell_trap_char = '□'
    cell_path_char = '■'
    
    def __init__(self, name, difficulty):
        self.difficulty = difficulty
        self.row = "".join([cell_trap_char for trap in 1:self.difficulty])
        self.field = "\n" + "\n".join([self.row for d in 1:self.difficulty]) + "\n" 
        self.first_index = random.choice(list(range(1, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1))
        self.field[self.first_index] = cell_path_char
        self.field[self.first_index + 1] = cell_path_char
        self.field_generated = False
        while self.field_generated == False:
            try:
                self.next_index = random.choice(self.first_index + 1, self.first.index - self.difficulty + 1, self.first.index - self.difficulty + 1)
            except IndexError:
                try:
                    self.next_index = random.choice(self.first_index + 1, self.first.index - self.difficulty + 1)
                except IndexError:
                    self.next_index = random.choice(self.first_index + 1, self.first.index + self.difficulty + 1)
            self.field[self.next_index] = cell_path_char
            if cell_path_char in range(self.difficulty, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1)
                self.field_generated == True

    def __repr__(self):
        print(self.field)

class NewGame:
    
    game_difficulty = {"Easy": 5, "Medium": 7, "Hard": 9, "Insane": 12}
    
    def __init__(self):
        print("Write player 1 name")
        self.player_1 = Player(input()).name
        print("Write player 2 name")
        self.player_2 = Player(input()).name
        self.selected_difficulty = "Yet to be selected"
        while title(lower(self.selected_difficulty)) not in NewGame.game_difficulty.keys():
            print("Select a difficulty among: Easy, Medium, Hard, Insane")
            self.selected_difficulty = input()
        self.difficulty = NewGame.game_difficulty[self.selected_difficulty]



