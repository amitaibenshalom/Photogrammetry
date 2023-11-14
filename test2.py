from vedo import *
import os

# mesh = Mesh("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texturedMesh.obj")
# mesh.texture("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texture_1001.png", scale=0.1)
# mesh.show()

photogrammetry_data_path = r'D:\Amitai_D\museum\photogrammetria\tests\OBJ_FILES\Amitai'
obj_file_path = os.path.join(photogrammetry_data_path, 'texturedMesh.obj')
texture_file_path = os.path.join(photogrammetry_data_path, 'texture_1001.png')
mesh = Mesh(obj_file_path)
mesh.texture(texture_file_path, scale=0.1)
# mesh.show(size=(screen_width, screen_height))
mesh.show(size=("f", "f"))
