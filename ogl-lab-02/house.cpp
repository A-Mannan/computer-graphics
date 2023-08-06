#include <GLFW/glfw3.h>
#include <cmath>


// Draw the trunk of the tree using GL_QUADS
void drawTrunk()
{
    glBegin(GL_QUADS);
    glColor3f(0.6f, 0.3f, 0.0f); // Brown color for the trunk
    glVertex2f(-0.05f, -0.5f);
    glVertex2f(-0.05f, 0.0f);
    glVertex2f(0.05f, 0.0f);
    glVertex2f(0.05f, -0.5f);
    glEnd();
}

// Draw the leaves of the tree using GL_TRIANGLE_FAN
void drawLeaves()
{
    const int numTriangles = 12;
    const float radius = 0.2f;
    const float centerX = 0.0f;
    const float centerY = 0.0f;

    glBegin(GL_TRIANGLE_FAN);
    glColor3f(0.0f, 0.4f, 0.0f);  // Green color for the leaves
    glVertex2f(centerX, centerY); // Center of the leaves
    for (int i = 0; i <= numTriangles; ++i)
    {
        float angle = 2.0f * M_PI * static_cast<float>(i) / static_cast<float>(numTriangles);
        float x = centerX + radius * cos(angle);
        float y = centerY + radius * sin(angle);
        glVertex2f(x, y);
    }
    glEnd();
}

// Draw a tree using GL_TRIANGLES
void drawTree(float x, float y)
{
    glPushMatrix();
    glTranslatef(x, y, 0.0f); // Translate to the position of the tree
    drawTrunk();
    drawLeaves();
    glPopMatrix();
}

void drawSun()
{
    const int numTriangles = 36;
    const float radius = 0.1f;
    const float centerX = 0.5f;
    const float centerY = 0.8f;

    glBegin(GL_TRIANGLE_FAN);
    glColor3f(1.0f, 1.0f, 0.0f);  // Yellow color for the sun
    glVertex2f(centerX, centerY); // Center of the sun
    for (int i = 0; i <= numTriangles; ++i)
    {
        float angle = 2.0f * M_PI * static_cast<float>(i) / static_cast<float>(numTriangles);
        float x = centerX + radius * cos(angle);
        float y = centerY + radius * sin(angle);
        glVertex2f(x, y);
    }
    glEnd();
}

// Draw the landscape using GL_POLYGON
void drawLandscape()
{
    glBegin(GL_POLYGON);
    glColor3f(0.0f, 0.6f, 0.0f); // Green color for grass
    glVertex2f(-1.0f, -0.4f);
    glVertex2f(-1.0f, -1.0f);
    glVertex2f(1.0f, -1.0f);
    glVertex2f(1.0f, -0.4f);
    glEnd();
}

void drawHouse()
{
    // Draw the walls
    glBegin(GL_QUADS);
    glColor3f(0.8f, 0.7f, 0.6f); // Light brown color for walls
    glVertex2f(-0.3f, -0.4f);
    glVertex2f(-0.3f, 0.2f);
    glVertex2f(0.3f, 0.2f);
    glVertex2f(0.3f, -0.4f);
    glEnd();

    // Draw the roof
    glBegin(GL_TRIANGLES);
    glColor3f(0.9f, 0.1f, 0.1f); // Dark red color for roof
    glVertex2f(-0.35f, 0.2f);
    glVertex2f(0.0f, 0.5f);
    glVertex2f(0.35f, 0.2f);
    glEnd();

    // Draw the door
    glBegin(GL_QUADS);
    glColor3f(0.4f, 0.2f, 0.0f); // Brown color for door
    glVertex2f(-0.1f, -0.4f);
    glVertex2f(-0.1f, -0.1f);
    glVertex2f(0.1f, -0.1f);
    glVertex2f(0.1f, -0.4f);
    glEnd();

    // Draw the windows
    glBegin(GL_QUADS);
    glColor3f(0.9f, 0.9f, 1.0f); // Light blue color for windows
    glVertex2f(-0.2f, 0.0f);
    glVertex2f(-0.2f, 0.1f);
    glVertex2f(-0.05f, 0.1f);
    glVertex2f(-0.05f, 0.0f);

    glVertex2f(0.05f, 0.0f);
    glVertex2f(0.05f, 0.1f);
    glVertex2f(0.2f, 0.1f);
    glVertex2f(0.2f, 0.0f);
    glEnd();

    // Draw the chimney
    glBegin(GL_QUADS);
    glColor3f(0.4f, 0.2f, 0.1f); // Dark brown color for chimney
    glVertex2f(0.15f, 0.25f);
    glVertex2f(0.15f, 0.4f);
    glVertex2f(0.25f, 0.4f);
    glVertex2f(0.25f, 0.25f);
    glEnd();
}

void myDisplay(void)
{
    glClearColor(0.6f, 0.85f, 1.0f, 1.0f); // Light sky blue background
    glClear(GL_COLOR_BUFFER_BIT);

    drawHouse();
    drawSun();
    drawLandscape();
    drawTree(-0.8f, -0.2f);
    // drawTree(0.0f, -0.1f);
    drawTree(0.8f, -0.3f);
    // drawGrid();
    // drawAxes();

    glFlush();
}

int main()
{
    if (!glfwInit())
        return -1;

    GLFWwindow *window = glfwCreateWindow(800, 600, "Draw a House with scene", NULL, NULL);
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
