import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables
dots = []
drawing = False
brush_size = 5
viewport_width, viewport_height = 800, 600
world_window_width, world_window_height = 100, 100


def draw_dot(x, y):
    glPointSize(brush_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_dots():
    glColor3f(1, 0, 0)  # Red color
    for dot in dots:
        draw_dot(*dot)

def draw_text(text, x, y):
    font = GLUT_BITMAP_TIMES_ROMAN_24
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(font, ord(char))

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_dots()
    draw_text("Brush Size: " + str(brush_size), 10, world_window_height - 30)
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)

def mouse_button_callback(window, button, action, mods):
    global drawing
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            drawing = True
        else:
            drawing = False

def cursor_position_callback(window, xpos, ypos):
    global drawing
    if drawing:
        x = xpos / viewport_width * world_window_width
        y = (viewport_height - ypos) / viewport_height * world_window_height
        dots.append((x, y))

def key_callback(window, key, scancode, action, mods):
    global brush_size
    if action == glfw.PRESS:
        if key == glfw.KEY_KP_ADD:
            brush_size += 1
        elif key == glfw.KEY_KP_SUBTRACT:
            brush_size = max(1, brush_size - 1)

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    window = glfw.create_window(viewport_width, viewport_height, "OpenGL Drawing", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, world_window_width, 0, world_window_height)
    glMatrixMode(GL_MODELVIEW)

    glfw.set_window_size_callback(window, reshape)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)
    glfw.set_key_callback(window, key_callback)

    # Main loop
    while not glfw.window_should_close(window):
        display()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
