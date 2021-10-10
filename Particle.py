class Particle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.ax = 2
        self.ay = -3
        self.clr = color(12, 13, 100)
   
    def display(self): 
        strokeWeight(self.r)
        stroke(self.clr)
        point(self.x, self.y)
        
    def move(self):
        self.x += self.ax
        self.y += self.ay
        self.handleEdge()
        
    def handleEdge(self):
        if (self.x < 0) or (self.x > width) :
            self.ax = -self.ax
        if (self.y < 0) or (self.y > height) :
            self.ay = -self.ay
            
        
    
    
