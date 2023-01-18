    

                
"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000     # Number of trials to run
SCORE_CURRENT = 2.0 #core for squares played by the current player
SCORE_OTHER = 2.0 #core for squares played by the other player
    
# Add your functions here.
def mc_trial(board,player):
    """ this function conducts a trial and changes the state of the board"""
    
    current_player=player
    winner=None
    
    while winner==None:
        emp_squares=board.get_empty_squares()
        dum_cell=random.choice(emp_squares)
        dum_row=dum_cell[0]
        dum_col=dum_cell[1]
        board.move(dum_row,dum_col,current_player)
        current_player=provided.switch_player(current_player)
        winner=board.check_win()
        

def mc_update_scores(scores,board,player):
    
    """ this function scores the grid and updates scores list"""
    
    winner = board.check_win()
  
    for col in range(board.get_dim()):
        for row in range(board.get_dim()):
            if winner == provided.DRAW:
                scores[row][col] += 0
            
            elif winner == player and board.square(row,col) == player:
                scores[row][col] += SCORE_CURRENT
            elif winner == player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] -= SCORE_OTHER
            elif winner != player and board.square(row,col) == player:
                scores[row][col] -= SCORE_CURRENT
            elif winner != player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] += SCORE_OTHER
            elif board.square(row, col) == provided.EMPTY:
                scores[row][col] -= 0.0   
    
    
        
         
      
def get_best_move(board,scores):
    
    """This function takes a current board and a grid of scores. The function should find all of the empty squares with the maximum score and randomly return one of them as a \color{red}{\verb|(row, column)|}(row, column) tuple"""
    
    max_score = -1000
    
    for col in range(board.get_dim()):
            for row in range(board.get_dim()):
                if scores[row][col] >  max_score and board.square(row, col) == provided.EMPTY:
                    
                    max_score = scores[row][col]
                    
    # find empty squares with max score                
    empty_squares = board.get_empty_squares()
    candidate_move_list = []
    for square in empty_squares:
        if scores[square[0]][square[1]] == max_score:
            candidate_move_list.append(square)

    best_move = candidate_move_list[random.randrange(0,len(candidate_move_list))] 
    return best_move
    
    

def mc_move(board,player,trials):
    """This function takes a current board, which player the machine player is, and the number of trials to run"""
   
    scores = [ [0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
           
    
    for dummy_item in range(trials):
        board_copy=board.clone() 
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
        
    best_move= get_best_move(board,scores) 
    return best_move
            
        
        
    
    
                
        




# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
