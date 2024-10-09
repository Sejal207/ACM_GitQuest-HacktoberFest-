#include <stdio.h>
#include <conio.h>  // For _kbhit() and _getch() on Windows
#include <stdlib.h> // For rand() and srand()
#include <windows.h> // For Sleep()

// Define game boundaries and variables
int width = 20, height = 20;
int x, y, fruitX, fruitY, score;
int tailX[100], tailY[100];
int nTail;
int gameOver;
enum eDirection { STOP = 0, LEFT, RIGHT, UP, DOWN };
enum eDirection dir;

void Setup() {
    gameOver = 0;
    dir = STOP;
    x = width / 2;
    y = height / 2;
    fruitX = rand() % width;
    fruitY = rand() % height;
    score = 0;
}

void Draw() {
    system("cls");  // Clear the screen

    // Draw the top boundary
    for (int i = 0; i < width + 2; i++)
        printf("#");
    printf("\n");

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (j == 0)
                printf("#");  // Draw left boundary

            if (i == y && j == x)
                printf("O");  // Draw snake head
            else if (i == fruitY && j == fruitX)
                printf("F");  // Draw fruit
            else {
                int isTail = 0;
                for (int k = 0; k < nTail; k++) {
                    if (tailX[k] == j && tailY[k] == i) {
                        printf("o");  // Draw snake tail
                        isTail = 1;
                    }
                }
                if (!isTail)
                    printf(" ");  // Empty space
            }

            if (j == width - 1)
                printf("#");  // Draw right boundary
        }
        printf("\n");
    }

    // Draw the bottom boundary
    for (int i = 0; i < width + 2; i++)
        printf("#");
    printf("\n");

    printf("Score: %d\n", score);
}

void Input() {
    if (_kbhit()) {  // Check if a key is pressed
        switch (_getch()) {
            case 'a':
                dir = LEFT;
                break;
            case 'd':
                dir = RIGHT;
                break;
            case 'w':
                dir = UP;
                break;
            case 's':
                dir = DOWN;
                break;
            case 'x':
                gameOver = 1;
                break;
        }
    }
}

void Logic() {
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y;

    // Move the tail
    for (int i = 1; i < nTail; i++) {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    // Move the snake
    switch (dir) {
        case LEFT:
            x--;
            break;
        case RIGHT:
            x++;
            break;
        case UP:
            y--;
            break;
        case DOWN:
            y++;
            break;
        default:
            break;
    }

    // Check if snake hits the boundaries
    if (x >= width || x < 0 || y >= height || y < 0)
        gameOver = 1;

    // Check if snake bites itself
    for (int i = 0; i < nTail; i++) {
        if (tailX[i] == x && tailY[i] == y)
            gameOver = 1;
    }

    // Check if snake eats the fruit
    if (x == fruitX && y == fruitY) {
        score += 10;
        fruitX = rand() % width;
        fruitY = rand() % height;
        nTail++;  // Increase the size of the snake
    }
}

int main() {
    Setup();

    while (!gameOver) {
        Draw();
        Input();
        Logic();
        Sleep(100);  // Delay for 100 milliseconds
    }

    return 0;
}
