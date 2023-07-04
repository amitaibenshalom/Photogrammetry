# from basic import *

import cv2
import time
import os
import datetime
import math
import numpy as np


from CONSTS import *

# ============================================
def make_dummy_image():  # make dummy image to fill image array, based on last image in image_array
    global dummy_image
    # last_image_index = len(image_array)-1
    # print("len image_array :", len(image_array))
    if (len(image_array) > 0):
        temp_image = image_array[len(image_array) - 1].copy()
        black_img = np.zeros(temp_image.shape, dtype=np.uint8)
        red_img = black_img.copy()
        red_img[:] = (0, 0, 255)
        dummy_image = red_img.copy()


# ============================================
def fill_temp_images(image, number_of_images):
    global image_array
    image_array = []
    for i in range(number_of_images):  # Fill the image array with same image
        image_array.append(image.copy())


# ============================================
def fill_dummy_images():
    global image_array
    global Number_of_Images
    global dummy_image
    Total_images = Optimal_grid[Number_of_Images - 1][0] * Optimal_grid[Number_of_Images - 1][1]
    if (Total_images - Number_of_Images >> 0):
        for i in range(Number_of_Images, Total_images):  # Fill dummy images
            image_array.append(dummy_image.copy())


# ============================================
def Make_2D_Image_Array():  # and resize to fit WINDOW_SIZE
    global image_array
    global Number_of_Images
    global dummy_image
    global TWO_D_Image_Array
    TWO_D_Image_Array = []
    X_array = Optimal_grid[Number_of_Images - 1][0]
    Y_array = Optimal_grid[Number_of_Images - 1][1]
    show_image = image_array[0].copy()  # make initial image to show
    for i in range(1, X_array):
        show_image = cv2.hconcat([show_image, image_array[i]])
        # show_image = cv2.hconcat([image_array[i],show_image])
    show_H_image = show_image.copy()  # make initial upper images stripe
    for j in range(1, Y_array):  # will do only if more then 1 row
        show_image = image_array[0].copy()  # make initial image to show
        show_image = image_array[0 + j * X_array].copy()  # make initial image to show
        for i in range(1, X_array):
            show_image = cv2.hconcat([show_image, image_array[i + j * X_array]])
            # show_image = cv2.hconcat([image_array[i+j*X_array],show_image])
        show_H_image = cv2.vconcat([show_H_image, show_image])
        # show_H_image =cv2.vconcat([show_image, show_H_image])
    TWO_D_Image_Array = cv2.resize(show_H_image, WINDOW_SIZE, cv2.INTER_CUBIC)


# ============================================
def Print_Window_Size():
    windowWidth = cv2.getWindowImageRect(MAIN_WINDOW)[2]
    windowHeight = cv2.getWindowImageRect(MAIN_WINDOW)[3]
    print(windowWidth)
    print(windowHeight)

# ============================================
def end():
    print("Program END")
    # Release camera resources
    for camera in cameras:
        camera.release()
    cv2.destroyAllWindows()
    exit()

# ======================
def takePictures(c):
    global image_array
    global cameras
    # image_array.append(amir_image.copy())
    print("len of image array is: ", len(image_array))
    if (len(cameras) == 0):
        print("No cameras found, can't take pictures")
        return

    if TAKE_IMAGE_ON_ALL_CAMERAS:
        for camera in cameras:
            try:
                ret, frame = camera.read()
                if ret:
                    image_array.append(frame)
                    # images.append(frame)
                #                cv2.imwrite("Test"+".jpg", frame ,[cv2.IMWRITE_JPEG_QUALITY, 100])
                else:
                    print(f"Error capturing image from camera {cameras.index(camera)}")
            except:
                print(f"Error try capturing image from camera {cameras.index(camera)}")
    else:
        # get the camera index
        camera_index = c % len(cameras)
        camera = cameras[camera_index]
        try:
            ret, frame = camera.read()
            if ret:
                image_array.append(frame)
            else:
                print(f"Error capturing image from camera {camera}")
        except:
            print(f"Error try capturing image from camera {camera}")

    print("len of image array after take picture is: ", len(image_array))
# ======================================
# find the name of the first folder in a given path
def get_first_folder_name(path):
	folder_list = os.listdir(path)
	for item in folder_list:
		item_path = os.path.join(path, item)
		if os.path.isdir(item_path):
			return item
	return None
# ==========================================
# save the images
def save_images():
	global image_array
	Number_of_Images = len(image_array)
	print("==============================")
	new_dir_name = ""
	# check if a usb drive is connected (the USB is the first folder in the path '/media/mada'
	first_folder_name = get_first_folder_name(PATH_OF_USBS)
	if first_folder_name:
		print("found USB drive:", first_folder_name)
		timeString = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
	    #new_dir_name = "/media/mada/80F2-CDC9/photogrammetria" + "/Images_" + timeString
		if not os.path.exists(PATH_OF_USBS + first_folder_name + "/" + NAME_OF_FOLDER_IN_USB):
			os.mkdir(PATH_OF_USBS + first_folder_name + "/" + NAME_OF_FOLDER_IN_USB)
		new_dir_name = PATH_OF_USBS + first_folder_name + "/" + NAME_OF_FOLDER_IN_USB + "/Images_" + timeString
	else:
		print("No USB drive found.")
		timeString = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
		new_dir_name = os.getcwd() + "/Images_" + timeString
	print(f'saving {Number_of_Images} images in directory {new_dir_name}')
	os.mkdir(new_dir_name)
	#save each image in the directory
	for i in range(Number_of_Images):
		# print (new_dir_name + "/" + str(i) + ".jpg")
		cv2.imwrite(new_dir_name + "/" + str(i) + ".jpg", image_array[i],[cv2.IMWRITE_JPEG_QUALITY, 100])
		print(f'saved image number {i}')
    

cv2.namedWindow(MAIN_WINDOW, cv2.WINDOW_FREERATIO)  # WINDOW_NORMAL place holder
cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE)
#cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)



# ================================
# ========== program start here===================
cv2.namedWindow(MAIN_WINDOW, cv2.WINDOW_NORMAL)  # plase holder for WINDOW_NORMAL
# amir_image = cv2.imread("AMIR12310_100.jpg")

# check  USB cameras
for i in range(0,4):
    camera = cv2.VideoCapture(i)
    if camera.isOpened():
        width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("original resolution: {}x{}".format(width, height))
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_RES[0])
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_RES[1])
        width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("new resolution: {}x{}".format(width, height))
        cameras.append(camera)
        print(f"Opened Camera {cameras.index(camera)}")
    else:
        print(f"Error opening camera {i}")
print(f"found  {len(cameras)} USB camera(s) ")

if len(cameras) == 0:
	end()

# images = []
takePictures(0)
Number_of_Images = len(image_array)  # global variable used in many routins
print("Number_of_Images", Number_of_Images)
# fill_temp_images(amir_image,Number_of_Images)
make_dummy_image()
fill_dummy_images()
Make_2D_Image_Array()
cv2.imshow(MAIN_WINDOW, TWO_D_Image_Array)
in_key = cv2.waitKey(1)  # 10, wait for key for 10us
time.sleep(0.5)
image_array = []  # clear images array !!! need to save before

while True:
    if SHOW_LIVE_VIDEO:
        for camera in cameras:
            try:
                ret, frame = camera.read()
                if ret:
                    image_array.append(frame)
                    # cv2.imshow(MAIN_WINDOW, frame)
                else:
                    print(f"Error capturing image from camera {cameras.index(camera)}")
                    end()
            except:
                print(f"Error try capturing image from camera {cameras.index(camera)}")
                end()

        Number_of_Images = len(image_array)  # global variable used in many routins
        make_dummy_image()
        fill_dummy_images()
        Make_2D_Image_Array()
        cv2.imshow(MAIN_WINDOW, TWO_D_Image_Array)
        image_array = []


    in_key = cv2.waitKey(10)  # wait for key for 10us
    if in_key != -1:
    	print(in_key)
    if (in_key == 27):  # esc
        break

    if (in_key == Noraml_Window_Size_Key_Code):
        cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE) #

    if (in_key == Full_Screen_Window_Size_Key_Code):
        cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty(MAIN_WINDOW, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE) #

    if (in_key == Start_Key_Code):  # "0" (zero - start) - make directory for save images
        SHOW_LIVE_VIDEO = False
        Char_from_KB = in_key
        print("Char_from_KB is ", Char_from_KB)
        image_array = []
        Number_of_Images = 0

    if ((in_key >= First_Angle_Key_Code) and (
            in_key <= Last_Angle_Key_Code)):  # first and last both included used later for file name
        if SHOW_LIVE_VIDEO: #letter key is pressed before 0
        	continue
        Char_from_KB = in_key
        Number_of_Cameras = len(cameras)
        print("Char_from_KB is ", Char_from_KB)
        Number_of_Images = len(image_array)  # global variable used in many routins
        if (Number_of_Images < MAX_IMAGE_TO_SHOW):
            takePictures(in_key)
    if in_key == All_Done_Key_Code:
        if SHOW_LIVE_VIDEO: #1 is pressed before any pictures were taken
            continue 
        SHOW_LIVE_VIDEO = True
        Char_from_KB = in_key
        print("Char_from_KB is ", Char_from_KB)
        Number_of_Images = len(image_array)  # global variable used in many routins
        save_images() # save the images in a new directory
        make_dummy_image()
        fill_dummy_images()
        Make_2D_Image_Array()
        cv2.imshow(MAIN_WINDOW, TWO_D_Image_Array)
        cv2.waitKey(10)
        time.sleep(0.5)

        time.sleep(TIME_SLEEP_AFTER_DONE)
        image_array = []  # cleare images array !!! nead to save before
        # in_key = cv2.waitKey(0)  # wait for key for 10us
        # if (in_key == 27):
        #     break


end()
