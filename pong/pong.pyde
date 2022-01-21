ball_x = 0
ball_y = 0
left_y = 0
right_y = 0
step_size = 6
paddle_height = 120
paddle_width = 20
ball_speed = 2
ball_size = 8
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
    global left_y
    global right_y
    global step_size
    if key =='w':
        left_y -= step_size
    if key =='s':
        left_y += step_size
    if key == 'i':
        right_y -= step_size
    if key == 'k': 
        right_y += step_size
    if left_y + paddle_height >= height: 
        left_y = height - paddle_height
    if right_y + paddle_height >= height: 
        right_y = height - paddle_height
    if left_y < 0: 
        left_y = 0 
    if right_y < 0:
        right_y = 0
    
        


def draw():
    left_sync = left_y
    right_sync = right_y
    global ball_x 
    global left_y
    global right_y
    global ball_y
    global ball_size
    global ball_x_dir
    global ball_y_dir
    global paddle_width
    global paddle_height
    background(0)
    if ball_x_dir == True: 
        ball_x += ball_speed
    else: 
        ball_x -= ball_speed
    if ball_x +ball_size >= width - paddle_width and ball_y <= right_sync + paddle_height and ball_y >= right_sync:
        ball_x_dir = False
    if ball_x < paddle_width and ball_y >= left_sync and ball_y <= left_sync + paddle_height: 
        ball_x_dir = True
    
    if ball_y_dir == True: 
        ball_y += ball_speed
    else: 
        ball_y -= ball_speed
    if ball_y +ball_size >= height:
        ball_y_dir = False
    if ball_y < 0: 
        ball_y_dir = True
        
    draw_ball(ball_x, ball_y)
    draw_left_paddle(left_sync)
    draw_right_paddle(right_sync)


    
