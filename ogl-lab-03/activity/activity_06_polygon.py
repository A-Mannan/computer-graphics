import glfw
from OpenGL.GL import *
import math


class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title

        self.__set_up_glfw()
        self.__set_up_opengl()

    def __set_up_glfw(self) -> None:
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        self._win = glfw.create_window(self.width, self.height, self.title, None, None)

        if not self._win:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        glfw.set_window_pos(self._win, 400, 200)
        glfw.make_context_current(self._win)

    def __set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)
        glColor3f(0.192, 0.882, 0.969, 1)
        glPointSize(2.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.width, 0.0, self.height, -1.0, 1.0)
        glViewport(0, 0, self.width, self.height)

    def __draw_regular_polygon(self, sides, radius, center_x, center_y, rotation_angle):
        glBegin(GL_LINE_LOOP)
        for i in range(sides):
            angle = 2.0 * math.pi * i / sides + math.radians(rotation_angle)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            glVertex2f(x, y)
        glEnd()

    def __display(self, sides, radius, center_x, center_y, rotation_angle) -> None:
        glClear(GL_COLOR_BUFFER_BIT)
        self.__draw_regular_polygon(sides, radius, center_x, center_y, rotation_angle)

    def run(self, sides, radius, center_x, center_y, rotation_angle) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display(sides, radius, center_x, center_y, rotation_angle)
            glfw.swap_buffers(self._win)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        glfw.terminate()


if __name__ == "__main__":
    width = 650
    height = 450
    title = "Regular Polygon"
    sides = 6  # Number of sides
    radius = 100  # Radius of the polygon
    center_x = width / 2  # X-coordinate of the center
    center_y = height / 2  # Y-coordinate of the center
    rotation_angle = 0  # Rotation angle in degrees

    with App(width, height, title) as app:
        app.run(sides, radius, center_x, center_y, rotation_angle)
