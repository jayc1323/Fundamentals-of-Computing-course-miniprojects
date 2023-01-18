"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    
    
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
        
        
    dummy_seq=set(hand)
    dummy_total_list=[]
    for dummy_item in dummy_seq:
        dummy_totals=hand.count(dummy_item)
        dummy_total_list.append(dummy_totals*dummy_item)
    dummy_total_list.sort()
    return max(dummy_total_list)



def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    dummy_outcomes=[]
    dummy_score=0
    for dummy_ in range(1,num_die_sides+1):
        dummy_outcomes.append(dummy_)
    dummy_sequences=gen_all_sequences(dummy_outcomes,num_free_dice)
    for dummy_item in dummy_sequences:
        dummy_score+=score(held_dice+dummy_item)
    exp_value=float(dummy_score)/float(len(dummy_sequences))    
    return exp_value 
        
def gen_all_holds(hand):
    """ Compute all possible holds of a hand
    """
    hand_hold = [()]
    for item in hand:
        for subset in hand_hold:
            hand_hold = hand_hold + [tuple(subset) + (item,)]
    return set(hand_hold)
    
   


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    dummy_holds=gen_all_holds(hand)
    exp_score=0
    best_hold=()
    
    for dummy_item in dummy_holds:
        
       
        num_free_sides=len(hand)-len(dummy_item)
        dummy_score=expected_value(dummy_item,num_die_sides,num_free_sides)
        if dummy_score>exp_score:
            exp_score=dummy_score
            best_hold=dummy_item
        
    
   
    return(exp_score,best_hold)
            
        
        
        
    
    
    


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print ("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)
    
    
#run_example()
#print gen_all_holds((1,))

print (strategy((1,),6))
import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)
