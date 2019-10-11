from tkinter import *
import time
import random

class Snake:
    ''''Class container all stuff from the snake object'''

    def __init__(self):
        '''Function to initiaize all the default variable
        needed for the snake

        Args:
        None

        Return:
        None
        '''

        self.shape = canvas.create_rectangle(0, 0, size, size, fill="black") # Snake square
        self.speedx = 25 # Default for snake
        self.dead = False
        self.speedy = 0
        self.active = True

        # Direction vars
        self.forward = False
        self.right = True
        self.left = False
        self.down = False

        # Stuff needed to calculate tail and stuff
        self.length = 0
        self.previoussnakes = []
        self.previoussnakes_objects = []

        self.apple = Apple()
        self.move_forward()

    def snake_update(self):
        '''Updates the snake field and calculates if the snake
        eats and apple or runs into a wall or runs into itself
        '''
        
        # For calculating apple and snake poss (and possible score up)
        pos = canvas.coords(self.shape) 
        pos2 = canvas.coords(self.apple.applelocation)

        # Check if the snake bites itself
        if self.length >= 1:
            if pos in self.previoussnakes[-(self.length+1):-1]:
                self.active = False
                self.snake_die()

        # Check if an apple is eaten
        if pos == pos2:
            self.apple.apple_eat()
            self.length += 1

        # Check if the snake runs into the wall
        if pos[2] > 500 or pos[2] < 25 or pos[3] > 500 or pos[3] < 25:
            self.active = False
            self.snake_die()

        # Load snake location and its tail
        canvas.move(self.shape, self.speedx, self.speedy)
        self.previoussnakes.append(list(canvas.coords(self.shape)))
        self.snake_2_update()

    def snake_2_update(self):
        '''Updates the tail of the snake'''


        if self.length >= 1:
            for item in self.previoussnakes_objects:
                canvas.delete(item)

            for i in self.previoussnakes[-(self.length+1):-1]:
                self.previoussnakes_objects.append(canvas.create_rectangle(i[0], i[1], i[2], i[3], fill="green"))

    def move_forward(self):
        '''Calculates the head of the snake and redoes this if
        the snake is still active'''

        if self.active:
            self.snake_update()
            tk.after(150, self.move_forward) 
            # Change ^ to change the speed of the whole game
            # Its defined in meliseconds

    def right_key(self, what_arg):
        '''If the snake isn't going left it can go right
        it will set the speed of the move on x to 25

        Args:
        what_arg: Value from thing that triggers this command
        we do nothing with the value'''

        if not self.left:
            self.right = True
            self.forward = False
            self.down = False
            self.speedx = 25
            self.speedy = 0  

    def left_key(self, what_arg):
        '''If the snake isn't going right it can go left
        it will set the speed of the move on x to -25

        Args:
        what_arg: Value from thing that triggers this command
        we do nothing with the value'''
        if not self.right:
            self.left = True
            self.forward = False
            self.down = False
            self.speedx = -25
            self.speedy = 0      

    def down_key(self, what_arg):
        '''If the snake isn't going up it can go down
        it will set the speed of the move on y to -25

        Args:
        what_arg: Value from thing that triggers this command
        we do nothing with the value'''

        if not self.forward: 
            self.left = False
            self.right = False
            self.down = True
            self.speedx = 0
            self.speedy = 25

    def up_key(self, what_arg):
        '''If the snake isn't going down it can go up
        it will set the speed of the move on y to 25

        Args:
        what_arg: Value from thing that triggers this command
        we do nothing with the value'''
        if not self.down:
            self.forward = True
            self.right = False
            self.left = False
            self.speedx = 0
            self.speedy = -25

    def snake_die(self):
        '''Function for killing the snake
        and showing the text of points and game over'''

        self.dead = True
        canvas.create_text(250,250,fill="black",font="Times 30 italic bold",
            text="You have died")
        canvas.create_text(250,300,fill="black",font="Times 20 italic bold",
            text=self.length)

class Apple:
    '''Class apple which initialy sets the apple
    and also able to eat it here'''

    def __init__(self):
        '''Sets apple so we can remove it in the recalled function without an error'''

        self.applelocation = canvas.create_rectangle(0, 0, size, size, fill="red")
        self.apple_place()

    def apple_place(self):
        '''Remvoes the apple
        and randomly sets it'''

        canvas.delete(self.applelocation)
        self.applelocation = canvas.create_oval(0, 0, size, size, fill="red")
        self.x = random.randrange(25, 475, 25)
        self.y = random.randrange(25, 475, 25)
        canvas.move(self.applelocation, self.x, self.y)

    def apple_eat(self):
        '''Eat apple function that replaces the apple
        in seperate function cuz in the future we will do more here'''

        self.apple_place()        

tk = Tk()
tk.title("Ralph's snake game")
canvas = Canvas(tk, width=500, height=500, bg="grey")
canvas.pack()
size = 25
snake = Snake()
tk.bind('<Left>', snake.left_key)
tk.bind('<Right>', snake.right_key)
tk.bind('<Up>', snake.up_key)
tk.bind('<Down>', snake.down_key)
tk.mainloop()