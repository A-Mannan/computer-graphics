import pygame as pg
from OpenGL.GL import *


class App:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title

        self.__set_up_pygame()
        self.__set_up_timer()
        self.__set_up_opengl()

    def __set_up_pygame(self) -> None:
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE
        )
        pg.display.set_mode((self.width, self.height), pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption(self.title)

    def __set_up_timer(self) -> None:
        self.clock = pg.time.Clock()

    def __set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)

    def run(self) -> None:
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            # timing
            self.clock.tick(60)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        pg.quit()


if __name__ == "__main__":
    with App(640, 480, "Hello World") as app:
        app.run()
