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

bgImage = pygame.image.load("Snake_Game_IMG.jpg").convert()
bgImage = pygame.transform.smoothscale(bgImage, (size_x, size_y))

clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
navy = (0, 255, 255)
blue = (0, 0, 180)
black = (0, 0, 0)


# Snake class with body, eyes, and movement logic
class Snake:
    def __init__(self, x, y, size):
        self.size = size
        self.body = [[x, y]]
        self.eyes_r = [[x + 2, y + self.size // 2]]  # Right eye
        self.eyes_l = [[x + 14, y + self.size // 2]]  # Left eye
        self.direction = "DOWN"
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.direction != "LEFT":
                    self.speed_x, self.speed_y = 2, 0
                    self.direction = "RIGHT"
                elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                    self.speed_x, self.speed_y = -2, 0
                    self.direction = "LEFT"
                elif event.key == pygame.K_UP and self.direction != "DOWN":
                    self.speed_x, self.speed_y = 0, -2
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN and self.direction != "UP":
                    self.speed_x, self.speed_y = 0, 2
                    self.direction = "DOWN"

        # Update snake body
        head = [self.body[-1][0] + self.speed_x, self.body[-1][1] + self.speed_y]
        self.body.append(head)

        # Update eyes based on direction
        if self.direction == "LEFT":
            self.eyes_r = [[head[0] + self.size - 14, head[1] + 2]]
            self.eyes_l = [[head[0] + self.size - 14, head[1] + 14]]
        if self.direction == "RIGHT":
            self.eyes_r = [[head[0] + self.size // 2, head[1] + 2]]
            self.eyes_l = [[head[0] + self.size // 2, head[1] + 14]]
        if self.direction == "UP":
            self.eyes_r = [[head[0] + 14, head[1] + self.size - 14]]
            self.eyes_l = [[head[0] + 2, head[1] + self.size - 14]]
        if self.direction == "DOWN":
            self.eyes_r = [[head[0] + 2, head[1] + self.size // 2]]
            self.eyes_l = [[head[0] + 14, head[1] + self.size // 2]]

    def draw(self, surface):
        """
        for index, segment in enumerate(self.body):
            if index < 3 or index >= len(self.body) - 3:
                pygame.draw.circle(
                    surface,
                    green,
                    (segment[0] + self.size // 2, segment[1] + self.size // 2),
                    self.size // 2,
                )
            else:
                pygame.draw.rect(
                    surface, green, [segment[0], segment[1], self.size, self.size]
                )
        """
        for segment in self.body:
            pygame.draw.circle(surface, green,
                (segment[0] + self.size // 2, segment[1] + self.size // 2),
                self.size // 2,
            )
        
        plotEyes(surface, black, self.eyes_r, 4)
        plotEyes(surface, black, self.eyes_l, 4)


# Function to draw boundary
def draw_boundary(surface, color):
    pygame.draw.rect(surface, color, [15, 30, 5, 555])  # Left boundary
    pygame.draw.rect(surface, color, [15, 585, 575, 5])  # Bottom boundary
    pygame.draw.rect(surface, color, [590, 35, 5, 555])  # Right boundary
    pygame.draw.rect(surface, color, [20, 30, 575, 5])  # Top boundary


# Function to plot the eyes
def plotEyes(surface, color, eye_list, size):
    for x, y in eye_list:
        pygame.draw.rect(surface, color, [x, y, size, size])


# Function to display text on the screen
def showText(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# Function to get the high score from a file
def get_highscore():
    if not os.path.exists("highscore.txt"):
        return 0
    with open("highscore.txt", "r") as f:
        return int(f.read())


# Function to set the high score in a file
def set_highscore(hiscore):
    with open("highscore.txt", "w") as f:
        f.write(str(hiscore))


# Function to display the welcome screen
def wlcScreen():
    gameWindow.fill(white)
    showText("Welcome to Snakes", blue, 160, 250)
    showText("Press Space To Play", black, 130, 290)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


# Function to detect collisions with boundaries or the snake itself
def detect_collision(snake, snakeList):
    left_boundary = 15
    right_boundary = 590
    top_boundary = 30
    bottom_boundary = 585

    if (
        snake.body[-1][0] < left_boundary
        or snake.body[-1][0] > right_boundary
        or snake.body[-1][1] < top_boundary
        or snake.body[-1][1] > bottom_boundary
    ):
        return True

    if snake.body[-1] in snakeList[:-1]:
        return True

    return False


# Game loop
def gameLoop():
    snake = Snake(25, 40, 20)
    snakeLen = 1
    score = 0
    fps = 60

    apple_x, apple_y = random.randint(25, 570), random.randint(40, 570)
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
            snake.move()

            # Snake eats apple
            if (
                abs(snake.body[-1][0] - apple_x) < 10
                and abs(snake.body[-1][1] - apple_y) < 10
            ):
                score += 10
                apple_x, apple_y = random.randint(25, 570), random.randint(40, 570)
                snakeLen += snake.size
                if score > hiscore:
                    hiscore = score

            if len(snake.body) > snakeLen:
                del snake.body[0]

            gameWindow.fill(white)
            gameWindow.blit(bgImage, (0, 0))

            showText("Score: " + str(score), blue, 15, 0)
            showText("Hiscore: " + str(hiscore), blue, 390, 0)

            pygame.draw.rect(gameWindow, red, [apple_x, apple_y, 15, 15])

            snake.draw(gameWindow)

            if detect_collision(snake, snake.body):
                game_over = True

            draw_boundary(gameWindow, navy)
            pygame.display.update()
            clock.tick(fps)


# Initialize and run the game
wlcScreen()
gameLoop()
