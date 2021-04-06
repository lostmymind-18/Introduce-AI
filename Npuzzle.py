import pygame
import math
import os
from collections import deque
pygame.init()
#Width of screen
WIDTH = 800
#set display window
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("N-PUZZLE - DEPTH-FIRST SEARCH")
#Set colour
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
#font = pygame.font.Font('freesansbold.ttf', 32)
def initialState(k):
    state = []
    a = 1
    for i in range(k):
        state.append([])
        if(i < k - 1):
            for j in range(k):
                state[i].append(a)
                a+=1
        elif i == k - 1:
            for j in range(k - 1):
                state[i].append(a)
                a+=1
            state[i].append(0)
    return state
#Get position of blank piece
def getPosBlank(grid):
    x = y = 0
    for row in grid:
        x = 0
        for piece in row:
            if piece == 0:
                return (x, y)
            x+=1
        y+=1
def move(state, action, k):
    x, y = getPosBlank(state)
    if action == "up":
        if y > 0:
            state[y][x], state[y - 1][x] = state[y - 1][x], state[y][x]
    if action == "down":
        if y < k - 1:
            state[y][x], state[y + 1][x] = state[y + 1][x], state[y][x]
    if action == "right":
        if x < k - 1:
            state[y][x], state[y][x + 1] = state[y][x + 1], state[y][x]
    if action == "left":
        if x > 0:
            state[y][x], state[y][x - 1] = state[y][x - 1], state[y][x]
    return state

def draw_grid(win, k, width):
	gap = width // k
	for i in range(k):
		pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
		for j in range(k):
			pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

def draw(win, width, k ,grid):
    gap = width // k
    fontSize = gap*3/4
    win.fill(WHITE)
    x = y = 0
    for row in grid:
        x = 0
        for piece in row:
            if piece == 0:
                pygame.draw.rect(win, GREY, (x*gap, y*gap, gap, gap))
            else:
                font = pygame.font.Font('freesansbold.ttf', int(fontSize))
                text = font.render(str(piece), True, BLACK, WHITE)
                textRect = text.get_rect(topleft=(x*gap+gap//10, y*gap+gap//10))
                win.blit(text, textRect)
                #pygame.draw.rect(win, WHITE, (x*gap, y*gap, gap, gap))
            x+=1
        y+=1
    draw_grid(win, k, width)
    pygame.display.update()

def getClickPos(pos, k, width):
    gap = width // k
    y, x = pos
    row = y // gap
    col = x // gap
    return row, gap


def main(win, width):
    run = False
    guide = False
    k = 0
    os.system("clear")
    print("Nice to see you, please enter the number of raws that you want to test:  ")
    while not run:
        try:
            k = int(input())
            run = True
        except:
            print("Please enter a number =.=: ")
        
        goalState = iniState = newState = initialState(k)
    while run:
        draw(win,width ,k, newState)
        if not guide: 
            print("Thank you, now you use Arrow buttons to change initial position: ")
            print("Please press Space button for the searching process")
            guide = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    newState = move(newState, "down", k)
                if event.key == pygame.K_DOWN:
                    newState = move(newState,"up", k)
                if event.key == pygame.K_RIGHT:
                    newState = move(newState,"left", k)
                if event.key == pygame.K_LEFT:
                    newState = move(newState,"right", k)
                if event.key == pygame.K_SPACE:
                    os.system("clear")
                    print("I'm looking for a solution...")
                    print("Please be a little bit patient.")
                    #ALGORITHM
    pygame.quit()
    print("bye bye")

main(WIN, WIDTH)