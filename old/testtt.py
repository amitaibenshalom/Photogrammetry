import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image


def main():
    pygame.init()
    display_info = pygame.display.Info()
    display = (display_info.current_w, display_info.current_h)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | FULLSCREEN)
    screen_width, screen_height = display_info.current_w, display_info.current_h
    gluPerspective(45, (screen_width / screen_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glClearColor(1.0, 1.0, 0.0, 1.0)

    # take the image and set it as the background
    # image_path = r"D:\Amitai_D\museum\photogrammetria\tamar pictures\amitai\2023-08-28-110536.jpg"
    # background_texture = glGenTextures(1)
    # glBindTexture(GL_TEXTURE_2D, background_texture)
    # image = Image.open(image_path)
    # image_data = np.array(list(image.getdata()), np.uint8)
    # image_width, image_height = image.size
    # texture_width, texture_height = image_width, image_height
    # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture_width, texture_height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 0.0, 1.0)
        
        image_path = r"D:\Amitai_D\museum\photogrammetria\tamar pictures\amitai\2023-08-28-110536.jpg"
        background_texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, background_texture)
        image = Image.open(image_path)
        image_data = np.array(list(image.getdata()), np.uint8)
        image_width, image_height = image.size
        texture_width, texture_height = image_width, image_height
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture_width, texture_height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        # # Draw the background
        # draw_background(background_texture, screen_width, screen_height, texture_width, texture_height)

        # # Add your 3D model rendering code here
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
