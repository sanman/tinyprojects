from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def WaterMarkImg(img_path, res_path, text, pos):
    img = Image.open(img_path)
    wm = ImageDraw.Draw(img)
    col = (9, 3, 10)
    wm.text(pos, text, fill=col)
    img.show()
    img.save(res_path)
    
    
img = '/home/sanman/tinyprojects/tinyprojects/one.png'
WaterMarkImg(img, '/home/sanman/tinyprojects/tinyprojects/result.png', 'Learn Apply Build', pos=(20,20) )