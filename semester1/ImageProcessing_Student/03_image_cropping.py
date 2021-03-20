from numpy.core.fromnumeric import resize
from numpy.lib.function_base import delete
from pycat.core import Window
from pycat.base import NumpyImage as Image
from pycat.core import Window, Sprite, KeyCode

import os
import random
def load_images(img_dir: str):
    face_images = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_dir_path = dir_path + "/" + img_dir
    for file in os.listdir(img_dir_path):
        filepath = img_dir_path + file
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            face_images.append(img_dir + "/" + file)
    return face_images

face_images = load_images("resized_faces")
# print(face_images)

window = Window()
# original_image = Image.get_array_from_file("baboon.jpeg")
original_image = Image.get_array_from_file(random.choice(face_images))
print(original_image.shape)
rows, cols, channels = original_image.shape

image_sprite = window.create_sprite()
image_sprite.texture = Image.get_texture_from_array(original_image)
image_sprite.position = (400, 400)



left_eye_image = original_image[50:70, 20:50, :]
left_eye = window.create_sprite()
left_eye.position = (600, 500)
left_eye.texture = Image.get_texture_from_array(left_eye_image)
left_eye.scale = 4

original_image = Image.get_array_from_file(random.choice(face_images))
right_eye_image = original_image[50:70, 55:85, :]
right_eye = window.create_sprite()
right_eye.position = (750, 500)
right_eye.texture = Image.get_texture_from_array(right_eye_image)
right_eye.scale = 4

original_image = Image.get_array_from_file(random.choice(face_images))
nose_image = original_image[27:70, 35:60, :]
nose = window.create_sprite()
nose.position = (675, 390)
nose.texture = Image.get_texture_from_array(nose_image)
nose.scale = 3

original_image = Image.get_array_from_file(random.choice(face_images))
mouth_image = original_image[10:30, 30:65, :]
mouth = window.create_sprite()
mouth.position = (675, 280)
mouth.texture = Image.get_texture_from_array(mouth_image)
mouth.scale = 4


class Change(Sprite):
    def on_update(self, dt):
        
        if window.get_key_down(KeyCode._1):
            global left_eye, right_eye, nose, mouth
            delete(left_eye, right_eye, nose)
            original_image = Image.get_array_from_file(random.choice(face_images))

            image_sprite = window.create_sprite()
            image_sprite.texture = Image.get_texture_from_array(original_image)
            image_sprite.position = (400, 400)



            left_eye_image = original_image[50:70, 20:50, :]
            left_eye = window.create_sprite()
            left_eye.position = (600, 500)
            left_eye.texture = Image.get_texture_from_array(left_eye_image)
            left_eye.scale = 4

            original_image = Image.get_array_from_file(random.choice(face_images))
            right_eye_image = original_image[50:70, 55:85, :]
            right_eye = window.create_sprite()
            right_eye.position = (750, 500)
            right_eye.texture = Image.get_texture_from_array(right_eye_image)
            right_eye.scale = 4

            original_image = Image.get_array_from_file(random.choice(face_images))
            nose_image = original_image[27:70, 35:60, :]
            nose = window.create_sprite()
            nose.position = (675, 390)
            nose.texture = Image.get_texture_from_array(nose_image)
            nose.scale = 3

            original_image = Image.get_array_from_file(random.choice(face_images))
            mouth_image = original_image[10:30, 30:65, :]
            mouth = window.create_sprite()
            mouth.position = (675, 280)
            mouth.texture = Image.get_texture_from_array(mouth_image)
            mouth.scale = 4


# right_eye = window.create_sprite()
# nose = window.create_sprite()
# mouth = window.create_sprite()
window.create_sprite(Change)
window.run()