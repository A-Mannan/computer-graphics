import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Canvas:
    def __init__(self):
        self.CP = {"x": 0.0, "y": 0.0}

    def line_to(self, x, y):
        glBegin(GL_LINES)
        glVertex2f(self.CP["x"], self.CP["y"])
        self.CP["x"], self.CP["y"] = x, y
        glVertex2f(self.CP["x"], self.CP["y"])
        glEnd()
        glFlush()

class App:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cvs = Canvas()
        self.num_sides = 5
        self.angle = 0.0
        self.del_angle = 0

        self.__set_up_glfw()
        self.__set_up_opengl()

    def __set_up_glfw(self) -> None:
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        self._win = glfw.create_window(self.width, self.height, "Rosette", None, None)

        if not self._win:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        glfw.set_window_pos(self._win, 100, 100)
        glfw.make_context_current(self._win)
        glfw.set_key_callback(self._win, self.__key_callback)

    def __set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)
        glColor3f(0.192, 0.882, 0.969, 1)
        glPointSize(2.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-10, 10, -10, 10)
        glViewport(0, 0, self.width, self.height)

    def __draw_rosette(self, N, radius):
        const_MaxNum = 97
        pt = [{"x": 0.0, "y": 0.0} for _ in range(const_MaxNum)]
        angle = 2 * 3.14159265 / N

        if N < 3 or N >= const_MaxNum:
            return

        for j in range(N):
            pt[j]["x"] = radius * math.cos(angle * j)
            pt[j]["y"] = radius * math.sin(angle * j)

        for i in range(N - 1):
            for j in range(i + 1, N):
                self.cvs.line_to(pt[i]["x"], pt[i]["y"])
                self.cvs.line_to(pt[j]["x"], pt[j]["y"])

    def __display(self):
        self.angle += self.del_angle
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(self.angle, 0, 0, 1)
        self.__draw_rosette(self.num_sides, 8)

    def __key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            if key == glfw.KEY_Q or key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(self._win, True)
            elif key == key == glfw.KEY_N and mods == glfw.MOD_SHIFT:
                self.num_sides -= 1
                print(self.num_sides)
            elif key == glfw.KEY_N:
                self.num_sides += 1
                print(self.num_sides)
            elif key == glfw.KEY_R and mods == glfw.MOD_SHIFT:
                self.del_angle -= 1.0
            elif key == glfw.KEY_R:
                self.del_angle += 1.0
            glfw.post_empty_event()

    def run(self):
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display()
            glfw.swap_buffers(self._win)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        glfw.terminate()

if __name__ == "__main__":
    width = 480
    height = 480

    with App(width, height) as app:
        app.run()
