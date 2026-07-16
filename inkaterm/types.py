from PIL import Image as Img
from io import BytesIO
from pathlib import Path
from .editors.filters import Filter
from .utils import open_image, type_handler
from .outputs.render import Render
from .exceptions import InvalidSizeError, InvalidTypeError, FileDoesNotExistsError

class Image(Render):
    def __init__(self, file, char, fill_background, cache, cache_dir, true_color):
        type_handler(False, file = file, char = char, fill_background = fill_background, cache = cache, cache_dir = cache_dir, true_color = true_color)
        self._fill_background = fill_background
        self._cache = cache
        self._cache_dir = cache_dir
        self._true_color = true_color
        self._char = char
        if isinstance(file, (str, BytesIO)):
            image = open_image(file)
        elif isinstance(file, (bytes, memoryview, bytearray)):
            image = open_image(BytesIO(file))
        self.filter = Filter(image, self._char, fill_background, self._cache, self._cache_dir, true_color)
    
    def __repr__(self):
        return f"""Image(
    size = {self.filter.img.size!r},
    mode = {self.filter.img.mode!r},
    fill_background = {self._fill_background!r},
    cache = {self._cache!r},
    cache_dir = {self._cache_dir!r},
    true_color = {self._true_color!r},
    char = {self._char!r}
)"""
    
    def resize(self, width, height):
        if isinstance(width, bool) or isinstance(height, bool):
            raise InvalidTypeError("width and height must be int objects, not bool")
        type_handler(False, width = width, height = height)
        if height < 1 or width < 1:
            raise InvalidSizeError("height and width must be bigger than zero")
        self.filter.update_image(self.filter.img.resize((width, height), Img.LANCZOS))
        return self
    
    def save(self, path) -> bool:
        type_handler(False, path = path)
        if not Path(path).parent.exists():
            raise FileDoesNotExistsError(f"directory for {path} does not exist")
        with open(path, "w", encoding = "utf-8") as f:
            f.write(str(self))
        return True