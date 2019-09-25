from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import random

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

image_dir = "images/"


def generate(main=False):
    with open("words.txt") as f:
        word_list = f.readlines()

    def get_random_string (word_list, words):
        string = ""
        for i in range(0, words):
            string += random.choice(word_list) + " "
        return string[:-1]

    im = Image.open(image_dir + random.choice(os.listdir(image_dir)))
    draw = ImageDraw.Draw(im)

    im_width, im_height = im.size
    font_size = (int)(im_height/8)

    font = ImageFont.truetype("font/impact/impact.ttf", font_size)

    top_text = get_random_string(word_list, 2)
    bottom_text = get_random_string(word_list, 2)

    top_text_width, top_text_height = draw.textsize(top_text, font)
    bottom_text_width, bottom_text_height = draw.textsize(bottom_text, font)

    top_text_x, top_text_y = ((im_width - top_text_width)/2, 0)
    bottom_text_x, bottom_text_y = ((im_width - bottom_text_width)/2, im_height - bottom_text_height)

    draw.text((top_text_x - 1, top_text_y - 1), top_text, (0, 0, 0), font)
    draw.text((top_text_x - 1, top_text_y + 1), top_text, (0, 0, 0), font)
    draw.text((top_text_x + 1, top_text_y - 1), top_text, (0, 0, 0), font)
    draw.text((top_text_x + 1, top_text_y + 1), top_text, (0, 0, 0), font)
    draw.text((top_text_x, top_text_y), top_text, (255, 255, 255), font)

    draw.text((bottom_text_x - 1, bottom_text_y - 1), bottom_text, (0, 0, 0), font)
    draw.text((bottom_text_x - 1, bottom_text_y + 1), bottom_text, (0, 0, 0), font)
    draw.text((bottom_text_x + 1, bottom_text_y - 1), bottom_text, (0, 0, 0), font)
    draw.text((bottom_text_x + 1, bottom_text_y + 1), bottom_text, (0, 0, 0), font)
    draw.text((bottom_text_x, bottom_text_y), bottom_text, (255, 255, 255), font)

    im.save("output.jpg")

    if main:
        im.show()
    else:
        return True


if __file__ == "__main__":
    generate(True)