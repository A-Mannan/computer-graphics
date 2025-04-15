#include <iostream>
#include <cmath>
#include <GL/glut.h>  // Include the appropriate OpenGL headers

typedef struct { float x, y; } tRealPoint;

class Canvas {
private:
    tRealPoint CP;
public:
    Canvas() { CP.x = CP.y = 0.0; }
    void lineTo(float x, float y);
    void moveTo(float x, float y) { CP.x = x; CP.y = y; }
};

void Canvas::lineTo(float x, float y) {
    glBegin(GL_LINES);
    glVertex2f((GLfloat)CP.x, (GLfloat)CP.y);
    CP.x = x; CP.y = y;
    glVertex2f((GLfloat)CP.x, (GLfloat)CP.y);
    glEnd();
    glFlush();
}

int screenWidth = 480, screenHeight = 480;
Canvas cvs;
int numSides = 20;
float angle = 0.0, delAngle = 0;

void Rosette(int N, float radius) {
    const int MaxNum = 97;
    tRealPoint pt[MaxNum];
    float angle = 2 * 3.14159265 / N;

    if (N < 3 || N >= MaxNum) return;
    for (int j = 0; j < N; j++) {
        pt[j].x = radius * cos(angle * j);
        pt[j].y = radius * sin(angle * j);
    }
    for (int i = 0; i < N - 1; i++)
        for (int j = i + 1; j < N; j++) {
            cvs.moveTo(pt[i].x, pt[i].y);
            cvs.lineTo(pt[j].x, pt[j].y);
        }
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glRotatef(angle, 0, 0, 1);
    Rosette(numSides, 8);
    glutSwapBuffers();
}

void myKeys(unsigned char key, int x, int y) {
    switch (key) {
        case 'q': exit(0);
        case 'n': numSides++; std::cout << numSides << std::endl; break;
        case 'N': numSides--; std::cout << numSides << std::endl; break;
        case 'r': delAngle += 1.0; break;
        case 'R': delAngle -= 1.0; break;
    }
    glutPostRedisplay();  // Mark the window as needing to be redisplayed
}

void spinner(void) {
    angle += delAngle;
    glutPostRedisplay();  // Mark the window as needing to be redisplayed
}

void myInit() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
    glColor3f(0.0f, 0.0f, 0.0f);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10, 10, -10, 10);
    glViewport(0, 0, screenWidth, screenHeight);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(screenWidth, screenHeight);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("here we go");
    glutKeyboardFunc(myKeys);
    glutDisplayFunc(display);
    glutIdleFunc(spinner);
    myInit();
    glutMainLoop();
    return 0;
}
