# Description: This file contains all the constants used in the project

# ============= constants nead to move to external constants file
Optimal_grid = [[1, 1], [2, 1], [3, 1], [2, 2], [3, 2], [3, 2], [3, 3], [3, 3], [3, 3], [4, 3], [4, 3], [4, 3], [4, 4],
                [4, 4], [4, 4], [4, 4],
                [5, 4], [5, 4], [5, 4], [5, 4], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [6, 5], [6, 5], [6, 5], [6, 5],
                [6, 5], [6, 6], [6, 6], [6, 6]
    , [6, 6], [6, 6], [6, 6]]
# Optimal_grid[23] = [6,4] # maybe better for 24 images
MIN_IMAGE_TO_SHOW = 1
MAX_IMAGE_TO_SHOW = 24
CAM_RES = (640,480) #(160,120),(320,240),(640,480),(800,600),(1024,768),(1280,720),(1280,1024),(1920,1080)
MAIN_WINDOW = 'Image capure for photogrametria Daphna'
WINDOW_SIZE = (640,480)  # (1280,720) #(1400, 800) # (1360 , 768) X,Y !
SCALE = 640.0/CAM_RES[0] #to make the same size independent of the cam resolution

PATH_OF_USBS = '/media/mada/'
NAME_OF_FOLDER_IN_USB = 'photogrammetria'

Start_Key_Code = ord('0')  # "0" (zero) keycode send when PB/Start preased
All_Done_Key_Code = ord('1')  # "1"  keycode send after all image shooting kecoade sent (pass all angles)
Idle_Time_Pass_Key_Code = ord('2')  # "2"
Noraml_Window_Size_Key_Code = ord('4')  # "4"
Full_Screen_Window_Size_Key_Code = ord('5')  # "5"
First_Angle_Key_Code = ord('a')  # "A" the first key code that will send at angle 0
Max_images = 24  # asume 2 cam and 12 images per cam , shoot every 15 deg
Last_Angle_Key_Code = First_Angle_Key_Code + (Max_images - 1)  # fboth irst and last are included
TIME_SLEEP_AFTER_DONE = 4  # sec

Char_from_KB = ""
new_dir_name = "NOT_SET"
String_from_KB = []
# Initialize list of cameras
cameras = []
# images =[]
image_array = []
TWO_D_Image_Array = []  # the final maimage matrix to show
dummy_image = []
Number_of_Images = 0
Demo_Counter = 0

# flag to indicate if we need to take image on all cameras or only on the one from the current angle
TAKE_IMAGE_ON_ALL_CAMERAS = False
# flag to indicate if we need to show live video or not
SHOW_LIVE_VIDEO = True
SHOW_IMAGE_AFTER_CAPTURE = True
