from Particle import Particle

def setup():
    size(600, 600)
    global ps
    ps = init_ps(100)
    
    
def draw():
    background(255)
    for p in ps:
        p.display()
        p.move()
    connections()
    

#################################
####    F U N C T I O N S    ####   
################################# 
    
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

def connections():
    l = len(ps) - 1 
    for i in range(l/2 + 1):
        idx_0 = i
        idx_1 = l-i
        
        p0 = ps[idx_0]
        p1 = ps[idx_1]
        strokeWeight(2)
        stroke(0)
        line(p0.x, p0.y, p1.x, p1.y)
