from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(50, 300, 200, 300, screen, [0, 255, 255])
draw_line(50, 100, 200, 100, screen, [0, 255, 255])
draw_line(50, 100, 200, 300, screen, [0, 255, 255])
draw_line(50, 200, 200, 200, screen, [0, 255, 255])



display(screen)
save_extension(screen, 'img.png')
