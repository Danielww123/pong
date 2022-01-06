def setup():
    size(800, 600) 
    background(0)
    print("greetings")
    draw_ball()
    draw_left_paddle()

def draw_ball():
    fill(255) 
    stroke(255)
    rect(0, 0, 8, 8)
    
def draw_left_paddle():
    fill(255)
    stroke(255)
    rect(0, 300, 20, 120)
