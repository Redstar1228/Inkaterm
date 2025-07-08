![Downloads](https://static.pepy.tech/personalized-badge/inkaterm?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads) [![GitHub stars](https://img.shields.io/github/stars/Redstar1228/Inkaterm?style=social)](https://github.com/Redstar1228/Inkaterm) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Redstar1228/Inkaterm) ![GitHub code search count](https://img.shields.io/github/search?query=Inkaterm)

# 🔏 Inkaterm
+ Inkaterm writes a png file pixel-by-pixel with approximate colors
## 🎨 Features
+ print image pixel-by-pixel
+ print image with any size
+ support too many colors
+ can be used in any project
+ high accuracy in print pixels
## 📦 installation
```Bash
pip install inkaterm
```
## 🚀 Usage
```Python
from inkaterm import *

ink(file = "path/to/image.png", char = "# ", same = True)
```
## ⚙️ parameters
### file
+ The file that will be printed
### char
+ The character that the image is made of
+ default char = "# "
### same
+ if same was True, ASCII chars haves background and if same was False, ASCII chars don't have any background
+ default same = True
