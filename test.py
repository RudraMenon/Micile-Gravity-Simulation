# --------------------------------------------------
# touchscreen_all_demo.py
# --------------------------------------------------
 
# import the ez_touchscreen library v0.9
# import the ez_graphics library v0.9
from ez_touchscreen_09 import *
from ez_graphics_09 import *
 
# clear the screen
clear_screen('black')
set_color('blue')
 
# main loop
while True:
    # read a single finger point from the touchscreen
    list_of_touch_points = touchscreen_finger_points_multitouch_all()
    for touch_points in list_of_touch_points:
        for point in touch_points:
            # get the x and y coordinates of the touch
            x = point['x']
            y = point['y']
            print [x,y]
            # draw a 10 x 10 rectangle where the finger touched
            draw_rect(x, y, 10, 10)   