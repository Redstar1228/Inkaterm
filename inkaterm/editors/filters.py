from PIL import Image, ImageOps, ImageFilter
from ..outputs.render import Render
from ..utils import type_handler
from ..exceptions import FilterError

class Filter(Render):
    def __init__(self, img, char, fill_background, cache, cache_dir, true_color):
        self._fill_background = fill_background
        self._cache = cache
        self._cache_dir = cache_dir
        self.img = img
        self._char = char
        self._true_color = true_color
    
    def update_image(self, img):
        self.img = img
    
    def apply(self, rx, gx, bx):
        type_handler(False, rx = rx, gx = gx, bx = bx)
        r, g, b = self.img.split()[0:3]
        r = r.point(lambda x: min(int(x * rx), 255))
        g = g.point(lambda x: min(int(x * gx), 255))
        b = b.point(lambda x: min(int(x * bx), 255))
        self.img = Image.merge("RGB", (r, g, b))
        return self
    
    def brightness(self, value):
        type_handler(False, value = value)
        self.img = self.img.point(lambda c: min(max(c + value, 0), 255))
        return self
    
    def contrast(self, factor):
        type_handler(False, factor = factor)
        self.img = self.img.point(lambda c: min(max(int(128 + (c - 128) * factor), 0), 255))
        return self
    
    def invert(self):
        self.img = ImageOps.invert(self.img)
        return self
    
    def grayscale(self):
        self.img = ImageOps.grayscale(self.img).convert("RGB")
        return self
    
    def sharpness(self, amount):
        type_handler(False, amount = amount)
        self.img = self.img.filter(
            ImageFilter.UnsharpMask(radius = 2, percent = int(amount * 100), threshold = 0)
        )
        return self
    
    def blur(self, radius):
        type_handler(False, radius = radius)
        self.img = self.img.filter(ImageFilter.BoxBlur(radius))
        return self
    
    def gaussian_blur(self, radius):
        type_handler(False, radius = radius)
        if radius < 0:
            raise FilterError("radius must be non-negative")
        self.img = self.img.filter(ImageFilter.GaussianBlur(radius))
        return self
    
    def sepia(self):
        self.apply(1.2, 1.0, 0.8)
        return self
    
    def vintage(self):
        self.apply(1.1, 0.9, 0.6)
        return self
    
    def cool_blue(self):
        self.apply(0.8, 0.9, 1.3)
        return self
    
    def retro_red(self):
        self.apply(1.4, 0.7, 0.5)
        return self
    
    def neon_green(self):
        self.apply(0.5, 1.5, 0.5)
        return self
    
    def dreamy(self):
        self.apply(1.1, 0.8, 1.3)
        return self
    
    def dark_mood(self):
        self.apply(0.6, 0.6, 0.8)
        return self
    
    def warm(self):
        self.apply(1.15, 1.0, 0.85)
        return self
    
    def frost(self):
        self.apply(0.85, 1.0, 1.25)
        return self
    
    def golden(self):
        self.apply(1.25, 1.05, 0.6)
        return self
    
    def sunset(self):
        self.apply(1.3, 0.8, 0.9)
        return self
    
    def mint(self):
        self.apply(0.8, 1.2, 0.9)
        return self