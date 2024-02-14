from __future__ import annotations
import time

import pygame
import os

import board

pygame.display.set_caption("Board")  # title name
display_board = board.Board()
clock = pygame.time.Clock()  # Clock obj to control the frame rate


def main(player1, player2):
    run = True
    while run and not display_board.is_finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                find_mouse = pygame.mouse.get_pos()
                display_board.process_player_choice(find_mouse)

        ticks = pygame.time.get_ticks()
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = "{minutes:02d}:{seconds:02d}".format(minutes=minutes, seconds=seconds)
        pygame.display.set_caption(out)
        display_board.draw_empty_board()
        display_board.draw_pieces_on_board()
        pygame.display.update()
        clock.tick(60)

    time.sleep(10)
    pygame.quit()


if __name__ == "__main__":
    # TODO Undefined variables :/
    main(palyer1, player2)
