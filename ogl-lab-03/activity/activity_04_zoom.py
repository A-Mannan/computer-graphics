import glfw
from OpenGL.GL import *


class App:
    def __init__(self, width: int, height: int, title: str, dat_file_path) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.dat_file_path = dat_file_path
        self.zoom_factor = 1.0

        self.__set_up_glfw()
        self.__set_up_opengl()
        self.__set_up_callbacks()

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

    def __draw_polyline_from_file(self):
        with open(self.dat_file_path) as file:
            num_of_polys = int(file.readline())
            for _ in range(num_of_polys):
                num_of_points = int(file.readline())
                glBegin(GL_LINE_STRIP)
                for _ in range(num_of_points):
                    x, y = map(float, file.readline().split())
                    glVertex2f(
                        x * self.zoom_factor, y * self.zoom_factor
                    )  # Apply zoom factor
                glEnd()

            glFlush()

    def __display(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT)
        self.__draw_polyline_from_file()

    def __set_up_callbacks(self) -> None:
        def key_callback(window, key, scancode, action, mods):
            if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
                glfw.set_window_should_close(window, True)
            elif (
                key == glfw.KEY_KP_ADD
                and action == glfw.PRESS
                or key == glfw.KEY_EQUAL
                and action == glfw.PRESS
                and mods == glfw.MOD_SHIFT
            ):  # '+' key
                self.zoom_factor *= 1.1
            elif (
                key == glfw.KEY_KP_SUBTRACT
                and action == glfw.PRESS
                or key == glfw.KEY_MINUS
                and action == glfw.PRESS
                and mods == glfw.MOD_SHIFT
            ):  # '-' key
                self.zoom_factor *= 0.9

        glfw.set_key_callback(self._win, key_callback)

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
    width = 650
    height = 450
    title = "Zooming In and Out"
    file_path = "./dino.dat"
    with App(width, height, title, file_path) as app:
        app.run()
