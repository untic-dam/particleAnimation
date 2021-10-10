from Particle import Particle

def setup():
    size(600, 600)
    global ps
    ps = init_ps(100)
    
def draw():
    background(200, 120, 130)
    for p in ps:
        p.display()
        p.move()
        
def init_ps(n):
    pss = []
    for i in range(n):
        x = random(0, width)
        y = random(0, height)
        r = random(5,20)
        ax = random(-3, 3)
        ay = random(-3, 3)
        p = Particle(x, y, r, ax, ay)
        pss.append(p)
        
    return pss
