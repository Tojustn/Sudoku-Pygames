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
YELLOW = (255,255,0)
CYAN = (0,255,255)
FPS = 60
srow = pygame.Surface((800,70))
scol = pygame.Surface((70,800))

down = False
win = False
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
    row,col = get_square()
    WIN.blit(srow, (0,col*70+15))
    WIN.blit(scol, (row*70+15,0))

    if down:
        num_highlight()
    if win:
        win_text = font.render("WIN!!!!!!!!!!!",True,BLACK)
        win_rect = pygame.Rect(240,300,250,80)
        pygame.draw.rect(WIN, CYAN, win_rect)
        WIN.blit(win_text,(270,330))
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
def click_display():  
    srow.set_alpha(50) 
    scol.set_alpha(50)              
    srow.fill(RED)
    scol.fill(RED)          
def num_highlight():
    block_size = 70
    row, col = get_square()
    if row < 9 and col > -1 and col <9 and row > -1 and game.valid_move(1,row,col):
        highlight_rect = pygame.Rect(row*70+15, col*70+15,block_size,block_size)
        pygame.draw.rect(WIN, YELLOW,highlight_rect,9)
    

def main():
    # Define clock object
    clock = pygame.time.Clock()
    run = True
    while run == True:
        clock.tick(FPS)
        square = get_square()
        global win
        global down
        srow.set_alpha(0)
        scol.set_alpha(0)
        # Implements FPS in run
        # For everything that happens
        for event in pygame.event.get():
            row,col = get_square()
            WIN.blit(srow, (0,col*70+15))
            WIN.blit(scol, (row*70+15,0))
            # If user quit program
            if event.type == pygame.QUIT:
                #End run
                run =  False
            if event.type == pygame.MOUSEMOTION:
                click_display()
            if event.type == pygame.MOUSEBUTTONDOWN:
                down = True
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
            if down:
                num_highlight()
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
                elif event.key == pygame.K_SPACE:
                    game.solve()
                    draw_number()
                if game.check_win(number_grid):
                    win = True

        # Constantly draws graph
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()