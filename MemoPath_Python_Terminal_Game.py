############################################################
#                                                          #
#  #   #  #####  #   #   ###   ####    ###   #####  #   #  #
#  ## ##  #      ## ##  #   #  #   #  #   #    #    #   #  #
#  # # #  #####  # # #  #   #  ####   #####    #    #####  #
#  #   #  #      #   #  #   #  #      #   #    #    #   #  #
#  #   #  #####  #   #   ###   #      #   #    #    #   #  #
#                                                          #
############################################################ 

"""
The program is a terminal based python game developed as a custom project for the Codecademy course in Computer Science.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os, random

class Player:
    
    def __init__(self, name):
        self.name = name
        self.winner = False
    
    def __repr__(self):
        return self.name
    
    def select_starting_cell(self, difficulty):
        selected_cell = 0
        while selected_cell not in range(1, difficulty + 1):
            try: selected_cell = int(input(self.name + ", choose a starting cell in the range 1 to " + str(difficulty) + ", where 1 is the top row of\nthe field: "))
            except ValueError: selected_cell = 0
        return selected_cell
    
    def move(self, player):
        selected_direction = "Yet to be selected"
        if player == 1:
            while selected_direction not in ["Up", "Down", "Right", "U", "D", "R"]:
                selected_direction = input(self.name + " move toward the next cell by writing Up, Down or Right: ").lower().title()
        if player == 2:
            while selected_direction not in ["Up", "Down", "Left", "U", "D", "L"]:
                selected_direction = input(self.name + " move toward the next cell by writing Up, Down or Left: ").lower().title()
        return selected_direction

class Field:
    cell_trap_char = 'N'
    cell_path_char = 'Y'
    
    def __init__(self, difficulty):
        self.difficulty = difficulty
        row = "".join([Field.cell_trap_char for trap in range(1, self.difficulty + 1)])
        self.field = "\n" + "\n".join([row for d in range(1, self.difficulty + 1)]) + "\n"
        self.empty_field = self.field
        first_index = random.choice(range(1, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1))
        self.field = self.field[:first_index] + Field.cell_path_char + self.field[first_index + 1:]
        field_generated = False
        next_index = first_index
        new_index = -1
        while field_generated == False:
            while new_index < 0 or new_index >= len(self.field):
                new_index = random.choice([next_index + 1, next_index - self.difficulty - 1, next_index + self.difficulty + 1])
            next_index = new_index
            new_index = -1
            self.field = self.field[:next_index] + Field.cell_path_char + self.field[next_index + 1:]
            for index in range(self.difficulty, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1):
                if self.field[index] == Field.cell_path_char:
                    field_generated = True

    def __repr__(self):
        return self.field

class MemoPath:
    
    game_difficulty = {"Easy": 6, "Medium": 12, "Hard": 18, "Insane": 24}
    
    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        self.difficulty = None
        self.field = None

    def __repr__(self):
        MemoPath.update_terminal()
        return """
    ############################################################
    #                                                          #
    #  #   #  #####  #   #   ###   ####    ###   #####  #   #  #
    #  ## ##  #      ## ##  #   #  #   #  #   #    #    #   #  #
    #  # # #  #####  # # #  #   #  ####   #####    #    #####  #
    #  #   #  #      #   #  #   #  #      #   #    #    #   #  #
    #  #   #  #####  #   #   ###   #      #   #    #    #   #  #
    #                                                          #
    ############################################################

    MEMOPATH is a terminal based game written in Python 3.
    The game is between two opponents that have to cross a randomly generated
    squared field and the first player that reaches the the other side wins.
    Every turn a player can move across the field toward the other side,
    until she falls into a trap and has to start over.
    There is only one path that can be followed to reach the other side of
    the field, hence the two player need to move in opposite directions along
    the same path.
    Both players are aware of their counterpart, meaning that they can take
    advantage from the opponent's mistake and memorize the path that the
    opponent have already crossed.
    
    A random player starts.
    The following steps describe a game round:
    1) The player select a location to move into the field, writing a number
       in the range between 1 and the maximum number of cells of the side of
       the field.
       eg. if a field have a 8 cell side, one can choose a starting location
       between 1 and 8.
    2) If in the selected starting location there is a trap the round ends,
       otherwise the player can continue moving in the field.
    3) The player can move by one cell, by selecting a direction.
    4) If in the new location there is a trap the round ends, otherwise the
       player can continue moving in the field.
    Steps 3 and 4 are repeated until the player falls in a trap or reaches
    the other side of the field and wins.
    Every time a player falls in a trap the round ends and has to start over,
    trying to remember the path that as been discovered so far. 
    
    The difficulty of the game depends on the field size: Easy - 6x6 cells;
    Medium - 12x12 cells; Hard - 18x18 cells; Insane - 24x24 cells.
    """

    def update_terminal(something = None):
        os.system('clear') # os.system('cls' if os.name == 'nt' else 'clear')
        if something != None: print(something)
        
    def get_next_player(next_player):
        if next_player == 1: next_player = 2
        else: next_player = 1
        return next_player

    def new_game(self):
        input("Press Enter to start a new game...")
        MemoPath.update_terminal()
        self.player_1 = Player(input("Write the name of player 1: "))
        self.player_2 = Player(input("Write the name of player 2: "))
        players = {1: self.player_1, 2: self.player_2}
        next_player = random.choice(list(players.keys()))
        print(players[next_player].name + " starts first.")
        selected_difficulty = "Yet to be selected"
        while selected_difficulty.lower().title() not in MemoPath.game_difficulty.keys():
            selected_difficulty = input("Select a difficulty among: Easy, Medium, Hard, Insane: ").lower().title()
        self.difficulty = MemoPath.game_difficulty[selected_difficulty]
        self.field = Field(self.difficulty)
        first_iteration = True
        while self.player_1.winner != True and self.player_2.winner != True: 
            if first_iteration == True:
                MemoPath.update_terminal(self.player_1.name + " goes right.\n" + self.player_2.name + " goes left.\nThe first player that finds the way to the other side of the field wins!\nNow it's " + players[next_player].name + " turn!\n" + self.field.empty_field)
                current_field = self.field.empty_field
                first_col = list(range(1, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1))
                last_col = list(range(self.difficulty, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1))
                selected_row = players[next_player].select_starting_cell(self.difficulty)-1
                if next_player == 1:
                    if self.field.field[first_col[selected_row]] == Field.cell_path_char:
                        current_field = current_field[:first_col[selected_row]] + Field.cell_path_char + current_field[first_col[selected_row] + 1:]
                        selected_cell = first_col[selected_row]
                        MemoPath.update_terminal(self.player_1.name + " goes right.\n" + self.player_2.name + " goes left.\nThe first player that finds the way to the other side of the field wins!\nNow it's " + players[next_player].name + " turn!\n" + current_field)
                        first_iteration = False
                    else:
                        print("You've fallen into a trap!!! Try again your next turn.")
                        input("Press Enter to leave the field to your opponent.")
                        first_iteration = True
                        next_player = MemoPath.get_next_player(next_player)
                else:
                    if self.field.field[last_col[selected_row]] == Field.cell_path_char:
                        current_field = current_field[:last_col[selected_row]] + Field.cell_path_char + current_field[last_col[selected_row] + 1:]
                        selected_cell = last_col[selected_row]
                        MemoPath.update_terminal(self.player_1.name + " goes right.\n" + self.player_2.name + " goes left.\nThe first player that finds the way to the other side of the field wins!\nNow it's " + players[next_player].name + " turn!\n" + current_field)
                        first_iteration = False
                    else:
                        print("You've fallen into a trap!!! Try again your next turn.")
                        input("Press Enter to leave the field to your opponent.")
                        first_iteration = True
                        next_player = MemoPath.get_next_player(next_player)
            else:
                selected_direction = players[next_player].move(next_player)
                if selected_direction == "Up" or selected_direction == "U": selected_cell = selected_cell - self.difficulty + 1
                if selected_direction == "Down" or selected_direction == "D": selected_cell = selected_cell + self.difficulty + 1
                if selected_direction == "Left" or selected_direction == "L": selected_cell = selected_cell - 1
                if selected_direction == "Right" or selected_direction == "R": selected_cell = selected_cell + 1
                try: current_field[selected_cell]
                except IndexError:
                    print("You are moving outside the field! Try another direction.")
                    continue
                if next_player == 1:
                    if self.field.field[selected_cell] == Field.cell_path_char:
                        current_field = current_field[:selected_cell] + Field.cell_path_char + current_field[selected_cell + 1:]
                        MemoPath.update_terminal(current_field)
                        for index in range(self.difficulty, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1):
                            if current_field[index] == Field.cell_path_char:
                                self.player_1.winner = True
                    else:
                        print("You've fallen into a trap!!! Try again your next turn.")
                        input("Press Enter to leave the field to your opponent.")
                        first_iteration = True
                        next_player = MemoPath.get_next_player(next_player)
                else:
                    if self.field.field[selected_cell] == Field.cell_path_char:
                        current_field = current_field[:selected_cell] + Field.cell_path_char + current_field[selected_cell + 1:]
                        MemoPath.update_terminal(current_field)
                        for index in range(1, (self.difficulty * self.difficulty) + self.difficulty, self.difficulty + 1):
                            if current_field[index] == Field.cell_path_char:
                                self.player_2.winner = True
                    else:
                        print("You've fallen into a trap!!! Try again your next turn.")
                        input("Press Enter to leave the field to your opponent.")
                        first_iteration = True
                        next_player = MemoPath.get_next_player(next_player)
        if self.player_1.winner == True: print(self.player_1.name + " wins!")
        if self.player_2.winner == True: print(self.player_2.name + " wins!")
        input("Press Enter to exit.")

memopath = MemoPath()
print(memopath)
memopath.new_game()
