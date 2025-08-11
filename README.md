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
+ default report = False
