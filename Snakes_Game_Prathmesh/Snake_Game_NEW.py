import pygame
import random
import os
from sys import exit

pygame.init()
pygame.mixer.init()

# Constants
FONT_SIZE = 50
WINDOW_SIZE = (610, 610)
BG_IMAGE_PATH = 'Snake_Game_IMG.jpg'
HIT_SOUND_PATH = 'Hit.mp3'
BG_MUSIC_PATH = 'Nagin.mp3'
HISCORE_FILE = "Highscore.txt"
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
NAVY = (0, 255, 255)
BLUE = (0, 0, 180)
BLACK = (0, 0, 0)
SNAKE_SIZE = 20
APPLE_SIZE = 15
EYE_SIZE = 4
EYE_OFFSET_X = 2
EYE_OFFSET_Y = 14
FPS = 60

# Initialize
font = pygame.font.SysFont(None, FONT_SIZE)
game_window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snakes By Prathmesh')
bg_image = pygame.image.load(BG_IMAGE_PATH)
bg_image = pygame.transform.scale(bg_image, WINDOW_SIZE).convert_alpha()
clock = pygame.time.Clock()


def show_text(text, color, x, y):
    screen_score = font.render(text, True, color)
    game_window.blit(screen_score, [x, y])


def plot_snake(surface, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(surface, color, [x, y, snake_size, snake_size])


def plot_eyes(surface, color, head_x, head_y, direction):
    if direction == "RIGHT":
        eye1 = (head_x + EYE_OFFSET_X, head_y + EYE_OFFSET_Y)
        eye2 = (head_x + EYE_OFFSET_X + SNAKE_SIZE // 2, head_y + EYE_OFFSET_Y)
    elif direction == "LEFT":
        eye1 = (head_x + EYE_OFFSET_X - SNAKE_SIZE // 2, head_y + EYE_OFFSET_Y)
        eye2 = (head_x + EYE_OFFSET_X - SNAKE_SIZE, head_y + EYE_OFFSET_Y)
    elif direction == "UP":
        eye1 = (head_x + EYE_OFFSET_X, head_y + EYE_OFFSET_Y - SNAKE_SIZE // 2)
        eye2 = (head_x + EYE_OFFSET_X + SNAKE_SIZE // 2, head_y + EYE_OFFSET_Y - SNAKE_SIZE // 2)
    else:  # DOWN
        eye1 = (head_x + EYE_OFFSET_X, head_y + EYE_OFFSET_Y)
        eye2 = (head_x + EYE_OFFSET_X + SNAKE_SIZE // 2, head_y + EYE_OFFSET_Y)
    pygame.draw.rect(surface, color, [eye1[0], eye1[1], EYE_SIZE, EYE_SIZE])
    pygame.draw.rect(surface, color, [eye2[0], eye2[1], EYE_SIZE, EYE_SIZE])


def welcome_screen():
    exit_screen = False
    while not exit_screen:
        game_window.fill(WHITE)
        show_text("Welcome To Snakes", BLACK, 140, 280)
        show_text("Press SpaceBar To Play", BLACK, 110, 330)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_screen = True
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                exit_screen = True
        pygame.display.update()
        clock.tick(FPS)


def load_hiscore():
    if not os.path.exists(HISCORE_FILE):
        with open(HISCORE_FILE, "w") as f:
            f.write("0")
    with open(HISCORE_FILE, "r") as f:
        return int(f.read())


def save_hiscore(hiscore):
    with open(HISCORE_FILE, "w") as f:
        f.write(str(hiscore))


def reset_game_state():
    return {
        'snake_x': 25,
        'snake_y': 40,
        'snake_list': [],
        'snake_len': 1,
        'speed_x': 0,
        'speed_y': 0,
        'score': 0,
        'apple_x': random.randint(25, 570),
        'apple_y': random.randint(40, 570),
        'direction': "RIGHT",
        'game_over': False
    }


def game_loop():
    state = reset_game_state()
    hiscore = load_hiscore()

    while True:
        if state['game_over']:
            save_hiscore(hiscore)
            game_window.fill(NAVY)
            show_text(f"Score: {state['score']}", BLUE, 15, 0)
            show_text(f"Hiscore: {hiscore}", BLUE, 390, 0)
            show_text("Game Over", RED, 200, 300)
            show_text("Press Enter To Continue", BLACK, 100, 355)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    state = reset_game_state()
            pygame.display.update()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and state['speed_x'] == 0:
                    state['speed_x'] = 2
                    state['speed_y'] = 0
                    state['direction'] = "RIGHT"
                if event.key == pygame.K_LEFT and state['speed_x'] == 0:
                    state['speed_x'] = -2
                    state['speed_y'] = 0
                    state['direction'] = "LEFT"
                if event.key == pygame.K_UP and state['speed_y'] == 0:
                    state['speed_x'] = 0
                    state['speed_y'] = -2
                    state['direction'] = "UP"
                if event.key == pygame.K_DOWN and state['speed_y'] == 0:
                    state['speed_x'] = 0
                    state['speed_y'] = 2
                    state['direction'] = "DOWN"
                if event.key == pygame.K_TAB:
                    if state['speed_x'] != 0:
                        state['speed_x'] = max(min(state['speed_x'] * 0.8, 2), -2)
                    if state['speed_y'] != 0:
                        state['speed_y'] = max(min(state['speed_y'] * 0.8, 2), -2)

        # Apple Collision
        if abs(state['snake_x'] - state['apple_x']) < 10 and abs(state['snake_y'] - state['apple_y']) < 10:
            state['score'] += 10
            state['apple_x'] = random.randint(25, 570)
            state['apple_y'] = random.randint(40, 570)
            state['snake_len'] += SNAKE_SIZE
            if state['score'] > hiscore:
                hiscore = state['score']

        # Update Snake Position
        state['snake_x'] += state['speed_x']
        state['snake_y'] += state['speed_y']

        head = [state['snake_x'], state['snake_y']]
        state['snake_list'].append(head)
        if len(state['snake_list']) > state['snake_len']:
            del state['snake_list'][0]

        # Collision with itself
        if head in state['snake_list'][:-1]:
            pygame.mixer.music.load(HIT_SOUND_PATH)
            pygame.mixer.music.play()
            state['game_over'] = True

        # Collision with boundaries
        if state['snake_x'] < 20 or state['snake_x'] + SNAKE_SIZE >= 590 or state['snake_y'] < 35 or state[
            'snake_y'] + SNAKE_SIZE >= 585:
            pygame.mixer.music.load(HIT_SOUND_PATH)
            pygame.mixer.music.play()
            state['game_over'] = True

        game_window.fill(WHITE)
        game_window.blit(bg_image, (0, 0))
        show_text(f"Score: {state['score']}", BLUE, 15, 0)
        show_text(f"Hiscore: {hiscore}", BLUE, 390, 0)
        pygame.draw.rect(game_window, RED, [state['apple_x'], state['apple_y'], APPLE_SIZE, APPLE_SIZE])

        plot_snake(game_window, GREEN, state['snake_list'], SNAKE_SIZE)

        pygame.draw.rect(game_window, NAVY, [15, 30, 5, 555])
        pygame.draw.rect(game_window, NAVY, [15, 585, 575, 5])
        pygame.draw.rect(game_window, NAVY, [590, 35, 5, 555])
        pygame.draw.rect(game_window, NAVY, [20, 30, 575, 5])

        pygame.display.update()
        clock.tick(FPS)


welcome_screen()
pygame.mixer.music.load(BG_MUSIC_PATH)
pygame.mixer.music.play(-1)
game_loop()
pygame.quit()
exit()
