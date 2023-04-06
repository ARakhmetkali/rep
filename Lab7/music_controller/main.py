import pygame, sys
from pygame import mixer
from classes import InterfaceElement, PauseButton, PlayButton, PrevButton, NextButton, ShuffleButton, VolumeUpButton


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ayan's player")
    pygame.display.set_icon(pygame.image.load('./assets/nike.jpg'))
    clock = pygame.time.Clock()
    isMusicOn = False
    isFirstPlayed = False
    songs_list = ['./assets/the_weeknd_daft_punk_starboy.mp3', './assets/the_weeknd_save_your_tears.mp3', './assets/the_weeknd_i_was_never_there.mp3']
    i = 0
    mixer.init()
    # button images
    album_logo = InterfaceElement(400, 200, "nike.jpg")
    play_btn = PlayButton(400, 400, "play_button.png")
    pause_btn = PauseButton(400, 400, "pause_button.png")
    prev_btn = PrevButton(300, 400, "prev_button.png")
    next_btn = NextButton(500, 400, "next_button.png")
    btn_list = [play_btn, prev_btn, next_btn]
    interface_elements_group = pygame.sprite.Group()
    for btn in btn_list:
        interface_elements_group.add(btn)

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.exit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            if not isMusicOn:
                                if not isFirstPlayed:
                                    mixer.music.load(songs_list[i])
                                    mixer.music.play()
                                    isFirstPlayed = True
                                    interface_elements_group.add(album_logo)
                                else:
                                    mixer.music.unpause()
                                    interface_elements_group.remove(play_btn)
                                    interface_elements_group.add(pause_btn)
                            else:
                                mixer.music.pause()
                                interface_elements_group.remove(pause_btn)
                                interface_elements_group.add(play_btn)
                            isMusicOn = not isMusicOn
                        case pygame.K_RIGHT:
                            if i < len(songs_list) - 1:
                                i += 1
                            else:
                                i = 0
                            mixer.music.load(songs_list[i])
                            mixer.music.play()
                            if not interface_elements_group.has(play_btn):
                                interface_elements_group.remove(pause_btn)
                                interface_elements_group.add(play_btn)
                        case pygame.K_LEFT:
                            if i > 0:
                                i -= 1
                            else:
                                i = len(songs_list) - 1
                            if not interface_elements_group.has(play_btn):
                                interface_elements_group.remove(pause_btn)
                                interface_elements_group.add(play_btn)
                            mixer.music.load(songs_list[i])
                            mixer.music.play()
                case pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > 370 and mouse_x < 430 and mouse_y > 370 and mouse_y < 430:
                        if not isMusicOn:
                            if not isFirstPlayed:
                                mixer.music.load(songs_list[i])
                                mixer.music.play()
                                isFirstPlayed = True
                                interface_elements_group.add(album_logo)
                            else:
                                mixer.music.unpause()
                            interface_elements_group.remove(play_btn)
                            interface_elements_group.add(pause_btn)
                        else:
                            mixer.music.pause()
                            interface_elements_group.remove(pause_btn)
                            interface_elements_group.add(play_btn)
                        isMusicOn = not isMusicOn
                    if mouse_x > 470 and mouse_x < 530 and mouse_y > 370 and mouse_y < 430:
                        if i < len(songs_list) - 1:
                            i += 1
                        else:
                            i = 0
                        mixer.music.load(songs_list[i])
                        mixer.music.play()
                        if not interface_elements_group.has(play_btn):
                            interface_elements_group.remove(pause_btn)
                            interface_elements_group.add(play_btn)
                    if mouse_x > 270 and mouse_x < 330 and mouse_y > 370 and mouse_y < 430:
                        if i > 0:
                            i -= 1
                        else:
                            i = len(songs_list) - 1
                        if not interface_elements_group.has(play_btn):
                            interface_elements_group.remove(pause_btn)
                            interface_elements_group.add(play_btn)
                        mixer.music.load(songs_list[i])
                        mixer.music.play()

        screen.fill((255, 255, 255))
        interface_elements_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()