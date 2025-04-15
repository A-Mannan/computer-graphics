import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import random


class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title

        self.mountain_color = [0.9294, 0.1294, 0.5333]
        self.mountains_created = False

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
        glfw.set_key_callback(self._win, self.key_callback)
        glfw.make_context_current(self._win)

    def __set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)

    def draw_mountains(self, r, g, b):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-10, 10, -10, 10)

        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(r, g, b)

        P1 = -10.0
        P2 = -5.0
        P3 = -7.5

        for i in range(5):
            glBegin(GL_TRIANGLES)
            glVertex2f(P1, 0.0)
            glVertex2f(P2, 0.0)
            glVertex2f(P3, 5)
            glEnd()

            P1 += 5.0
            P2 += 5.0
            P3 += 5.0

            glFlush()

    def key_callback(self, window, key, scancode, action, mods):
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, True)
        elif key == glfw.KEY_M and action == glfw.PRESS:
            self.mountains_created = True
            self.draw_mountains(0.9294, 0.1294, 0.5333)
        elif key == glfw.KEY_SPACE and action == glfw.PRESS:
            self.mountain_color = self.get_random_rgb_color()
        elif key == glfw.KEY_C and action == glfw.PRESS:
            self.mountains_created = False
            self.__set_up_opengl()

    def get_random_rgb_color(self):
        r = random.uniform(0, 1)
        g = random.uniform(0, 1)
        b = random.uniform(0, 1)
        return r, g, b

    def __display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.mountains_created:
            self.draw_mountains(*self.mountain_color)

    def run(self) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display()
            glfw.swap_buffers(self._win)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        glfw.terminate()


if __name__ == "__main__":
    with App(800, 600, "OpenGL App") as app:
        app.run()
