from game_over import GameOver

ROWS = 15
class Snake:
    def __init__(self,start):
        self.snake_body = []
        self.snake_body.append(start)

    def move_right(self): 
        new_point = [self.snake_body[0][0],(self.snake_body[0][1]+1)%ROWS] #one step in y axis  
        self.snake_body.insert(0,new_point) 
        return self.snake_body.pop()
    
    def move_left(self):
        new_point = [self.snake_body[0][0],(self.snake_body[0][1]-1)%ROWS] #one step in y axis  
        self.snake_body.insert(0,new_point)
        return self.snake_body.pop()
    
    def move_up(self):
        new_point = [(self.snake_body[0][0]-1)%ROWS,self.snake_body[0][1]] #one step in x axis  
        self.snake_body.insert(0,new_point) 
        return self.snake_body.pop()
       
    def move_down(self):
        new_point = [(self.snake_body[0][0]+1)%ROWS,self.snake_body[0][1]] #one step in x axis  
        self.snake_body.insert(0,new_point) 
        return self.snake_body.pop()

    def grow(self,point):
        self.snake_body.append(point)

    def get_body(self):
        return self.snake_body
    
    def get_head(self):
        return self.snake_body[0]
    
    def get_tail(self):
        return self.snake_body[len(self.snake_body) - 1]
    
    def if_crossing (self):
        head = self.snake_body[0]
        if head in self.snake_body[1:]:
            raise GameOver("The snake crosses itself")