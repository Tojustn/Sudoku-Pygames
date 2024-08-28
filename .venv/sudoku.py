import pygame

WIDTH, HEIGHT = 600, 800
# Makes a window with WIDTH, HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    run = True
    while run == True:
        # For everything that happens
        for event in pygame.event.get():
            # If user quit program
            if event.type == pygame.QUIT:
                #End run
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()