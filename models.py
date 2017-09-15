class Snake:
    MOVE_WAIT = 0.2

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
 
    def update(self, delta):
        self.wait_time += delta

        if self.wait_time < Snake.MOVE_WAIT:
            return

        if self.x > self.world.width:
            self.x = 0
        self.x += 16
        self.wait_time = 0
 
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.snake = Snake(self, width // 2, height // 2)
 
 
    def update(self, delta):
        self.snake.update(delta)