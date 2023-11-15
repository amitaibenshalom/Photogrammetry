from vedo import *
import os
import time
import threading
import pygame

# mesh = Mesh("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texturedMesh.obj")
# mesh.texture("D:/Amitai_D/museum/photogrammetria/tests/OBJ_FILES/SHALEV/texture_1001.png", scale=0.1)
# mesh.show()


def get_last_obj(path):
    obj_file_path = os.path.join(max([os.path.join(path, d) for d in os.listdir(path)], key=os.path.getmtime), 'output/texturedMesh.obj')
    texture_file_path = os.path.join(max([os.path.join(path, d) for d in os.listdir(path)], key=os.path.getmtime), 'output/texture_1001.png')
    return obj_file_path, texture_file_path

def show_mesh(obj_file_path, texture_file_path):
    try:
        mesh = Mesh(obj_file_path)
        mesh.texture(texture_file_path, scale=0.1)
        mesh.show(size=("f","f")).clear()
    except:
        print("Error showing mesh")

# def get_nth_item_in_folder(folder_path, n):
#     items = os.listdir(folder_path)
#     if len(items) == 0:
#         return None
#     return items[-n]

def get_nth_obj_in_folder(folder_path, n):
    items = os.listdir(folder_path)
    if len(items) == 0 or n >= len(items):
        return None
    obj_file_path = os.path.join(folder_path, items[-n], 'output/texturedMesh.obj')
    texture_file_path = os.path.join(folder_path, items[-n], 'output/texture_1001.png')
    return obj_file_path, texture_file_path

photogrammetry_data_path = r'C:\Users\amita\OneDrive - The Bloomfield Science Museum in Jerusalem\photogrammetry_data'
# obj_file_path = os.path.join(photogrammetry_data_path, 'texturedMesh.obj')
# texture_file_path = os.path.join(photogrammetry_data_path, 'texture_1001.png')

# wait for the object file to be created by Meshroom (or use a timeout)
# while not os.path.exists(obj_file_path):
#     time.sleep(1)

# get the last modified folder in the photogrammetry data path (the one that was just created by Meshroom) and get the obj file path from it
# obj_file_path, texture_file_path = get_last_obj(photogrammetry_data_path)
#
# mesh = Mesh(obj_file_path)
# mesh.texture(texture_file_path, scale=0.1)
# mesh.show(size=("f","f"))

model_number = 0
# screen = pygame.display.set_mode((640, 480), 0, 32)
while True:
    # show the mesh number model_number
    obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
    if obj_file_path is None:
        break
    show_mesh(obj_file_path, texture_file_path)
    model_number += 1
    if model_number >= len(os.listdir(photogrammetry_data_path)):
        model_number = 0

# thread = threading.Thread(target=mesh.show(size=("f", "f")))
#
# thread.start()
# # # print(time.time())
# thread.join(timeout=5)
# # # print(time.time())
# if thread.is_alive():
#     print("Timeout reached. Interrupting the thread.")
#     thread.join()  # Wait for the thread to finish after interruption
# else:
#     print("Thread completed before timeout.")
print("done")