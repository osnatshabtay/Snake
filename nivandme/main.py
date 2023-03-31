# TODO
# 1. game over when crossing snake body
# 2. 


import random
from time import sleep
import pygame
from board import Board
from snake import Snake
import pygame.time
from game_over import GameOver,display_game_over




EMPTY = (255, 255, 255)  # white
SNAKE = (0, 0, 0)  # black
FRUIT = (255, 0, 0)  # red
DIFFICULTY = 0.25 # sleep time (in seconds) between each snake movement
WIDTH = 600
ROWS = 15
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake")

    

def main():

    game_board = Board(ROWS, WIDTH)

    run = True  
    fruit_avaliable = False
    start_point = [random.randint(0, ROWS-1),random.randint(0, ROWS-1)]
    snake = Snake(start_point)

    move_direction = None 
    movment = {'up': snake.move_up, 'down': snake.move_down, 'left': snake.move_left, 'right': snake.move_right}
    empty_points_set = {(i, j) for i in range(ROWS) for j in range(ROWS)}

    while run:
        # update snake position        
        for point in snake.get_body(): 
            game_board.change_color(point[0],point[1],SNAKE)
            empty_points_set.discard(tuple(point))

        # check if snake ate the fruit
        if fruit_avaliable and snake.get_head() == random_fruit:
            new_point = snake.get_tail().copy()
            #----
            if new_point[1] + 1 < ROWS:
                new_point[1] += 1
            elif new_point[0] + 1 < ROWS:
                new_point[0] += 1
            else: 
                print('need to do')
                exit(1)                 
            
            #----
            snake.grow(new_point)

            print("--------------- ate fruit ---------------")
            print("snake -> ", snake.get_body())
            print("empty points -> ", empty_points_set)
            print("fruin -> ", random_fruit)
            for p in snake.get_body():
                if tuple(p) in empty_points_set:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ", p)

            fruit_avaliable = False

        # update fruit location - when snake eats the fruit
        if not fruit_avaliable:
            random_fruit = list(random.choice(list(empty_points_set)))
            empty_points_set.remove(tuple(random_fruit))
            print("--------------- genrating new fruit ---------------")
            print("snake -> ", snake.get_body())
            print("empty points -> ", empty_points_set)
            print("fruin -> ", random_fruit)
            for p in snake.get_body():
                if tuple(p) in empty_points_set:
                    print("!!!!!????????????????????????????????????????????/ ", p)

            game_board.change_color(random_fruit[0],random_fruit[1],FRUIT)
            fruit_avaliable = True

        
        # draw board
        game_board.draw(SCREEN)  



        try: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                

                elif event.type == pygame.KEYDOWN:
                    pressed_on_arrows = False

                    if event.key == pygame.K_UP and move_direction != 'down':
                        pressed_on_arrows = True
                        move_direction = 'up'

                    if event.key == pygame.K_DOWN and move_direction != 'up':
                        pressed_on_arrows = True
                        move_direction = 'down'

                    if event.key == pygame.K_LEFT and move_direction != 'right':
                        pressed_on_arrows = True
                        move_direction = 'left'

                    if event.key == pygame.K_RIGHT and move_direction != 'left':
                        pressed_on_arrows = True
                        move_direction = 'right' 
                        
                    if pressed_on_arrows:
                        empty_point = movment[move_direction]() # prev tail position of snake
                        game_board.change_color(empty_point[0],empty_point[1],EMPTY)
                        empty_points_set.add(tuple(empty_point))
                        snake.if_crossing()


        except GameOver as error:
            print(error)
            display_game_over(SCREEN,WIDTH)
            pygame.time.wait(3000)  # Pause for 3 seconds before quitting
            pygame.quit()
            exit(1)
        
                # move in continuity
        if move_direction != None:
            sleep(DIFFICULTY)
            empty_point = movment[move_direction]() # prev tail position of snake
            game_board.change_color(empty_point[0],empty_point[1],EMPTY)
            empty_points_set.add(tuple(empty_point))

            try:
                snake.if_crossing()

            except GameOver as error:
                print(error)
                display_game_over(SCREEN,WIDTH)
                pygame.time.wait(3000)  # Pause for 3 seconds before quitting
                pygame.quit()
                exit(1)
        

    pygame.quit()

main()