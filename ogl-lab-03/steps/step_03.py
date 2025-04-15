import glfw
from OpenGL.GL import *
import random

class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.background_color = [0.1, 0.2, 0.2]
        self.points = []
        self.brush_size = 5.0
        self.is_drawing = False

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

        # Set callbacks
        glfw.set_mouse_button_callback(self._win, self.__mouse_button_callback)
        glfw.set_cursor_pos_callback(self._win, self.__cursor_pos_callback)
        glfw.set_key_callback(self._win, self.__key_callback)

    def __set_up_opengl(self) -> None:
        glClearColor(*self.background_color, 1.0)

    def __display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.192, 0.882, 0.969, 1)
        glPointSize(self.brush_size)

        glBegin(GL_POINTS)
        for point in self.points:
            glVertex2f(*point)
        glEnd()

    def __mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT:
            if action == glfw.PRESS:
                self.is_drawing = True
            elif action == glfw.RELEASE:
                self.is_drawing = False

    def __cursor_pos_callback(self, window, x, y):
        if self.is_drawing:
            x = (x / self.width) * 2 - 1
            y = -((y / self.height) * 2 - 1)
            self.points.append((x, y))

    def __key_callback(self, window, key, scancode, action, mods):
        if key == glfw.KEY_SPACE and action == glfw.PRESS:
            self.__change_background_color()
        elif key == glfw.KEY_C and action == glfw.PRESS:
            self.__clear_screen()
        elif key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(self._win, True)
        elif key == glfw.KEY_EQUAL and action == glfw.PRESS:
            self.__increase_brush_size()
        elif key == glfw.KEY_MINUS and action == glfw.PRESS:
            self.__decrease_brush_size()

    def __change_background_color(self):
        self.background_color = [random.uniform(0, 1) for _ in range(3)]
        glClearColor(*self.background_color, 1.0)

    def __clear_screen(self):
        self.points = []
        glClear(GL_COLOR_BUFFER_BIT)

    def __increase_brush_size(self):
        self.brush_size += 1.0

    def __decrease_brush_size(self):
        if self.brush_size > 1.0:
            self.brush_size -= 1.0

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
    with App(640, 480, "Painting App") as app:
        app.run()
