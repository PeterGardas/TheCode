import pygame
import pygame.gfxdraw
import pygame.mixer
from GUI import *
import random


pygame.init()

pygame.mixer.init()

typewriter_sound = pygame.mixer.music.load('soundtypewriter.mp3')


window_disp_vyska = 768
window_disp_sirska = 1366



window_disp = pygame.display.set_mode([window_disp_sirska, window_disp_vyska])
name_disp = pygame.display.set_caption("The Code")

display_black = [0, 0, 0]
display_white = [255, 255, 255]
display_red = [255, 0, 0]
display_green = [0, 200, 0]



image = pygame.image.load('ubuntu5.jpg')
image = pygame.transform.scale(image, (1366, 768))
image2 = pygame.image.load('google.jpg')
image2 = pygame.transform.scale(image, (1366, 768))

def game_main_loop():
    x = 0
    y = 0
    clock = pygame.time.Clock()

    crashed = False
    mouse = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    while not crashed:
        for event in pygame.event.get(): # Trackuje vsechny veci co hrac dela!
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                pygame.font.quit()
                quit()
        linux_background(x, y)
        transparent_button(7, 325, 50, 53, lambda: under_construction("The writer is not finished, sorry, come back soon!", display_white, display_black, display_black, 40, window_disp_sirska/2, window_disp_vyska/6.5)) #Libre Impress button
        transparent_button(7, 265, 50, 53, lambda: under_construction("The writer is not finished, sorry, come back soon!", display_white, display_black, display_black, 40, window_disp_sirska/2, window_disp_vyska/6.5)) #Libre Excel button
        transparent_button(7, 207, 50, 53, lambda: under_construction("The writer is not finished, sorry, come back soon!", display_white, display_black, display_black, 40, window_disp_sirska/2, window_disp_vyska/6.5)) #Libre Office button
        transparent_button(7, 147, 50, 53, lambda: suspicious_print("Suspicious print test!kkk", "munro", 30, 300, 100, display_black, display_black, display_white)) #Firefox button
  	    #transparent_button(7, 89, 50, 53, web_app_run) #Shelf button
        transparent_button(7, 89, 50, 53, lambda: web_app("google.jpg")) #You can actually use this so you must not create _run functions
        transparent_button(7, 30, 50, 53, lambda: under_construction("This is ubuntu actually so cannot publish this", display_white, display_black, display_black, 40, window_disp_sirska/2, window_disp_vyska/6.5)) #Ubunt button
        pygame.display.update()  # You can use pygame.display.flip(). But the pygame.display.update() becouse it is 2D game.
        clock.tick(30) # FPS


def button(text, x, y, w, h, a, font, w_s, w_v, action = None): #x, z, sirka, vyska, barva najeta na button, window sirka, window vyska, co chci delat jak to klikne, parametr akce
    mouse_location = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if x+w > mouse_location[0] > x and y+h > mouse_location[1] > y:
        menu_bars_font = pygame.font.SysFont(font, 125)
        text_print_menu_bars_exit = menu_bars_font.render(text, 1, a)
        menu_exit_rect = text_print_menu_bars_exit.get_rect(center = (w_s, w_v))
        pygame.draw.rect(window_disp, display_black, [x, y, w, h])
        window_disp.blit(text_print_menu_bars_exit, menu_exit_rect)
        if mouse_click[0] == 1 and action != None:
            action()


def transparent_button(x, y, w, h, action = None):
    mouse_location = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if x+w > mouse_location[0] > x and y+h > mouse_location[1] > y:
        pygame.gfxdraw.box(window_disp, pygame.Rect(x, y, w, h), (255, 255, 255, 40))  #0, 0, 50, 50 is resolution, the other thing is colour
        if mouse_click[0] == 1 and action != None:
            action()
def web_app(pic):
    web_app = True
    picture = pygame.image.load(pic)
    picture = pygame.transform.scale(picture, [window_disp_sirska, window_disp_vyska])
    rect = picture.get_rect()
    rect = rect.move((0, 0))
    font = pygame.font.SysFont("monospace", 111)
    font_render = font.render("", 1, display_white)
    font_rect = font_render.get_rect(center = (window_disp_sirska/2, window_disp_vyska/2))
    input_box = InLineTextBox((265, 68), 200, display_red)
    while web_app == True:
        for e in pygame.event.get():
            input_box.update(e)
            if e.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                exit()
        window_disp.blit(picture, rect)
        window_disp.blit(font_render, font_rect)
        input_box.render(window_disp)
        pygame.display.update()


def exit_func():
    pygame.font.quit()
    pygame.quit()
    quit()
def suspicious_print(text, font, font_big, t_w, t_h, fill_colour, rect_colour, text_colour):
    pygame.font.init()
    font = pygame.font.SysFont(font, font_big)
    window_disp.fill(fill_colour)
    text_print = ""
    for letter in text:
        text_print += letter
        render = font.render(text_print, 1, text_colour)
        render_rect = render.get_rect()
        render_rect.x = t_w
        render_rect.y = t_h
        pygame.draw.rect(window_disp, rect_colour, render_rect)
        window_disp.blit(render, render_rect)
        pygame.display.update()
        pygame.mixer.music.play(1)
        pygame.time.delay(random.randint(150, 500))
        pygame.mixer.music.stop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.font.quit()
                pygame.quit()
                quit()


def under_construction(text, text_colur, background_colour, rect_colour, font_big, w_s, w_v):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.font.init()
        fill = window_disp.fill(background_colour)
        font = pygame.font.SysFont("monospace", font_big)
        font_render = font.render(text, 1, text_colur)
        text_rect = font_render.get_rect(center = (w_s, w_v))
        pygame.draw.rect(window_disp, rect_colour, text_rect)
        window_disp.blit(font_render, text_rect)
        pygame.display.update()
        pygame.time.delay(500)
        game_main_loop()
        pygame.font.quit()

def linux_background(x, y):
    window_disp.blit(image, [x, y])
    mouse = pygame.mouse.get_pos()
def screen_typing(text):
    pygame.font.init()
    defalut_font = pygame.font.SysFont("monospace", 150)
    text_print = defalut_font.render(text, 1, [255, 255, 0])
    window_disp.blit(text_print, [100, 100])
    pygame.display.update()

def game_intro():
    intro = True
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window_disp.fill(display_black)
        pygame.font.init()
        defalut_font = pygame.font.SysFont("pixelart", 150, "bold")
        menu_bars_font = pygame.font.SysFont("monospace", 125)
        text_print_title = defalut_font.render("THE CODE", 1, display_black)
        text_print_menu_bars_play = menu_bars_font.render("PLAY", 1, display_black)
        text_print_menu_bars_settings = menu_bars_font.render("SETUP", 1, display_black)
        text_print_menu_bars_exit = menu_bars_font.render("EXIT", 1, display_black)
        text_rect = text_print_title.get_rect(center = (window_disp_sirska/2, window_disp_vyska/6.5))
        menu_play_rect = text_print_menu_bars_play.get_rect(center = (window_disp_sirska/2, window_disp_vyska/2.5))
        menu_settings_rect = text_print_menu_bars_settings.get_rect(center = (window_disp_sirska/2, window_disp_vyska/1.6))
        menu_exit_rect = text_print_menu_bars_exit.get_rect(center = (window_disp_sirska/2, window_disp_vyska/1.17))
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(window_disp, display_white, text_rect)
        pygame.draw.rect(window_disp, display_white, menu_play_rect)
        pygame.draw.rect(window_disp, display_white, menu_settings_rect)
        pygame.draw.rect(window_disp, display_white, menu_exit_rect)
        window_disp.blit(text_print_title, text_rect)
        window_disp.blit(text_print_menu_bars_play, menu_play_rect)
        window_disp.blit(text_print_menu_bars_settings, menu_settings_rect)
        window_disp.blit(text_print_menu_bars_exit, menu_exit_rect)
        button("EXIT", 533, 593, 300, 126, display_white, "monospace", window_disp_sirska/2, window_disp_vyska/1.17, exit_func) #Button exit
        button("PLAY", 533, 244, 300, 126, display_white, "monospace",window_disp_sirska/2, window_disp_vyska/2.5, game_main_loop) #Button start
        button("SETUP", 496, 417, 375, 126, display_white, "monospace", window_disp_sirska/2, window_disp_vyska/1.6, lambda: under_construction("The settings are not ready, sorry come back soon!", display_white, display_black, display_black, 40, window_disp_sirska/2, window_disp_vyska/6.5)) #Button setup


        pygame.display.update()
game_intro()
pygame.quit()
pygame.font.quit()
quit()
