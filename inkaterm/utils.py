from PIL import Image
from hashlib import sha512
from pathlib import Path
import os
import io
import lz4.frame
from .exceptions import InvalidTypeError

TYPE_RULES = {
        "root_dir": (str,),
        "file": (str, bytes, bytearray, memoryview, io.BytesIO),
        "char": (str,),
        "fill_background": (bool,),
        "cache": (bool,),
        "cache_dir": (str,),
        "true_color": (bool,),
        "width": (int,),
        "height": (int,),
        "rx": (int, float),
        "gx": (int, float),
        "bx": (int, float),
        "value": (int, float),
        "factor": (int, float),
        "radius": (int, float),
        "amount": (int, float),
        "path": (str,)
    }

def open_image(path):
    with Image.open(path) as img:
        return img.convert("RGB")

def supports_truecolor():
    colorterm = os.environ.get("COLORTERM", "").lower()
    if colorterm in ("truecolor", "24bit"):
        return True
    if os.environ.get("WT_SESSION"):
        return True
    term_program = os.environ.get("TERM_PROGRAM", "").lower()
    if term_program in (
        "vscode",
        "iterm2",
        "apple_terminal",
        "wezterm",
        "kitty",
        "alacritty",
    ):
        return True
    term = os.environ.get("TERM", "").lower()
    if any(x in term for x in (
        "truecolor",
        "24bit",
        "direct",
        "kitty",
    )):
        return True
    return False

def get_path(cache_dir, img, char, true_color, number):
    return str(Path(cache_dir) / (sha512(img.tobytes()+ char.encode("utf-8") + str(true_color).encode("utf-8") + str(number).encode("utf-8")).hexdigest()  + ".ink"))

def hash_data(cache_dir, pixels, rendered, char, true_color, number):
    path = get_path(cache_dir, pixels, char, true_color, number)
    os.makedirs(os.path.dirname(path), exist_ok = True)
    with open(path, "wb") as f:
        rendered = lz4.frame.compress(rendered.encode("utf-8"))
        f.write(rendered)

def read_cache(cache_dir, pixels, char, true_color, number):
    path = get_path(cache_dir, pixels, char, true_color, number)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "rb") as f:
            return lz4.frame.decompress(f.read()).decode("utf-8")
    except (RuntimeError, ValueError, OSError, UnicodeDecodeError):
        return None

def type_handler(none, **kwargs):

    for key, value in kwargs.items():
        types = TYPE_RULES[key] if not none else TYPE_RULES[key] + (type(None),)
        if not isinstance(value, types):
            names = [i.__name__ for i in TYPE_RULES[key]]

            if len(names) == 1:
                expected = names[0]
            else:
                expected = ", ".join(names[:-1]) + " or " + names[-1]
            raise InvalidTypeError(f"{key} argument must be a {expected} object, not {type(value).__name__}")