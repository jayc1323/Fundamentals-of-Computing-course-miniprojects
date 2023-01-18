# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer_hand=None
player_hand=None
deck=None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return (self.suit)+(self.rank)

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]
        
        # create Hand object
    
    def __str__(self):
        a= " "
        for card in self.hand:
            
           
            a+=str(card)+" "
        return "hand contains"+a     
  
        
        
         
            # return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)
        # add a card object to a hand

    def get_value(self):
        a=0
        for card in self.hand:
            a+=VALUES[card.get_rank()]
            
        for card in self.hand:
            if card.get_rank()=='A' and a+10<=21:
                a=a+10
            
           
        return a        
            
        
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        i=0
        for card in self.hand:
            card.draw(canvas,[ pos[0]+80*i,pos[1]])
            i=i+1
        
            # draw a hand on the canvas, use the draw method for cards
         
        

   

    

        
# define deck class
class Deck:
    def __init__(self):
        global deck
        self.deck=[]
       
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
            
        # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
          # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()
       
    
        
        # deal a card object from the deck
    
    def __str__(self):
        a=" "
        for i in self.deck:
            a+=str(i.get_suit())+str(i.get_rank())+" "
        return "deck contains"+a
            # return a string representing the deck




#define event handlers for buttons
def deal():
    global deck
    global score
    global outcome, in_play
    global player_hand
    global dealer_hand
    
    if in_play:
        score-=1
        outcome=" Player loses "
        in_play=False
        
    else:
        
        
        
        outcome="Choose to Hit or Stand"
        dealer_hand=Hand()
        player_hand=Hand()
        deck=Deck()
        deck.shuffle()
        dealer_hand.add_card( deck.deal_card())
        dealer_hand.add_card( deck.deal_card())
        player_hand.add_card( deck.deal_card())
        player_hand.add_card( deck.deal_card())
        print ("player hand is"+ str(player_hand))
        print ("dealer hand is" +str(dealer_hand))
        in_play = True
    



    
    
    
    
    
    
    
   
    
    
    
    

    # your code goes here
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    

def hit():
    global outcome
    global score
    global in_play
    if in_play:
        if player_hand.get_value()<=21:
            player_hand.add_card(deck.deal_card())
            outcome= "Hit or Stand"
            in_play=True
          
       
        
        
       
       
        
        if player_hand.get_value()>21:
            
            
            
            outcome="you have busted, press deal for new deal"
            in_play=False
            score-=1
            
        
        
        

        
    
    
        
      
        
        
        
        
        
    
        # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome
    global score
    global in_play
    
    if in_play:
        
        if player_hand.get_value()>21:
            outcome="Player loses, press deal for new deal"
            in_play=False
       
        
        
        
        
        while dealer_hand.get_value()<17:
                dealer_hand.add_card(deck.deal_card())
                
        if dealer_hand.get_value()>21:
            
            
            outcome="dealer busted, Player Wins"
            
            score+=1
            in_play=False
        if dealer_hand.get_value()<player_hand.get_value():  
            outcome="Player wins, press deal for new deal"
            score+=1
            in_play=False
        elif dealer_hand.get_value()>player_hand.get_value(): 
            outcome="player loses , press deal for new deal"
            score-=1
            in_play=False
        elif dealer_hand.get_value()==player_hand.get_value():
            outcome="Hand Values are equal,player loses ,press deal for new deal"
            score-=1
            in_play=False
                   
                
        
        
        
        
            
                
    
        
        
        
        
        
    
    
        
      
        
        
    
        
        
        
        
    
        
        
        
        
        
    
     
   
    
    
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas,[50,100])  
    player_hand.draw(canvas,[50,300])
    canvas.draw_text("Score is "+str(score),[300,500],50,'white')  
    canvas.draw_text("Dealer's Hand",[52,215]  ,20,'white')
    canvas.draw_text("Player Hand",[52,415],20,'white')
    canvas.draw_text("player hand value ="+str(player_hand.get_value()),[52,430],20,"white")
   
    canvas.draw_text(outcome,[100,550],30,"white")
    canvas.draw_text("BlackJack",[300,40],40,"yellow")
    
    
    if in_play :
        card_loc = (CARD_CENTER[0], CARD_CENTER[1] ) 
        canvas.draw_image(card_back, card_loc, CARD_SIZE,[85,148], CARD_SIZE)
        
        
  
    
    # test to make sure that card.draw works, replace with your code below
    
   #  card = Card("S", "A")
   #  card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
frame.add_label("Dealer gets a new card when player stands until dealer hand value>17",200)
frame.add_label("If hand value>21, Game over, opponent wins", 210)
frame.add_label("The dealer wins ties.", 200)
frame.add_label("pressing deal in between a round will lead to a loss", 200)
frame.add_label("", 200)
frame.add_label("Values of the cards:", 200)
frame.add_label("A - 1 or 11", 200)
frame.add_label("2-9,card number", 200)
frame.add_label("10 and face cards-10", 200)



# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
