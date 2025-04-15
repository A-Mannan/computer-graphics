import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *

class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title

        glutInit()
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

    def __display(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(1.0, 1.0, 1.0)  # Set color to white
        glRasterPos2f(-0.5, 0.5)  # Position for the heading
        glutBitmapString(GLUT_BITMAP_HELVETICA_18, b"OGL Lab# 03")

        glRasterPos2f(-0.6, 0.4)  # Position for the subheading
        glutBitmapString(GLUT_BITMAP_HELVETICA_12, b"Computer Graphics using OpenGL :)")

        glFlush()

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
    with App(640, 480, "OpenGL Text Example") as app:
        app.run()
