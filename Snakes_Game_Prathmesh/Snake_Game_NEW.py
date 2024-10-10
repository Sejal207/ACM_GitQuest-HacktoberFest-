import pygame
import random
import os
from sys import exit

pygame.init()
pygame.mixer.init()

font = pygame.font.SysFont(None, 50)

# Game Window
size_x = 610
size_y = 610
gameWindow = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Snakes By Prathmesh")

bgImage = pygame.image.load("Snake_Game_IMG_2.jpg").convert()
bgImage = pygame.transform.smoothscale(bgImage, (size_x, size_y))

clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
navy = (0, 255, 255)
blue = (0, 0, 180)
black = (0, 0, 0)


# Game Welcome Screen
def wlcScreen():
    exit_screen = False
    while not exit_screen:
        gameWindow.fill(white)
        showText("Welcome To Snakes", black, 140, 280)
        showText("Press SpaceBar To Play", black, 110, 330)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                exit_screen = True
        pygame.display.update()
        clock.tick(60)


# Function to draw boundary
def draw_boundary(surface, color):
    pygame.draw.rect(surface, color, [15, 30, 5, 555])  # Left boundary
    pygame.draw.rect(surface, color, [15, 585, 575, 5])  # Bottom boundary
    pygame.draw.rect(surface, color, [590, 35, 5, 555])  # Right boundary
    pygame.draw.rect(surface, color, [20, 30, 575, 5])  # Top boundary


# Functions to handle file reading and writing
def get_highscore():
    if not os.path.exists("Highscore.txt"):
        with open("Highscore.txt", "w") as f:
            f.write("0")
    with open("Highscore.txt", "r") as f:
        return int(f.read())


def set_highscore(hiscore):
    with open("Highscore.txt", "w") as f:
        f.write(str(hiscore))


# Function to display text
def showText(text, color, x, y):
    screenScore = font.render(text, True, color)
    gameWindow.blit(screenScore, [x, y])


# Updated plotSnake function
def plotSnake(surface, snakeList, snakeSize, snakeColor, eyesListR, eyesListL):
    tail_indices = lambda length: (length - 1, length - 2, length - 3)

    for index, (x, y) in enumerate(snakeList):
        if index in (0, 1, 2):  # Draw the head as a circle
            pygame.draw.circle(
                surface,
                snakeColor,
                (x + snakeSize // 2, y + snakeSize // 2),
                snakeSize // 2,
            )
        elif index in tail_indices(len(snakeList)):  # Draw the tail as a circle
            pygame.draw.circle(
                surface,
                snakeColor,
                (x + snakeSize // 2, y + snakeSize // 2),
                snakeSize // 2,
            )
        else:  # Draw the body as squares
            pygame.draw.rect(surface, snakeColor, [x, y, snakeSize, snakeSize])

    # Plot eyes for the head
    plotEyes(surface, black, eyesListR, 4)
    plotEyes(surface, black, eyesListL, 4)


# Function to plot the right eye
def plotEyes(surface, color, List, size):
    for x, y in List:
        pygame.draw.rect(surface, color, [x, y, size, size])


# Function to handle player input
def handle_input(speed_x, speed_y, a, b, snake_x, snake_y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                return 2, 0, snake_x + b, snake_x + b, snake_y + a, snake_y + b
            if event.key == pygame.K_LEFT:
                return -2, 0, snake_x + a, snake_x + a, snake_y + a, snake_y + b
            if event.key == pygame.K_UP:
                return 0, -2, snake_x + a, snake_x + b, snake_y + a, snake_y + a
            if event.key == pygame.K_DOWN:
                return 0, 2, snake_x + a, snake_x + b, snake_y + b, snake_y + b
            if event.key == pygame.K_TAB:
                return adjust_speed(speed_x, speed_y)
    return speed_x, speed_y, None, None, None, None


# Function to adjust speed for 'Tab' key
def adjust_speed(speed_x, speed_y):
    if speed_x > 1:
        speed_x -= 0.2
    elif speed_x < -1:
        speed_x += 0.2
    if speed_y > 1:
        speed_y -= 0.2
    elif speed_y < -1:
        speed_y += 0.2
    return speed_x, speed_y


# Function to detect collisions with boundaries or the snake itself
def detect_collision(snake_x, snake_y, snakeList):
    # Define boundary limits
    left_boundary = 15
    right_boundary = 590
    top_boundary = 30
    bottom_boundary = 585

    # Check if the snake hits the boundaries
    if (
        snake_x < left_boundary
        or snake_x > right_boundary
        or snake_y < top_boundary
        or snake_y > bottom_boundary
    ):
        return True

    # Check if the snake collides with itself
    if [snake_x, snake_y] in snakeList[:-1]:
        return True

    return False


# Game loop logic
def gameLoop():
    snake_x, snake_y = 25, 40
    snakeSize, snakeLen, score, fps = 20, 1, 0, 60
    apple_x, apple_y = random.randint(25, 570), random.randint(40, 570)
    snakeList, eyesList1, eyesList2 = [], [], []
    speed_x, speed_y = 0, 0
    a, b = 2, 14
    snake_x_1, snake_x_2 = snake_x + a, snake_x + b
    snake_y_1, snake_y_2 = snake_y + b, snake_y + b
    eyesList1.append([snake_x_1, snake_y_1])
    eyesList2.append([snake_x_2, snake_y_2])

    hiscore = get_highscore()

    game_over = False
    while True:
        if game_over:
            set_highscore(hiscore)
            gameWindow.fill(navy)
            showText("Score: " + str(score), blue, 15, 0)
            showText("Hiscore: " + str(hiscore), blue, 390, 0)
            showText("Game Over", red, 200, 300)
            showText("Press Enter To Continue", black, 100, 355)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameLoop()
            pygame.display.update()
        else:
            speed_x, speed_y, new_x1, new_x2, new_y1, new_y2 = handle_input(
                speed_x, speed_y, a, b, snake_x, snake_y
            )
            if new_x1 and new_x2:
                snake_x_1, snake_x_2 = new_x1, new_x2
                snake_y_1, snake_y_2 = new_y1, new_y2

            snake_x += speed_x
            snake_y += speed_y
            snake_x_1 += speed_x
            snake_y_1 += speed_y
            snake_x_2 += speed_x
            snake_y_2 += speed_y

            gameWindow.fill(white)
            gameWindow.blit(bgImage, (0, 0))

            showText("Score: " + str(score), blue, 15, 0)
            showText("Hiscore: " + str(hiscore), blue, 390, 0)

            pygame.draw.rect(gameWindow, red, [apple_x, apple_y, 15, 15])

            # Update snake and eyes
            head = [snake_x, snake_y]
            eyes1, eyes2 = [snake_x_1, snake_y_1], [snake_x_2, snake_y_2]
            snakeList.append(head)
            eyesList1.append(eyes1)
            eyesList2.append(eyes2)

            # Snake eats apple
            if abs(snake_x - apple_x) < 10 and abs(snake_y - apple_y) < 10:
                score += 10
                apple_x, apple_y = random.randint(25, 570), random.randint(40, 570)
                snakeLen += snakeSize
                if score > hiscore:
                    hiscore = score

            # Keep snake length in check
            if len(snakeList) > snakeLen:
                del snakeList[0]
            if len(eyesList1) > 1 and len(eyesList2) > 1:
                del eyesList1[0]
                del eyesList2[0]

            # Plot the snake and eyes using the updated plotSnake function
            plotSnake(gameWindow, snakeList, snakeSize, green, eyesList1, eyesList2)

            # Check collision with boundaries or itself using the new function
            if detect_collision(snake_x, snake_y, snakeList):
                game_over = True

            draw_boundary(gameWindow, navy)
            pygame.display.update()
            clock.tick(fps)


wlcScreen()
gameLoop()
