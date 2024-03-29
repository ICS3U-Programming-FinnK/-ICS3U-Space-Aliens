#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: January 8th, 2023
# This program is a space fighter game

import ugame
import stage
import time
import random
import supervisor
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

    # the image banks for CircuitPython menu scene
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # menu scene text
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(10, 10)
    text1.text("Kitor Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(50, 30)
    text2.text("PRESENTS")
    text.append(text2)

    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(15, 50)
    text3.text("SpaceFighter for")
    text.append(text3)

    text4 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text4.move(50, 70)
    text4.text("PyBadge")
    text.append(text4)

    text5 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text5.move(35, 110)
    text5.text("PRESS START")
    text.append(text5)

    # set background to image 0 in the image bank and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y )

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)

     #set layers of sprites, they will show up in order
    game.layers = text + [background]

    # render the sprites
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            instructions_scene()

        # redraw the sprites
        game.tick()#

def instructions_scene():

    # the image banks for CircuitPython menu
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add the text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(10, 10)
    text1.text("How to play:")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(10, 30)
    text2.text("B button: shoot")
    text.append(text2)

    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(10, 50)
    text3.text("D pad: move ship")
    text.append(text3)

    text4 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text4.move(5, 70)
    text4.text("you will score back")
    text.append(text4)

    text5 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text5.move(5, 80)
    text5.text("if you miss a ship")
    text.append(text5)

    text6 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text6.move(10, 110)
    text6.text("GET READY TO PLAY!")
    text.append(text6)

    # set background to image 0 in the image bank and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y )

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)

     #set layers of sprites, they will show up in order
    game.layers = text + [background]

    # render the sprites
    game.render_block()

    # game loop
    while True:
    # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            time.sleep(10.0)
            game_scene()

        # redraw the sprites
        game.tick()#

# this is the game scene function
def game_scene():

    #for the score
    score = 0

    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format (score))

    #alien function, it moves them on the screen
    def show_alien():
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)

                break


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
    
    #create a list of aliens to spawn them
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

#place an alien on the screen
    show_alien()
    
    # creating a list of lasers for when the player shoots
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # creating a stage for the background to show up on and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)

    # set layers of sprites, they will show up in order
    game.layers =  [score_text] + lasers + [ship] + aliens + [background]

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
            #when button is pressed, fire the laser
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                sound.play(pew_sound)
                break

            
        # each frame moves the lasers that have been fired
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,
                                              lasers[laser_number].y -
                                                constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                  constants.OFF_SCREEN_Y)
                    
                        
        # each frame moves the aliens down that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                              aliens[alien_number].y +
                                                constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                                  constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))

        # when the laser hits the alien
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y,
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            #if you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            boom_sound = open("boom.wav", 'rb')
                            sound.play(boom_sound)
                            sound.stop()
                            show_alien()
                            show_alien()  
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))

         #frame check if any aliens are touching the ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    #alien hits the ship
                    crash_sound = open("crash.wav", 'rb')
                    sound.play(crash_sound)
                    sound.stop
                    time.sleep(3.0)
                    game_over_scene(score)

        # redraw the sprites
        game.render_sprites(lasers + aliens + [ship])
        game.tick()

def game_over_scene(final_score):

    #image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    #set background to image 0
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    #add text objects
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(22,20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(43,60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)

    #create a stage for the background to show up on
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    #game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

    #update game logic
        game.tick()

if __name__ == "__main__":
    splash_scene()