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

    def __draw_arc(self, center_x, center_y, radius, start_angle, end_angle, num_segments=100):
        glBegin(GL_LINE_STRIP)
        for i in range(num_segments + 1):
            angle = math.radians(start_angle + (end_angle - start_angle) * i / num_segments)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            glVertex2f(x, y)
        glEnd()

    def __display(self, center_x, center_y, radius, start_angle, end_angle) -> None:
        glClear(GL_COLOR_BUFFER_BIT)
        self.__draw_arc(center_x, center_y, radius, start_angle, end_angle)

    def run(self, center_x, center_y, radius, start_angle, end_angle) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display(center_x, center_y, radius, start_angle, end_angle)
            glfw.swap_buffers(self._win)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        glfw.terminate()

if __name__ == "__main__":
    width = 650
    height = 450
    title = "Simple Arc"
    center_x = width / 2  # X-coordinate of the center
    center_y = height / 2  # Y-coordinate of the center
    radius = 100  # Radius of the arc
    start_angle = 30  # Starting angle in degrees
    end_angle = 150  # Ending angle in degrees

    with App(width, height, title) as app:
        app.run(center_x, center_y, radius, start_angle, end_angle)
