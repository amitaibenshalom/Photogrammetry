import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up the Pygame window
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Set up the OpenGL perspective projection matrix
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Set up the OpenGL rendering
glShadeModel(GL_FLAT)
glClearColor(0.0, 0.0, 0.0, 0.0)
glClearDepth(1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)

# Load the object file and associated MTL file
obj_vertices = []
obj_texture_coords = []
obj_faces = []
obj_file_path = r"C:\Users\mada\Documents\photogrammetry\photogrammetry_data\2024-01-01-10-35-52-0016\output\texturedMesh.obj"

with open(obj_file_path, 'r') as obj_file:
    for line in obj_file:
        if line.startswith('v '):
            vertices = line.split()[1:]
            obj_vertices.append([float(v) for v in vertices])
        elif line.startswith('vt '):
            texture_coords = line.split()[1:]
            obj_texture_coords.append([float(t) for t in texture_coords])
        elif line.startswith('f '):
            face_data = line.split()[1:]
            obj_faces.append([list(map(int, vertex.split('/'))) for vertex in face_data])

# Rotation angle
angle = 0.0

# Function to compute face normals
def compute_normals():
    normals = []
    for face in obj_faces:
        v1 = [obj_vertices[face[0][0] - 1][i] - obj_vertices[face[1][0] - 1][i] for i in range(3)]
        v2 = [obj_vertices[face[2][0] - 1][i] - obj_vertices[face[1][0] - 1][i] for i in range(3)]
        normal = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]
        normals.append(normal)
    return normals

# Function to handle rendering
def render():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Move the model-view matrix to the center of the object
    glTranslatef(0.0, 0.0, -5.0)

    # Rotate around the local Y-axis
    glPushMatrix()
    glRotatef(angle, 0.0, 1.0, 0.0)

    # Draw the loaded object with computed normals
    glBegin(GL_TRIANGLES)
    normals = compute_normals()
    for i, face in enumerate(obj_faces):
        for j, vertex in enumerate(face):
            glNormal3fv(normals[i])
            glTexCoord2fv(obj_texture_coords[vertex[1] - 1])
            glVertex3fv(obj_vertices[vertex[0] - 1])
    glEnd()

    # Restore the model-view matrix
    glPopMatrix()

    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Update the rotation angle
    angle += 1.0

    render()
    pygame.time.wait(10)  # Add a small delay to control the frame rate

# Quit Pygame
pygame.quit()
