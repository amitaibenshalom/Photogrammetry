import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to load a texture from file
def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    return texture

# Function to draw a cube
def draw_cube():
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)  # Red color
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glEnd()

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Load texture
texture = load_texture(r"D:\Amitai_D\museum\photogrammetria\tamar pictures\amitai\2023-08-28-110536.jpg")

# Set up perspective projection matrix
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

# Set up initial camera position and rotation
glTranslatef(0.0, 0.0, -5)
glRotatef(0, 0, 0, 0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw background image
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-10, -10, -15)  # Move the background image a bit back
    glTexCoord2f(1, 0)
    glVertex3f(10, -10, -15)
    glTexCoord2f(1, 1)
    glVertex3f(10, 10, -15)
    glTexCoord2f(0, 1)
    glVertex3f(-10, 10, -15)
    glEnd()

    # Preserve the model view matrix of the background
    glPushMatrix()

    # Rotate the cube
    glRotatef(1, 1, 1, 1)
    
    # Draw the cube
    draw_cube()

    # Restore the model view matrix for the background
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
