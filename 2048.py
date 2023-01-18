"""
Clone of 2048 game.
"""
import random
import poc_2048_gui


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line): 
    """
    Function that merges a single row or column in 2048.
    """
    kom=list(line)
    copy=list(line)
    qwe=len(copy)
    asd=qwe-1
    dummy_count=0
    dummy_count2=0  
    
    for dummy_wer in range(qwe):
        if copy[dummy_wer]==0:
            kom.remove(0)
            dummy_count+=1
    for dummy_itek in range(dummy_count):
        kom.append(0)
        
    for dummy_itek in range(asd):
        
        if kom[dummy_itek]==kom[dummy_itek+1]:
            kom[dummy_itek]=2*kom[dummy_itek]
            kom[dummy_itek+1]=0
            
    joi=list(kom)        
    for dummy_wer in range(qwe):
        if joi[dummy_wer]==0:
            kom.remove(0)
            dummy_count2+=1
    for dummy_itek in range(dummy_count2):
        kom.append(0)        
            
            
 
            
            
    
   
    # replace with your code
    return kom





class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        """
        initialize class
        """
        
        self._rows=grid_height 
        self._cols=grid_width   
        self.reset()
        self._initup=[]
        self._initdown=[]
        self._initright=[]
        self._initleft=[]

        for col in range(0,self._cols):
            self._initup.append( (0,col))
            self._initdown.append( (self._rows-1,col))
        for rows in range(0,self._rows):
            self._initright.append((rows,self._cols-1))
            self._initleft.append((rows,0))
            
        self._refdict={UP:self._initup,DOWN:self._initdown,RIGHT:self._initright,LEFT:self._initleft}    


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid= [[0 for dummy_col in range(0,self._cols)]for dummy_row in range(0,self._rows)]
        self.new_tile() 
        self.new_tile()
        
    def __str__(self):
        """
        Print out the representation of grid
        """
        
        for dummy_rows in range(0, self._rows):
            luop=[]
            for dummy_cols in range(0, self._cols):
                luop.append(self._grid[dummy_rows][dummy_cols])
            print(luop) 
            for dummy_a in range(0,self._cols): 
                luop.pop(0)
        return "2048"        
              
        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._rows

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._cols

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
    
        num_steps=0
        vect=OFFSETS[direction]
        initial_tiles=self._refdict[direction]
        if vect[0]==0:
            num_steps=self._cols
        elif vect[1]==0:
            num_steps=self._rows
            
        temp_list3=list(self._grid)
            
        for start_cell in initial_tiles:
            
            temp_list=[]
            temp_list1=[]
            
            
            for dummy_step in range(num_steps):
                row = start_cell[0] + dummy_step* vect[0]
                col = start_cell[1] + dummy_step* vect[1]
          
            
                temp_list.append((row,col))
            for item in temp_list:
                temp_list1.append(self._grid[item[0]][item[1]])
                
            temp_list1=merge(temp_list1)
            
            dummy_ads=0
            
            for item in temp_list:
                temp_list3[item[0]][item[1]]=temp_list1[dummy_ads]
                dummy_ads+=1
                
        dummy_obj=TwentyFortyEight(self._rows,self._cols) 
        dummy_obj._grid=self._grid
        if  dummy_obj._grid!=temp_list3: 
            
            self._grid=temp_list3
        self.new_tile()
        
        
                
                
                
            
            
            
                    
           
                    
                    
                    
                    
                    
            
                
                
            
        
                
                
                
        
                
    
        
        
       

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code 
        
        dummy_b=10  
        for dummy_i in range(0,dummy_b): 
            dummy_b+=1
            
     
            randrow=random.randrange(0,self._rows)
            randcol=random.randrange(0,self._cols)
            if self._grid[randrow][randcol]==0:
               
            
               
                probb=random.random()
                if probb<=0.1:
                    var=4
                else:
                    var=2
                self.set_tile(randrow,randcol,var) 
                break
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]



 


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
