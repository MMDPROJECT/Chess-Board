import pygame
import os
import board


pygame.display.set_caption("Board") #title name
width, height = 512,512
window = pygame.display.set_mode((width, height))

display_board = board.Board()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                find_mouse = pygame.mouse.get_pos()
                #print(find_mouse[0]//64);print(find_mouse[1]//64)
                display_board.find_piece(find_mouse)

        display_board.draw_color(window)
        display_board.set_pieces(window)

        

    
        pygame.display.update()
    
        
    
    pygame.quit()


if __name__ == "__main__":
    main()
