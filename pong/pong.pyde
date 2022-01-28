ball_x = 0
ball_y = 0
left_y = 0
right_y = 0
step_size_left = 0
step_size_right = 0
paddle_height = 120
paddle_width = 20
ball_speed = 2
ball_size = 8
scoreleft = 0
scoreright = 0
#True: Increasing False: Decreasing
ball_x_dir = True
ball_y_dir = True

def setup():
    size(800, 600) 
    background(0)
    print("greetings")
    draw_ball(width/2, 20)


def draw_ball(X_pos, Y_pos):
    fill(255) 
    stroke(255)
    rect(X_pos, Y_pos, ball_size, ball_size)
    
def draw_left_paddle(Y_pos):
    fill(255)
    stroke(255)
    rect(0, Y_pos, paddle_width, paddle_height)
    

def draw_right_paddle(Y_pos):
    fill(255)
    stroke(255)
    rect(width-20, Y_pos, paddle_width , paddle_height)

def keyPressed():
    global step_size_left
    global step_size_right
    if key =='w':
        step_size_left = -2
    if key =='s':
        step_size_left = 2
    if key == 'i':
        step_size_right = -2
    if key == 'k': 
        step_size_right = 2

    
def repose():
    global ball_x
    global ball_y
    global ball_x_dir
    global ball_y_dir
    
    ball_x = width/2
    ball_y = int(random(50, height-50))
    outcomes = [True, False]
    ball_x_dir = outcomes[int(random(0, 2))]
    ball_y_dir = outcomes[int(random(0, 2))]


def draw():
  
    global step_size_left
    global step_size_right
    global ball_x 
    global left_y
    global right_y
    global ball_y
    global ball_size
    global ball_x_dir
    global ball_y_dir
    global paddle_width
    global paddle_height
    global scoreleft
    global scoreright
    
    background(0)
    if ball_x_dir == True: 
        ball_x += ball_speed
    else: 
        ball_x -= ball_speed
    if ball_x +ball_size >= width - paddle_width and ball_y <= right_y + paddle_height and ball_y >= right_y:
        ball_x_dir = False
    if ball_x < paddle_width and ball_y >= left_y and ball_y <= left_y + paddle_height: 
        ball_x_dir = True
    
    if ball_y_dir == True: 
        ball_y += ball_speed
    else: 
        ball_y -= ball_speed
    if ball_y +ball_size >= height:
        ball_y_dir = False
    if ball_y < 0: 
        ball_y_dir = True
        
    if ball_x > width:
        scoreleft += 1
        print ("left score is equal to " + str(scoreleft), "right score is equal to " + str(scoreright))
        repose()
           
    if ball_x < 0 : 
        scoreright += 1
        print ("left score is equal to " + str(scoreleft), "right score is equal to " + str(scoreright))
        repose()
        

        
        
    draw_ball(ball_x, ball_y)
    left_y += step_size_left
    right_y += step_size_right
    if left_y + paddle_height >= height: 
        left_y = height - paddle_height
    if right_y + paddle_height >= height: 
        right_y = height - paddle_height
    if left_y < 0: 
        left_y = 0 
    if right_y < 0:
        right_y = 0
    draw_left_paddle(left_y)
    draw_right_paddle(right_y)


    
