import glfw
from OpenGL.GL import *
import math

class App:
    def __init__(self, width: int, height: int, title: str, parametric_function) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.parametric_function = parametric_function

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
        glOrtho(-self.width/2, self.width/2, -self.height/2, self.height/2, -1.0, 1.0)
        glViewport(0, 0, self.width, self.height)

    def __draw_curve(self, t_range, num_segments=100):
        glBegin(GL_LINE_STRIP)
        for i in range(num_segments + 1):
            t = t_range[0] + (t_range[1] - t_range[0]) * i / num_segments
            x, y = self.parametric_function(t)
            glVertex2f(x, y)
        glEnd()

    def __display(self, t_range) -> None:
        glClear(GL_COLOR_BUFFER_BIT)
        self.__draw_curve(t_range)

    def run(self, t_range) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display(t_range)
            glfw.swap_buffers(self._win)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        glfw.terminate()

if __name__ == "__main__":
    width = 650
    height = 450
    title = "Parametric Curve: Lemniscate of Bernoulli"

    def parametric_function(t):
        a = 200  # Scale factor
        x = a * math.cos(t) / (1 + math.sin(t)**2)**0.5
        y = a * math.sin(t) * math.cos(t) / (1 + math.sin(t)**2)**0.5
        return x, y

    t_range = (0, 2 * math.pi)  # Range of parameter 't' for the parametric function

    with App(width, height, title, parametric_function) as app:
        app.run(t_range)
