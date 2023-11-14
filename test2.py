from vedo import *
return
mesh = Mesh("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texturedMesh.obj", )

mesh.texture("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texture_1001.png", scale=0.1)

mesh.show()