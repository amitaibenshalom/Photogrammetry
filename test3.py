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

# photogrammetry_data_path = r'C:\Users\amita\OneDrive - The Bloomfield Science Museum in Jerusalem\photogrammetry_data'
photogrammetry_data_path = r'D:\photogrammetry\OneDrive - The Bloomfield Science Museum in Jerusalem\photogrammetry_data'

def next(obj, ename):
    # mesh.alpha(1 - mesh.alpha())  # toggle mesh transparency
    # bu.switch()                   # change to next status
    # printc(bu.status(), box="_", dim=True)
    global model_number
    model_number += 1
    if model_number >= len(os.listdir(photogrammetry_data_path)):
        model_number = 0
    plt.clear()
    obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
    mesh = Mesh(obj_file_path)
    mesh.texture(texture_file_path, scale=0.1)
    # plt.show(mesh, __doc__,size=("f","f"))
    # plt.add(mesh, __doc__)
    plt.show(mesh, __doc__)

def prev(obj, ename):
    # mesh.alpha(1 - mesh.alpha())  # toggle mesh transparency
    # bu.switch()                   # change to next status
    # printc(bu.status(), box="_", dim=True)
    global model_number
    model_number -= 1
    if model_number < 0:
        model_number = len(os.listdir(photogrammetry_data_path)) - 1
    plt.clear()
    obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
    mesh = Mesh(obj_file_path)
    mesh.texture(texture_file_path, scale=0.1)
    # plt.show(mesh, __doc__,size=("f","f"))
    plt.show(mesh, __doc__)


model_number = 0

print("showing model number", model_number)
plt = Plotter()
bu = plt.add_button(
    next,
    pos=(0.9, 0.1),   # x,y fraction from bottom left corner
    states=["NEXT", "error"],  # text for each state
    c=["w", "w"],     # font color for each state
    bc=["dg", "dv"],  # background color for each state
    font="courier",   # font type
    size=45,          # font size
    bold=True,        # bold font
    italic=False,     # non-italic font style
)
bu2 = plt.add_button(
    prev,
    pos=(0.8, 0.1),   # x,y fraction from bottom left corner
    states=["PREV", "error"],  # text for each state
    c=["w", "w"],     # font color for each state
    bc=["dg", "dv"],  # background color for each state
    font="courier",   # font type
    size=45,          # font size
    bold=True,        # bold font
    italic=False,     # non-italic font style
)

obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
mesh = Mesh(obj_file_path)
mesh.texture(texture_file_path, scale=0.1)
plt.show(mesh, __doc__,size=("f","f"))

# while True:

#     if model_number >= len(os.listdir(photogrammetry_data_path)):
#         model_number = 0
#     if model_number < 0:
#         model_number = len(os.listdir(photogrammetry_data_path)) - 1
#     obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
#     if obj_file_path is None:
#         break
#     # show_mesh(obj_file_path, texture_file_path)

print("done")