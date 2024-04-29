import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image

def load_texture(filename):
    image = pygame.image.load(filename)
    texture_data = pygame.image.tostring(image, "RGB", 1)
    texture_width, texture_height = image.get_width(), image.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture_width, texture_height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    return texture_id, texture_width, texture_height

def draw_background(texture_id, screen_width, screen_height, texture_width, texture_height):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Calculate aspect ratio of the screen and the texture
    screen_aspect_ratio = screen_width / screen_height
    texture_aspect_ratio = texture_width / texture_height
    
    # Adjust texture coordinates to cover the entire screen
    if screen_aspect_ratio > texture_aspect_ratio:
        # Screen is wider than texture, adjust vertically
        tex_width_scaled = screen_aspect_ratio / texture_aspect_ratio
        glTexCoord2f(0, 0)
        glVertex3f(-tex_width_scaled, -1, 0)
        glTexCoord2f(1, 0)
        glVertex3f(tex_width_scaled, -1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(tex_width_scaled, 1, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-tex_width_scaled, 1, 0)
    else:
        # Screen is taller than texture, adjust horizontally
        tex_height_scaled = texture_aspect_ratio / screen_aspect_ratio
        glTexCoord2f(0, 0)
        glVertex3f(-1, -tex_height_scaled, 0)
        glTexCoord2f(1, 0)
        glVertex3f(1, -tex_height_scaled, 0)
        glTexCoord2f(1, 1)
        glVertex3f(1, tex_height_scaled, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-1, tex_height_scaled, 0)
    
    glEnd()
    glDisable(GL_TEXTURE_2D)

def main():
    pygame.init()
    display_info = pygame.display.Info()
    display = (display_info.current_w, display_info.current_h)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | FULLSCREEN)
    screen_width, screen_height = display_info.current_w, display_info.current_h
    gluPerspective(45, (screen_width / screen_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Load the background image as a texture
    background_texture, texture_width, texture_height = load_texture(r"D:\Amitai_D\museum\photogrammetria\tamar pictures\amitai\2023-08-28-110536.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the background
        draw_background(background_texture, screen_width, screen_height, texture_width, texture_height)

        # Add your 3D model rendering code here
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
