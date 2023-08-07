import glfw


class Window:
    def __init__(self, width: int, height: int, title: str) -> None:
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        self._win = glfw.create_window(width, height, title, None, None)

        if not self._win:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        glfw.set_window_pos(self._win, 400, 200)
        glfw.make_context_current(self._win)

    def main_loop(self) -> None:
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            glfw.swap_buffers(self._win)

        glfw.terminate()


if __name__ == "__main__":
    win = Window(640, 480, "Hello World")
    win.main_loop()