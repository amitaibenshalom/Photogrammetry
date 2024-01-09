import pygame

instructions_pic = pygame.image.load("pictures/instructions_pic.jpg")
taking_pictures_pic = pygame.image.load("pictures/red_dot.jpg")
processing_pic0 = pygame.image.load("pictures/processing_pic0.jpg")
processing_pic1 = pygame.image.load("pictures/processing_pic1.jpg")
processing_pic2 = pygame.image.load("pictures/processing_pic2.jpg")
processing_pic3 = pygame.image.load("pictures/processing_pic3.jpg")
model_view_pic = pygame.image.load("pictures/model_view_pic.jpg")
error_pic = pygame.image.load("pictures/error_pic.jpg")
camera_error_pic = pygame.image.load("pictures/camera_error_pic.png")
face_pic = pygame.image.load("pictures/face_pic.png")

instructions_pic = pygame.transform.scale(instructions_pic, (1920, 1080))
taking_pictures_pic = pygame.transform.scale(taking_pictures_pic, (1920, 1080))
processing_pic0 = pygame.transform.scale(processing_pic0, (1920, 1080))
processing_pic1 = pygame.transform.scale(processing_pic1, (1920, 1080))
processing_pic2 = pygame.transform.scale(processing_pic2, (1920, 1080))
processing_pic3 = pygame.transform.scale(processing_pic3, (1920, 1080))
model_view_pic = pygame.transform.scale(model_view_pic, (1920, 1080))
error_pic = pygame.transform.scale(error_pic, (1920, 1080))
camera_error_pic = pygame.transform.scale(camera_error_pic, (1920, 1080))

processing_pics = [processing_pic0, processing_pic1, processing_pic2, processing_pic3]
