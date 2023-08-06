#include <GLFW/glfw3.h>
#include <cmath>

// Function declarations
void drawLandscape();
void drawSun();
void drawTree(float x, float y);
void drawTrunk();
void drawLeaves();

// Draw the landscape using GL_POLYGON
void drawLandscape() {
    glBegin(GL_POLYGON);
    glColor3f(0.0f, 0.6f, 0.0f); // Green color for grass
    glVertex2f(-1.0f, -0.5f);
    glVertex2f(-1.0f, -1.0f);
    glVertex2f(1.0f, -1.0f);
    glVertex2f(1.0f, -0.5f);
    glEnd();
}

// Draw the sun using GL_TRIANGLE_FAN
void drawSun() {
    const int numTriangles = 36;
    const float radius = 0.1f;
    const float centerX = 0.5f;
    const float centerY = 0.8f;

    glBegin(GL_TRIANGLE_FAN);
    glColor3f(1.0f, 1.0f, 0.0f);  // Yellow color for the sun
    glVertex2f(centerX, centerY); // Center of the sun
    for (int i = 0; i <= numTriangles; ++i) {
        float angle = 2.0f * M_PI * static_cast<float>(i) / static_cast<float>(numTriangles);
        float x = centerX + radius * cos(angle);
        float y = centerY + radius * sin(angle);
        glVertex2f(x, y);
    }
    glEnd();
}

// Draw a tree using GL_TRIANGLES
void drawTree(float x, float y) {
    glPushMatrix();
    glTranslatef(x, y, 0.0f); // Translate to the position of the tree
    drawTrunk();
    drawLeaves();
    glPopMatrix();
}

// Draw the trunk of the tree using GL_QUADS
void drawTrunk() {
    glBegin(GL_QUADS);
    glColor3f(0.6f, 0.3f, 0.0f); // Brown color for the trunk
    glVertex2f(-0.05f, -0.5f);
    glVertex2f(-0.05f, 0.0f);
    glVertex2f(0.05f, 0.0f);
    glVertex2f(0.05f, -0.5f);
    glEnd();
}

// Draw the leaves of the tree using GL_TRIANGLE_FAN
void drawLeaves() {
    const int numTriangles = 12;
    const float radius = 0.2f;
    const float centerX = 0.0f;
    const float centerY = 0.0f;

    glBegin(GL_TRIANGLE_FAN);
    glColor3f(0.0f, 0.4f, 0.0f); // Green color for the leaves
    glVertex2f(centerX, centerY); // Center of the leaves
    for (int i = 0; i <= numTriangles; ++i) {
        float angle = 2.0f * M_PI * static_cast<float>(i) / static_cast<float>(numTriangles);
        float x = centerX + radius * cos(angle);
        float y = centerY + radius * sin(angle);
        glVertex2f(x, y);
    }
    glEnd();
}

void myDisplay(void) {
    glClearColor(0.6f, 0.85f, 1.0f, 1.0f); // Light sky blue background
    glClear(GL_COLOR_BUFFER_BIT);

    drawLandscape();
    drawSun();
    drawTree(-0.8f, -0.2f); // Adjusted y value to place the tree above the ground
    drawTree(0.0f, -0.1f);  // Adjusted y value to place the tree above the ground
    drawTree(0.8f, -0.3f);  // Adjusted y value to place the tree above the ground

    glFlush();
}

int main() {
    if (!glfwInit())
        return -1;

    GLFWwindow *window = glfwCreateWindow(800, 600, "Draw a Simple Scenery", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, [](GLFWwindow *win, int width, int height) {
        glViewport(0, 0, width, height);
    });

    while (!glfwWindowShouldClose(window)) {
        myDisplay();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // Terminate GLFW
    glfwTerminate();
    return 0;
}
