import os
from PIL import Image
import glob
import pygame, sys
import random
import time
import threading
import sys
from pygame import *
import pygame_menu
from pygame_menu.examples import create_example_window
from random import randrange
from typing import Tuple, Any, Optional, List
import pygame_menu
from pygame_menu.examples import create_example_window
pygame.init()
# from tkinter import *
# from tkinter import ttk

# # #window
# Create the surface
surface = create_example_window('МЕНЮШКА', (400, 280))

# Create a custom theme
my_theme = pygame_menu.themes.THEME_DARK.copy()
my_theme.title = False  # Hide the menu title

menu = pygame_menu.Menu(
    height=280,  # Use full-screen
    theme=my_theme,
    title='',
    center_content=False,
    width=400
)

# Button options
b1 = menu.add.button(
    'ГЛАВНОЕ МЕНЮ',
    # lambda: print(f'My method')
    os.system('plants vs zombie.py'),
    align=pygame_menu.locals.ALIGN_LEFT,
    float=True,
    selection_color='#fff'
)
b1.translate(70, 30)
b2 = menu.add.button(
    'ВЫХОД',
    pygame_menu.events.EXIT,
    align=pygame_menu.locals.ALIGN_LEFT,
    float=True,
    selection_color='#fff'
)
b2.translate(130, 200)

# b3 = menu.add.button(
#     'ПРОДОЛЖИТЬ'
#     pygame_menu.events.BACK,
#     align=pygame_menu.locals.ALIGN_LEFT,
#     float=True,
#     selection_color='#fff'
# )
# b3.translate(40, 235)



if __name__ == '__main__':
    menu.mainloop(surface)