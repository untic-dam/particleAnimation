from Particle import Particle
from delaunay import Delaunay

def setup():
    size(600, 600)
    global ps
    ps = init_ps(6)
    
    
    
def draw():
    background(255)
    for p in ps:
        #p.display()
        p.move()
    #connection_2points()
    #connection_3points()
    connection_mesh()
    

#################################
####    F U N C T I O N S    ####   
################################# 
    
def init_ps(n):
    ps_s = []
    for i in range(n):
        x = random(0, width)
        y = random(0, height)
        r = random(5,20)
        ax = random(-3, 3)
        ay = random(-3, 3)
        p = Particle(x, y, r, ax, ay)
        ps_s.append(p)
        
    return ps_s

def connection_2points():
    tot = len(ps) - 1 #total number of particles
    for i in range(tot/2 + 1):
        #first and last idx of particle
        idx_0 = i
        idx_1 = tot-i
        
        #first and last particle
        p0 = ps[idx_0]
        p1 = ps[idx_1]
        
        #draw connections
        strokeWeight(2)
        stroke(0)
        line(p0.x, p0.y, p1.x, p1.y)

def connection_3points():
    n_triangle = int(len(ps)/3)
    cnt = 0
    tgl = []
    for i in range(len(ps)):
        tgl.append(i)
        cnt += 1
        if cnt == 3:
            display_triangle(tgl)
            cnt = 0
            tgl = []

def connection_mesh():
    tot = len(ps)
    n_triangle = tot - 2

    for i in range(n_triangle):
        i0 = i
        i1 = i + 1
        i2 = i + 2
        tgl = [i0, i1, i2]
        display_triangle(tgl)
    
def connection_mesh_short():
    pass

def display_triangle(tgl):
    p0 = ps[tgl[0]]
    p1 = ps[tgl[1]]
    p2 = ps[tgl[2]]
    
    fill(p0.clr, 50)
    stroke(0)
    strokeWeight(1)
    triangle(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y)
    

        
