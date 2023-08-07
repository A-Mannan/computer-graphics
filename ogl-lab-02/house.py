import glfw
from OpenGL.GL import *
from math import pi, cos, sin


class HouseScene:
    def __init__(self, width: int, height: int, title: str) -> None:
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        self._win = glfw.create_window(width, height, title, None, None)

        if not self._win:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        glfw.set_window_pos(self._win, 400, 200)
        glfw.make_context_current(self._win)

    def draw_trunk(self):
        glBegin(GL_QUADS)
        glColor3f(0.6, 0.3, 0.0)  # Brown color for the trunk
        glVertex2f(-0.05, -0.5)
        glVertex2f(-0.05, 0.0)
        glVertex2f(0.05, 0.0)
        glVertex2f(0.05, -0.5)
        glEnd()

    def draw_leaves(self):
        num_triangles = 12
        radius = 0.2
        center_x, center_y = 0.0, 0.0

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.0, 0.4, 0.0)  # Green color for the leaves
        glVertex2f(center_x, center_y)  # Center of the leaves
        for i in range(num_triangles + 1):
            angle = 2.0 * pi * float(i) / float(num_triangles)
            x = center_x + radius * cos(angle)
            y = center_y + radius * sin(angle)
            glVertex2f(x, y)
        glEnd()

    def draw_tree(self, x, y):
        glPushMatrix()
        glTranslatef(x, y, 0.0)  # Translate to the position of the tree
        self.draw_trunk()
        self.draw_leaves()
        glPopMatrix()

    def draw_sun(self):
        num_triangles = 36
        radius = 0.1
        center_x, center_y = 0.5, 0.8

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 1.0, 0.0)  # Yellow color for the sun
        glVertex2f(center_x, center_y)  # Center of the sun
        for i in range(num_triangles + 1):
            angle = 2.0 * pi * float(i) / float(num_triangles)
            x = center_x + radius * cos(angle)
            y = center_y + radius * sin(angle)
            glVertex2f(x, y)
        glEnd()

    def draw_landscape(self):
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.6, 0.0)  # Green color for grass
        glVertex2f(-1.0, -0.4)
        glVertex2f(-1.0, -1.0)
        glVertex2f(1.0, -1.0)
        glVertex2f(1.0, -0.4)
        glEnd()

    def draw_house(self):
        glBegin(GL_QUADS)
        glColor3f(0.8, 0.7, 0.6)  # Light brown color for walls
        glVertex2f(-0.3, -0.4)
        glVertex2f(-0.3, 0.2)
        glVertex2f(0.3, 0.2)
        glVertex2f(0.3, -0.4)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.9, 0.1, 0.1)  # Dark red color for roof
        glVertex2f(-0.35, 0.2)
        glVertex2f(0.0, 0.5)
        glVertex2f(0.35, 0.2)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.4, 0.2, 0.0)  # Brown color for door
        glVertex2f(-0.1, -0.4)
        glVertex2f(-0.1, -0.1)
        glVertex2f(0.1, -0.1)
        glVertex2f(0.1, -0.4)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.9, 0.9, 1.0)  # Light blue color for windows
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
        glColor3f(0.4, 0.2, 0.1)  # Dark brown color for chimney
        glVertex2f(0.15, 0.25)
        glVertex2f(0.15, 0.4)
        glVertex2f(0.25, 0.4)
        glVertex2f(0.25, 0.25)
        glEnd()

    def my_display(self):
        glClearColor(0.6, 0.85, 1.0, 1.0)  # Light sky blue background
        glClear(GL_COLOR_BUFFER_BIT)

        self.draw_house()
        self.draw_sun()
        self.draw_landscape()
        self.draw_tree(-0.8, -0.2)
        self.draw_tree(0.8, -0.3)

        glFlush()

    def main_loop(self):
        while not glfw.window_should_close(self._win):
            self.my_display()
            glfw.swap_buffers(self._win)
            glfw.poll_events()

        glfw.terminate()


if __name__ == "__main__":
    win = HouseScene(800, 600, "Draw a House with Scene")
    win.main_loop()
