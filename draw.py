from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1 < x0:
        x0, y0, x1, y1 = x1, y1, x0, y0
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)

    if A >= 0 and (x1 - x0) > A:
        d = 2*A + B
        while x <= x1:
            plot (screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    elif A > 0 and A >= (x1 - x0):
        d = 2*B + A
        while y <= y1:
            plot (screen, color, x, y)
            if d < 0:
                x += 1
                d += A * 2
            y += 1
            d += 2 * B
