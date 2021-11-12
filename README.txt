############################################################
#                                                          #
#  #   #  #####  #   #   ###   ####    ###   #####  #   #  #
#  ## ##  #      ## ##  #   #  #   #  #   #    #    #   #  #
#  # # #  #####  # # #  #   #  ####   #####    #    #####  #
#  #   #  #      #   #  #   #  #      #   #    #    #   #  #
#  #   #  #####  #   #   ###   #      #   #    #    #   #  #
#                                                          #
############################################################       

Developer: MZ

MEMOPATH is a terminal based game written in Python 3.
The game is between two opponents that have to cross a randomly generated squared field and the first player that reaches the the other side wins.
Every turn a player can move across the field toward the other side, until she falls into a trap and has to start over.
There is only one path that can be followed to reach the other side of the field, hence the two player need to move in opposite directions along the same path.
Both players are aware of their counterpart, meaning that they can take advantage from the opponent's mistake and memorize the path that the opponent have already crossed.
        
A random player starts.
The following steps describe a game round:
1) The player select a location to move into the field, writing a number in the range between 1 and the maximum number of cells of the side of the field.
   eg. if a field have a 8 cell side, one can choose a starting location between 1 and 8.
2) If in the selected starting location there is a trap the round ends, otherwise the player can continue moving in the field.
3) The player can move by one cell, by selecting a direction.
4) If in the new location there is a trap the round ends, otherwise the player can continue moving in the field.
Steps 3 and 4 are repeated until the player falls in a trap or reaches the other side of the field and wins.
Every time a player falls in a trap the round ends and has to start over, trying to remember the path that as been discovered so far. 
        
The difficulty of the game depends on the field size: Easy - 6x6 cells; Medium - 12x12 cells; Hard - 18x18 cells; Insane - 24x24 cells.