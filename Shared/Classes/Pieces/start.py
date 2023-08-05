from __future__ import annotations

import pygame
import os

import board

pygame.display.set_caption("Board") #title name
display_board = board.Board()
clock = pygame.time.Clock() # Clock obj to control the frame rate

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                find_mouse = pygame.mouse.get_pos()
                display_board.find_piece(find_mouse)

        display_board.draw_empty_board()
        display_board.draw_pieces_on_board()
        pygame.display.update()
        clock.tick(25)
    
        
    
    pygame.quit()


if __name__ == "__main__":
    main()
