# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from doctest import ELLIPSIS_MARKER
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    diameter = 15
    space = 5
    interval = diameter + space
    x = 100
    y = 300
    min_diam = 3
    max_diam = 7
    x+= interval
    for i in range(500):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,fill="white")
    
    #Draw clouds
    diameter = 100
    interval = 50
    x = -10
    y = 435
    for i in range(50):
        number = random.randint(1, 5)
        if number > 1:
            draw_oval(canvas, x, y, x + diameter, y + diameter, outline="white", fill="white")
        x += interval
        height = round(scene_height / 5)
        min_diam = 15
        max_diam = 30
    
    draw_ground(canvas, scene_width, scene_height)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="white")

    # Draw a pine trees
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)
    tree_center_x = 400
    tree_bottom = 70
    tree_height = 190
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)
    tree_center_x = 30
    tree_bottom = 20
    tree_height = 230
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)
    tree_center_x = 650
    tree_bottom = 40
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)
    tree_center_x = 500
    tree_bottom = 85
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="gray20", width=1, fill="tan3")
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top,skirt_left, trunk_top,outline="gray20", width=1, fill="dark green")

# Call the main function so that
# this program will start executing.
main()