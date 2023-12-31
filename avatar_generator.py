import os
from layer import Layer
from typing import List
from PIL import Image
import random

class AvavatrGenerator:
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (random.randint(20, 200), random.randint(20, 200), random.randint(20, 200))
        self.output_path: str = './output'
        os.makedirs(self.output_path, exist_ok=True)

    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        layers  = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        return layers

    def generate_image_sequence(self):
        image_path_sequence = []
        for layer in self.layers:
            image_path = layer.get_random_image_path()
            image_path_sequence.append(image_path)
        return image_path_sequence

    def render_avatar_image(self, image_path_sequence: List[str]):
        image = Image.new('RGBA', (2000, 2000), (random.randint(20, 200), random.randint(20, 200), random.randint(20, 200)))
        for image_path in image_path_sequence:
            layer_image = Image.open(image_path)
            image = Image.alpha_composite(image, layer_image)
        return image

    def save_image(self, image: Image.Image, i: int = 0):
        image_file_name = f"avatar_{i}.png"
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)

    def generate_avatar(self, n: int = 1):
        print("Generating Avatar!")
        for i in range(n):
            image_path_sequence = self.generate_image_sequence()
            image = self.render_avatar_image(image_path_sequence)
            self.save_image(image, i)