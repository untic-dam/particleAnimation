class Particle():

    def __init__(self):
        self.x = 100
        self.y = 100
        self.r = 10
        self.ax = 1
        self.ay = 1
   
    def display(self): 
        strokeWeight(self.r)
        stroke(0)
        point(self.x, self.y)
        
    def move(self):
        self.x += self.ax
        self.y += self.ay
    
    
