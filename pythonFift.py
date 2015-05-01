"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """
    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [ [col + puzzle_width * row for col in range(self._width)] for row in range(self._height)]
        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]  
           
    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        check = True
                
        if self.get_number(target_row, target_col) != 0: 
            check = False
            
        if target_row == 0:    
            target_row = 2
            
        for col in range(self._width):
            if col > target_col and self.current_position(target_row, col) != (target_row, col): 
                check = False
            for row in range(target_row+1, self._height):
                if self.current_position(row, col) != (row, col): 
                    check = False            
            
        return check
    
    def get_val(self, row, col, width):
        """
        calculate value at pos in board
        """
        return row * width + col
    
    def get_pos(self, param):
        """
        gives back the tuple position of the param
        """
        return [(i, sublist.index(param)) for i, sublist in enumerate(self._grid) if param in sublist][0]
        
    def make_string(self, tgt, pos, target_row, target_col):
        """
        generate string of moves
        """
        mk_str = ""
        grid_copy = self.clone()
        new_target_row = target_row
        # pos_copy is location of 0 tile
        pos_copy = (target_row, target_col)
        if pos_copy[1] == 0:
            # help solve_col0 method
            grid_copy.update_puzzle('ur')
            mk_str += 'ur'
            target_col += 1
            new_target_row -= 1
            pos_copy = (new_target_row, target_col)

        # get target tile in same col as target pos
        while True:
            tgt_pos = grid_copy.get_pos(tgt)
            if target_col == tgt_pos[1]:
                break;
            elif tgt_pos[1] < pos_copy[1] and tgt_pos[0] == pos_copy[0]:
                grid_copy.update_puzzle('l')
                mk_str += 'l'
            elif tgt_pos[0] < pos_copy[0]:
                grid_copy.update_puzzle('u')
                mk_str += 'u'
            elif tgt_pos[1] < pos_copy[1]:
                grid_copy.update_puzzle('l')
                mk_str += 'l' 
            elif tgt_pos[1] > pos_copy[1] and tgt_pos[1] - pos_copy[1] > 1:
                #if target tile is more than one space to the right
                grid_copy.update_puzzle('r')
                mk_str += 'r'
            elif tgt_pos[1] > pos_copy[1]:
                if tgt_pos[1] == self.get_width() - 1: 
                    #if tgt tile is at right edge                    
                    grid_copy.update_puzzle('r')
                    mk_str += 'r'
                    pos_copy = grid_copy.get_pos(0)
                    tgt_pos = grid_copy.get_pos(tgt)
                    #use original target_row to check if below line isn't solved and needs to move let
                    if (target_row - 1) != pos_copy[0]:
                        while tgt_pos[1] != target_col:
                            grid_copy.update_puzzle('dllur')
                            mk_str += 'dllur'                            
                            tgt_pos = grid_copy.get_pos(tgt)
                    elif (target_row - 1) == pos_copy[0]:                      
                        while tgt_pos[1] != target_col:                        
                            grid_copy.update_puzzle('ulldr')
                            mk_str += 'ulldr'
                            tgt_pos = grid_copy.get_pos(tgt)
                        
                #if one spot to left of tgt tile and not at edge and needs to move left                    
                elif (target_row - 1) != pos_copy[0] and target_col < tgt_pos[1]:
                    move_var = None
                    if target_col < tgt_pos[1]:
                        grid_copy.update_puzzle('r')
                        mk_str += 'r' 
                        move_var = "dllur"
                    elif target_col > tgt_pos[1]:
                        move_var = "drrul"                                       
                    grid_copy.update_puzzle(move_var)
                    mk_str += move_var
                    pos_copy = grid_copy.get_pos(0)
                #move right
                else:
                    move_var = None
                    if target_col < tgt_pos[1]:
                        grid_copy.update_puzzle('r')
                        mk_str += 'r' 
                        move_var = "ulldr"
                    elif target_col > tgt_pos[1]:
                        if tgt_pos[0] != 0:
                            move_var = "urrdl"                             
                        else:
                            move_var = "drrul"
                    grid_copy.update_puzzle(move_var)
                    mk_str += move_var
            
            pos_copy = grid_copy.get_pos(0)
               
        # prepare to do looping if pos_copy not @ target_col - 1
        # get on left side of tgt tile

        if tgt_pos[0] == pos_copy[0] and tgt_pos[1] < pos_copy[1]:
            if (target_row - 1) != pos_copy[0]:
                grid_copy.update_puzzle('dllu')
                mk_str += 'dllu'
            else:        
                grid_copy.update_puzzle('ulld')
                mk_str += 'ulld'
        elif tgt_pos[1] == pos_copy[1] and (pos_copy[0] + 1 == tgt_pos[0] or pos_copy[0] - 1 == pos_copy[0]):
            if tgt_pos[0] > pos_copy[0]:    
                grid_copy.update_puzzle('ld')
                mk_str += 'ld'
            else:   
                grid_copy.update_puzzle('lu')
                mk_str += 'lu' 
        #if tgt_pos[1] != pos_copy[1]:
        elif (tgt_pos[0], tgt_pos[1] - 1) != (pos_copy[0], pos_copy[1]):
            move_up = 'u' * (pos_copy[0] - tgt_pos[0])
            grid_copy.update_puzzle('l')
            grid_copy.update_puzzle(move_up)            
            mk_str += 'l' 
            mk_str += move_up                
                
        # loop
  
        while tgt_pos != (new_target_row, target_col):
            grid_copy.update_puzzle('druld')          
            mk_str += 'druld'
            tgt_pos = grid_copy.get_pos(tgt)
 
        return mk_str                          
    
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        move_string = ""
        # does all tiles below and to the right satisfy order req'd
        assert self.lower_row_invariant(target_row, target_col), 'Did not meet expectations'

        #tgt is target tile
        tgt = target_row * self._width + target_col
        #pos is position of target tile
        pos = [(i, sublist.index(tgt)) for i, sublist in enumerate(self._grid) if tgt in sublist][0]

        move_string = self.make_string(tgt, pos, target_row, target_col)
        self.update_puzzle(move_string)
        
        # prevent assert with solve_col0_tile b/c not done updating yet

        if target_col != 0:
            assert self.lower_row_invariant(target_row, target_col-1) == True, "Wrong moves homie"
        
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        move_string = ""
        grid_copy = self.clone()
        assert grid_copy.lower_row_invariant(target_row, 0)
        if grid_copy.current_position(target_row, 0) == (target_row - 1, 0):
            move_string = 'u'                        
            grid_copy.update_puzzle('u')        
            #target_row = target_row - 1
            move_right = 'r'*(grid_copy.get_width() - 1)  
            grid_copy.update_puzzle(move_right)                    
            move_string += move_right
        else:
            move_string += grid_copy.solve_interior_tile(target_row, 0) 
            move_string += 'ruldrdlurdluurddlu'
            move_string += 'r' * (grid_copy.get_width() -1)
            
        self.update_puzzle(move_string)
        assert self.lower_row_invariant(target_row - 1, grid_copy.get_width() - 1), "col0 error"
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        check = True
        if (0, target_col) != self.get_pos(0):
            check = False
        else:
            if ((1*self.get_width() + target_col) != self.get_number(1, target_col)):
                check = False                    
            elif target_col != self.get_width() - 1:
                ((1*self.get_width() + target_col+1) != self.get_number(1, target_col+1))
            if check == True:
                check = self.lower_row_invariant(0, target_col)

        return check

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        check = True
        width = self.get_width() - 1
        if (1, target_col) != self.get_pos(0):
            check = False
        #check above value
        #if (self.current_position(0, width) != (0, width)):
            #check = False
        
        if check == True:
            check = self.lower_row_invariant(1, target_col)

        return check

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """  	
        self.update_puzzle('ld')
        mk_str = ""
        mk_str += 'ld'

        #if not already solved      
        if self.current_position(0, target_col) != (0, target_col):
            pos = self.get_pos(target_col)
            tile0 = self.get_pos(0)
            #if not on same row

            if pos[0] < tile0[0]:
                mk_str += 'u'
                self.update_puzzle('u')

            #if pos already to left of row
            #move until on top of tgt tile
            pos = self.get_pos(target_col)
            tile0 = self.get_pos(0)

            left_move = 'l' * (tile0[1] - pos[1])
            mk_str += left_move
            self.update_puzzle(left_move)
            # note target_col is psuedo for the target pos col
            pos = self.get_pos(target_col)
            tile0 = self.get_pos(0)

            if pos[1] < self.get_width() - 2:                     
                #check if not col 0 and not far enought away to do loop and not one col away from pos  
                while pos[1] >= 1 and pos[1] < self.get_width() -2 and pos[1] != target_col - 1:

                    #move into (1, j-2) pos
                    if (pos[0] == 1):
                        mk_str += 'urrdl'
                        self.update_puzzle('urrdl')
                    elif (pos[0] == 0):
                        mk_str += 'drrul'                    
                        self.update_puzzle('drrul')
                    #update tuple pos for while loop
                    pos = self.get_pos(target_col)
                    tile0 = self.get_pos(0) 
        
            pos = self.get_pos(target_col)
            tile0 = self.get_pos(0) 
            #if on line 0, do smaller loop
            print self
            if pos[0] == 0:
                mk_str += 'druld'                
                self.update_puzzle('druld')
                pos = self.get_pos(target_col)
                tile0 = self.get_pos(0)
            print self, tile0
            if tile0[0] == 0 and tile0[1] != 0:
                print self
                mk_str += 'ld'                
                self.update_puzzle('ld')
                print self
            #2x3 puzzle solve    
            mk_str += 'urdlurrdluldrruld'
            self.update_puzzle('urdlurrdluldrruld')
            
        return mk_str

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col), "err"
        #solve width-1 numbers for row 1
        mk_str = self.solve_interior_tile(1, target_col)   
        #move to (i-1 l-1) 
        mk_str += 'ur'
        self.update_puzzle('ur')    

        #assert self.row0_invariant(target_col)

        #self.solve_row0_tile(target_col)
        
        #assert self.row1_invariant(target_col - 1)

        return mk_str

    #############################################l##############
    # Phase 3 methods
    
    def check_2x2(self, tile0):
        """
        check length of solved items
        """
        arr = [tile0,
                self.get_pos(1),
                self.get_pos(1* self.get_width()),
                self.get_pos(1*self.get_width() + 1)]
        return [i for i in arr if self.current_position(i[0], i[1]) == (i[0], i[1])]

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        #assert self.row1_invariant(1), "Check your 2x2 inputs"
        mk_str = ""
        add_string = ""
        
        tile0 = self.get_pos(0)
        #move to (0,0) in order to do looping
        if tile0 != (0,0):
            if self.get_val(tile0[0], tile0[1], 2) == 3:
                mk_str += 'ul'
                self.update_puzzle('ul')
            elif self.get_val(tile0[0], tile0[1], 2) == 2:
                mk_str += 'u'
                self.update_puzzle('u')
            elif self.get_val(tile0[0], tile0[1], 2) == 1:
                mk_str += 'l'
                self.update_puzzle('l')
                            
        square_list = self.check_2x2(tile0)

        if len(square_list) != 4:            
            while (len(square_list) != 4):              
                self.update_puzzle('rdlu')
                mk_str += 'rdlu'            
                square_list = self.check_2x2(tile0)
        
        return mk_str

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        mk_str = ""
        width = self.get_width()
        height = self.get_height()
        #decrement number until find cell not solved
        num = ((height - 1) * width) + (width - 1)
        new_num = num
        arr = []
        arr_height = []
        arr.extend(range(width))
        arr_height.extend(range(height))

        while True:
            num_pos = self.get_pos(num)
            if num_pos != self.current_position(num_pos[0], num_pos[1]) or new_num == 0:
                break;
            else:
                new_num -= 1  
        
        if num != (height - 1) * width + (width - 1):
            last_solved = self.get_pos(new_num+1) if num != new_num else self.get_pos(min(new_num, new_num+1))
            last_solved_row = last_solved[0] if last_solved[1] > 0 else last_solved[0] - 1
            pos = (arr_height[last_solved_row] , arr[last_solved[1] - 1])
        else:
            pos = (height - 1, width - 1)
            
        tile0 = self.get_pos(0)                         

        if tile0 != (height-1, width-1):
            if pos[1] > tile0[1]:
                go_right = "r" * (pos[1] - tile0[1]) 
                self.update_puzzle(go_right)
                mk_str += go_right
            elif pos[1] < tile0[1]:
                go_left = 'l' * (tile0[1] - pos[1])
                self.update_puzzle(go_left)
                mk_str += go_left                
            if pos[0] > tile0[0]: 
                go_down = "d" * (pos[0] - tile0[0])              
                self.update_puzzle(go_down) 
                mk_str += go_down
        
        tgt_tile = height - 1 * width + width - 1
        tgt_tile_pos = self.get_pos(tgt_tile)
        while tgt_tile != 0: 
            tile0 = self.get_pos(0)           
            if (tile0[0] > 1 and tile0[1] > 0):
                mk_str += self.solve_interior_tile(tile0[0], tile0[1])

            elif tile0[0] > 1 and tile0[1] == 0:
                mk_str += self.solve_col0_tile(tile0[0])

            elif tile0[0] == 1 and tile0[1] > 1:
                mk_str += self.solve_row1_tile(tile0[1])
                
            elif tile0[0] == 0 and tile0[1] > 1:
                mk_str += self.solve_row0_tile(tile0[1])
                
            elif (tile0[0] == 1 or tile0[0] == 0) and (tile0[1] == 1 or tile0[1] == 0):
                mk_str += self.solve_2x2()   
                                           
            tgt_tile = self.get_pos(0)[0] * width + self.get_pos(0)[1]
            
        return mk_str

# Start interactive simulation
GRID = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#GRID = Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], [3, 0, 14, 10, 12, 6], [4, 15, 2, 11, 8, 1]])
#GRID = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
#GRID = Puzzle(4, 5, [[7, 6, 5, 3, 0], [4, 8, 2, 1, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#GRID = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
GRID.solve_puzzle()
poc_fifteen_gui.FifteenGUI(GRID)

