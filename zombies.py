"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
 
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._zombie_list=[]
        self._human_list=[]
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for dummy_item in self._zombie_list:
            yield dummy_item

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for dummy_item in self._human_list:
            yield dummy_item
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited=poc_grid.Grid(self._grid_height,self._grid_width)
        distance_field=[[self._grid_height*self._grid_width for col in range(self._grid_width)]for row in range(self._grid_height)]
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == FULL:
                    
                    visited.set_full(row, col)    
        
        
        boundary = poc_queue.Queue()
        if entity_type==ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        else:
            for human in self.humans():
                boundary.enqueue(human)

        for cell in boundary:
            visited.set_full(cell[0],cell[1])
            distance_field[cell[0]][cell[1]] = 0
        
        while len(boundary)>0:
            current_cell = boundary.dequeue() 
            neighbours = visited.four_neighbors(current_cell[0],current_cell[1])
            for neigh in neighbours:
                if visited.is_empty(neigh[0],neigh[1]) and self.is_empty(neigh[0],neigh[1]):
                    visited.set_full(neigh[0],neigh[1])
                    boundary.enqueue(neigh)
                    distance_field[neigh[0]][neigh[1]]=distance_field[current_cell[0]][current_cell[1]] + 1


        return distance_field
          
                
                
                    
                    
                    
                
                             
                    
                    
            
            
            
           

    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        newhumanlist=list(self._human_list)
        visited=poc_grid.Grid(self._grid_height,self._grid_width)
        for row in range(self._grid_height):
                for col in range(self._grid_width):
                    if self._cells[row][col] == FULL:
                        
                        
                        
                    
                        visited.set_full(row, col)
     
        
        
        for human in newhumanlist:
            dummy_=0
            maxd=0
            human_neighbors=visited.eight_neighbors(human[0],human[1])
            human_distance=zombie_distance_field[human[0]][human[1]]
            
       
               
     
            
            for neighbor in human_neighbors:
                
                
                dummy_=zombie_distance_field[neighbor[0]][neighbor[1]]
               
                    
                if  dummy_>maxd and visited.is_empty(neighbor[0],neighbor[1]):
                    maxd= dummy_
                    best_neighbor=neighbor 
            if human_distance>maxd:
                best_neighbor=human
            self._human_list.append(best_neighbor)    
            self._human_list.remove(human)
            
            
            
        
       
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        
        visited=poc_grid.Grid(self._grid_height,self._grid_width)
        newzombielist=list(self._zombie_list)
        for row in range(self._grid_height):
                for col in range(self._grid_width):
                    if self._cells[row][col] == FULL:
                        
                        
                    
                        visited.set_full(row, col)
        for zombie in newzombielist:
            
            dummy_=0
            mind=self._grid_height*self._grid_width
            
            zombie_neighbors=visited.four_neighbors(zombie[0],zombie[1])
            best_neighbor=zombie
     
           
            for neighbor in zombie_neighbors:
                dummy_=human_distance_field[neighbor[0]][neighbor[1]]
                if zombie in self._human_list and  dummy_==1:
                    best_neighbor=zombie
                    
                    
                
                elif dummy_<mind and visited.is_empty(neighbor[0],neighbor[1]):
                    
                    
                    mind=dummy_
                    best_neighbor=neighbor    
            self._zombie_list.remove(zombie)
            self._zombie_list.append(best_neighbor)
            
       

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
