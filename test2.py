from vedo import *
import os
# import pygame

# pygame.init()
# infoObject = pygame.display.Info()
# screen_width = infoObject.current_w
# screen_height = infoObject.current_h
# pygame.quit()

# mesh = Mesh("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texturedMesh.obj", )
#
# mesh.texture("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texture_1001.png", scale=0.1)
#
# mesh.show()

# get screen siz

photogrammetry_data_path = r'D:\Amitai_D\museum\photogrammetria\tests\OBJ_FILES\Amitai'
# get the path to the obj file
obj_file_path = os.path.join(photogrammetry_data_path, 'texturedMesh.obj')
# get the path to the texture file
texture_file_path = os.path.join(photogrammetry_data_path, 'texture_1001.png')
# load the obj file
mesh = Mesh(obj_file_path)
# load the texture file
mesh.texture(texture_file_path, scale=0.1)
# show the mesh on fullscreen

# mesh.show(size=(screen_width, screen_height))
mesh.show(size=("f","f"))