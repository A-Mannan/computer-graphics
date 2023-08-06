#include <GLFW/glfw3.h>

void myDisplay(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    glPointSize(8.0f); // Increase the point size
    glBegin(GL_POINTS);
    glColor3f(1.0f, 0.0f, 0.0f); // Red color for the points
    glVertex2f(0.0f, 0.0f);
    glVertex2f(0.2f, 0.4f);
    glVertex2f(-0.5f, -0.3f);
    glEnd();

    glFlush();
}

int main() {
    if (!glfwInit())
        return -1;

    GLFWwindow *window = glfwCreateWindow(800, 600, "OpenGL Points", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    while (!glfwWindowShouldClose(window)) {
        myDisplay();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
