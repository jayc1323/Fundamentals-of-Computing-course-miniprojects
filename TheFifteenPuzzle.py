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
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

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
        # replace with your code
        dummy_a=0
        dummy_k=0
        dummy_j=0
        if self.get_number(target_row,target_col)==0:
            dummy_a+=1
        for itema in range(target_row+1,self.get_height()):
            for itemb in range(0,self.get_width()):
                if self.get_number(itema,itemb)== itemb+self._width*itema:
                    dummy_k+=1
                    
        if dummy_k==(self.get_height()-target_row-1)*self.get_width():
            dummy_a+=1
            
        for dummy_col in range(target_col+1,self.get_width()):
            if self.get_number(target_row,dummy_col)== dummy_col+self._width*target_row:
                dummy_j+=1
        if dummy_j==(self.get_width()-target_col-1):
            dummy_a+=1

        if dummy_a==3:
            return True
        
        return False

    def solve_interior_tile(self, target_row, target_col):
        
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        move_string=""
        
        
            
        assert target_row>1 and target_col>0  
        assert self.lower_row_invariant(target_row,target_col)
            
        
        (current_row,current_col)=self.current_position(target_row,target_col)
        if current_row==target_row:
            
            dummy_diff=target_col-current_col
            for dummy_i in range(dummy_diff):
                 move_string+="l"
            for dummy_i in range((dummy_diff-1)):
                 move_string+="urrdl"
        elif current_col==target_col:
            
            dummy_diff=target_row-current_row
            for dummy_i in range(dummy_diff):
                move_string+="u"
            for dummy_i in range(dummy_diff-1):
                move_string+="lddru"
            move_string+="ld"
        elif current_row<target_row and current_col<target_col:
            diff_row=target_row-current_row
            diff_col=target_col-current_col
            for dummy_i in range(diff_row):
                move_string+="u"
            for dummy_i in range(diff_col):
                move_string+="l"
            for dummy_i in range(diff_col-1):
                move_string+="drrul"
            for dummy_i in range(diff_row):
                move_string+="druld"
            
        elif current_row<target_row and current_col>target_col:
                if current_row>0:
                
                    diff_row=target_row-current_row
                    diff_col=current_col-target_col
                    for dummy_i in range(diff_row):
                        move_string+="u"
                    for dummy_i in range(diff_col):
                        move_string+="r"
                    for dummy_i in range(diff_col-1):
                        move_string+="ulldr"
                    for dummy_i in range(1):
                        move_string+="ullddruld"
                    for dummy_i in range(diff_row-1):
                        move_string+="druld"
        

                
               
                    
                        
       
        self.update_puzzle(move_string)
        assert self.lower_row_invariant(target_row,target_col-1)
        return move_string   
        
        

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        
        assert target_row>1
        assert self.lower_row_invariant(target_row,0)
        move_string=""
        special_move="ruldrdlurdluurddlur"
        (current_row,current_col)=self.current_position(target_row,0)
        diff_row=target_row-current_row
        diff_col=current_col-0
        if current_col==0:
            
            if diff_row==1:
                move_string+="u"
                for dummy_ in range(self.get_width()-1):
                    move_string+="r"
            else:
                for dummy_ in range(diff_row):
                    move_string+="u"
                for dummy_ in range(diff_row-2):
                    move_string+="rddlu"
                move_string+="rdl"
                move_string+=special_move
                for dummy_ in range(self.get_width()-2):
                    move_string+="r"
                
        elif  current_col!=0 and diff_row==1:
            if diff_col==1:
                move_string+="u"
                move_string+=special_move
            if diff_col>1:
                move_string+="u"
                for dummy_ in range(diff_col-1):
                    move_string+="r"
                for dummy_ in range(diff_col-1):
                    move_string+="rulld"
                move_string+=special_move    
            
            for dummy_ in range(self.get_width()-2):
                    move_string+="r"
                    
                    
            
        elif diff_row>1 and diff_col>0:
            for dummy_i in range(diff_row-1):
                move_string+="u"
            for dummy_i in range(diff_col):
                move_string+="r"
            move_string+="u"
            
            for dummy_ in range(diff_row-2):
                move_string+="lddru"
            move_string+="ld"
            
            for dummy_ in range(diff_col-1):
                move_string+="rulld"
            
            move_string+=special_move
            
            for dummy_ in range(self.get_width()-2):
                move_string+="r"
                
        
        self.update_puzzle(move_string)
        assert self.lower_row_invariant(target_row-1,self.get_width()-1)
        
        
        return move_string
                
                
            
            
            
            
                    
                    

        
       
        
        
        
        
        #return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        dummy_1=0
        dummy_2=0
        dummy_3=0
        dummy_4=0
        if self.get_number(0,target_col)==0:
            dummy_1+=1
        for dummy_col in range(target_col+1,self.get_width()):
            if self.get_number(0,dummy_col)==dummy_col:
                dummy_2+=1
        if dummy_2==(self.get_width()-1-(target_col)):
            dummy_1+=1
        for dummy_col in range(target_col,self.get_width()):
            if self.get_number(1,dummy_col)==dummy_col+self.get_width()*1:
                dummy_3+=1
        if dummy_3==self.get_width()-target_col:
            dummy_1+=1
            
        for dummy_row in range(2,self.get_height()):
            for dummy_col in range(self.get_width()):
                if self.get_number(dummy_row,dummy_col)==dummy_col+self.get_width()*dummy_row:
                    dummy_4+=1
        
        if dummy_4==self.get_width()*(self.get_height()-2):
            dummy_1+=1
            
        if dummy_1==4:
            return True
        
            
            
        
        
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        dummy_=0
        dummy2_=0
        if self.lower_row_invariant(1,target_col):
            dummy_+=1
        for dummy_col in range(target_col+1,self.get_width()):
            if self.get_number(0,dummy_col)==dummy_col:
                dummy2_+=1
        if dummy2_==self.get_width()-target_col-1:
            dummy_+=1
        if dummy_==2:
            return True
            
            
           
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.row0_invariant(target_col)
        move_string=""
        (current_row,current_col)=self.current_position(0,target_col)
        diff_row=current_row-0
        diff_col=target_col-current_col
        move="urdlurrdluldrruld"
        if diff_row==0 and diff_col==1:
            move_string+="ld"
        if diff_row==1:
            if diff_col==1:
                move_string+="lld"+move
            if diff_col==2:
                move_string+="ldl"+move
            if diff_col>2:
                move_string+="ld"
                for dummy_ in range(diff_col-1):
                    move_string+="l"
                for dummy_ in range(diff_col-2):
                    move_string+="urrdl"
                move_string+=move    
                    
        if diff_row==0 and diff_col>1:
            for dummy_ in range(diff_col):
                move_string+="l"
            for dummy_ in range(diff_col-2):
                move_string+="drrul"
            move_string+="druld"
            move_string+=move
            
        self.update_puzzle(move_string)
        assert self.row1_invariant(target_col-1)
        return move_string    
     

    def solve_row1_tile(self, target_col):
            
            
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        
            
         
        
            
           
        assert self.row1_invariant(target_col)
        move_string=""
        (current_row,current_col)=self.current_position(1,target_col)
        diff_row=1-current_row
        diff_col=target_col-current_col
        if diff_row==0:
            for dummy_ in range(diff_col):
                move_string+="l"
            for dummy_ in range(diff_col-1):
                move_string+="urrdl"
            move_string+="ur"
        
        if diff_row==1:
            if diff_col==0:
                move_string+="u"
            if diff_col>0:
                move_string+="u"
                for dummy_ in range(diff_col):
                    move_string+="l"
                for dummy_ in range(diff_col-1):
                    move_string+="drrul"
                move_string+="dru"
                
        self.update_puzzle(move_string)
        assert self.row0_invariant(target_col)
        return move_string
                   
                
                
                
        
       

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        
        assert self.row1_invariant(1)
        move_string=""
        
        pos_one=self.current_position(0,1)
        pos_three=self.current_position(1,1)
        
        
        if pos_one==(1,0) and pos_three==(0,0):
            move_string+="uldrul"
        if pos_one==(0,0) and pos_three==(0,1) :
            move_string+="ul"
        if pos_one==(0,1) and pos_three==(1,0):
            move_string+="ulrdlu"
            
        
        self.update_puzzle(move_string)
        
        
        return move_string
        
        
    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        move_string=""
        r_string=""
        d_string=""
        
        dummy_rows=self.get_height()
        dummy_cols=self.get_width()
        (dummy_zr,dummy_zc)=self.current_position(0,0)
        for dummy_ in range(self.get_width()-1-dummy_zc):
            
            r_string+="r"
        self.update_puzzle(r_string)
        for dummy_ in range(self.get_height()-1-dummy_zr):
            
            d_string+="d"
        self.update_puzzle(d_string)    
        for dummy_row in range(dummy_rows-1,1,-1):
            for dummy_col in range(dummy_cols-1,0,-1):
                move_string+=self.solve_interior_tile(dummy_row,dummy_col)
               
            move_string+=self.solve_col0_tile(dummy_row)
        for dummy_col in range(dummy_cols-1,1,-1):
            move_string+=self.solve_row1_tile(dummy_col)
            move_string+=self.solve_row0_tile(dummy_col)
        move_string+=self.solve_2x2()
        return r_string+ d_string+ move_string
        
       

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI( Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
#a=Puzzle(4,4,[[8,9,6,3],[2,0,5,7],[1,10,4,11],[12,14,13,15]])
#print a._grid
#obj = Puzzle(3, 3, [[1, 2, 6], [3, 5, 4], [8, 7, 0]])
#print obj
#obj.solve_interior_tile(2, 2)
#print obj
#assert my_puzzle.row1_invariant(j)
#my_puzzle.solve_row1_tile(j)
#assert my_puzzle.row0_invariant(j)
#my_puzzle.solve_row0_tile(j)
#assert my_puzzle.row1_invariant(j - 1)
#For obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]]), obj.solve_puzzle()
#obj = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#obj.solve_puzzle() 