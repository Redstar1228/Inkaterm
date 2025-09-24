![Downloads](https://static.pepy.tech/personalized-badge/inkaterm?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads&cachebuster=1) [![GitHub stars](https://img.shields.io/github/stars/Redstar1228/Inkaterm?style=social)](https://github.com/Redstar1228/Inkaterm) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Redstar1228/Inkaterm) ![GitHub code search count](https://img.shields.io/github/search?query=Inkaterm) ![GitHub issues](https://img.shields.io/github/issues/Redstar1228/Inkaterm) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Redstar1228/Inkaterm) ![GitHub last commit](https://img.shields.io/github/last-commit/Redstar1228/Inkaterm)

# 🔏 Inkaterm
+ Inkaterm writes a png file pixel-by-pixel with approximate colors
## 🎨 Features
+ prints image pixel-by-pixel
+ prints image with any size
+ supports many colors
+ can be used in any project
+ high accuracy in print pixels
## 📦 installation
```Bash
pip install inkaterm
```
## 🚀 Usage
for return a image:
```Python
from inkaterm import *

ink(file = "path/to/image.png", char = "# ", same = True, report = False)
```
for show the history:
```Python
from inkaterm import *

ops = ["delete", "show", "nothing"]
history(op = ops[0 or 1 or 2])
```
## ⚙️ parameters
## 🔏 ink
### file
+ The file that will be printed
### char
+ The character that the image is made of
+ default char = "# "
### same
+ if same was True, ASCII chars have background and if same was False, ASCII chars don't have any background
+ default same = True
### report
+ if report was True, file name, file format, image size and date and time will be saved in a json file.
+ default report = True
## history
### op
+ the operation that will be performed
+ default op = nothing
+ if op equal to "delete" all history will be deleted
