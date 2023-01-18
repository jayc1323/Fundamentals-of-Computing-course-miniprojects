# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1=0
score2=0
ball_pos=[300,200]
ball_vel=[0.1*random.randrange(12,24),-0.1*(random.randrange(6,18))]

direction=True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel,direction,score1,score2
    # these are vectors stored as lists
    score1=0
    score2=0
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction==RIGHT:
        ball_vel[0]=0.1*random.randrange(12,24)
        ball_vel[1]=-0.1*(random.randrange(6,18))
    elif direction==LEFT:
        ball_vel[0]=-0.1*(random.randrange(12,24))
        ball_vel[1]=-0.1*(random.randrange(6,18))


# define event handlers
def new_game():
    spawn_ball()
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos,ball_vel,direction  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    paddle1_vel=0
    paddle2_vel=0
    
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel
    global paddle2_vel,direction
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "black")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "black")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "black")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
            
    # draw ball
    canvas.draw_circle([ball_pos[0],ball_pos[1]],BALL_RADIUS,2,"red","red")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    if paddle1_pos<=40 or paddle1_pos>=360:
        paddle1_vel=0
     
    if paddle2_pos<=40 or paddle2_pos>=360:
        paddle2_vel=0
    # draw paddles
    #paddle1
    canvas.draw_line([0,paddle1_pos+40],[8,paddle1_pos+40],1,"black")
    canvas.draw_line([0,paddle1_pos-40],[8,paddle1_pos-40],1,"black")
    canvas.draw_line([592,paddle2_pos+40],[600,paddle2_pos+40],1,"black")
    canvas.draw_line([592,paddle2_pos-40],[600,paddle2_pos-40],1,"black")
    
    
    # determine whether paddle and ball collide 
    
    if ball_pos[0]<=28 and ball_pos[1]>=(paddle1_pos-40) and ball_pos[1]<=(paddle1_pos+40):
        direction=LEFT
        ball_vel[0]*=-1.1
        ball_vel[1]*=1.1
    elif ball_pos[0]>=572 and ball_pos[1]>=(paddle2_pos-40) and ball_pos[1]<=(paddle2_pos+40):
        direction=RIGHT
        ball_vel[0]*=-1.1
        ball_vel[1]*=1.1
    elif ball_pos[1]>380:
        ball_vel[1]*=-1.1
        ball_vel[0]*=1.1
    elif ball_pos[1]<20:
        ball_vel[1]*=-1.1
        ball_vel[0]*=1.1
    elif ball_pos[0]<=28 and ball_pos[1]<(paddle1_pos-40):
        ball_pos[0]=300
        ball_pos[1]=200
        
        direction=LEFT 
        
        score2+=1
        
        ball_vel[0]=0.1*random.randrange(12,24)
        ball_vel[1]=-0.1*(random.randrange(6,18))
    elif ball_pos[0]<=28 and ball_pos[1]>(paddle1_pos+40):
        ball_pos[0]=300
        ball_pos[1]=200
        
        direction=LEFT
       
        score2+=1
        
        ball_vel[0]=0.1*random.randrange(12,24)
        ball_vel[1]=-0.1*(random.randrange(6,18))
    elif ball_pos[0]>=572 and ball_pos[1]>(paddle2_pos+40): 
        ball_pos[0]=300
        ball_pos[1]=200 
         
        direction=RIGHT
        
        score1+=1
        
        ball_vel[0]=-0.1*random.randrange(12,24)
        ball_vel[1]=-0.1*(random.randrange(6,18))
    elif ball_pos[0]>=572 and ball_pos[1]<(paddle2_pos-40): 
        ball_pos[0]=300
        ball_pos[1]=200
        
        direction=RIGHT
        
        score1+=1
        
        ball_vel[0]=-0.1*random.randrange(12,24)
        ball_vel[1]=-0.1*(random.randrange(6,18))
    canvas.draw_text(str(score1),(150,50),30,"black")
    canvas.draw_text(str(score2),(450,50),30,"black")
        
        
        
        
        
        
   
        
    
        
    
    
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-5
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=5
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-5
    elif key==simplegui.KEY_MAP["down"]: 
        paddle2_vel=5
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["w"]: 
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["up"]: 
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0
        


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('yellow')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('restart',spawn_ball)


# start frame
new_game()
frame.start()