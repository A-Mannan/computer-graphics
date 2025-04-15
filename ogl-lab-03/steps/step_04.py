import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.VP_Bottom = 0
        self.VP_Left = 0
        self.VP_Width = 640
        self.VP_Height = 480
        self.minX = -10
        self.minY = -10
        self.maxX = 10
        self.maxY = 10

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
        glfw.set_key_callback(self._win, self.__key_callback)

    def __set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)
        glColor3f(0.192, 0.882, 0.969, 1)

    def __display(self):
        glClear(GL_COLOR_BUFFER_BIT)

    def draw_axis(self):
        glBegin(GL_LINES)
        glVertex2f(self.minX, 0)
        glVertex2f(self.maxX, 0)
        glEnd()

        glBegin(GL_LINES)
        glVertex2f(0, self.minY)
        glVertex2f(0, self.maxY)
        glEnd()

    def my_display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glViewport(self.VP_Bottom, self.VP_Left, self.VP_Width, self.VP_Height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(self.minX, self.maxX, self.minY, self.maxY)
        self.draw_axis()
        glFlush()

    def __key_callback(self, window, key, scancode, action, mods):
        if key == glfw.KEY_C and action == glfw.PRESS:
            self.__clear_screen()

    def __clear_screen(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.draw_axis()
        glFlush()

    def run(self) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            self.__display()
            self.my_display()
            glfw.swap_buffers(self._win)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        glfw.terminate()


if __name__ == "__main__":
    with App(640, 480, "Using Viewport and World Window") as app:
        app.run()
