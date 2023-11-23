from basic_functions import *

# show first model - the rest will be shown by the buttons
model_number = 0
obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
mesh = Mesh(obj_file_path)
mesh.texture(texture_file_path, scale=0.1)
plt.show(mesh, __doc__,size=("f","f"))