from pathlib import Path
from io import BytesIO
from ..types import Image
from ..utils import supports_truecolor, type_handler
from ..exceptions import ImageNotFoundError

class Ink:
    def __init__(self, root_dir = ".", char = "██", fill_background = False, cache = False, cache_dir = "inkaterm_cache", true_color = None):
        type_handler(False, root_dir = root_dir, char = char, fill_background = fill_background, cache = cache, cache_dir = cache_dir)
        type_handler(True, true_color = true_color)
        self._fill_background = fill_background
        self._images_count = 0
        self._cache = cache
        self._cache_dir = cache_dir
        self._dir = root_dir
        self._char = char
        if true_color is not None:
            self._true_color = true_color
        else:
            self._true_color = supports_truecolor()
    
    def __repr__(self):
        return f"""Ink(
    root_dir = {self._dir!r},
    fill_background = {self._fill_background!r},
    cache = {self._cache!r},
    cache_dir = {self._cache_dir!r},
    true_color = {self._true_color!r},
    char = {self._char!r},
    images = {self._images_count!r}
)"""
    
    def image(self, file, char = None, fill_background = None, cache = None, cache_dir = None, true_color = None) -> Image:
        type_handler(False, file = file)
        type_handler(True, char = char, fill_background = fill_background, cache = cache, cache_dir = cache_dir, true_color = true_color)
        if isinstance(file, str):
            img = Path(self._dir) / file
            if not img.is_file():
                raise ImageNotFoundError(f'"{img}" not found')
            img = str(img)
        elif isinstance(file, (bytes, BytesIO, memoryview, bytearray)):
            img = file
        if char is None:
            char = self._char
        if fill_background is None:
            fill_background = self._fill_background
        if cache is None:
            cache = self._cache
        if cache_dir is None:
            cache_dir = self._cache_dir
        if true_color is None:
            true_color = self._true_color
        image = Image(img, char, fill_background, cache, cache_dir, true_color)
        self._images_count += 1
        return image