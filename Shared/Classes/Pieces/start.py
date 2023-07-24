import pygame
import os
import board


pygame.display.set_caption("Board") #title name

#set up image of pieces

#black
black_pawn = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_pdt60.png'))
black_rook = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_rdt60.png'))
black_king = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_qdt60.png'))
black_knight = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_ndt60.png'))
black_queen = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_kdt60.png'))
black_bishop = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_bdt60.png'))

#white
white_pawn = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_plt60.png'))
white_rook = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_rlt60.png'))
white_king = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_qlt60.png'))
white_knight = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_nlt60.png'))
white_queen = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_klt60.png'))
white_bishop = pygame.image.load(os.path.join('Shared/Classes/Image/Chess_blt60.png'))

display_board = board.Board()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        display_board.draw_color()   
        display_board.set_pieces()
        
    pygame.quit()


if __name__ == "__main__":
    main()
