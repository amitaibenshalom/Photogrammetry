import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def load_obj(file_path):
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertices.append(list(map(float, line.strip().split()[1:])))
            elif line.startswith('f '):
                faces.append(list(map(int, line.strip().split()[1:])))

    return vertices, faces


def draw_obj(vertices, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            vertex = vertices[vertex_index - 1]
            glVertex3fv(vertex)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -50)

    # Replace 'path/to/your/object.obj' with the actual path to your object file
    obj_file_path = 'D:\Amitai_D\museum\photogrammetria\\videos and pictures\ImageToStl.com_text\\text.obj'
    vertices, faces = load_obj(obj_file_path)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_obj(vertices, faces)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
