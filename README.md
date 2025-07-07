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
