import glfw
from OpenGL.GL import *
import random

class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.background_color = [0.1, 0.2, 0.2]

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

        # Set mouse button callback
        glfw.set_mouse_button_callback(self._win, self.__mouse_button_callback)

        # Set key callback
        glfw.set_key_callback(self._win, self.__key_callback)

    def __set_up_opengl(self) -> None:
        glClearColor(*self.background_color, 1.0)

    def __display(self):
        glClear(GL_COLOR_BUFFER_BIT)

    def __mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
            self.__change_background_color()

    def __key_callback(self, window, key, scancode, action, mods):
        if key == glfw.KEY_SPACE and action == glfw.PRESS:
            self.__change_background_color()
        elif key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(self._win, True)

    def __change_background_color(self):
        self.background_color = [random.uniform(0, 1) for _ in range(3)]
        glClearColor(*self.background_color, 1.0)

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
    with App(640, 480, "Step# 01") as app:
        app.run()
