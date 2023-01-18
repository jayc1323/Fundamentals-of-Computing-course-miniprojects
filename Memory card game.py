# implementation of card game - Memory

import simplegui
import random
state=0
l1=[0,1,2,3,4,5,6,7]
l2=[0,1,2,3,4,5,6,7]
l3=l1+l2
o="0"

exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
a=[0,0,0,0]
k1=0
k2=0
k=0
k3=0
t=0
m=0



# helper function to initialize globals
def new_game():
    global t
    global o
    global m
    random.shuffle(l3)
    t=0
    m=0
    o="0"
    global state
    state=0
    for i in range(0,16):
        exposed[i]=False
    

     
# define event handlers
def mouseclick(pos):
    global exposed
    global a
    global k 
    global k1
    global k2
    global k3
    global t
    global o
    t=t+1
    m=t//2
    o=str(m)
    
    
    
    
    # add game state logic here
    lpos=list(pos)
    x=lpos[0]
    k=x//50
    
   
   
    
    global state
    if state == 0:
        k1=k
        a[1]=l3[k1]
        
        exposed[k1]=True
        
        
        state = 1
  
    elif state == 1:
        if exposed[k]==True:
            return 'hi'
        else:
            
            k2=k
            exposed[k2]=True
        
            a[2]=l3[k2]
            state = 2
    else:
        if exposed[k]==True:
            return 'hi'
        else:
            
            if a[1]==a[2]:
                exposed[k1]=True
                exposed[k2]=True
            else:
                exposed[k1]=False
                exposed[k2]=False
            
            k1=k
            exposed[k1]=True
        
            a[1]=l3[k1]
        
            state = 1
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = "+o)
    for i in range(0,16):
        if exposed[i]==False:
            
             canvas.draw_polygon([[50*i, 0], [50*i, 100], [50*(i+1), 0], [50*(i+1), 100]], 5, 'white', 'red')
        else:
            
            canvas.draw_text(str(l3[i]),[(i+1)*50-45,80],60,'red')
       
        
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns =0')


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric