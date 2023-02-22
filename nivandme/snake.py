class Snake:
    def __init__(self,start):
        self.snake_body = []
        self.snake_body.append(start)

    def move_up(self):
        new_point = (self.snake_body[0][0],self.snake_body[0][1]+1) #one step in y axis  
        self.snake_body.insert(0,new_point) 
        self.snake_body.pop()
    
    def move_down(self):
        new_point = (self.snake_body[0][0],self.snake_body[0][1]-1) #one step in y axis  
        self.snake_body.insert(0,new_point) 
        self.snake_body.pop()
    
    def move_left(self):
        new_point = (self.snake_body[0][0]-1,self.snake_body[0][1]) #one step in x axis  
        self.snake_body.insert(0,new_point) 
        self.snake_body.pop()
       
        
    def move_right(self):
        new_point = (self.snake_body[0][0]+1,self.snake_body[0][1]) #one step in x axis  
        self.snake_body.insert(0,new_point) 
        self.snake_body.pop()

    
    def grow(self,point):
        new_point = (self.snake_body[0][0]+1,self.snake_body[0][1]) #one step in x axis  
        self.snake_body.insert(0,new_point)

    def get_body(self):
        return self.snake_body