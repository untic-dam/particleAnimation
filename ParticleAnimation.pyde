xg = 0
yg = 0

def setup():
    size(600, 600)
    global xg, yg
    xg = width/2
    yg = height/2
    
def draw():
    background(200, 120, 130)
    global xg, yg
    display(xg, yg, 100)
    move(1, 3)
    

def display(x, y, r):
    strokeWeight(r)
    stroke(0)
    point(x, y)

def move(ax, ay):
    global xg, yg
    xg += ax
    yg += ay
