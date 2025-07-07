from PIL import Image

def ppm(file, element = "lts"):
    str = "P3\n"
    image = Image.open(file)
    img = list(image.convert("RGB").getdata())
    w, h = image.size
    size = f"{w} {h}"
    return img if element != "size" else size