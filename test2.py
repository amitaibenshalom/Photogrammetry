from vedo import *
import os
import time
import threading

# mesh = Mesh("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texturedMesh.obj")
# mesh.texture("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texture_1001.png", scale=0.1)
# mesh.show()

photogrammetry_data_path = r'D:\Amitai_D\museum\photogrammetria\tests\OBJ_FILES\Amitai'
obj_file_path = os.path.join(photogrammetry_data_path, 'texturedMesh.obj')
texture_file_path = os.path.join(photogrammetry_data_path, 'texture_1001.png')
mesh = Mesh(obj_file_path)
mesh.texture(texture_file_path, scale=0.1)
# mesh.show(size=("f","f"))

thread = threading.Thread(target=mesh.show(size=("f", "f")))
# print(time.time())
thread.start()
# print(time.time())
thread.join(timeout=5)
# print(time.time())
if thread.is_alive():
    print("Timeout reached. Interrupting the thread.")
    # mesh.clean()
    # thread.join()  # Wait for the thread to finish after interruption
    exit()
else:
    # print(time.time())
    print("Thread completed before timeout.")
# print(time.time())
print("done")