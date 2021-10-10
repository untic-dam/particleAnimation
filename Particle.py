class Particle():

    def __init__(self, x, y, r, ax, ay):
        self.x = x
        self.y = y
        self.r = r
        self.ax = ax
        self.ay = ay
    
        self.clr = self.randomColor()
    
    def randomColor(self):
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
        return color(r, g, b)
   
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
            
        
    
    
