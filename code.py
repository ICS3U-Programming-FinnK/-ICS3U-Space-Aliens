#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: January 8th, 2023
# This program is a space fighter game

import ugame
import stage
import time
import random
import constants


# this is the splash scene function
def splash_scene():

    #coin sound effect
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # the image banks for CircuitPython menu
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set background to image 0 in the image bank and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y )

    # create a stage for the background to show up on
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y )

    # used this program to split the image into tile: 

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white



    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white



    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white



    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)

    # set layers of sprites, they will show up in order
    game.layers = [background]

    # render the sprites
    game.render_block()

    # game loop
    while True:
        #wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

# this is the menu scene function 
def menu_scene():

    # the image banks for CircuitPython menu
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add the text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("SpaceFighter")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START!")
    text.append(text2)

    # set background to image 0 in the image bank and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y )

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)

    # set layers of sprites, they will show up in order
    game.layers = text + [background]

    # render the sprites
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # redraw the sprites
        game.tick()

# this is the game scene function
def game_scene():

    # the image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # the buttons to keep information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # sound effects while shooting
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set background to image 0 in the image bank and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y )

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
            
    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
    alien = stage.Sprite(image_bank_sprites, 9,
                         int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                         16)

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)

    # set layers of sprites, they will show up in order
    game.layers = [ship] + [alien] + [background]

    # render the sprites
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # a button to fire the ship
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        
        # b button
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                 ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0: 
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
           
        # update game logic
        # play the pew sound effect when A is pressed

        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw the sprites
        game.render_sprites([ship] + [alien])
        game.tick()

if __name__ == "__main__":
    menu_scene()