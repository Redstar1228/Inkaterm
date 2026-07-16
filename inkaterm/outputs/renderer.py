from ..utils import hash_data, read_cache

class Renderer:
    def __init__(self, char, fill_background, cache, cache_dir, true_color):
        self._number = 48 if fill_background else 38
        self._cache = cache
        self._cache_dir = cache_dir
        self._char = char if not fill_background else " " * len(char)
        self._true_color = true_color
    
    def to_ansi(self, colors) -> str:
        if self._true_color:
            r, g, b = colors
            return f"\033[{self._number};2;{r};{g};{b}m{self._char}"
        else:
            code = self.to_256(*colors)
            return f"\033[{self._number};5;{code}m{self._char}"
    
    def to_256(self, r, g, b) -> int:
        if abs(r - g) < 10 and abs(g - b) < 10 and abs(r - b) < 10:
            gray_code = 232 + round((r + g + b) / 3 / 10.65)
            return max(232, min(255, gray_code))
        levels = [0, 95, 135, 175, 215, 255]
    
        def closest(val):
            return min(levels, key = lambda x: abs(x - val))
        ri = levels.index(closest(r))
        gi = levels.index(closest(g))
        bi = levels.index(closest(b))
        code = 16 + (ri * 36) + (gi * 6) + bi
        return code
    
    def render_image(self, img) -> str:
        pixels = tuple(img.getdata())
        width, height = img.size
        parts = []
        result = ""
        if self._cache:
            result = read_cache(self._cache_dir, img, self._char, self._true_color, self._number)
            if result is None:
                result = ""
        if len(result):
            return result
        for y in range(height):
            for x in range(width):
                parts.append(self.to_ansi(pixels[x + (y * width)]))
            parts.append("\033[0m\n")
        result = "".join(parts)
        if self._cache:
            hash_data(self._cache_dir, img, result[:-1], self._char, self._true_color, self._number)
        return result[:-1]