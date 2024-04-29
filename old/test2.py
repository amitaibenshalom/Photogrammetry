import pygame
import datetime as dt
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from pygame.constants import *
from objloader import *
from consts import *


def init_model(obj_file):
    global viewport, output_directory, rx, ry, rz, zpos, obj, state
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(226/255,233/255,241/255,1.0)
    glLoadIdentity()

    center_object(obj_file)
    obj = OBJ(obj_file, swapyz=True)
    obj.generate()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(70.0, width/float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glTranslate(0,0,zpos)
    glRotatef(ry, 0.0, 1.0, 0.0)
    glRotatef(rx, 1.0, 0.0, 0.0)
    glRotatef(rz, 0.0, 0.0, 1.0)
    obj.render()

def rotate_model():
    global rx, ry, rz, obj, zpos
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(226/255,233/255,241/255,1.0)
    glLoadIdentity()
    ry += 1
    glTranslate(0,0,zpos)
    glRotatef(ry, 0.0, 1.0, 0.0)
    glRotatef(rx, 1.0, 0.0, 0.0)
    glRotatef(rz, 0.0, 0.0, 1.0)
    obj.render()

def render_model():
    global rx, ry, rz, obj, zpos
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(226/255,233/255,241/255,1.0)
    glLoadIdentity()
    glTranslate(0,0,zpos)
    glRotatef(ry, 0.0, 1.0, 0.0)
    glRotatef(rx, 1.0, 0.0, 0.0)
    glRotatef(rz, 0.0, 0.0, 1.0)
    obj.render()

def draw_line(vertices):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for vertex in vertices:
        glVertex2f(*vertex)
    glColor3f(1.0, 1.0, 1.0)
    glEnd()

def render_border():
    global line_vertices
    draw_line(line_vertices)

def get_nth_obj_in_folder(folder_path, n):
    items = os.listdir(folder_path)
    if len(items) == 0 or n >= len(items):
        return None, None
    obj_file_path = os.path.join(folder_path, items[-n], obj_path)
    texture_file_path = os.path.join(folder_path, items[-n], texture_path)
    if not os.path.exists(obj_file_path) or not os.path.exists(texture_file_path):
        return None, None
    return obj_file_path, texture_file_path


pygame.init()
screen_info = pygame.display.Info()
viewport = (screen_info.current_w,screen_info.current_h)
width = screen_info.current_w
height = screen_info.current_h
# a list of the vertices of the border of the screen from -1 to 1 each axis (x,y)
line_vertices = [(2*borders[0]-1, 2*borders[1]-1), (2*borders[0]-1, 1-2*borders[1]), (1-2*borders[0], 1-2*borders[1]), (1-2*borders[0], 2*borders[1]-1), (2*borders[0]-1, 2*borders[1]-1)]


screen = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF | pygame.FULLSCREEN)
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)

# image_path = "D:\Amitai_D\museum\photogrammetria\Photogrammetry\outside_screen\pictures\loading.png" 
# image_surface = pygame.image.load(image_path)
# image_data = pygame.image.tostring(image_surface, "RGBA", 1)

# Create an OpenGL texture
# texture = glGenTextures(1)
# glBindTexture(GL_TEXTURE_2D, texture)
# glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
# glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
# glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_surface.get_width(), image_surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, width, height, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

clock = pygame.time.Clock()
rx, ry, rz = (-90,180,0)
zpos = -4
obj = None

last_touch = time.time()
time_to_idle = 10
idle = False

obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
print(f"model path: {obj_file_path}")
init_model(obj_file_path)
# Render the fixed line
glPushMatrix()  # Save the current matrix
glLoadIdentity()  # Reset the matrix to identity
render_border()
glPopMatrix()  # Restore the previous matrix
# Apply transformations to the 3D model
glRotatef(1, 3, 1, 1)  # Example rotation (replace with your model rotation)
render_model()  # Render the 3D model


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                break
            if event.key == K_RIGHT:
                model_number += 1
                if model_number >= MAX_MODEL_NUMBER or model_number >= len(os.listdir(photogrammetry_data_path)):
                    model_number = 0
                obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
                # print(f"model path: {obj_file_path}")
                max_iterations = MAX_MODEL_NUMBER
                while obj_file_path is None:
                    print("Path not found - skipping one model")
                    max_iterations -= 1
                    if max_iterations <= 0:
                        print("NO MODELS IN FOLDER - must be at least one")
                        exit()
                    model_number += 1
                    if model_number >= MAX_MODEL_NUMBER or model_number >= len(os.listdir(photogrammetry_data_path)):
                        model_number = 0
                    obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
                init_model(obj_file_path)
            if event.key == K_LEFT:
                model_number -= 1
                if model_number < 0:
                    model_number = min(MAX_MODEL_NUMBER-1, len(os.listdir(photogrammetry_data_path)) - 1)
                obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
                # print(f"model path: {obj_file_path}")
                max_iterations = MAX_MODEL_NUMBER
                while obj_file_path is None:
                    print("Path not found - skipping one model")
                    max_iterations -= 1
                    if max_iterations <= 0:
                        print("NO MODELS IN FOLDER - must be at least one")
                        exit()
                        break
                    model_number -= 1
                    if model_number < 0:
                        model_number = min(MAX_MODEL_NUMBER-1, len(os.listdir(photogrammetry_data_path)) - 1)
                    obj_file_path, texture_file_path = get_nth_obj_in_folder(photogrammetry_data_path, model_number)
                init_model(obj_file_path)        
        elif event.type == MOUSEBUTTONDOWN:  # if mouse is CLICKED and dragged then rotate the model accordingly
            last_touch = time.time()
            idle = False
            if event.button == 4:
                # zpos = max(zpos - 1, -30)
                pass
            elif event.button == 5:
                # zpos = min(zpos + 1, -1)
                pass
            elif event.button == 1:
                # x, y = event.pos
                # rx += (y - ry)
                # ry += (x - rx)
                pass
        elif event.type == MOUSEMOTION:
            last_touch = time.time()
            idle = False
            if event.buttons[0]:
                x, y = event.rel
                rx -= y * 0.3
                ry += x * 0.3
        elif event.type == MOUSEWHEEL:
            # zpos += event.y
            pass

    if time.time() - last_touch > time_to_idle:
        idle = True
    if idle:
        rotate_model()
        rx = -90
    else:
        render_model()
        pass

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(226/255,233/255,241/255,1.0)

    # Render the fixed line
    glPushMatrix()  # Save the current matrix
    glLoadIdentity()  # Reset the matrix to identity
    render_border()
    glPopMatrix()  # Restore the previous matrix
    # Apply transformations to the 3D model
    glRotatef(1, 3, 1, 1)  # Example rotation (replace with your model rotation)
    render_model()  # Render the 3D model


    # render_model()
    # render_border()
    pygame.display.flip()
    clock.tick(30)


