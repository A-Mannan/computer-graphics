#include <GLFW/glfw3.h>
#include <cmath>

// Draw a single mountain using GL_TRIANGLES
void drawMountain(float x)
{
    glBegin(GL_TRIANGLES);
    glColor3f(0.2f, 0.2f, 0.2f); // Dark gray color for mountain
    glVertex2f(x - 0.3f, -0.6f);
    glVertex2f(x, 0.2f);
    glVertex2f(x + 0.3f, -0.6f);
    glEnd();
}

// Draw little stars using GL_POINTS
void drawStars()
{
    glPointSize(2.0f);
    glBegin(GL_POINTS);
    glColor3f(1.0f, 1.0f, 1.0f); // White color for stars
    glVertex2f(-0.8f, 0.8f);
    glVertex2f(-0.5f, 0.9f);
    glVertex2f(-0.2f, 0.7f);
    glVertex2f(0.1f, 0.85f);
    glVertex2f(0.4f, 0.95f);
    glVertex2f(0.7f, 0.75f);
    glVertex2f(0.85f, 0.9f);
    glEnd();
}

// Draw the moon using GL_TRIANGLE_FAN
void drawMoon()
{
    const int numTriangles = 36;
    const float radius = 0.15f;
    const float centerX = 0.8f;
    const float centerY = 0.8f;

    glBegin(GL_TRIANGLE_FAN);
    glColor3f(1.0f, 1.0f, 1.0f); // White color for the moon
    glVertex2f(centerX, centerY); // Center of the moon
    for (int i = 0; i <= numTriangles; ++i)
    {
        float angle = 2.0f * M_PI * static_cast<float>(i) / static_cast<float>(numTriangles);
        float x = centerX + radius * cos(angle);
        float y = centerY + radius * sin(angle);
        glVertex2f(x, y);
    }
    glEnd();
}

// Draw the sea using GL_POLYGON
void drawSea()
{
    glBegin(GL_POLYGON);
    glColor3f(0.0f, 0.0f, 0.3f); // Dark blue color for the sea
    glVertex2f(-1.0f, -0.6f);
    glVertex2f(-1.0f, -1.0f);
    glVertex2f(1.0f, -1.0f);
    glVertex2f(1.0f, -0.6f);
    glEnd();
}

void myDisplay(void)
{
    glClearColor(0.0f, 0.0f, 0.1f, 1.0f); // Dark blue background for night vision
    glClear(GL_COLOR_BUFFER_BIT);

    drawStars();
    drawMoon();

    // Draw the mountains in a row
    for (float x = -1.0f; x <= 1.0f; x += 0.6f)
    {
        drawMountain(x);
    }

    drawSea();

    glFlush();
}

int main()
{
    if (!glfwInit())
        return -1;

    GLFWwindow *window = glfwCreateWindow(800, 600, "Night Vision Sea Port Scene", NULL, NULL);
    if (!window)
    {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    while (!glfwWindowShouldClose(window))
    {
        myDisplay();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
