# Name: Ashwin Lanka
# ComputingID: xng3hg
# Partner Name: Krish Dhansinghani
# Partner ComputingID: bje9jj

import gamebox
import pygame
import random
#fourth requirement
    #small enough window- we will make the window length 400 x 400
camera = gamebox.Camera(500,400)

gameon = False
initialwalllocationX = 20
initialwalllocationY = 0
wallsX = [gamebox.from_color(initialwalllocationX,300, "white", 1, 1000000)]
wallsY = [gamebox.from_color(400, initialwalllocationY, "white", 1, 1000000)]
x = 230
y = 250
xchange = 0
ychange = 0
applex =random.randrange(10,390,20)
appley = random.randrange(10,390,20)
snake = [(x, y)]

enemyx = random.randrange(10,snake[0][0],20)
enemyy = random.randrange(10,snake[0][1],20)
enemy = [(gamebox.from_color(enemyx, enemyy, "blue", 20, 20))]
score = len(snake)
newscore = 0
healthbar = 1
def tick(keys):
    global initialwalllocationX
    global initialwalllocationY
    global x
    global y
    global xchange
    global ychange
    global applex
    global appley
    global snake
    global gameon
    global score
    global newscore
    global healthbar
    global enemyy,enemyx
    global enemy
    # first requirement
        # user input - we will use the up, down, and side arrow keys to move the snake so that it can eat objects to eventually have it grow

    if pygame.K_SPACE in keys:
        gameon = True
    if pygame.K_LEFT in keys and (snake[0][0]%20 == 10 and snake[0][1]%20 == 10):
        if xchange != 20:
            xchange = -20
        ychange = 0
    if pygame.K_RIGHT in keys and (snake[0][0]%20 == 10 and snake[0][1]%20 == 10):
        if xchange != -20:
            xchange = 20
        ychange = 0
    if pygame.K_UP in keys and (snake[0][0]%20 == 10 and snake[0][1]%20 == 10):
        if ychange != 20:
            ychange = -20
        xchange = 0
    if pygame.K_DOWN in keys and (snake[0][0]%20 == 10 and snake[0][1]%20 == 10):
        if ychange != -20:
            ychange = 20
        xchange = 0

    if gameon == True:
        # fifth requirement
        # graphcis - we will import images from google to add to our file, ie instead of cubes we will use snake and apple images
        # has not been done yet
        camera.clear('dark green')
        camera.draw(gamebox.from_image(applex, appley, "https://docs.replit.com/images/tutorials/21-snake-kaboom/pizza.png"))

        for z in enemy:
            camera.draw(z)
            if z.x >0 and z.x <400:
                z.x +=5
            if z.x>=400:
                z.x = 1
            if z.x -17 <= snake[0][0] <= z.x +17 and z.y -17 <= snake[0][1] <= z.y +17:
                healthbar -=1

        for newx, newy in snake:
            camera.draw(gamebox.from_image(newx, newy, "https://docs.replit.com/images/tutorials/21-snake-kaboom/snake-skin.png"))
        for wall in range(len(wallsX)):
            if wall == len(wallsX) - 1:
                initialwalllocationX += 20
                wallsX.append(gamebox.from_color(initialwalllocationX, 200, "white", 1, 1000000))
                wall = len(wallsX) - 2
            camera.draw(wallsX[wall])
        for wall in range(len(wallsY)):
            if wall == len(wallsY) - 1:
                initialwalllocationY += 20
                wallsY.append(gamebox.from_color(40, initialwalllocationY, "white", 1000000, 1))
                wall = len(wallsY) - 2
            camera.draw(wallsY[wall])
        camera.draw(gamebox.from_color(450,0,"black",100,800))
        camera.draw(gamebox.from_text(450,25,"Score:"+ str(score),30,"purple"))
        camera.draw(gamebox.from_text(450, 100, "HealthBar", 30, "Green"))
        if healthbar >= 1:
            camera.draw(gamebox.from_color(450,150,"green",70,20))
        x+=xchange
        y+=ychange
        snake.append((x,y))
        if (x-15 <=applex <= x+15 and y-15<=appley <= y+15):
            while (x-15 <=applex <= x+15 and y-15<=appley <= y+15):
                applex = random.randrange(10,390,20)
                appley = random.randrange(10,390,20)
                score +=1
                enemy.pop()
                enemyx = random.randrange(10,390,20)
                enemyy = random.randrange(10,390,20)
                enemy.append((gamebox.from_color(enemyx, enemyy, "blue", 20, 20)))

        else:
            del snake[0]

        if x <0 or x>400 or y <0 or y >400:
            healthbar -=1
            x = 230
            y = 250
            xchange = 0
            ychange = 0
            print(healthbar)

        if healthbar !=1 and healthbar>=0:

            camera.draw(gamebox.from_color(432.2,150,"red",35,20))

        if healthbar < 0:
            healthbar = 1
            newscore = score
            gameon = False
        if (snake[0][0],snake[0][1]) in snake[1:][1:] and len(snake)>2:
            healthbar -=1

    # third requirement
        # gameover- once the snake hits the game will revert back to the start screen and say "Your score was ____, press Space Key to Play"
    # second requirement
        #   start screen - we will start the game running with a screen that has a statement "Press Space Key to Play" and underneath
        # it will list what keys move the snake, how to grow the snake, and how to avoid a game-over situation(not hitting the walls)

    else:
        camera.clear("black")
        camera.draw(gamebox.from_text(250, 120, "Press Space to Play", 40, "Purple"))
        camera.draw(gamebox.from_text(250, 160, "Rules to Play", 40, "Pink"))
        camera.draw(gamebox.from_text(250, 180, "1. Use the arrows to move the snake in a direction", 20, "Pink"))
        camera.draw(gamebox.from_text(250, 200, "2.Avoid the edges of the screen", 20, "Pink"))
        camera.draw(gamebox.from_text(250, 220, "3.don't let the snake hit itself", 20, "Pink"))
        camera.draw(gamebox.from_text(250, 240, "4.Eat the pizza slices to grow the snake", 20, "Pink"))
        camera.draw(gamebox.from_text(250,60, "Your Latest Score: " + str(newscore),40, "Pink"))
        # drawing the latest score does not appear to work because it looks like everything in this "else" statement
        #is working at the same time and I don't know how to fix this.
        x = 230
        y = 250
        xchange = 0
        ychange = 0
        applex = random.randrange(10, 390, 20)
        appley = random.randrange(10, 390, 20)
        snake = [(x, y)]
        score = len(snake)
        enemyx =random.randrange(10, 390, 20)
        enemyy = random.randrange(10, 390, 20)

    camera.display()

#first optional
    #enemies - These are the blue squares that move on their own. If the snake touches them then the healthbar will lose a life
#second optional
    #restart from gameover - returns the user back to the start screen so they can press space to restart the game and play again.
#third optional
    #collectibles - these will be apples that the snake can eat to increase the snakes size
#fourth optional
    #healthbar- the snake will have 1 hitpoint, essentially 2 lives. It will be displayed as a bar at the top of the screen. If the snake hits the
    #wall once then the health bar will decrease in size by half and the health bar will go to 0. If the snake has a reduction again then the game will be over.
ticks_per_second = 10

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)



