#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: January 8th, 2023
# This program is a space fighter game

import ugame
import stage

def game_scene():

    # the image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set background to image 0 in the image bank and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, 60)

    # set layers of sprites, they will show up in order
    game.layers = [ship] + [background]

    # render the sprites
    game.render_block()

    # game loop
    while True:
        pass # for now, this is a placeholder

if __name__ == "__main__":
    game_scene()