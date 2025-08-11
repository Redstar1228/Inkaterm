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
```Python
from inkaterm import *

data = {
    "key": "YOUR_KEY",
    "report": True,
}
ink(file = "path/to/image.png", char = "# ", same = True, pro = data)
```
## ⚙️ parameters
### file
+ The file that will be printed
### char
+ The character that the image is made of
+ default char = "# "
### same
+ if same was True, ASCII chars have background and if same was False, ASCII chars don't have any background
+ default same = True
### pro
+ pro is a dictionary with a main key named **key**. The key is a unique key created specifically for you. You can get a key as a 32-character text for yourself for 50 cents, with any cryptocurrency! if you don't have a key, you can't use any pro feature, and you can't copy another key but keys hashed by sha512 😏
+ message to **aliakbarzarei41@gmail.com** to buying a key.
#### pro features
##### report
+ if report was True the image details and time will save in a json file to save your history
