import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
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
        gluOrtho2D(-self.width / 2, self.width / 2, -self.height / 2, self.height / 2)
        glViewport(0, 0, self.width, self.height)

    def __draw_circle(self, radius, num_segments=100):
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            angle = 2.0 * math.pi * i / num_segments
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex2f(x, y)
        glEnd()

    def __display(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.__draw_circle(100)
        glfw.swap_buffers(self._win)

    def run(self) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        glfw.terminate()


if __name__ == "__main__":
    with App(800, 800, "Circle Drawing") as app:
        app.run()
