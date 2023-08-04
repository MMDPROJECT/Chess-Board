import pygame
import os
import board


pygame.display.set_caption("Board") #title name


display_board = board.Board()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                find_mouse = pygame.mouse.get_pos()
                display_board.find_piece(find_mouse)

        display_board.draw_color()
        display_board.set_pieces()

        

    
        pygame.display.update()
    
        
    
    pygame.quit()


if __name__ == "__main__":
    main()
