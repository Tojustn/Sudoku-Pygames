import pygame
import unittest
import sudoku
import time


pygame.init()
WIDTH, HEIGHT = 660, 660
# Makes a window with WIDTH, HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (0,255,255)
FPS = 60
square = []
game = sudoku.Sudoku()
game.generate_numbers()
game.remove_nums(6)
number_grid = game.board
square_pos = {}
font = pygame.font.SysFont(None,size=50)
def draw_window():
    # Constantly fills window with white
    WIN.fill(WHITE)
    draw_grid()
    draw_number()

    # pygame.display.update always at bottom
    pygame.display.update()

def draw_number():
        for row in range(9):
            for col in range(9):
                output = number_grid[row][col]
                n_text = font.render(str(output),True,BLACK)

                # Position of number
                position = row * 70+40, col*70+40
    
                #Draws number on screen using text and position
                WIN.blit(n_text,position)



def draw_grid():
    # Draws outer rectangle, using rect object ( starts at 15,15) (630,630 length and width) (10, border size)
    outer_rect = pygame.Rect(15,15, 630, 630)
    pygame.draw.rect(WIN, BLACK,outer_rect,10)
    block_size = 70
    # Draws the inner grid rectangles
    for x in range(0,WIDTH-30,block_size):
        for y in range(0,HEIGHT-30,block_size):
            rect = pygame.Rect(x+15, y+15, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)

    #Draws the edge of each rectangle
    block_size = 210
    for x in range(0,WIDTH-30,block_size):
        for y in range(0,HEIGHT-30,block_size):
            rect = pygame.Rect(x+15, y+15, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 4)
def get_square():
    position = pygame.mouse.get_pos()
    position_list = []
    position_list = list(map(lambda x: x//70,position))
    return  position_list

# Shows user the row and column they chose
def click_display(row,col):
    block_size = 70
    srow = pygame.Surface((800,block_size))
    scol = pygame.Surface((block_size,800))    
    srow.set_alpha(50) 
    scol.set_alpha(50)              
    srow.fill(RED)
    scol.fill(RED)          
    WIN.blit(srow, (0,col*70+15))
    WIN.blit(scol, (row*70+15,0))
    pygame.display.update()
    time.sleep(.2)
def main():
    # Define clock object
    clock = pygame.time.Clock()
    run = True
    while run == True:
        down = False
        # Implements FPS in run
        clock.tick(FPS)
        # For everything that happens
        for event in pygame.event.get():
            
            # If user quit program
            if event.type == pygame.QUIT:
                #End run
                run =  False
            if event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square()
                click_display(square[0],square[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if game.valid_move(1, square[0], square[1]):
                        game.board[square[0]][square[1]] = 1
                elif event.key == pygame.K_2:
                    if game.valid_move(2, square[0], square[1]):
                        game.board[square[0]][square[1]] = 2
                elif event.key == pygame.K_3:
                    if game.valid_move(3, square[0], square[1]):
                        game.board[square[0]][square[1]] = 3
                elif event.key == pygame.K_4:
                    if game.valid_move(4, square[0], square[1]):
                        game.board[square[0]][square[1]] = 4
                elif event.key == pygame.K_5:
                    if game.valid_move(5, square[0], square[1]):
                        game.board[square[0]][square[1]] = 5
                elif event.key == pygame.K_6:
                    if game.valid_move(6, square[0], square[1]):
                        game.board[square[0]][square[1]] = 6
                elif event.key == pygame.K_7:
                    if game.valid_move(7, square[0], square[1]):
                        game.board[square[0]][square[1]] = 7
                elif event.key == pygame.K_8:
                    if game.valid_move(8, square[0], square[1]):
                        game.board[square[0]][square[1]] = 8
                elif event.key == pygame.K_9:
                    if game.valid_move(9, square[0], square[1]):
                        game.board[square[0]][square[1]] = 9
                if game.check_win():
                    win_text = font.render("WIN!!!!!!!!!!!",True,YELLOW)
                    WIN.blit(win_text,330,330)

        # Constantly draws graph
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()