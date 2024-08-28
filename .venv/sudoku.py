import pygame

WIDTH, HEIGHT = 600, 800
# Makes a window with WIDTH, HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 30

def draw_window():
    # Constantly fills window with white
    WIN.fill(WHITE)
    draw_grid()
    pygame.display.update()


def draw_grid():
    block_size = 30
    for x in range(0,WIDTH,block_size):
        for y in range(0,HEIGHT,block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)

def main():
    # Define clock object
    clock = pygame.time.Clock()
    run = True
    while run == True:
        # Implements FPS in run
        clock.tick(FPS)
        # For everything that happens
        for event in pygame.event.get():
            # If user quit program
            if event.type == pygame.QUIT:
                #End run
                run =  False
        # Constantly draws graph
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()