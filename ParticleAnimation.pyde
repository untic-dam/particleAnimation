from Particle import Particle

def setup():
    size(600, 600)
    global p
    p = Particle()
    
def draw():
    background(200, 120, 130)
    p.display()
    p.move()
