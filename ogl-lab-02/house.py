import glfw
from OpenGL.GL import *
from math import pi, cos, sin

def draw_trunk():
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.3, 0.0) # Brown color for the trunk
    glVertex2f(-0.05, -0.5)
    glVertex2f(-0.05, 0.0)
    glVertex2f(0.05, 0.0)
    glVertex2f(0.05, -0.5)
    glEnd()

def draw_leaves():
    num_triangles = 12
    radius = 0.2
    center_x, center_y = 0.0, 0.0

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.4, 0.0) # Green color for the leaves
    glVertex2f(center_x, center_y) # Center of the leaves
    for i in range(num_triangles + 1):
        angle = 2.0 * pi * float(i) / float(num_triangles)
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_tree(x, y):
    glPushMatrix()
    glTranslatef(x, y, 0.0) # Translate to the position of the tree
    draw_trunk()
    draw_leaves()
    glPopMatrix()

def draw_sun():
    num_triangles = 36
    radius = 0.1
    center_x, center_y = 0.5, 0.8

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 0.0) # Yellow color for the sun
    glVertex2f(center_x, center_y) # Center of the sun
    for i in range(num_triangles + 1):
        angle = 2.0 * pi * float(i) / float(num_triangles)
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_landscape():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.6, 0.0) # Green color for grass
    glVertex2f(-1.0, -0.4)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, -0.4)
    glEnd()

def draw_house():
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.7, 0.6) # Light brown color for walls
    glVertex2f(-0.3, -0.4)
    glVertex2f(-0.3, 0.2)
    glVertex2f(0.3, 0.2)
    glVertex2f(0.3, -0.4)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1) # Dark red color for roof
    glVertex2f(-0.35, 0.2)
    glVertex2f(0.0, 0.5)
    glVertex2f(0.35, 0.2)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.0) # Brown color for door
    glVertex2f(-0.1, -0.4)
    glVertex2f(-0.1, -0.1)
    glVertex2f(0.1, -0.1)
    glVertex2f(0.1, -0.4)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.9, 0.9, 1.0) # Light blue color for windows
    glVertex2f(-0.2, 0.0)
    glVertex2f(-0.2, 0.1)
    glVertex2f(-0.05, 0.1)
    glVertex2f(-0.05, 0.0)

    glVertex2f(0.05, 0.0)
    glVertex2f(0.05, 0.1)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.2, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1) # Dark brown color for chimney
    glVertex2f(0.15, 0.25)
    glVertex2f(0.15, 0.4)
    glVertex2f(0.25, 0.4)
    glVertex2f(0.25, 0.25)
    glEnd()

def my_display():
    glClearColor(0.6, 0.85, 1.0, 1.0) # Light sky blue background
    glClear(GL_COLOR_BUFFER_BIT)

    draw_house()
    draw_sun()
    draw_landscape()
    draw_tree(-0.8, -0.2)
    draw_tree(0.8, -0.3)

    glFlush()

def main():
    if not glfw.init():
        return -1

    window = glfw.create_window(800, 600, "Draw a House with scene", None, None)
    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        my_display()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
    return 0

if __name__ == "__main__":
    main()
