import pygame
from Player import PlayerClient
# creates the screen that the client uses
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client this is cool")

#this will hold the client number
clientNumber = 0

#this function will draw all the elements onto the control window
def redrawWindow(win,playClient):
    winColor = (255, 255, 255)
    win.fill(winColor)
    playClient.draw(win)
    pygame.display.update()



def main():
    # This is the game loop
    run = True
    player = PlayerClient(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        try:
            clock.tick(144)
            # when the user quits end the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            player.movePlayer()
            redrawWindow(win,player)
        except:
            print(f"The program failed to run")
            run = False


main()
